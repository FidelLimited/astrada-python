"""Behaviour of astrada.Astrada against the local stand-in API (test/standin/server.py)."""

import inspect
import json
import os
import re
import socket
import subprocess
import time
import typing
import urllib.request
from pathlib import Path

import pydantic
from urllib3.util.retry import Retry

import pytest

import astrada
from astrada.testing import MockAstrada
from standin.server import ACCOUNT_ID, CLIENT_ID, CLIENT_SECRET


def make(standin, **kwargs):
    settings = dict(
        account_id=ACCOUNT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
        environment="sandbox", base_url=standin.url,
    )
    settings.update(kwargs)
    return astrada.Astrada(**settings)


def fail_next(standin, status, count=1, retry_after=None):
    body = json.dumps({"status": status, "count": count, "retryAfter": retry_after}).encode()
    request = urllib.request.Request(standin.url + "/_standin/fail", data=body, method="POST")
    urllib.request.urlopen(request).read()


def calls(standin, path=None):
    return [c for c in standin.state.log if path is None or c["path"] == path]


TOKEN_PATH = "/auth/realms/%s/protocol/openid-connect/token" % ACCOUNT_ID


# Login


def test_a_wrong_secret_raises_authentication_error_with_the_login_message(standin):
    client = make(standin, client_secret="wrong")
    with pytest.raises(astrada.AuthenticationError) as raised:
        client.subaccounts.list_subaccounts()
    error = raised.value
    assert error.status == 401
    assert error.code == "invalid_client"
    assert error.detail == "Invalid client or Invalid client credentials"
    assert "Login failed (401): Invalid client or Invalid client credentials" in str(error)
    assert "client_secret" in str(error)
    assert calls(standin, "/subaccounts") == []  # the call was never sent without a token


def test_a_wrong_account_names_the_account(standin):
    client = make(standin, account_id="acc_nope")
    with pytest.raises(astrada.NotFoundException) as raised:
        client.subaccounts.list_subaccounts()
    assert raised.value.status == 404
    assert not isinstance(raised.value, astrada.AuthenticationError)
    assert "account_id" in str(raised.value)


def test_main_banking_and_sandbox_share_one_login(standin):
    client = make(standin, sandbox_base_url=True)
    client.subaccounts.list_subaccounts()
    client.banking.bank_links.list_bank_links()
    client.sandbox.simulate_transaction(
        astrada.sandbox.SimulateTransactionRequest(
            card_id="3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b", type="authorization", amount=100
        )
    )
    assert len(calls(standin, TOKEN_PATH)) == 1
    assert client.auth is client.banking_configuration.get_auth_client()
    assert client.auth is client.sandbox_configuration.get_auth_client()


def test_user_agent_and_version(standin):
    make(standin).subaccounts.list_subaccounts()
    assert calls(standin, "/subaccounts")[-1]["userAgent"] == "astrada-python/" + astrada.__version__


def test_environment_is_required_and_checked():
    with pytest.raises(TypeError):
        astrada.Astrada("a", "b", "c")  # type: ignore[call-arg]
    with pytest.raises(ValueError, match="sandbox"):
        astrada.Astrada("a", "b", "c", environment="staging")
    assert astrada.Astrada("a", "b", "c", environment="Sandbox").base_url == astrada.Environment.SANDBOX
    assert astrada.Astrada("a", "b", "c", environment="production").base_url == astrada.Environment.PRODUCTION


def test_missing_credentials_name_the_environment_variables(monkeypatch):
    for name in ("ASTRADA_ACCOUNT_ID", "ASTRADA_CLIENT_ID", "ASTRADA_CLIENT_SECRET"):
        monkeypatch.delenv(name, raising=False)
    with pytest.raises(ValueError, match="ASTRADA_CLIENT_SECRET"):
        astrada.Astrada(environment="sandbox")


# Errors


def test_a_404_carries_the_problem_body(standin):
    with pytest.raises(astrada.NotFoundException) as raised:
        make(standin).subaccounts.get_subaccount("00000000-0000-0000-0000-000000000000")
    error = raised.value
    assert (error.status, error.title, error.detail) == (404, "Not Found", "No resource with that id")
    assert error.request_id == "req_standin"
    assert "(404) Not Found: No resource with that id" in str(error)


def test_an_unreachable_host_raises_api_connection_error():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    client = astrada.Astrada(environment="sandbox", base_url="http://127.0.0.1:%d" % port,
                             access_token="t", retries=0)
    with pytest.raises(astrada.ApiConnectionError) as raised:
        client.subaccounts.list_subaccounts()
    assert raised.value.status == 0
    assert isinstance(raised.value, astrada.ApiException)


def test_error_codes_this_sdk_does_not_know_still_reach_the_exception():
    with MockAstrada() as mock:
        mock.respond("get_enrollment_link", status=404,
                     body={"title": "Not Found", "detail": "Gone", "code": "A_CODE_ADDED_LATER"})
        with pytest.raises(astrada.NotFoundException) as raised:
            mock.client.enrollment_links.get_enrollment_link("3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b")
    assert raised.value.code == "A_CODE_ADDED_LATER"


def test_a_400_lists_its_errors():
    with MockAstrada() as mock:
        mock.respond("create_subaccount", status=400, body={
            "title": "Bad Request", "detail": "Invalid body",
            "errors": [{"title": "name", "detail": "is required"}]})
        with pytest.raises(astrada.BadRequestException) as raised:
            mock.client.subaccounts.create_subaccount(
                astrada.SubaccountCreateParams.from_dict({"name": "x", "configurations": {}}))
    assert raised.value.errors == [{"title": "name", "detail": "is required"}]
    assert "name; is required" in str(raised.value)


