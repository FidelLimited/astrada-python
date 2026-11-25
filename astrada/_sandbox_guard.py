# coding: utf-8
"""The check that keeps sandbox-only calls off production. Hand-written; not generated.

Every request of the generated ``astrada.sandbox`` package goes through :func:`check` first (its
ApiClient calls it before building the request, so not even a login is sent). A call passes only
when the configuration's environment is ``"sandbox"`` and its base URL is the sandbox API, or a
custom base URL that was explicitly marked as a sandbox with ``sandbox_base_url=True``.
"""

from typing import Any
from urllib.parse import urlsplit

from astrada.environments import Environment
from astrada.exceptions import SandboxOnlyError


def check(configuration: Any) -> None:
    """Raise SandboxOnlyError unless ``configuration`` points at a sandbox."""
    environment = getattr(configuration, "environment", None)
    if environment != "sandbox":
        raise SandboxOnlyError(
            "Sandbox-only calls (simulations and test-data deletes) only run in the sandbox; this "
            "client's environment is %s."
            % ("production" if environment is None else repr(environment))
        )
    parts = urlsplit(str(configuration.host))
    host = parts.netloc.lower()
    sandbox = urlsplit(Environment.SANDBOX)
    if host == sandbox.netloc.lower():
        if parts.scheme.lower() != sandbox.scheme.lower():
            # The login sends the client secret: never over plain HTTP to the real sandbox.
            raise SandboxOnlyError(
                "Sandbox-only calls to %s need %s; this client's base URL is %s."
                % (Environment.SANDBOX, sandbox.scheme, configuration.host)
            )
        return
    hostname = (parts.hostname or "").lower().rstrip(".")
    astrada_host = hostname == "astrada.co" or hostname.endswith(".astrada.co")
    # The marker is for hosts outside Astrada (a local mock, Prism, a proxy). An Astrada host other
    # than the sandbox API (production above all) is refused even when marked.
    if getattr(configuration, "sandbox_base_url", False) is True and not astrada_host:
        return
    raise SandboxOnlyError(
        "Sandbox-only calls only run against %s; this client's base URL is %s. Pass "
        "sandbox_base_url=True to mark a custom base URL (a proxy or a local mock) as a sandbox."
        % (Environment.SANDBOX, configuration.host)
    )
