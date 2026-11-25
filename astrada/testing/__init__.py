# coding: utf-8
"""Test your code that uses the SDK without calling Astrada. Hand-written; not generated.

:class:`MockAstrada` gives you an :class:`astrada.Astrada` client whose requests never leave the
process: every operation of the API answers with the example from the API definition
(``responses.json`` next to this file, regenerated with each release so it follows the API),
and you can set the answer of any operation yourself.

    from astrada.testing import MockAstrada

    def test_lists_subaccounts():
        with MockAstrada() as mock:
            mock.respond("list_subaccounts", body={"_embedded": {"subaccounts": []},
                                                   "_links": {"self": {"href": "/subaccounts"}}})
            page = mock.client.subaccounts.list_subaccounts()
            assert page.embedded.subaccounts == []
            assert mock.calls[-1].operation == "list_subaccounts"

To mock an HTTP server instead (for code in another language, or a whole app), run Prism on the
definition; see the README.
"""

import io
import json
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from urllib.parse import parse_qs, urlsplit

import urllib3

from astrada.client import Astrada

_RESPONSES = Path(__file__).resolve().parent / "responses.json"

Handler = Callable[["MockCall"], Union[Tuple[int, Any], Tuple[int, Any, Dict[str, str]]]]


class MockCall:
    """One request the mock received."""

    def __init__(
        self, operation: Optional[str], method: str, path: str, query: Dict[str, List[str]],
        body: Any, headers: Dict[str, str],
    ) -> None:
        self.operation = operation
        """The method name (``"list_subaccounts"``), or None for a path no operation has."""
        self.method = method
        self.path = path
        self.query = query
        self.body = body
        """The JSON request body, parsed."""
        self.headers = headers

    def __repr__(self) -> str:
        return "MockCall(%r, %s %s)" % (self.operation, self.method, self.path)


class _Route:
    def __init__(self, answer: Dict[str, Any]) -> None:
        self.operation: str = answer["operation"]
        self.method: str = answer["method"]
        self.template: str = answer["path"]
        self.pattern = re.compile("^" + re.sub(r"\{[^/]+\}", "[^/]+", answer["path"]) + "$")
        self.status: int = answer["status"]
        self.body: Any = answer["body"]


def _load_routes() -> List[_Route]:
    routes = [_Route(answer) for answer in json.loads(_RESPONSES.read_text(encoding="utf-8"))]
    # Literal paths before templated ones (/network-bulk-enrollments/open before /{id}).
    routes.sort(key=lambda route: route.template.count("{"))
    return routes


def _response(status: int, body: Any, headers: Optional[Dict[str, str]] = None) -> Any:
    data = b"" if body is None else json.dumps(body).encode("utf-8")
    all_headers = {"Content-Type": "application/json"} if body is not None else {}
    all_headers.update(headers or {})
    return urllib3.HTTPResponse(
        body=io.BytesIO(data), status=status, headers=all_headers, preload_content=False,
        reason="Mock",
    )


class _MockPool:
    def __init__(self, mock: "MockAstrada") -> None:
        self.mock = mock

    def request(self, method: str, url: str, body: Any = None, fields: Any = None,
                headers: Optional[Dict[str, str]] = None, **_: Any) -> Any:
        return self.mock._answer(method, url, body, headers or {})

    def clear(self) -> None:
        return None


class MockAstrada:
    """An Astrada client that answers from the API definition's examples, in-process.

    :param client: an :class:`astrada.Astrada` client to answer for; default: a new sandbox client
        with made-up credentials
    :param environment: the new client's environment (``"sandbox"`` or ``"production"``)

    ``mock.client`` is the client. Its login always succeeds (unless you
    :meth:`refuse_login`), every operation answers its example, and ``mock.calls`` records what
    was sent. Retries are turned off on a client the mock makes.
    """

    def __init__(self, client: Optional[Astrada] = None, *, environment: str = "sandbox") -> None:
        self.routes = _load_routes()
        self.calls: List[MockCall] = []
        self._overrides: Dict[str, Handler] = {}
        self._login_refused = False
        self.client = client or Astrada(
            "mock_account", "mock_client", "mock_secret", environment=environment, retries=0
        )
        pool = _MockPool(self)
        for api_client in (
            self.client.api_client, self.client.banking_api_client, self.client.sandbox_api_client
        ):
            api_client.rest_client.pool_manager = pool  # type: ignore[assignment]
        if self.client.auth is not None:
            self.client.auth.pool_manager = pool  # type: ignore[assignment]
            self.client.auth.clear_cache()

    def __enter__(self) -> "MockAstrada":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.client.close()

    def respond(
        self,
        operation: str,
        body: Any = None,
        status: int = 200,
        headers: Optional[Dict[str, str]] = None,
        handler: Optional[Handler] = None,
    ) -> None:
        """Set the answer of one operation, by its method name (``"get_subaccount"``).

        Give ``body`` and ``status`` (and ``headers``), or a ``handler`` that receives the
        :class:`MockCall` and returns ``(status, body)`` or ``(status, body, headers)``. An error
        status raises the SDK's matching exception, as the real API would.
        """
        if operation not in {route.operation for route in self.routes}:
            raise ValueError("No operation named %r" % operation)
        if handler is None:
            fixed = (status, body, headers or {})
            handler = lambda call: fixed  # noqa: E731
        self._overrides[operation] = handler

    def reset(self) -> None:
        """Forget the recorded calls and every answer set with :meth:`respond`."""
        self.calls.clear()
        self._overrides.clear()
        self._login_refused = False

    def refuse_login(self) -> None:
        """Make the next login fail as wrong credentials do (``AuthenticationError``)."""
        self._login_refused = True
        if self.client.auth is not None:
            self.client.auth.clear_cache()

    def _answer(self, method: str, url: str, body: Any, headers: Dict[str, str]) -> Any:
        parts = urlsplit(url)
        path = parts.path
        if path.endswith("/protocol/openid-connect/token"):
            if self._login_refused:
                return _response(401, {"error": "invalid_client",
                                       "error_description": "Invalid client or Invalid client credentials"})
            return _response(200, {"access_token": "mock-token", "token_type": "Bearer",
                                   "expires_in": 3600})
        base = urlsplit(self.client.base_url).path.rstrip("/")
        if base and path.startswith(base):
            path = path[len(base):]
        try:
            parsed = json.loads(body) if isinstance(body, (str, bytes)) and body else body
        except ValueError:
            parsed = body
        route = next(
            (r for r in self.routes if r.method == method.upper() and r.pattern.match(path)), None
        )
        call = MockCall(route.operation if route else None, method.upper(), path,
                        parse_qs(parts.query), parsed, dict(headers))
        self.calls.append(call)
        if route is None:
            return _response(404, {"title": "Not Found", "detail": "No operation for %s %s" % (
                method.upper(), path)})
        override = self._overrides.get(route.operation)
        if override is not None:
            answer = override(call)
            status, answer_body = answer[0], answer[1]
            extra = answer[2] if len(answer) > 2 else {}
            return _response(status, answer_body, extra)
        return _response(route.status, route.body)