# Retries and timeouts


def test_a_get_is_retried_after_503_and_succeeds(standin):
    client = make(standin)
    client.subaccounts.list_subaccounts()  # log in first
    before = len(calls(standin, "/subaccounts"))
    fail_next(standin, 503, count=2, retry_after="0")
    page = client.subaccounts.list_subaccounts(limit=2)
    assert len(page.embedded.subaccounts) == 2
    assert len(calls(standin, "/subaccounts")) - before == 3


def test_a_post_is_not_sent_twice(standin):
    client = make(standin)
    client.subaccounts.list_subaccounts()
    fail_next(standin, 503, count=1)
    with pytest.raises(astrada.ServiceException):
        client.subaccounts.create_subaccount(
            astrada.SubaccountCreateParams.from_dict({"name": "x", "configurations": {}}))
    assert len(calls(standin, "/subaccounts")) == 2  # the first list and one POST


def test_429_honours_retry_after_then_raises_rate_limit_error(standin):
    client = make(standin, retries=1)
    client.subaccounts.list_subaccounts()
    fail_next(standin, 429, count=2, retry_after="1")
    started = time.monotonic()
    with pytest.raises(astrada.RateLimitError) as raised:
        client.subaccounts.list_subaccounts()
    assert time.monotonic() - started >= 0.9  # waited the Retry-After once
    assert raised.value.retry_after == 1.0


def test_a_retry_after_longer_than_60_seconds_ends_the_retries(standin):
    client = make(standin)
    client.subaccounts.list_subaccounts()
    before = len(calls(standin, "/subaccounts"))
    fail_next(standin, 429, count=3, retry_after="120")
    started = time.monotonic()
    with pytest.raises(astrada.RateLimitError) as raised:
        client.subaccounts.list_subaccounts()
    assert time.monotonic() - started < 5
    assert raised.value.retry_after == 120.0
    assert len(calls(standin, "/subaccounts")) - before == 1


def test_retry_after_as_an_http_date():
    import email.utils

    when = email.utils.formatdate(time.time() + 30, usegmt=True)
    error = astrada.RateLimitError(status=429, headers={"Retry-After": when})
    assert 25 <= error.retry_after <= 31
    past = astrada.RateLimitError(status=429, headers={"Retry-After": "Wed, 21 Oct 2015 07:28:00 GMT"})
    assert past.retry_after == 0.0


class _StallingServer:
    """Answers every request with headers promising 100 bytes, sends 10, then stalls or hangs up."""

    def __init__(self, hang_up):
        import threading

        self.hang_up = hang_up
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(5)
        self.url = "http://127.0.0.1:%d" % self.sock.getsockname()[1]
        self.release = threading.Event()
        self.requests = 0
        threading.Thread(target=self._serve, daemon=True).start()

    def _serve(self):
        while True:
            try:
                conn, _ = self.sock.accept()
            except OSError:
                return
            self.requests += 1
            conn.recv(65536)
            conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
                         b"Content-Length: 100\r\n\r\n{\"_embedde")
            if not self.hang_up:
                self.release.wait(10)
            conn.close()

    def close(self):
        self.release.set()
        self.sock.close()


@pytest.mark.parametrize("hang_up", [False, True], ids=["stalled-body", "dropped-connection"])
def test_a_body_that_does_not_arrive_raises_api_connection_error(hang_up):
    server = _StallingServer(hang_up)
    try:
        client = astrada.Astrada(environment="sandbox", base_url=server.url, access_token="t",
                                 timeout=0.5)
        with pytest.raises(astrada.ApiConnectionError) as raised:
            client.subaccounts.list_subaccounts()
        assert raised.value.status == 0
        assert "No complete answer from %s/subaccounts" % server.url in str(raised.value)
        with pytest.raises(astrada.ApiConnectionError):
            client.request("GET", "/subaccounts")
    finally:
        server.close()


def test_retries_can_be_turned_off(standin):
    client = make(standin, retries=0)
    client.subaccounts.list_subaccounts()
    fail_next(standin, 503, count=1)
    with pytest.raises(astrada.ServiceException):
        client.subaccounts.list_subaccounts()


def test_default_timeout_is_set_on_every_client(standin):
    client = make(standin)
    assert client.configuration.timeout == 60.0
    assert client.api_client.rest_client.default_timeout == 60.0
    assert client.auth is not None and client.auth.timeout == 60.0
    assert make(standin, timeout=5).banking_api_client.rest_client.default_timeout == 5.0


# Responses the SDK does not fully know


def test_an_unknown_enum_value_in_a_response_is_kept():
    with MockAstrada() as mock:
        answer = next(r.body for r in mock.routes if r.operation == "get_card_subscription")
        changed = dict(answer, state="a-state-added-later", deactivationReason="a-reason-added-later",
                       aFieldAddedLater={"x": 1})
        mock.respond("get_card_subscription", body=changed)
        subscription = mock.client.card_subscription.get_card_subscription(
            "3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b")
    assert subscription.state == "a-state-added-later"
    assert subscription.deactivation_reason is not None
    assert subscription.deactivation_reason.value == "a-reason-added-later"


