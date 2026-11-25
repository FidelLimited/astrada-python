"""The Banking API defaults to production, like the main API (sandbox only by explicit choice)."""

import astrada
from astrada import banking

PRODUCTION = "https://api.astrada.co"


def test_the_banking_configuration_defaults_to_production():
    assert banking.Configuration().host == PRODUCTION
    assert astrada.Configuration().host == PRODUCTION


def test_the_banking_servers_are_the_main_api_servers():
    # The generated server list (server_index, the docs' base URL) comes from the banking bundle,
    # which can list only the sandbox; generate.sh copies the public bundle's servers into it.
    banking_servers = [s["url"] for s in banking.Configuration().get_host_settings()]
    main_servers = [s["url"] for s in astrada.Configuration().get_host_settings()]
    assert banking_servers == main_servers
    assert banking_servers[0] == PRODUCTION
