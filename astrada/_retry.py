# coding: utf-8
"""The default retry policy and timeout. Hand-written; not generated."""

from typing import Any, Optional, Union

from urllib3.exceptions import InvalidHeader, MaxRetryError, ResponseError
from urllib3.util.retry import Retry

DEFAULT_TIMEOUT = 60.0
"""Seconds to wait for the API to answer, per request (connect and read)."""

DEFAULT_MAX_RETRIES = 2
"""Retries after the first attempt."""

SANDBOX_DELETE_TIMEOUT = 300.0
"""Seconds the sandbox-only deletes wait at least (they answer when the cascading delete is done).
They are never retried: a second call while the first still runs is not safe."""

RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})
IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "PUT", "DELETE", "OPTIONS"})
MAX_RETRY_AFTER = 60.0
"""The longest Retry-After wait the SDK honours, in seconds; a longer one ends the retries."""


class AstradaRetry(Retry):
    """urllib3 Retry that gives up instead of sleeping through a very long Retry-After.

    When a 429 or 503 asks for a wait longer than MAX_RETRY_AFTER, the retries end there and the
    response is raised as its exception (``RateLimitError.retry_after`` gives the wait), so the SDK
    never retries earlier than the API asked.
    """

    def get_retry_after(self, response: Any) -> Optional[float]:
        """The Retry-After wait, or None when the header is missing or malformed (``1.5``): a bad
        header then means the usual backoff, not an error that hides the real answer."""
        try:
            return super().get_retry_after(response)
        except InvalidHeader:
            return None

    def increment(  # type: ignore[override]
        self,
        method: Optional[str] = None,
        url: Optional[str] = None,
        response: Any = None,
        error: Optional[Exception] = None,
        _pool: Any = None,
        _stacktrace: Any = None,
    ) -> Retry:
        if response is not None and self.respect_retry_after_header \
                and response.status in self.RETRY_AFTER_STATUS_CODES:
            wait = self.get_retry_after(response)
            if wait is not None and wait > MAX_RETRY_AFTER:
                raise MaxRetryError(_pool, url or "", ResponseError(
                    "Retry-After of %.0f s is longer than %.0f s" % (wait, MAX_RETRY_AFTER)))
        return super().increment(method, url, response, error, _pool, _stacktrace)


def build_retry(retries: Union[None, int, Retry]) -> Retry:
    """The urllib3 Retry for ``retries``: a count, a Retry of your own, or None for the default.

    Connection failures are retried for every method (nothing reached the API). A response with
    status 429, 500, 502, 503 or 504 is retried only for GET, HEAD, PUT, DELETE and OPTIONS, so a
    POST or PATCH is never sent twice. Waits grow 0.5 s, 1 s, 2 s and so on (at most 8 s), and a
    Retry-After header on 429 or 503 is honoured when it is at most 60 s; a longer one ends the
    retries at once. When the retries run out, the last
    response is returned and raised as the matching exception (for example ``RateLimitError``).
    """
    if isinstance(retries, Retry):
        # A Retry of your own is used as given, except that running out of retries returns the
        # last answer (raised as its exception, such as RateLimitError) instead of MaxRetryError.
        return retries.new(raise_on_status=False)
    count = DEFAULT_MAX_RETRIES if retries is None else int(retries)
    return AstradaRetry(
        total=count,
        connect=count,
        read=count,
        status=count,
        other=0,
        backoff_factor=0.5,
        backoff_max=8,
        status_forcelist=RETRY_STATUSES,
        allowed_methods=IDEMPOTENT_METHODS,
        respect_retry_after_header=True,
        raise_on_status=False,
        raise_on_redirect=False,
    )


def build_login_retry(retries: Union[None, int, Retry]) -> Retry:
    """The Retry for the login (the OAuth2 token request): the same as ``build_retry``, and its POST
    is retried too (a 429, a 5xx or a read timeout), as asking for a token again changes nothing.
    POST is added to a Retry of your own as well."""
    retry = build_retry(retries)
    allowed = retry.allowed_methods
    if allowed:
        retry = retry.new(allowed_methods=frozenset(allowed) | {"POST"})
    return retry


def timeout_or_default(value: Optional[float]) -> float:
    return DEFAULT_TIMEOUT if value is None else float(value)