def test_a_request_with_an_unknown_enum_value_is_still_refused():
    with pytest.raises(ValueError):
        astrada.EnrollmentLinkCreateParams(subaccount_id="3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b",
                                           kind="cardholder", starting_point="nowhere")
    with pytest.raises(ValueError):
        astrada.CardSubscriptionUpdateParams.from_dict({"state": "deactivated",
                                                        "deactivationReason": "not-a-reason"})


# Pagination


def test_paginate_follows_the_cursor(standin):
    client = make(standin)
    ids = [s.id for s in astrada.paginate(client.subaccounts.list_subaccounts, limit=2)]
    assert len(ids) == 5 and len(set(ids)) == 5
    assert [c["query"] for c in calls(standin, "/subaccounts")][0] == "limit=2"
    assert len(calls(standin, "/subaccounts")) == 3


def test_paginate_banking_lists(standin):
    client = make(standin)
    links = list(astrada.paginate(client.banking.bank_links.list_bank_links))
    assert [link.id for link in links] == [
        "enrollment_standin_0", "enrollment_standin_1", "enrollment_standin_2"]


def test_paginate_offset_lists():
    with MockAstrada() as mock:
        pages = {
            None: {"next": {"href": "/card-subscriptions?offset=2&limit=2"}},
            "2": {},
        }

        def answer(call):
            offset = call.query.get("offset", [None])[0]
            body = next(r.body for r in mock.routes if r.operation == "list_card_subscriptions")
            body = json.loads(json.dumps(body))
            body["_links"] = {"self": {"href": "/card-subscriptions"}, **pages[offset]}
            return 200, body

        mock.respond("list_card_subscriptions", handler=answer)
        items = list(astrada.paginate(mock.client.card_subscription.list_card_subscriptions, limit=2))
    assert len(mock.calls) == 2
    assert mock.calls[1].query["offset"] == ["2"]
    assert items


# The sandbox check


SIMULATION = dict(card_id="3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b", type="authorization", amount=100)


def _no_requests(client, monkeypatch):
    sent = []

    def refuse(*args, **kwargs):
        sent.append(args)
        raise AssertionError("a request was sent")

    for api_client in (client.api_client, client.sandbox_api_client):
        monkeypatch.setattr(api_client.rest_client.pool_manager, "request", refuse)
    if client.auth is not None:
        monkeypatch.setattr(client.auth.pool_manager, "request", refuse)
    return sent


@pytest.mark.parametrize("settings", [
    dict(environment="production"),
    dict(environment="production", base_url="https://api.sandbox.astrada.co"),
    dict(environment="sandbox", base_url="https://proxy.example.com"),
    dict(environment="production", base_url="https://proxy.example.com", sandbox_base_url=True),
    dict(environment="sandbox", base_url="https://api.astrada.co"),
    dict(environment="sandbox", base_url="https://api.astrada.co", sandbox_base_url=True),
    dict(environment="sandbox", base_url="https://API.Astrada.co/", sandbox_base_url=True),
    dict(environment="sandbox", base_url="https://api.astrada.co:443", sandbox_base_url=True),
    dict(environment="sandbox", base_url="https://other.astrada.co", sandbox_base_url=True),
    dict(environment="sandbox", base_url="https://astrada.co", sandbox_base_url=True),
])
def test_sandbox_calls_are_refused_before_any_request(settings, monkeypatch):
    client = astrada.Astrada("a", "b", "c", **settings)
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.SandboxOnlyError):
        client.sandbox.simulate_transaction(astrada.sandbox.SimulateTransactionRequest(**SIMULATION))
    with pytest.raises(astrada.SandboxOnlyError):
        client.request("POST", "/simulate/transactions", body={"cardId": "x"})
    assert sent == []


def test_a_generated_sandbox_client_used_directly_is_checked_too(monkeypatch):
    configuration = astrada.sandbox.Configuration(host="https://api.astrada.co", access_token="t")
    api = astrada.sandbox.SandboxSimulationApi(astrada.sandbox.ApiClient(configuration))
    with pytest.raises(astrada.SandboxOnlyError):
        api.simulate_transaction(astrada.sandbox.SimulateTransactionRequest(**SIMULATION))


def test_sandbox_calls_pass_on_the_sandbox_and_on_a_marked_base_url(standin):
    assert astrada.Astrada("a", "b", "c", environment="sandbox").base_url == astrada.Environment.SANDBOX
    client = make(standin, sandbox_base_url=True)
    client.sandbox.simulate_transaction(astrada.sandbox.SimulateTransactionRequest(**SIMULATION))
    assert calls(standin, "/simulate/transactions")


def test_sandbox_error_is_not_an_api_error():
    assert not issubclass(astrada.SandboxOnlyError, astrada.ApiException)


# astrada.testing


def test_mock_answers_every_operation_from_the_definition():
    mock = MockAstrada()
    operations = {route.operation for route in mock.routes}
    assert {"list_subaccounts", "list_bank_links", "simulate_transaction"} <= operations
    page = mock.client.subaccounts.list_subaccounts()
    assert page.embedded.subaccounts
    assert mock.calls[-1].operation == "list_subaccounts"


def test_mock_overrides_and_handlers():
    with MockAstrada() as mock:
        mock.respond("get_subaccount", handler=lambda call: (404, {"title": "Not Found",
                                                                    "detail": call.path}))
        with pytest.raises(astrada.NotFoundException) as raised:
            mock.client.subaccounts.get_subaccount("3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b")
        assert raised.value.detail == "/subaccounts/3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b"
        with pytest.raises(ValueError):
            mock.respond("no_such_operation", body={})
        mock.reset()
        assert mock.client.subaccounts.get_subaccount("3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b")


