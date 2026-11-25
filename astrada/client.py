# coding: utf-8
"""The Astrada client: one object for the card APIs, the Banking API and the sandbox simulations.
Hand-written; not generated.

    import astrada

    client = astrada.Astrada(
        account_id="...", client_id="...", client_secret="...", environment="sandbox"
    )
    page = client.subaccounts.list_subaccounts(limit=10)
    bank_links = client.banking.bank_links.list_bank_links()
    client.sandbox.simulate_transaction(...)

The API groups (``client.subaccounts``, ``client.enrollment_links``, ``client.banking.bank_links``
and the rest) and the ``client.sandbox`` methods are generated from the API definitions in
``astrada/_services.py``, ``astrada/banking/_services.py`` and ``astrada/sandbox/_services.py``,
so a new group or method appears here with the next release.
"""

import json
import re
import os
from urllib.parse import unquote, urlsplit
from typing import Any, Dict, Iterable, List, Optional, Union

from urllib3.util.retry import Retry

from astrada import _sandbox_guard
from astrada import banking as _banking
from astrada import sandbox as _sandbox
from astrada._sandbox_routes import SANDBOX_ROUTES
from astrada._services import Services
from astrada.api_client import ApiClient
from astrada.auth_client import AuthenticationClient
from astrada.banking._services import Services as _BankingServices
from astrada.configuration import Configuration
from astrada.exceptions import ApiException, ApiValueError, SandboxOnlyError, UnexpectedScopesError
from astrada.sandbox._services import Services as _SandboxServices


class Banking(_BankingServices):
    """The Banking API groups: ``bank_links``, ``bank_accounts``, ``bank_subscriptions``,
    ``bank_transactions`` and ``transaction_matches``."""


class Sandbox(_SandboxServices):
    """The sandbox-only methods: simulations (test transactions and network bulk-feed files) and
    the deletes that clear test data (``delete_subaccount``, ``delete_card_subscription``,
    ``delete_network_bulk_feed``). The deletes cannot be undone and are never retried by the SDK (a
    second call while the first runs is not safe). A delete that finishes within the sandbox
    gateway's 29 seconds answers when done; a longer one gets a 504 while it keeps running. Then read
    the resource every few seconds: 404 means it finished. A delete runs for at most about 5
    minutes, so if the resource still answers after 6 minutes, the first delete stopped part-way
    and calling it again is safe (finished steps are skipped).

    Every method raises :class:`astrada.SandboxOnlyError` before sending anything (not even the
    login) unless the client was made with ``environment="sandbox"`` and calls the sandbox API, or
    a custom ``base_url`` marked with ``sandbox_base_url=True``.
    """

    BULK_FEED_FILE_TYPES = ("gl", "smartdata", "vbds", "vcf")
    """The bulk-feed file kinds: American Express GL, Mastercard SmartData, Visa VBDS and VCF."""

    def simulate_bulk_feed_file(self, type: str, network_reference: str, **fields: Any) -> Any:
        """Simulate the network delivering a bulk-feed file for a feed you created.

        Picks ``simulate_bulk_feed_file_gl``, ``_smartdata``, ``_vbds`` or ``_vcf`` by ``type``.

        :param type: ``"gl"`` (American Express), ``"smartdata"`` (Mastercard), ``"vbds"`` or
            ``"vcf"`` (Visa)
        :param network_reference: the feed's network reference, as given when it was created
        :param fields: the other request fields, by their Python names (``card_count``,
            ``new_card_count``, ``transactions_per_card``)
        :raises SandboxOnlyError: on a client that is not set up for the sandbox
        """
        kind = type.strip().lower()
        if kind not in self.BULK_FEED_FILE_TYPES:
            raise ValueError(
                "type must be one of %s, not %r" % (", ".join(self.BULK_FEED_FILE_TYPES), type)
            )
        method = getattr(self, "simulate_bulk_feed_file_" + kind)
        request_class = getattr(
            _sandbox, "SimulateBulkFeedFile%sRequest" % kind.capitalize()
        )
        return method(request_class(network_reference=network_reference, **fields))


