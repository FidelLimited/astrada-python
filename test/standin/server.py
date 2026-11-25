"""A local stand-in for the Astrada API, for the tests and the documentation examples.

It answers every path of the two API definitions (openapi-main.json and openapi-banking.json, copied
here when the SDK is generated) with a body built from the response schema, so any generated method
can be called against it. Nothing here talks to Astrada.

Behaviour the tests and examples rely on:
- Login: POST /auth/realms/<account>/protocol/openid-connect/token. Account ``acc_standin`` with
  client ``client_standin`` and secret ``secret_standin`` gets a token. Another secret gets 401
  ``invalid_client``; another account gets 404 ``Realm does not exist``, as the real login does.
- Every other call needs a token from that login, else 401. That client is a customer client: a
  staff-only Banking API operation answers it 403 (missing scope). Client ``client_staff`` (same
  secret) is a staff client and gets 200.
- A path id of 00000000-0000-0000-0000-000000000000 answers 404 with a problem body.
- GET /subaccounts holds five subaccounts, served in pages of ``limit`` with a cursor in
  ``_links.next``; GET /bank-links holds three bank links, paged with ``pagination``.
- POST /_standin/fail {"status": 503, "count": 2, "retryAfter": "0"} makes the next ``count``
  calls answer ``status``. GET /_standin/log lists the calls received (method, path, user agent).

Run on its own: python test/standin/server.py [port]
"""

import base64
import json
import re
import sys
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlsplit

HERE = Path(__file__).resolve().parent
ACCOUNT_ID = "acc_standin"
CLIENT_ID = "client_standin"
CLIENT_SECRET = "secret_standin"
STAFF_CLIENT_ID = "client_staff"
SDK_CLIENT_ID = "client_sdk"
"""A browser SDK client: its token carries only the scopes the Unified Enrollment SDK needs."""
SDK_SCOPES = ("subaccounts:read card-subscriptions:read card-subscriptions:write card-verifications:read "
              "card-verifications:write enrollment-methods:write banking:read banking:write")
MISSING_ID = "00000000-0000-0000-0000-000000000000"
FIXED_UUID = "3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b"


def _load(name: str) -> Dict[str, Any]:
    with open(HERE / name, encoding="utf-8") as handle:
        return json.load(handle)


class Spec:
    def __init__(self, document: Dict[str, Any]) -> None:
        self.document = document
        self.routes: List[Tuple[str, re.Pattern, Dict[str, Any]]] = []
        for path, operations in document["paths"].items():
            pattern = re.compile("^" + re.sub(r"\{[^/]+\}", "([^/]+)", path) + "$")
            for method, operation in operations.items():
                if isinstance(operation, dict) and "responses" in operation:
                    self.routes.append((method.upper(), pattern, operation))
        # Literal paths before templated ones (/network-bulk-enrollments/open before /{id}).
        self.routes.sort(key=lambda route: route[1].pattern.count("([^/]+)"))

    def resolve(self, node: Any) -> Any:
        seen = 0
        while isinstance(node, dict) and "$ref" in node and seen < 20:
            target: Any = self.document
            for part in node["$ref"].lstrip("#/").split("/"):
                target = target[part]
            node = target
            seen += 1
        return node

    def find(self, method: str, path: str) -> Optional[Tuple[Dict[str, Any], Tuple[str, ...]]]:
        for route_method, pattern, operation in self.routes:
            match = pattern.match(path)
            if route_method == method and match:
                return operation, match.groups()
        return None

    def sample(self, schema: Any, depth: int = 0) -> Any:
        schema = self.resolve(schema)
        if not isinstance(schema, dict) or depth > 24:
            return None
        if "example" in schema and not isinstance(schema["example"], (dict, list)):
            return schema["example"]
        if "allOf" in schema:
            parts = [self.sample(part, depth + 1) for part in schema["allOf"]]
            if not all(isinstance(part, dict) for part in parts):
                return next((part for part in parts if part is not None), None)
            merged: Dict[str, Any] = {}
            for part in parts:
                merged.update(part)
            return merged
        for key in ("oneOf", "anyOf"):
            if key in schema:
                return self.sample(schema[key][0], depth + 1)
        if "enum" in schema:
            return schema["enum"][0]
        kind = schema.get("type")
        if isinstance(kind, list):
            kind = next((k for k in kind if k != "null"), None)
        if kind == "object" or "properties" in schema:
            out = {}
            required = schema.get("required", [])
            for name, prop in schema.get("properties", {}).items():
                if depth > 6 and name not in required:
                    continue  # deep optional parts stay out, so samples stay small and finite
                value = self.sample(prop, depth + 1)
                if value is not None or name in schema.get("required", []):
                    out[name] = value
            return out
        if kind == "array":
            item = self.sample(schema.get("items", {}), depth + 1)
            if item is None:
                return []
            return [item] * max(1, int(schema.get("minItems", 1)))
        if kind == "string":
            fmt = schema.get("format")
            if fmt == "uuid":
                return FIXED_UUID
            if fmt == "date-time":
                return "2026-01-15T10:00:00Z"
            if fmt == "date":
                return "2026-01-15"
            if fmt in ("uri", "url"):
                return "https://example.com/path"
            if fmt == "email":
                return "someone@example.com"
            if fmt == "byte":
                return base64.b64encode(b"standin").decode()
            if "pattern" in schema or "minLength" in schema:
                return "x" * max(1, int(schema.get("minLength", 1)))
            return "standin"
        if kind == "integer":
            return int(schema.get("minimum", 1))
        if kind == "number":
            return float(schema.get("minimum", 1))
        if kind == "boolean":
            return True
        return None

    def response(self, operation: Dict[str, Any]) -> Tuple[int, Any]:
        codes = sorted(code for code in operation["responses"] if code.startswith("2"))
        if not codes:
            return 200, {}
        code = codes[0]
        response = self.resolve(operation["responses"][code])
        content = (response or {}).get("content") or {}
        media = content.get("application/json") or content.get("application/hal+json")
        if media is None and content:
            media = next(iter(content.values()))
        if not media or "schema" not in media:
            return int(code), None
        return int(code), self.sample(media["schema"])


