# coding: utf-8
"""OAuth2 client-credentials login with a token cache. Hand-written; not generated.

One :class:`AuthenticationClient` serves every API group of an :class:`astrada.Astrada` client
(the main API and banking), so they share one token. The token is requested on the first call,
cached, and requested again 30 seconds before it expires. A login refused with 400 or 401 raises
:class:`astrada.AuthenticationError` with the token endpoint's own message. A 429 or 5xx from the
token endpoint is retried with backoff like other calls, then raises :class:`astrada.RateLimitError`
or :class:`astrada.ServiceException`, so an outage of the login does not look like bad
credentials. The API call is never sent without a token.
"""

import json
import threading
import time
from typing import Any, Dict, List, Optional, Type, Union

from urllib.parse import urljoin, urlsplit

import urllib3
from urllib3.util.retry import Retry

from astrada._retry import build_login_retry, build_retry, timeout_or_default
from astrada.exceptions import (
    ApiConnectionError,
    ApiException,
    AuthenticationError,
    ForbiddenException,
    NotFoundException,
    RateLimitError,
    ServiceException,
)

_EXPIRY_MARGIN_SECONDS = 30


class AccessToken:
    """An OAuth2 access token from the token endpoint."""

    def __init__(
        self,
        access_token: str,
        token_type: Optional[str],
        expires_in: int,
        scope: Optional[str] = None,
    ) -> None:
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.scope = scope


def _expires_in(value: Any) -> int:
    """Seconds the token lasts; 300 when the token endpoint leaves it out or sends null."""
    try:
        return int(value) if value is not None else 300
    except (TypeError, ValueError):
        return 300


def _login_error(status: int) -> Type[ApiException]:
    """The exception for an unsuccessful login: only 400 and 401 mean refused credentials."""
    if status in (400, 401):
        return AuthenticationError
    if status == 429:
        return RateLimitError
    if 500 <= status <= 599:
        return ServiceException
    if status == 403:
        return ForbiddenException
    if status == 404:
        return NotFoundException
    return ApiException


def _login_hint(status: int, error: Optional[str]) -> str:
    if status == 404:
        return " Check account_id: no such account in this environment."
    if status in (400, 401) and error in ("invalid_client", "unauthorized_client", None):
        return (
            " Check client_id and client_secret, and that they were made in this environment"
            " (sandbox and production credentials are separate)."
        )
    if status == 429:
        return " Too many logins in a short time; this is not a credentials problem. Retry later."
    if 500 <= status <= 599:
        return " The login service is unavailable; this is not a credentials problem. Retry later."
    return ""