class Astrada(Services):
    """The Astrada API client.

    :param account_id: your Astrada account ID; default: the ``ASTRADA_ACCOUNT_ID`` environment
        variable
    :param client_id: your API client's ID; default: ``ASTRADA_CLIENT_ID``
    :param client_secret: your API client's secret; default: ``ASTRADA_CLIENT_SECRET``
    :param environment: ``"sandbox"`` or ``"production"`` (required, so a sandbox script never
        reaches production by accident). Credentials belong to one environment.
    :param timeout: seconds to wait for each request (default 60)
    :param retries: retries after a failed attempt (default 2), or a urllib3 ``Retry``. Connection
        failures are retried for every call except the sandbox deletes (never retried); 429 and 5xx
        only for GET, HEAD, PUT, DELETE and OPTIONS, so a POST or PATCH is never sent twice.
        Retry-After is honoured.
    :param access_token: a token you got yourself, instead of the three credentials
    :param base_url: another base URL for the environment (a proxy, or a local mock server)
    :param sandbox_base_url: mark ``base_url`` as a sandbox, so ``client.sandbox`` calls go to it
        (only with ``environment="sandbox"``)

    The client logs in on the first call and keeps the token until shortly before it expires; the
    card APIs, ``client.banking`` and ``client.sandbox`` share that one login. A refused login
    raises :class:`astrada.AuthenticationError` with the reason the login service gave.
    Use it as a context manager, or call :meth:`close`, to release its connections.
    """

    def __init__(
        self,
        account_id: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        *,
        environment: str,
        timeout: Optional[float] = None,
        retries: Union[None, int, Retry] = None,
        access_token: Optional[str] = None,
        base_url: Optional[str] = None,
        sandbox_base_url: bool = False,
    ) -> None:
        if access_token is None:
            account_id = account_id or os.environ.get("ASTRADA_ACCOUNT_ID")
            client_id = client_id or os.environ.get("ASTRADA_CLIENT_ID")
            client_secret = client_secret or os.environ.get("ASTRADA_CLIENT_SECRET")
            missing = [
                name
                for name, value in (
                    ("account_id", account_id),
                    ("client_id", client_id),
                    ("client_secret", client_secret),
                )
                if not value
            ]
            if missing:
                raise ValueError(
                    "Missing %s: pass them, or set ASTRADA_ACCOUNT_ID, ASTRADA_CLIENT_ID and "
                    "ASTRADA_CLIENT_SECRET" % ", ".join(missing)
                )

        _require_https_for_astrada(base_url)
        settings: Dict[str, Any] = dict(
            environment=environment,
            host=base_url.strip().rstrip("/") if base_url else None,
            account_id=account_id,
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            timeout=timeout,
            retries=retries,
            sandbox_base_url=sandbox_base_url,
        )
        self.configuration = Configuration(**settings)
        """The main package's Configuration (host, timeout, retries, logging)."""
        self.api_client = ApiClient(self.configuration)
        """The ApiClient the card API groups use."""
        self.auth: Optional[AuthenticationClient] = self.configuration.get_auth_client()
        """The login and token cache, shared with ``banking`` and ``sandbox``."""
        settings.update(host=self.configuration.host, auth_client=self.auth)

        self.banking_configuration = _banking.Configuration(**settings)
        self.banking_api_client = _banking.ApiClient(self.banking_configuration)
        self.sandbox_configuration = _sandbox.Configuration(**settings)
        self.sandbox_api_client = _sandbox.ApiClient(self.sandbox_configuration)
        super().__init__(self.api_client)
        self.banking = Banking(self.banking_api_client)
        """The Banking API: bank links, bank accounts, bank subscriptions, bank transactions and
        transaction matches."""
        self.sandbox = Sandbox(self.sandbox_api_client)
        """The sandbox-only simulations and deletes; refused outside the sandbox."""

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Dict[str, Any]] = None,
        body: Any = None,
    ) -> Any:
        """Call an endpoint this SDK has no method for, with the same login, retries and errors.

        Returns the parsed JSON body, or None for an empty one. Every sandbox-only operation
        (listed from the sandbox API definition when the SDK is built, such as
        ``DELETE /subaccounts/{id}``) and any ``/simulate`` path get the same sandbox check as
        ``client.sandbox``, and the sandbox-only deletes are never retried and wait as long as
        ``client.sandbox``'s. The path follows one rule, the same in the three SDKs: ``.`` and
        ``..`` are resolved and repeated or trailing slashes dropped; a raw ``?``, ``#``, ``\\``,
        space or control character, a broken percent escape, or an encoded ``/``, ``\\``, ``.``,
        ``?``, ``#`` or control character is refused (send a space as ``%20``). The checks run on
        the path that is sent.

        :param method: ``"GET"``, ``"POST"``, ``"PATCH"``, ``"PUT"`` or ``"DELETE"``
        :param path: the path, starting with ``/``, for example ``"/subaccounts"``
        :param query: query parameters; a list, tuple or set is sent as one pair per item, and
            None values are left out
        :param body: a JSON-serialisable request body
        :raises ApiException: (a subclass of) for any status outside 2xx
        :raises SandboxOnlyError: a sandbox-only operation or a ``/simulate`` path on a client not
            set up for the sandbox
        :raises ApiValueError: a path the rule above refuses
        """
        path = _normalise_path(path)
        # Compared decoded, so an encoded letter (/%73imulate) does not slip past the check.
        decoded = unquote(path).lower()
        verb = str(method).upper()
        api_client: Any = self.api_client
        sandbox_only = any(m == verb and pattern.match(decoded) for m, pattern in SANDBOX_ROUTES)
        if sandbox_only or decoded == "/simulate" or decoded.startswith("/simulate/"):
            _sandbox_guard.check(self.configuration)
            # Through the sandbox client that client.sandbox uses: its deletes are never retried
            # and wait longer.
            api_client = self.sandbox_api_client
        method, url, headers, serialized, _ = api_client.param_serialize(
            method=verb,
            resource_path=path,
            query_params=_query_pairs(query),
            header_params={"Accept": "application/json", "Content-Type": "application/json"},
            body=body,
            auth_settings=["main-auth"],
        )
        response = api_client.call_api(method, url, header_params=headers, body=serialized)
        response.read()
        text = response.data.decode("utf-8") if response.data else ""
        if not 200 <= response.status <= 299:
            raise ApiException.from_response(http_resp=response, body=text, data=None)
        return json.loads(text) if text.strip() else None

    def mint_sdk_access_token(
        self,
        client_id: str,
        client_secret: str,
        allowed_scopes: Optional[Iterable[str]] = None,
    ) -> str:
        """A short-lived token for the Unified Enrollment SDK v2 in the browser (its
        ``getAccessToken`` option): your backend calls this and returns the token to the page as
        plain text, with no ``Bearer `` in front.

        It is minted with your **SDK client**: the separate ``client_id`` and ``client_secret``
        Astrada gives you for the browser. The token carries every scope that SDK client holds (the
        login does not narrow it on request), so that client must hold only the scopes the browser
        SDK needs. Never this client's own credentials: their token would carry every backend
        scope. This client's ``client_id`` is refused unless this client calls the sandbox API (a
        sandbox self sign-up gives one client for both).

        Pass ``allowed_scopes`` to check the token before it leaves your server: if it carries any
        other scope, this raises instead of returning it. The token reaches every subaccount of your
        account, so check on your server that the user may use the ``subaccountId`` the page opens.
        Each call mints a new token (tokens last 5 minutes).

        :raises ApiValueError: an empty ``client_id`` or ``client_secret``; this client's own
            ``client_id`` when this client does not call the sandbox API; a client made with
            ``access_token`` (no account to log in to); ``allowed_scopes`` given as a string
        :raises UnexpectedScopesError: the token carries a scope outside ``allowed_scopes``, or the
            login did not state its scopes (the check relies on the login's ``scope`` field)
        :raises AuthenticationError: the token endpoint refused the SDK client's credentials
        :raises RateLimitError: the token endpoint answered 429, after the retries
        :raises ServiceException: the token endpoint answered 5xx, after the retries
        :raises NotFoundException: no such account (404)
        :raises ApiConnectionError: the token endpoint could not be reached
        """
        if self.auth is None:
            raise ApiValueError(
                "mint_sdk_access_token needs a client made with account_id (not access_token)")
        if not client_id or not client_secret:
            raise ApiValueError(
                "mint_sdk_access_token needs your SDK client's client_id and client_secret "
                "(one of them is empty)")
        if client_id == self.auth.client_id:
            # Keyed on the host this client calls, not its environment label.
            try:
                _sandbox_guard.check(self.configuration)
            except SandboxOnlyError:
                raise ApiValueError(
                    "mint_sdk_access_token takes your SDK client's credentials, not this backend "
                    "client's: its token would carry every scope the backend client has") from None
        if isinstance(allowed_scopes, (str, bytes)):
            raise ApiValueError(
                "allowed_scopes takes a list of scope names, such as [\"subaccounts:read\"], not a "
                "string")
        allowed = None if allowed_scopes is None else set(allowed_scopes)
        sdk_login = AuthenticationClient(
            self.auth.account_id, client_id, client_secret, self.auth.base_path,
            pool_manager=self.auth.pool_manager, timeout=self.auth.timeout,
            retries=self.auth.retries,
        )
        token = sdk_login._request_new_token()
        if allowed is not None:
            # The check covers what the login states in its ``scope`` field.
            if not isinstance(token.scope, str) or not token.scope.strip():
                raise UnexpectedScopesError(
                    [], "The login did not state the scopes of the SDK client's token, so "
                    "allowed_scopes cannot be checked (the token is not returned).")
            extra = sorted(set(token.scope.split()) - allowed)
            if extra:
                raise UnexpectedScopesError(
                    extra, "The SDK client's token carries scopes outside allowed_scopes: %s. Remove "
                    "them from the SDK client (the token is not returned)." % ", ".join(extra))
        return token.access_token

    @property
    def environment(self) -> Optional[str]:
        """``"sandbox"`` or ``"production"``."""
        return self.configuration.environment

    @property
    def base_url(self) -> str:
        """The base URL this client calls."""
        return self.configuration.host

    def close(self) -> None:
        """Release the client's connections, the login's included."""
        for client in (self.api_client, self.banking_api_client, self.sandbox_api_client):
            pool = getattr(client.rest_client, "pool_manager", None)
            if pool is not None:
                pool.clear()
        login_pool = getattr(self.auth, "pool_manager", None)
        if login_pool is not None:
            login_pool.clear()

    def __enter__(self) -> "Astrada":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return "Astrada(environment=%r, base_url=%r)" % (self.environment, self.base_url)