class State:
    def __init__(self) -> None:
        self.specs = [Spec(_load("openapi-banking.json")), Spec(_load("openapi-main.json"))]
        if (HERE / "openapi-sandbox.json").exists():
            self.specs.append(Spec(_load("openapi-sandbox.json")))
        self.tokens: Dict[str, bool] = {}
        """token -> staff client"""
        from astrada.banking import _staff_only

        self.staff_only = _staff_only
        self.fail: List[Dict[str, Any]] = []
        self.log: List[Dict[str, Any]] = []
        self.lock = threading.Lock()
        self.subaccounts = [
            {"id": str(uuid.UUID(int=index + 1)), "name": "Subaccount %d" % (index + 1)}
            for index in range(5)
        ]


def _problem(status: int, title: str, detail: str, **extra: Any) -> Dict[str, Any]:
    return {"title": title, "detail": detail, **extra}


class Handler(BaseHTTPRequestHandler):
    server_version = "AstradaStandin/1"
    state: State

    def log_message(self, *args: Any) -> None:  # quiet
        return

    def _send(self, status: int, body: Any, headers: Optional[Dict[str, str]] = None) -> None:
        data = b"" if body is None else json.dumps(body).encode()
        self.send_response(status)
        if body is not None:
            self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("x-request-id", "req_standin")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if data:
            self.wfile.write(data)

    def _body(self) -> bytes:
        length = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(length) if length else b""

    def _handle(self, method: str) -> None:
        state = self.state
        url = urlsplit(self.path)
        path = url.path
        query = parse_qs(url.query)
        raw = self._body()
        with state.lock:
            state.log.append(
                {"method": method, "path": path, "query": url.query,
                 "userAgent": self.headers.get("User-Agent")}
            )

        if path == "/_standin/fail" and method == "POST":
            spec = json.loads(raw or b"{}")
            with state.lock:
                for _ in range(int(spec.get("count", 1))):
                    state.fail.append(spec)
            return self._send(204, None)
        if path == "/_standin/log":
            return self._send(200, state.log)

        with state.lock:
            failure = state.fail.pop(0) if state.fail else None
        if failure is not None:
            headers = {}
            if failure.get("retryAfter") is not None:
                headers["Retry-After"] = str(failure["retryAfter"])
            status = int(failure["status"])
            return self._send(status, _problem(status, "Standin failure", "Forced by the test"),
                              headers)

        login = re.match(r"^/auth/realms/([^/]+)/protocol/openid-connect/token$", path)
        if login and method == "POST":
            form = parse_qs(raw.decode())
            if login.group(1) != ACCOUNT_ID:
                return self._send(404, {"error": "Realm does not exist"})
            if form.get("client_id") not in ([CLIENT_ID], [STAFF_CLIENT_ID], [SDK_CLIENT_ID]) \
                    or form.get("client_secret") != [CLIENT_SECRET]:
                return self._send(401, {"error": "invalid_client",
                                        "error_description": "Invalid client or Invalid client credentials"})
            token = uuid.uuid4().hex
            with state.lock:
                state.tokens[token] = form.get("client_id") == [STAFF_CLIENT_ID]
            # The scopes the real login states in its answer (it grants a client all of them).
            scope = SDK_SCOPES if form.get("client_id") == [SDK_CLIENT_ID] else (
                "subaccounts:read cards:read"
                + (" banking:admin" if form.get("client_id") == [STAFF_CLIENT_ID] else ""))
            return self._send(200, {"access_token": token, "token_type": "Bearer", "expires_in": 300,
                                    "scope": scope})

        auth = self.headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or auth[len("Bearer "):] not in state.tokens:
            return self._send(401, _problem(401, "Unauthorized", "Missing or invalid token"))

        staff_op = state.staff_only.operation(method, path, "")
        if staff_op is not None and not state.tokens[auth[len("Bearer "):]]:
            return self._send(403, _problem(403, "Forbidden",
                                            "Missing scope '%s'" % staff_op["scope"]))

        if MISSING_ID in path.split("/"):
            return self._send(404, _problem(404, "Not Found", "No resource with that id"))

        if path == "/subaccounts" and method == "GET":
            return self._subaccounts(query)

        for spec in state.specs:
            found = spec.find(method, path)
            if found:
                operation, _ = found
                status, body = spec.response(operation)
                if path == "/bank-links" and method == "GET":
                    body = self._bank_links(spec, body, query)
                elif isinstance(body, dict):
                    body = self._last_page(body)
                return self._send(status, body)
        return self._send(404, _problem(404, "Not Found", "No such route: %s %s" % (method, path)))

    def _last_page(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """Generic list answers are one page: no next link, no more results."""
        links = body.get("_links")
        if isinstance(links, dict):
            links.pop("next", None)
        pagination = body.get("pagination")
        if isinstance(pagination, dict):
            pagination["hasMore"] = False
            pagination.pop("cursor", None)
        return body

    def _subaccounts(self, query: Dict[str, List[str]]) -> None:
        limit = int(query.get("limit", ["50"])[0])
        start = self._cursor(query)
        spec = self.state.specs[1]
        found = spec.find("GET", "/subaccounts/" + FIXED_UUID)
        assert found
        _, template = spec.response(found[0])
        items = []
        for subaccount in self.state.subaccounts[start:start + limit]:
            item = dict(template)
            item.update(subaccount)
            item["_links"] = {"self": {"href": "/subaccounts/" + subaccount["id"]}}
            items.append(item)
        links: Dict[str, Any] = {"self": {"href": "/subaccounts?limit=%d" % limit}}
        if start + limit < len(self.state.subaccounts):
            cursor = base64.b64encode(str(start + limit).encode()).decode()
            links["next"] = {"href": "/subaccounts?limit=%d&cursor=%s" % (limit, cursor)}
        self._send(200, {"_embedded": {"subaccounts": items}, "_links": links})

    @staticmethod
    def _cursor(query: Dict[str, List[str]]) -> int:
        try:
            return int(base64.b64decode(query["cursor"][0]).decode())
        except (KeyError, ValueError):
            return 0

    def _bank_links(self, spec: Spec, body: Any, query: Dict[str, List[str]]) -> Any:
        if not isinstance(body, dict) or not body.get("items"):
            return body
        cursor = query.get("cursor", ["0"])[0]
        start = int(cursor) if cursor.isdigit() else 0
        template = body["items"][0]
        items = []
        for index in range(start, min(start + 2, 3)):
            item = dict(template)
            item["id"] = "enrollment_standin_%d" % index
            items.append(item)
        more = start + 2 < 3
        body["items"] = items
        body["pagination"] = {"hasMore": more, **({"cursor": str(start + 2)} if more else {})}
        return body

    def do_GET(self) -> None:
        self._handle("GET")

    def do_POST(self) -> None:
        self._handle("POST")

    def do_PATCH(self) -> None:
        self._handle("PATCH")

    def do_PUT(self) -> None:
        self._handle("PUT")

    def do_DELETE(self) -> None:
        self._handle("DELETE")


class Standin:
    """A running stand-in on 127.0.0.1. Use as a context manager, or call stop()."""

    def __init__(self, port: int = 0) -> None:
        handler = type("BoundHandler", (Handler,), {"state": State()})
        self.server = ThreadingHTTPServer(("127.0.0.1", port), handler)
        self.state: State = handler.state
        self.url = "http://127.0.0.1:%d" % self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.server.shutdown()
        self.server.server_close()

    def __enter__(self) -> "Standin":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.stop()


if __name__ == "__main__":
    standin = Standin(int(sys.argv[1]) if len(sys.argv) > 1 else 8099)
    print(standin.url, flush=True)
    try:
        standin.thread.join()
    except KeyboardInterrupt:
        standin.stop()