def test_mock_records_request_bodies_and_refuses_login():
    with MockAstrada() as mock:
        mock.client.enrollment_links.create_enrollment_link(astrada.EnrollmentLinkCreateParams(
            subaccount_id="3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b", kind="team"))
        assert mock.calls[-1].body["kind"] == "team"
        mock.refuse_login()
        with pytest.raises(astrada.AuthenticationError):
            mock.client.subaccounts.list_subaccounts()


def test_mock_keeps_the_sandbox_check():
    with MockAstrada(environment="production") as mock:
        with pytest.raises(astrada.SandboxOnlyError):
            mock.client.sandbox.simulate_transaction(
                astrada.sandbox.SimulateTransactionRequest(**SIMULATION))
        assert mock.calls == []


def test_request_reaches_endpoints_without_a_method(standin):
    client = make(standin)
    body = client.request("GET", "/subaccounts", query={"limit": 1})
    assert len(body["_embedded"]["subaccounts"]) == 1


def test_request_logs_in_retries_only_idempotent_calls_and_raises_typed_errors(standin):
    client = make(standin)
    # The stand-in answers 401 without the login's bearer token, so a body means it was sent.
    assert client.request("GET", "/subaccounts")["_embedded"]["subaccounts"]
    before = len(calls(standin, "/subaccounts"))
    fail_next(standin, 503, count=1, retry_after="0")
    assert client.request("GET", "/subaccounts", query={"limit": 1})
    assert len(calls(standin, "/subaccounts")) - before == 2  # a GET is retried
    fail_next(standin, 503, count=1)
    with pytest.raises(astrada.ServiceException):
        client.request("POST", "/subaccounts", body={"name": "x", "configurations": {}})
    assert len(calls(standin, "/subaccounts")) - before == 3  # a POST is sent once
    with pytest.raises(astrada.NotFoundException):
        client.request("GET", "/subaccounts/00000000-0000-0000-0000-000000000000")


@pytest.mark.parametrize("path", ["subaccounts", ".example.com/x", "/subaccounts?limit=1",
                                  "/%2e%2e/simulate/transactions"])
def test_request_refuses_a_path_that_could_change_the_host_or_slip_past_the_check(path, monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.ApiValueError):
        client.request("GET", path)
    assert sent == []


@pytest.mark.parametrize("path", ["/./simulate/transactions", "//simulate/transactions",
                                  "/subaccounts/../simulate/transactions", "/simulate",
                                  "/%73imulate/transactions", "/Simulate/transactions"])
def test_request_checks_simulate_paths_after_normalising_them(path, monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.SandboxOnlyError):
        client.request("POST", path, body={})
    assert sent == []


def test_close_releases_the_login_connections_too(standin):
    client = make(standin)
    client.subaccounts.list_subaccounts()
    assert client.auth.pool_manager.pools
    client.close()
    assert not client.auth.pool_manager.pools


# Banking operations that need banking:admin


def test_an_operation_needing_a_scope_names_it_for_a_client_without_it(standin):
    client = make(standin)
    with pytest.raises(astrada.ScopeRequiredError) as raised:
        client.banking.bank_subscriptions.list_bank_subscriptions()
    error = raised.value
    assert isinstance(error, astrada.ForbiddenException)
    assert isinstance(error, astrada.ApiException)
    assert (error.status, error.operation, error.required_scope) == (
        403, "list_bank_subscriptions", "banking:admin")
    assert str(error).startswith(
        "(403) list_bank_subscriptions needs the `banking:admin` scope. The likely cause is that "
        "your API client does not have it; if so, ask Astrada to enable it. A 403 can also mean "
        "the resource is not this account's.")
    assert "staff" not in str(error).lower() and "customer" not in str(error).lower()


def test_a_client_with_the_scope_reaches_those_operations(standin):
    from standin.server import STAFF_CLIENT_ID

    make(standin, client_id=STAFF_CLIENT_ID).banking.bank_subscriptions.list_bank_subscriptions()


def test_other_403s_stay_forbidden_exception():
    with MockAstrada() as mock:
        mock.respond("list_bank_links", status=403, body={"title": "Forbidden", "detail": "no"})
        with pytest.raises(astrada.ForbiddenException) as raised:
            mock.client.banking.bank_links.list_bank_links()
    assert not isinstance(raised.value, astrada.ScopeRequiredError)


def test_docstrings_name_the_scope_first():
    import inspect

    from astrada.banking import _staff_only

    assert _staff_only.OPERATIONS
    for op in _staff_only.OPERATIONS:
        for api in astrada.Astrada("a", "b", "c", environment="sandbox").banking.__dict__.values():
            method = getattr(api, op["operation"], None)
            if method is not None:
                doc = inspect.getdoc(method) or ""
                assert doc.startswith("Needs %s. If your API client does not have the `%s` scope"
                                      % (op["scope"], op["scope"])), op


# Bulk-feed file simulations


REFERENCES = {"gl": "R123456", "smartdata": "G1234567", "vbds": "1_123_45_6789",
              "vcf": "1_123_45_6789"}


