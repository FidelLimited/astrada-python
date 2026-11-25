# coding: utf-8
"""Astrada environments. Hand-written; not generated.

Pass ``"sandbox"`` or ``"production"`` (or one of the constants below) as ``environment`` to
:class:`astrada.Astrada` or :class:`astrada.Configuration`. Sandbox and production have separate
accounts and credentials: credentials made in one do not log in to the other.
"""

from typing import Dict


class Environment:
    """Base URLs of the Astrada environments."""

    SANDBOX = "https://api.sandbox.astrada.co"
    PRODUCTION = "https://api.astrada.co"


_NAMES: Dict[str, str] = {
    "sandbox": Environment.SANDBOX,
    "production": Environment.PRODUCTION,
}


def name(environment: str) -> str:
    """``"sandbox"`` or ``"production"`` for ``environment`` (any case); ValueError otherwise."""
    value = environment.strip().lower() if isinstance(environment, str) else ""
    if value not in _NAMES:
        raise ValueError(
            'environment must be "sandbox" or "production", not %r. For another base URL '
            "(a proxy or a local mock) pass base_url as well." % (environment,)
        )
    return value


def base_url(environment: str) -> str:
    """The base URL for ``environment``: ``"sandbox"``, ``"production"`` or a full https URL."""
    if not isinstance(environment, str) or not environment:
        raise ValueError('environment must be "sandbox" or "production"')
    name = environment.strip().lower()
    if name in _NAMES:
        return _NAMES[name]
    if name.startswith("https://") or name.startswith("http://"):
        return environment.strip().rstrip("/")
    raise ValueError(
        'environment must be "sandbox" or "production" (or a base URL), not %r' % environment
    )
