# coding: utf-8
"""Tests for the hand-written client-credentials support (astrada/auth_client.py and the
token wiring in the configuration template).

urllib3 is replaced with a fake, so the tests need no network or account.
"""

import io
import json
import unittest
import uuid
from unittest import mock

import urllib3

from astrada import ApiClient, Configuration, SubaccountsApi
from astrada.auth_client import AuthenticationClient
from astrada.exceptions import AuthenticationError

SANDBOX = "https://api.sandbox.astrada.co"
SUBACCOUNT_ID = uuid.UUID("2f8a3c1e-5b6d-4e7f-8a9b-0c1d2e3f4a5b")


def _response(status, payload):
    return urllib3.HTTPResponse(
        body=io.BytesIO(json.dumps(payload).encode("utf-8")),
        status=status,
        headers={"Content-Type": "application/json"},
        preload_content=False,
    )


class FakeHttp:
    """Answers token requests and API requests the way the Astrada API does."""

    def __init__(self, token_status=200):
        self.token_status = token_status
        self.calls = []

    def __call__(self, _pool, method, url, **kwargs):
        self.calls.append({"method": method, "url": url, **kwargs})
        if "/protocol/openid-connect/token" in url:
            if self.token_status != 200:
                return _response(
                    self.token_status,
                    {"error": "unauthorized_client", "error_description": "Invalid client credentials"},
                )
            return _response(
                200,
                {"access_token": f"token-{len(self.calls)}", "token_type": "Bearer", "expires_in": 300},
            )
        return _response(200, {"id": str(SUBACCOUNT_ID)})

    def token_calls(self):
        return [c for c in self.calls if "/protocol/openid-connect/token" in c["url"]]


def _api(host=None):
    configuration = Configuration(
        host=host,
        account_id="acct-1",
        client_id="client-1",
        client_secret="secret-1",
    )
    return SubaccountsApi(ApiClient(configuration))


class TestAuthClient(unittest.TestCase):
    def test_defaults_to_production(self):
        self.assertEqual(Configuration().host, "https://api.astrada.co")

    def test_requests_a_client_credentials_token_from_the_account_realm(self):
        fake = FakeHttp()
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            _api(SANDBOX).get_subaccount_without_preload_content(SUBACCOUNT_ID)

        token = fake.token_calls()[0]
        self.assertEqual(token["method"], "POST")
        self.assertEqual(token["url"], f"{SANDBOX}/auth/realms/acct-1/protocol/openid-connect/token")
        self.assertEqual(token["headers"]["Content-Type"], "application/x-www-form-urlencoded")
        self.assertEqual(
            token["fields"],
            {"client_id": "client-1", "client_secret": "secret-1", "grant_type": "client_credentials"},
        )

    def test_sends_the_token_as_a_bearer_header_to_the_configured_host(self):
        fake = FakeHttp()
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            response = _api(SANDBOX).get_subaccount_without_preload_content(SUBACCOUNT_ID)

        self.assertEqual(response.status, 200)
        call = fake.calls[-1]
        self.assertEqual(call["url"], f"{SANDBOX}/subaccounts/{SUBACCOUNT_ID}")
        self.assertEqual(call["headers"]["Authorization"], "Bearer token-1")

    def test_reuses_a_token_until_it_expires(self):
        fake = FakeHttp()
        api = _api()
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            api.get_subaccount_without_preload_content(SUBACCOUNT_ID)
            api.get_subaccount_without_preload_content(SUBACCOUNT_ID)

        self.assertEqual(len(fake.token_calls()), 1)
        self.assertEqual(len(fake.calls), 3)

    def test_a_refused_token_request_raises_authentication_error(self):
        fake = FakeHttp(token_status=401)
        client = AuthenticationClient(
            account_id="acct-1", client_id="client-1", client_secret="wrong", base_path=SANDBOX
        )
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            with self.assertRaises(AuthenticationError) as raised:
                client.get_access_token()

        self.assertEqual(raised.exception.status, 401)
        self.assertIn("Invalid client credentials", str(raised.exception))
        self.assertEqual(raised.exception.detail, "Invalid client credentials")
        self.assertEqual(raised.exception.code, "unauthorized_client")


    def test_a_400_from_the_token_endpoint_raises_authentication_error(self):
        fake = FakeHttp(token_status=400)
        client = AuthenticationClient(
            account_id="acct-1", client_id="client-1", client_secret="wrong", base_path=SANDBOX
        )
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            with self.assertRaises(AuthenticationError) as raised:
                client.get_access_token()
        self.assertEqual(raised.exception.status, 400)

    def test_the_token_request_is_retried_under_the_client_retries(self):
        fake = FakeHttp()
        client = AuthenticationClient(
            account_id="acct-1", client_id="c", client_secret="s", base_path=SANDBOX, retries=3
        )
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            client.get_access_token()
        retry = fake.token_calls()[0]["retries"]
        self.assertEqual(retry.total, 3)
        self.assertIn("POST", retry.allowed_methods)
        self.assertIn(503, retry.status_forcelist)

    def test_a_null_expires_in_means_the_default(self):
        def answer(_pool, method, url, **kwargs):
            return _response(200, {"access_token": "t", "token_type": "Bearer", "expires_in": None})

        client = AuthenticationClient(
            account_id="acct-1", client_id="c", client_secret="s", base_path=SANDBOX
        )
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=answer):
            self.assertEqual(client.get_access_token(), "Bearer t")
        self.assertEqual(client._cached_token.expires_in, 300)