class AuthenticationClient:
    """Requests and caches the OAuth2 token for one set of credentials."""

    def __init__(
        self,
        account_id: str,
        client_id: str,
        client_secret: str,
        base_path: str,
        pool_manager: Optional[urllib3.PoolManager] = None,
        timeout: Optional[float] = None,
        retries: Union[None, int, Retry] = None,
    ) -> None:
        """
        :param account_id: the Astrada account ID (the login realm)
        :param client_id: the API client's ID
        :param client_secret: the API client's secret
        :param base_path: the environment's base URL, for example https://api.sandbox.astrada.co
        :param pool_manager: urllib3 pool to send the token request through
        :param timeout: seconds to wait for the token endpoint (default 60)
        :param retries: the client's ``retries`` setting; a 429 or 5xx from the token endpoint is
            retried under it (see :func:`astrada._retry.build_login_retry`)
        """
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_path = base_path.rstrip("/")
        self.timeout = timeout_or_default(timeout)
        self.retries = build_login_retry(retries)
        self._cached_token: Optional[AccessToken] = None
        self._token_expiry: float = 0
        self._lock = threading.Lock()
        if pool_manager is None:
            pool_manager = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", retries=build_retry(None))
        self.pool_manager = pool_manager

    @property
    def token_url(self) -> str:
        return f"{self.base_path}/auth/realms/{self.account_id}/protocol/openid-connect/token"

    def get_access_token(
        self, name: Optional[str] = None, scopes: Optional[List[str]] = None
    ) -> str:
        """The Authorization header value ("Bearer ..."), logging in first if needed.

        :param name: unused; kept for the generated Configuration's call
        :param scopes: unused; the token carries every scope the API client has
        :raises AuthenticationError: the token endpoint refused the credentials (400 or 401)
        :raises RateLimitError: the token endpoint answered 429, after the retries
        :raises ServiceException: the token endpoint answered 5xx, after the retries
        :raises NotFoundException: no such account (404)
        :raises ApiConnectionError: the token endpoint could not be reached
        """
        with self._lock:
            if not self._is_token_valid():
                self._cache_token(self._request_new_token())
            assert self._cached_token is not None
            return self._format_token(self._cached_token)

    def _format_token(self, token: AccessToken) -> str:
        token_type = token.token_type or "Bearer"
        if token_type.lower() == "bearer":
            token_type = "Bearer"
        return f"{token_type} {token.access_token}"

    def _request_new_token(self) -> AccessToken:
        fields = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }
        try:
            response = self.pool_manager.request(
                "POST",
                self.token_url,
                fields=fields,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                encode_multipart=False,
                timeout=urllib3.Timeout(total=self.timeout),
                # Never follow a redirect: it would send the client secret to another address.
                retries=self.retries.new(redirect=False),
                redirect=False,
            )
            body = response.data
        except urllib3.exceptions.HTTPError as e:
            raise ApiConnectionError(
                reason=f"Could not reach the Astrada login at {self.base_path}: {e}"
            ) from e

        text = body.decode("utf-8", errors="replace") if body else ""
        data: Dict[str, Any] = {}
        try:
            parsed = json.loads(text) if text else {}
            if isinstance(parsed, dict):
                data = parsed
        except ValueError:
            pass

        if 200 <= response.status < 300 and isinstance(data.get("access_token"), str):
            return AccessToken(
                access_token=data["access_token"],
                token_type=data.get("token_type"),
                expires_in=_expires_in(data.get("expires_in")),
                scope=data.get("scope"),
            )

        if 300 <= response.status < 400:
            # The origin only: a redirect's query string can carry tokens, so neither the Location
            # header nor the redirect page goes into the exception.
            target = "another address"
            try:
                parts = urlsplit(urljoin(self.token_url, response.headers.get("Location") or ""))
                host = parts.netloc.rsplit("@", 1)[-1]  # keeps IPv6 brackets and the port
                _ = parts.port  # raises ValueError for a port that is not a number in range
                if parts.scheme in ("http", "https") and parts.hostname:
                    target = "%s://%s" % (parts.scheme, host)
            except ValueError:
                pass  # a malformed Location (bad port, broken IPv6): say only that it redirects
            raise ApiException(
                status=response.status,
                reason=(f"Login failed ({response.status}): the login answered with a redirect to "
                        f"{target}. The SDK does not send the client secret there; check base_url "
                        f"({self.base_path})."),
                headers={k: v for k, v in response.headers.items() if k.lower() != "location"},
            )

        error = data.get("error") if isinstance(data.get("error"), str) else None
        description = data.get("error_description")
        message = description or error or (text.strip()[:200] if text else "") or response.reason
        reason = f"Login failed ({response.status}): {message}.{_login_hint(response.status, error)}"
        raise _login_error(response.status)(
            status=response.status,
            reason=reason,
            body=text,
            headers=dict(response.headers),
            code=error,
            detail=description if isinstance(description, str) else None,
        )

    def _cache_token(self, token: AccessToken) -> None:
        self._cached_token = token
        self._token_expiry = time.time() + token.expires_in - _EXPIRY_MARGIN_SECONDS

    def _is_token_valid(self) -> bool:
        return self._cached_token is not None and time.time() < self._token_expiry

    def clear_cache(self) -> None:
        """Forget the cached token, so the next call logs in again."""
        with self._lock:
            self._cached_token = None
            self._token_expiry = 0
