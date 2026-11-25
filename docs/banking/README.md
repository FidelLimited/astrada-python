# Banking API methods

`client.banking.<group>.<method>` on an `astrada.Astrada` client. API version 2024-02-28.

| Method | HTTP request | |
|---|---|---|
| [`client.banking.bank_accounts.backfill_bank_account`](BankAccountsApi.md#backfill_bank_account) | `POST /bank-accounts/{bankAccountId}/backfill` | Needs banking:admin |
| [`client.banking.bank_accounts.delete_bank_account`](BankAccountsApi.md#delete_bank_account) | `DELETE /bank-accounts/{bankAccountId}` | Needs banking:admin |
| [`client.banking.bank_accounts.get_bank_account`](BankAccountsApi.md#get_bank_account) | `GET /bank-accounts/{bankAccountId}` |
| [`client.banking.bank_accounts.link_enrolled_cards`](BankAccountsApi.md#link_enrolled_cards) | `POST /bank-accounts/link-enrolled-cards` |
| [`client.banking.bank_accounts.list_bank_accounts`](BankAccountsApi.md#list_bank_accounts) | `GET /bank-accounts` |
| [`client.banking.bank_accounts.refresh_bank_account`](BankAccountsApi.md#refresh_bank_account) | `POST /bank-accounts/{bankAccountId}/refresh` |
| [`client.banking.bank_accounts.refresh_bank_account_transactions`](BankAccountsApi.md#refresh_bank_account_transactions) | `POST /bank-accounts/{bankAccountId}/transactions/refresh` | Needs banking:admin |
| [`client.banking.bank_accounts.run_bank_account_maintenance`](BankAccountsApi.md#run_bank_account_maintenance) | `POST /bank-accounts/maintenance` | Needs banking:admin |
| [`client.banking.bank_accounts.update_bank_account`](BankAccountsApi.md#update_bank_account) | `PATCH /bank-accounts/{bankAccountId}` |
| [`client.banking.bank_links.create_bank_link`](BankLinksApi.md#create_bank_link) | `POST /bank-links` |
| [`client.banking.bank_links.delete_bank_link`](BankLinksApi.md#delete_bank_link) | `DELETE /bank-links/{bankLinkId}` | Needs banking:admin |
| [`client.banking.bank_links.get_bank_link`](BankLinksApi.md#get_bank_link) | `GET /bank-links/{bankLinkId}` |
| [`client.banking.bank_links.list_bank_links`](BankLinksApi.md#list_bank_links) | `GET /bank-links` |
| [`client.banking.bank_links.sync_bank_link`](BankLinksApi.md#sync_bank_link) | `POST /bank-links/{bankLinkId}/sync` | Needs banking:admin |
| [`client.banking.bank_links.update_bank_link`](BankLinksApi.md#update_bank_link) | `PATCH /bank-links/{bankLinkId}` |
| [`client.banking.bank_subscriptions.get_bank_subscription`](BankSubscriptionsApi.md#get_bank_subscription) | `GET /bank-subscriptions/{bankSubscriptionId}` | Needs banking:admin |
| [`client.banking.bank_subscriptions.get_bank_subscription_by_connection`](BankSubscriptionsApi.md#get_bank_subscription_by_connection) | `GET /bank-subscriptions/by-connection/{connectionId}` | Needs banking:admin |
| [`client.banking.bank_subscriptions.list_bank_subscriptions`](BankSubscriptionsApi.md#list_bank_subscriptions) | `GET /bank-subscriptions` | Needs banking:admin |
| [`client.banking.bank_transactions.get_bank_transaction`](BankTransactionsApi.md#get_bank_transaction) | `GET /bank-transactions/{subaccountId}/{transactionId}` |
| [`client.banking.bank_transactions.list_bank_transactions`](BankTransactionsApi.md#list_bank_transactions) | `GET /bank-transactions/{subaccountId}` |
| [`client.banking.bank_transactions.trigger_bank_transaction_webhooks`](BankTransactionsApi.md#trigger_bank_transaction_webhooks) | `POST /bank-transactions/{subaccountId}/webhooks` | Needs banking:admin |
| [`client.banking.transaction_matches.get_transaction_match`](TransactionMatchesApi.md#get_transaction_match) | `GET /transaction-matches/{subaccountId}/{transactionMatchId}` |
| [`client.banking.transaction_matches.list_transaction_matches`](TransactionMatchesApi.md#list_transaction_matches) | `GET /transaction-matches/{subaccountId}` |

