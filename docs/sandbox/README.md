# Sandbox methods

`client.sandbox.<method>` on an `astrada.Astrada` client made with `environment="sandbox"`.
Every method raises `astrada.SandboxOnlyError`, before sending anything, on any other client. API version 2024-02-28.

| Method | HTTP request |
|---|---|
| [`client.sandbox.delete_card_subscription`](CardSubscriptionApi.md#delete_card_subscription) | `DELETE /card-subscriptions/{subscriptionId}` |
| [`client.sandbox.delete_network_bulk_feed`](NetworkBulkFeedsApi.md#delete_network_bulk_feed) | `DELETE /network-bulk-feeds/{networkBulkFeedId}` |
| [`client.sandbox.simulate_bulk_feed_file_gl`](SandboxSimulationApi.md#simulate_bulk_feed_file_gl) | `POST /simulate/ingestion/amex-gl` |
| [`client.sandbox.simulate_bulk_feed_file_smartdata`](SandboxSimulationApi.md#simulate_bulk_feed_file_smartdata) | `POST /simulate/ingestion/smartdata` |
| [`client.sandbox.simulate_bulk_feed_file_vbds`](SandboxSimulationApi.md#simulate_bulk_feed_file_vbds) | `POST /simulate/ingestion/vbds` |
| [`client.sandbox.simulate_bulk_feed_file_vcf`](SandboxSimulationApi.md#simulate_bulk_feed_file_vcf) | `POST /simulate/ingestion/vcf` |
| [`client.sandbox.simulate_transaction`](SandboxSimulationApi.md#simulate_transaction) | `POST /simulate/transactions` |
| [`client.sandbox.simulate_transaction_message`](SandboxSimulationApi.md#simulate_transaction_message) | `POST /simulate/transactions/{transactionId}` |
| [`client.sandbox.simulate_transaction_scenario`](SandboxSimulationApi.md#simulate_transaction_scenario) | `POST /simulate/transaction/scenario` |
| [`client.sandbox.delete_subaccount`](SubaccountsApi.md#delete_subaccount) | `DELETE /subaccounts/{subaccountId}` |

