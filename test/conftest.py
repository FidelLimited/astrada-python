"""Shared fixtures: the local stand-in API (test/standin/server.py)."""

import base64
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from standin.server import ACCOUNT_ID, CLIENT_ID, CLIENT_SECRET, SDK_CLIENT_ID, Standin  # noqa: E402

# A made-up webhook secret for the examples (whsec_ plus base64 of 32 bytes).
WEBHOOK_SECRET = "whsec_" + base64.b64encode(b"standin webhook secret, 32 bytes").decode()


@pytest.fixture
def standin():
    with Standin() as server:
        yield server


@pytest.fixture
def standin_env(standin, monkeypatch):
    """The stand-in as both "sandbox" and "production", and its credentials in the environment."""
    from astrada import environments

    # The sandbox check compares the base URL with Environment.SANDBOX, so the stand-in takes its
    # place here (tests of the check itself use their own clients, without this fixture).
    monkeypatch.setattr(environments.Environment, "SANDBOX", standin.url)
    monkeypatch.setitem(environments._NAMES, "sandbox", standin.url)
    monkeypatch.setitem(environments._NAMES, "production", standin.url)
    monkeypatch.setenv("ASTRADA_ACCOUNT_ID", ACCOUNT_ID)
    monkeypatch.setenv("ASTRADA_CLIENT_ID", CLIENT_ID)
    monkeypatch.setenv("ASTRADA_CLIENT_SECRET", CLIENT_SECRET)
    # The SDK client (README: minting a token for the browser enrollment SDK).
    monkeypatch.setenv("ASTRADA_SDK_CLIENT_ID", SDK_CLIENT_ID)
    monkeypatch.setenv("ASTRADA_SDK_CLIENT_SECRET", CLIENT_SECRET)
    monkeypatch.setenv("ASTRADA_WEBHOOK_SECRET", WEBHOOK_SECRET)
    return standin
