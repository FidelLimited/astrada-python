# coding: utf-8
"""Written by scripts/sandbox-routes.mjs from the sandbox-only API definition; do not edit."""

import re
from typing import List, Pattern, Tuple

SANDBOX_ROUTES: List[Tuple[str, Pattern[str]]] = [
    ("DELETE", re.compile(r"^/card-subscriptions/[^/]+$")),  # /card-subscriptions/{subscriptionId}
    ("DELETE", re.compile(r"^/network-bulk-feeds/[^/]+$")),  # /network-bulk-feeds/{networkBulkFeedId}
    ("POST", re.compile(r"^/simulate/ingestion/amex-gl$")),  # /simulate/ingestion/amex-gl
    ("POST", re.compile(r"^/simulate/ingestion/smartdata$")),  # /simulate/ingestion/smartdata
    ("POST", re.compile(r"^/simulate/ingestion/vbds$")),  # /simulate/ingestion/vbds
    ("POST", re.compile(r"^/simulate/ingestion/vcf$")),  # /simulate/ingestion/vcf
    ("POST", re.compile(r"^/simulate/transaction/scenario$")),  # /simulate/transaction/scenario
    ("POST", re.compile(r"^/simulate/transactions/[^/]+$")),  # /simulate/transactions/{transactionId}
    ("POST", re.compile(r"^/simulate/transactions$")),  # /simulate/transactions
    ("DELETE", re.compile(r"^/subaccounts/[^/]+$")),  # /subaccounts/{subaccountId}
]
"""The sandbox-only operations: method and a pattern for the decoded, lower-case path."""