@pytest.mark.parametrize("kind", ["gl", "smartdata", "vbds", "vcf"])
def test_simulate_bulk_feed_file_picks_the_file_kind(kind, standin):
    client = make(standin, sandbox_base_url=True)
    client.sandbox.simulate_bulk_feed_file(type=kind, network_reference=REFERENCES[kind],
                                           card_count=2)
    path = {"gl": "amex-gl"}.get(kind, kind)
    assert calls(standin, "/simulate/ingestion/" + path)


def test_simulate_bulk_feed_file_is_sandbox_only_and_checks_the_kind(monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.SandboxOnlyError):
        client.sandbox.simulate_bulk_feed_file(type="vcf", network_reference="1_123_45_6789")
    for name in ("gl", "smartdata", "vbds", "vcf"):
        method = getattr(client.sandbox, "simulate_bulk_feed_file_" + name)
        request = getattr(astrada.sandbox, "SimulateBulkFeedFile%sRequest" % name.capitalize())
        with pytest.raises(astrada.SandboxOnlyError):
            method(request(network_reference=REFERENCES[name]))
    assert sent == []
    with pytest.raises(ValueError):
        astrada.Astrada("a", "b", "c", environment="sandbox").sandbox.simulate_bulk_feed_file(
            type="csv", network_reference="x")


def test_marking_the_production_host_as_sandbox_is_refused(monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="sandbox",
                             base_url="https://api.astrada.co", sandbox_base_url=True)
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.SandboxOnlyError):
        client.sandbox.simulate_bulk_feed_file(type="vcf", network_reference="1_123_45_6789")
    assert sent == []


# Login transport


def test_a_refused_login_is_sent_once_not_retried(standin):
    client = make(standin, client_secret="wrong")  # default retries
    with pytest.raises(astrada.AuthenticationError):
        client.subaccounts.list_subaccounts()
    assert len(calls(standin, TOKEN_PATH)) == 1


def test_a_login_answering_503_is_retried_and_succeeds(standin):
    client = make(standin)
    fail_next(standin, 503, count=1, retry_after="0")
    client.subaccounts.list_subaccounts()
    assert len(calls(standin, TOKEN_PATH)) == 2


@pytest.mark.parametrize("status, error", [(429, astrada.RateLimitError),
                                           (500, astrada.ServiceException),
                                           (502, astrada.ServiceException),
                                           (503, astrada.ServiceException)])
def test_a_login_failing_on_astradas_side_is_retried_then_not_an_authentication_error(
        standin, status, error):
    client = make(standin, retries=1)
    fail_next(standin, status, count=5, retry_after="0")
    with pytest.raises(error) as raised:
        client.subaccounts.list_subaccounts()
    assert raised.value.status == status
    assert not isinstance(raised.value, astrada.AuthenticationError)
    assert "not a credentials problem" in raised.value.reason
    assert len(calls(standin, TOKEN_PATH)) == 2  # the first try and one retry
    assert calls(standin, "/subaccounts") == []


def test_a_login_with_retries_off_is_sent_once(standin):
    client = make(standin, retries=0)
    fail_next(standin, 429, count=1, retry_after="0")
    with pytest.raises(astrada.RateLimitError):
        client.subaccounts.list_subaccounts()
    assert len(calls(standin, TOKEN_PATH)) == 1


def test_login_uses_the_client_http_settings():
    import urllib3

    configuration = astrada.Configuration(
        environment="sandbox", account_id="a", client_id="b", client_secret="c", timeout=7,
        retries=4,
    )
    configuration.proxy = "http://proxy.example.com:3128"
    auth = configuration.get_auth_client()
    assert isinstance(auth.pool_manager, urllib3.ProxyManager)
    assert auth.timeout == 7.0
    assert auth.pool_manager.connection_pool_kw["retries"].total == 4

    client = astrada.Astrada("a", "b", "c", environment="sandbox", timeout=9)
    assert client.auth.timeout == 9.0
    assert client.banking_configuration.get_auth_client() is client.auth


def test_a_one_of_field_takes_a_plain_value():
    """countries is a list of codes or "*" (a oneOf): the plain value is accepted and sent as given."""
    from astrada.models.create_subaccount_configurations_visa import (
        CreateSubaccountConfigurationsVISA,
    )

    assert CreateSubaccountConfigurationsVISA(countries=["USA", "CAN"]).to_dict() == {
        "countries": ["USA", "CAN"]
    }
    assert CreateSubaccountConfigurationsVISA(countries="*").to_dict() == {"countries": "*"}
    with pytest.raises(ValueError):
        CreateSubaccountConfigurationsVISA(countries=5)


# Review Bot follow-ups on #149

SUBACCOUNT_ID = "3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b"


def _sandbox_operations():
    spec = json.loads((Path(__file__).parent / "standin" / "openapi-sandbox.json").read_text())
    return sorted(
        re.sub(r"(?<!^)(?=[A-Z])", "_", op["operationId"]).lower()
        for item in spec["paths"].values() for op in item.values()
        if isinstance(op, dict) and "operationId" in op
    )