def _require_https_for_astrada(base_url: Optional[str]) -> None:
    """Refuse a base URL without http(s), and a plain-HTTP one on an Astrada host: the login sends
    the client secret to it. A local mock (http://localhost:4010) is fine."""
    if not base_url:
        return
    parts = urlsplit(base_url.strip())
    if parts.scheme.lower() not in ("http", "https") or not parts.hostname:
        # "api.astrada.co" or "api.astrada.co:80" would otherwise be sent over plain http.
        raise ApiValueError(
            "base_url %r needs a scheme and a host, such as https://api.sandbox.astrada.co" % (base_url,))
    hostname = parts.hostname.lower().rstrip(".")
    if (hostname == "astrada.co" or hostname.endswith(".astrada.co")) and parts.scheme.lower() != "https":
        raise ApiValueError(
            "base_url %r is an Astrada host over %s; Astrada hosts need https, as the login "
            "sends the client secret" % (base_url, parts.scheme or "no scheme"))


def _query_pairs(query: Optional[Dict[str, Any]]) -> List[Any]:
    """The query rule shared by the three SDKs: a list, tuple or set is sent as one pair per item
    (``status=a&status=b``), and None values and items are left out."""
    pairs: List[Any] = []
    for key, value in (query or {}).items():
        if value is None:
            continue
        if isinstance(value, (list, tuple, set, frozenset)):
            pairs.extend((key, item) for item in value if item is not None)
        else:
            pairs.append((key, value))
    return pairs


