# coding: utf-8
"""Tests for the Banking API subpackage (astrada.banking, generated from api-spec's `banking`
bundle): it logs in with client credentials like the main client and calls the banking routes on
the configured host. urllib3 is replaced with a fake, so the tests need no network or account.
"""

import io
import json
import unittest
from unittest import mock

import urllib3

from astrada import banking

SANDBOX = "https://api.sandbox.astrada.co"


def _response(payload):
    return urllib3.HTTPResponse(
        body=io.BytesIO(json.dumps(payload).encode("utf-8")),
        status=200,
        headers={"Content-Type": "application/json"},
        preload_content=False,
    )


class TestBanking(unittest.TestCase):
    def test_exports_the_banking_apis(self):
        for name in ("BankLinksApi", "BankAccountsApi", "BankSubscriptionsApi",
                     "BankTransactionsApi", "TransactionMatchesApi"):
            self.assertTrue(hasattr(banking, name), name)

    def test_logs_in_and_calls_a_banking_route(self):
        calls = []

        def fake(_pool, method, url, **kwargs):
            calls.append({"method": method, "url": url, **kwargs})
            if "/protocol/openid-connect/token" in url:
                return _response({"access_token": "token-1", "token_type": "Bearer", "expires_in": 300})
            return _response({"id": "bl-1"})

        configuration = banking.Configuration(
            host=SANDBOX, account_id="acct-1", client_id="client-1", client_secret="secret-1"
        )
        api = banking.BankLinksApi(banking.ApiClient(configuration))
        with mock.patch.object(urllib3.PoolManager, "request", autospec=True, side_effect=fake):
            response = api.get_bank_link_without_preload_content("bl-1")

        self.assertEqual(response.status, 200)
        self.assertEqual(calls[0]["url"], f"{SANDBOX}/auth/realms/acct-1/protocol/openid-connect/token")
        self.assertEqual(calls[1]["url"], f"{SANDBOX}/bank-links/bl-1")
        self.assertEqual(calls[1]["headers"]["Authorization"], "Bearer token-1")


if __name__ == "__main__":
    unittest.main()