def test_every_sandbox_operation_is_refused_outside_the_sandbox(monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    operations = _sandbox_operations()
    assert {"delete_subaccount", "delete_card_subscription", "delete_network_bulk_feed"} <= set(operations)
    for name in operations:
        method = getattr(client.sandbox, name)
        # Arguments that pass validation without real data: an id, or an unvalidated model.
        arguments = []
        for parameter in inspect.signature(method).parameters.values():
            if parameter.default is not inspect.Parameter.empty or parameter.name.startswith("_"):
                continue
            annotation = typing.get_args(parameter.annotation)[0] if typing.get_args(parameter.annotation) else parameter.annotation
            if isinstance(annotation, type) and issubclass(annotation, pydantic.BaseModel):
                arguments.append(annotation.model_construct())
            else:
                arguments.append(SUBACCOUNT_ID)
        with pytest.raises(astrada.SandboxOnlyError):
            method(*arguments)
    assert sent == []


def test_the_sandbox_deletes_succeed_and_are_never_retried(standin, monkeypatch):
    client = make(standin, sandbox_base_url=True, timeout=5, retries=2)
    seen = []
    send = client.sandbox_api_client.rest_client.request

    def spy(*args, **kwargs):
        seen.append((kwargs.get("_request_timeout"), kwargs.get("_retries")))
        return send(*args, **kwargs)

    monkeypatch.setattr(client.sandbox_api_client.rest_client, "request", spy)
    client.sandbox.delete_subaccount(SUBACCOUNT_ID)
    assert calls(standin, "/subaccounts/" + SUBACCOUNT_ID)
    assert seen[-1] == ((5.0, 300.0), False)  # connect as configured, read at least 300 s, no retries

    fail_next(standin, 502)
    with pytest.raises(astrada.ServiceException):
        client.sandbox.delete_subaccount(SUBACCOUNT_ID)
    assert len(calls(standin, "/subaccounts/" + SUBACCOUNT_ID)) == 2  # one more, not three


def test_sandbox_calls_to_the_sandbox_host_need_https():
    # The Astrada client refuses such a base URL when it is made (below); the generated sandbox
    # package's own guard refuses it too.
    configuration = astrada.sandbox.Configuration(host="http://api.sandbox.astrada.co", access_token="t")
    configuration.environment = "sandbox"
    api = astrada.sandbox.SandboxSimulationApi(astrada.sandbox.ApiClient(configuration))
    with pytest.raises(astrada.SandboxOnlyError, match="need https"):
        api.simulate_transaction(astrada.sandbox.SimulateTransactionRequest(**SIMULATION))


@pytest.mark.parametrize("countries", ["USA", "**", ["USA", "XXX"], ["USA", "USA"], {}])
def test_countries_refuses_what_the_definition_does_not_allow(countries):
    from astrada.models.create_subaccount_configurations_visa import (
        CreateSubaccountConfigurationsVISA,
    )

    with pytest.raises(ValueError):
        CreateSubaccountConfigurationsVISA(countries=countries)


def test_countries_in_a_response_keeps_a_code_added_later():
    from astrada.models.create_subaccount_configurations_visa import (
        CreateSubaccountConfigurationsVISA,
    )
    from astrada._lenient import lenient

    with lenient():
        parsed = CreateSubaccountConfigurationsVISA.from_dict({"countries": ["USA", "NEW"]})
    assert parsed.to_dict() == {"countries": ["USA", "NEW"]}


def test_a_malformed_retry_after_does_not_hide_the_answer(standin):
    client = make(standin, retries=0)
    client.subaccounts.list_subaccounts()  # log in first
    fail_next(standin, 429, retry_after="1.5")
    with pytest.raises(astrada.RateLimitError):
        client.subaccounts.list_subaccounts()


def test_a_retry_of_your_own_still_raises_the_matching_exception(standin):
    client = make(standin, retries=Retry(total=1, status_forcelist=[503], backoff_factor=0))
    client.subaccounts.list_subaccounts()  # log in first
    fail_next(standin, 503, count=2)
    with pytest.raises(astrada.ServiceException):
        client.subaccounts.list_subaccounts()



@pytest.mark.parametrize("base_url", ["http://api.sandbox.astrada.co", "http://api.astrada.co",
                                      "HTTP://API.Astrada.co/"])
def test_an_astrada_host_over_plain_http_is_refused_before_any_login(base_url):
    with pytest.raises(astrada.ApiValueError, match="need https"):
        astrada.Astrada("a", "b", "c", environment="sandbox", base_url=base_url)


@pytest.mark.parametrize("base_url", ["api.astrada.co", "api.astrada.co:80", "//api.astrada.co",
                                      "ftp://api.astrada.co", "localhost:4010"])
def test_a_base_url_without_http_or_https_is_refused(base_url):
    with pytest.raises(astrada.ApiValueError, match="needs a scheme and a host"):
        astrada.Astrada("a", "b", "c", environment="sandbox", base_url=base_url)


def test_a_local_mock_over_http_is_fine(standin):
    assert make(standin).base_url.startswith("http://127.0.0.1")


@pytest.mark.parametrize("countries", [["USA"], "*"])
def test_countries_in_lenient_mode_still_accepts_valid_values(countries):
    from astrada._lenient import lenient
    from astrada.models.create_subaccount_configurations_visa import (
        CreateSubaccountConfigurationsVISA,
    )

    with lenient():
        assert CreateSubaccountConfigurationsVISA(countries=countries).to_dict() == {"countries": countries}


def test_a_sandbox_delete_refused_with_401_is_sent_once(standin):
    # The Python client does not log in again on a 401 to an API call, so the no-retry delete path
    # and a re-login never meet: the 401 is raised after one send.
    client = make(standin, sandbox_base_url=True)
    client.subaccounts.list_subaccounts()  # log in first
    fail_next(standin, 401)
    with pytest.raises(astrada.UnauthorizedException):
        client.sandbox.delete_subaccount(SUBACCOUNT_ID)
    assert len(calls(standin, "/subaccounts/" + SUBACCOUNT_ID)) == 1


def test_a_base_url_with_spaces_is_used_trimmed(standin):
    assert make(standin, base_url="  %s/  " % standin.url).base_url == standin.url


def test_a_post_on_a_dropped_connection_is_not_sent_again():
    """The connection drops after the POST arrives: urllib3 does not resend it (POST is not in the
    retried methods), so the call fails once instead of creating something twice."""
    import http.server
    import threading

    received = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *args):
            return

        def do_POST(self):
            length = int(self.headers.get("Content-Length") or 0)
            self.rfile.read(length)
            received.append(self.path)
            self.connection.close()  # no answer at all

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        client = astrada.Astrada(environment="production", access_token="t",
                                 base_url="http://127.0.0.1:%d" % server.server_port, retries=2)
        with pytest.raises(astrada.ApiConnectionError):
            client.request("POST", "/subaccounts", body={"name": "x"})
    finally:
        server.shutdown()
        server.server_close()
    assert received == ["/subaccounts"]