def test_a_login_redirect_is_not_followed_and_the_secret_goes_nowhere_else():
    """A 3xx from the token endpoint is a login error; the client secret is not re-sent."""
    import http.server
    import threading

    import pytest

    from astrada.exceptions import ApiException

    received = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *args):
            return

        def do_POST(self):
            length = int(self.headers.get("Content-Length") or 0)
            received.append((self.path, self.rfile.read(length).decode()))
            if self.path.startswith("/auth/"):
                self.send_response(307)
                self.send_header("Location", "/elsewhere?code=secret-code")
                self.send_header("Content-Length", "0")
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-Length", "2")
                self.end_headers()
                self.wfile.write(b"{}")

    server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        client = AuthenticationClient("acct", "client", "s3cret", "http://127.0.0.1:%d" % server.server_port)
        with pytest.raises(ApiException, match=r"redirect to http://127\.0\.0\.1:%d\." % server.server_port) as raised:
            client.get_access_token()
        assert "secret-code" not in str(raised.value) and "elsewhere" not in str(raised.value)
    finally:
        server.shutdown()
    assert [path for path, _ in received] == ["/auth/realms/acct/protocol/openid-connect/token"]

def _redirecting_server(location):
    import http.server
    import threading

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *args):
            return

        def do_POST(self):
            self.rfile.read(int(self.headers.get("Content-Length") or 0))
            self.send_response(302)
            self.send_header("Location", location)
            self.send_header("Content-Length", "0")
            self.end_headers()

    server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def test_a_malformed_or_ipv6_redirect_still_raises_the_login_error_without_the_location():
    import pytest

    from astrada.exceptions import ApiException

    for location, shown in [("https://host:abc/x?code=1", "another address"),
                            ("http://[::1:8080/x", "another address"),
                            ("http://[::1]:8080/x?code=1", "http://[::1]:8080")]:
        server = _redirecting_server(location)
        try:
            client = AuthenticationClient("acct", "client", "s3cret", "http://127.0.0.1:%d" % server.server_port)
            with pytest.raises(ApiException) as raised:
                client.get_access_token()
        finally:
            server.shutdown()
            server.server_close()
        assert "redirect to %s." % shown in str(raised.value)
        assert "code=1" not in str(raised.value)
        assert not any(k.lower() == "location" for k in (raised.value.headers or {}))
        assert not raised.value.body


if __name__ == "__main__":
    unittest.main()