def _normalise_path(path: str) -> str:
    """The one path rule of the generic request method, the same in the three SDKs.

    The path must start with ``/``. A ``?``, ``#``, ``\\``, space or control character in it, a broken
    percent escape, or an encoded ``/``, ``\\``, ``.``, ``?``, ``#`` or control character is refused (so an id containing an encoded slash
    cannot be sent this way). ``.`` and ``..`` segments are resolved and empty segments (repeated
    or trailing slashes) dropped. The result is the path that is sent and checked.
    """
    if not isinstance(path, str) or not path.startswith("/"):
        raise ApiValueError("request() needs a path that starts with '/', got %r" % (path,))
    if re.search(r"[\x00-\x20\x7f]", path):
        raise ApiValueError(
            "request() does not take a space or control character (tab, CR, LF and the like) in the "
            "path; send a space as %%20: %r" % (path,))
    if re.search(r"[?#\\]", path):
        raise ApiValueError(
            "request() does not take a '?', '#' or '\\' in the path (pass query parameters with "
            "query=): %r" % (path,))
    if re.search(r"%(?![0-9a-fA-F]{2})", path):
        raise ApiValueError("request() got a broken percent escape in the path: %r" % (path,))
    if re.search(r"%(2f|5c|2e|3f|23|[01][0-9a-f]|7f)", path, re.IGNORECASE):
        raise ApiValueError(
            "request() does not take an encoded '/', '\\', '.', '?', '#' or control character in the "
            "path: %r" % (path,))
    segments: List[str] = []
    for segment in path.split("/"):
        if segment in ("", "."):
            continue
        if segment == "..":
            if segments:
                segments.pop()
            continue
        segments.append(segment)
    return "/" + "/".join(segments)