@pytest.mark.parametrize("operation,model", [
    ("get_transaction_message", "TransactionMessage"),
    ("get_transaction", "Transaction"),
    ("get_subaccount", "Subaccount"),
])
def test_to_json_round_trips_the_definition_examples(operation, model):
    """to_json() writes UUIDs and datetimes as JSON (it used to raise TypeError)."""
    route = next(r for r in MockAstrada().routes if r.operation == operation)
    cls = getattr(astrada, model)
    parsed = cls.from_dict(route.body)
    again = cls.from_json(parsed.to_json())
    assert again == parsed


@pytest.mark.parametrize("raw,aware", [("2026-01-01T10:00:00", False), ("2026-01-01T10:00:00Z", True)])
def test_transaction_message_date_time_keeps_wall_time_or_utc_and_round_trips(raw, aware, monkeypatch):
    """Mastercard sends the merchant's local time without an offset (a naive datetime); Visa and
    Amex send UTC (aware). Neither depends on the host time zone, and to_json writes each back."""
    import time

    route = next(r for r in MockAstrada().routes if r.operation == "get_transaction_message")
    zones = ("UTC", "America/Los_Angeles", "Asia/Tokyo") if hasattr(time, "tzset") else (None,)
    try:
        for zone in zones:
            if zone is not None:  # time.tzset is not on Windows: there the host zone is used as is
                monkeypatch.setenv("TZ", zone)
                time.tzset()
            message = astrada.TransactionMessage.from_dict({**route.body, "dateTime": raw})
            assert (message.date_time.tzinfo is not None) is aware
            assert message.date_time.replace(tzinfo=None).isoformat() == "2026-01-01T10:00:00"
            assert json.loads(message.to_json())["dateTime"] == ("2026-01-01T10:00:00Z" if aware else raw)
    finally:
        monkeypatch.undo()
        if hasattr(time, "tzset"):
            time.tzset()


def test_mint_sdk_access_token_uses_the_sdk_client_and_never_returns_the_backend_token(standin, monkeypatch):
    from standin.server import STAFF_CLIENT_ID

    client = make(standin)
    backend = client.auth.get_access_token()[len("Bearer "):]
    sent = []
    send = client.auth.pool_manager.request

    def spy(method, url, **kwargs):
        sent.append(kwargs.get("fields"))
        return send(method, url, **kwargs)

    monkeypatch.setattr(client.auth.pool_manager, "request", spy)
    token = client.mint_sdk_access_token(STAFF_CLIENT_ID, CLIENT_SECRET)
    assert token and token != backend and not token.startswith("Bearer ")
    assert sent[-1]["client_id"] == STAFF_CLIENT_ID and "scope" not in sent[-1]
    assert client.mint_sdk_access_token(STAFF_CLIENT_ID, CLIENT_SECRET) != token  # a new token each call


def test_mint_sdk_access_token_checks_the_granted_scopes(standin):
    from standin.server import STAFF_CLIENT_ID

    client = make(standin)
    assert client.mint_sdk_access_token(
        STAFF_CLIENT_ID, CLIENT_SECRET, allowed_scopes=["subaccounts:read", "cards:read", "banking:admin"])
    with pytest.raises(astrada.UnexpectedScopesError, match="banking:admin") as error:
        client.mint_sdk_access_token(STAFF_CLIENT_ID, CLIENT_SECRET, allowed_scopes=["subaccounts:read", "cards:read"])
    assert error.value.extra_scopes == ["banking:admin"]


def test_mint_sdk_access_token_refuses_the_backend_client_unless_it_calls_the_sandbox(monkeypatch):
    for client in (astrada.Astrada("acct", "backend-client", "secret", environment="production"),
                   # The label says sandbox, the host is production: refused too.
                   astrada.Astrada("acct", "backend-client", "secret", environment="sandbox",
                                   base_url="https://api.astrada.co")):
        sent = _no_requests(client, monkeypatch)
        with pytest.raises(astrada.ApiValueError, match="SDK client"):
            client.mint_sdk_access_token("backend-client", "secret")
        assert sent == []
    client = astrada.Astrada("acct", "backend-client", "secret", environment="production")
    for empty in (("", "secret"), ("sdk", ""), (None, "secret")):
        with pytest.raises(astrada.ApiValueError, match="empty"):
            client.mint_sdk_access_token(*empty)
    with pytest.raises(astrada.ApiValueError, match="account_id"):
        astrada.Astrada(environment="sandbox", access_token="given").mint_sdk_access_token("sdk", "s")


def test_request_sends_sandbox_only_deletes_once_and_only_in_the_sandbox(standin, monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    for path in ("/subaccounts/s1", "/card-subscriptions/c1", "/network-bulk-feeds/f1", "/x/../subaccounts/s1"):
        with pytest.raises(astrada.SandboxOnlyError):
            client.request("DELETE", path)
    assert sent == []
    sandbox = make(standin, sandbox_base_url=True)
    sandbox.subaccounts.list_subaccounts()  # log in first
    path = "/subaccounts/00000000-0000-4000-8000-000000000001"
    fail_next(standin, 503, count=1, retry_after="0")
    with pytest.raises(astrada.ServiceException):
        sandbox.request("DELETE", path)
    assert len(calls(standin, path)) == 1  # never sent twice


def test_mint_sdk_access_token_raises_the_login_error_for_a_refused_sdk_client(standin):
    client = make(standin)
    with pytest.raises(astrada.AuthenticationError):
        client.mint_sdk_access_token("sdk-client", "wrong-secret")


def test_the_readme_allowed_scopes_take_the_sdk_client_and_refuse_a_backend_scope(standin):
    from standin.server import SDK_CLIENT_ID, STAFF_CLIENT_ID

    readme = ["subaccounts:read", "card-subscriptions:read", "card-subscriptions:write", "card-verifications:read",
              "card-verifications:write", "enrollment-methods:write", "banking:read", "banking:write"]
    client = make(standin)
    assert client.mint_sdk_access_token(SDK_CLIENT_ID, CLIENT_SECRET, allowed_scopes=readme)
    with pytest.raises(astrada.UnexpectedScopesError, match="banking:admin"):
        client.mint_sdk_access_token(STAFF_CLIENT_ID, CLIENT_SECRET, allowed_scopes=readme)


@pytest.mark.parametrize("path", ["/subaccounts/s1#/x", "/subaccounts/s1?x=1", "/subaccounts%2Fs1",
                                  "/a%2e%2e/b", "/x\\y", "/x%zz", "subaccounts", "/simu\tlate/transactions",
                                  "/x/.\t./subaccounts/s1", "/x\r\ny", "/x%5Cy", "/x%3Fy", "/x%23y", "/x%0Ay",
                                  "/simulate ", "/subaccounts/s1/. ", "/x y", "/x%00", "/x%1f", "/x%7F"])
def test_request_path_rule_refuses(path, monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.ApiValueError):
        client.request("GET", path)
    assert sent == []


@pytest.mark.parametrize("method,path", [("DELETE", "/x/..//subaccounts/s1"), ("DELETE", "/subaccounts//s1/"),
                                         ("delete", "/Card-Subscriptions/c1"), ("POST", "//simulate/transactions"),
                                         ("POST", "/simulate/transactions/t1"), ("DELETE", "/network-bulk-feeds/f1")])
def test_request_checks_the_normalised_path_against_the_generated_routes(method, path, monkeypatch):
    client = astrada.Astrada("a", "b", "c", environment="production")
    sent = _no_requests(client, monkeypatch)
    with pytest.raises(astrada.SandboxOnlyError):
        client.request(method, path)
    assert sent == []


def test_the_generated_routes_cover_the_sandbox_definition():
    from astrada._sandbox_routes import SANDBOX_ROUTES

    spec = json.load(open(os.path.join(os.path.dirname(__file__), "standin", "openapi-sandbox.json")))
    for path, item in spec["paths"].items():
        for method in item:
            if method in ("get", "put", "post", "delete", "patch"):
                sample = re.sub(r"\{[^}]+\}", "x1", path).lower()
                assert any(m == method.upper() and p.match(sample) for m, p in SANDBOX_ROUTES), path


def test_allowed_scopes_refuses_a_string_and_a_login_that_states_no_scope(standin, monkeypatch):
    from standin.server import SDK_CLIENT_ID

    client = make(standin)
    with pytest.raises(astrada.ApiValueError, match="list"):
        client.mint_sdk_access_token(SDK_CLIENT_ID, CLIENT_SECRET, allowed_scopes="subaccounts:read")
    real = astrada.auth_client.AuthenticationClient._request_new_token

    for stated in (["not", "a", "string"], "", "   ", None):
        def no_scope(self, stated=stated):
            token = real(self)
            token.scope = stated
            return token

        monkeypatch.setattr(astrada.auth_client.AuthenticationClient, "_request_new_token", no_scope)
        with pytest.raises(astrada.UnexpectedScopesError, match="did not state") as error:
            client.mint_sdk_access_token(SDK_CLIENT_ID, CLIENT_SECRET, allowed_scopes=["subaccounts:read"])
        assert error.value.extra_scopes == []


def test_unexpected_scopes_error_survives_pickling():
    import pickle

    copy = pickle.loads(pickle.dumps(astrada.UnexpectedScopesError(["banking:admin"], "extra")))
    assert copy.extra_scopes == ["banking:admin"] and str(copy) == "extra"


def test_request_sends_query_lists_as_repeated_pairs(standin):
    client = make(standin)
    client.request("GET", "/subaccounts", query={"status": ["a", None, "b"], "network": ("VISA",), "gone": None,
                                                  "limit": 5})
    sent = [c for c in calls(standin, "/subaccounts")][-1]
    assert sent["query"] == "status=a&status=b&network=VISA&limit=5"

