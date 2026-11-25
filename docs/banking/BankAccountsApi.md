# astrada.banking.BankAccountsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backfill_bank_account**](BankAccountsApi.md#backfill_bank_account) | **POST** /bank-accounts/{bankAccountId}/backfill | Needs banking:admin: Backfill bank account history
[**delete_bank_account**](BankAccountsApi.md#delete_bank_account) | **DELETE** /bank-accounts/{bankAccountId} | Needs banking:admin: Delete bank account
[**get_bank_account**](BankAccountsApi.md#get_bank_account) | **GET** /bank-accounts/{bankAccountId} | Retrieve bank account
[**link_enrolled_cards**](BankAccountsApi.md#link_enrolled_cards) | **POST** /bank-accounts/link-enrolled-cards | Link enrolled cards to bank accounts (admin backfill)
[**list_bank_accounts**](BankAccountsApi.md#list_bank_accounts) | **GET** /bank-accounts | List bank accounts
[**refresh_bank_account**](BankAccountsApi.md#refresh_bank_account) | **POST** /bank-accounts/{bankAccountId}/refresh | Refresh bank account
[**refresh_bank_account_transactions**](BankAccountsApi.md#refresh_bank_account_transactions) | **POST** /bank-accounts/{bankAccountId}/transactions/refresh | Needs banking:admin: Refresh transactions
[**run_bank_account_maintenance**](BankAccountsApi.md#run_bank_account_maintenance) | **POST** /bank-accounts/maintenance | Needs banking:admin: Bank account maintenance for a subaccount
[**update_bank_account**](BankAccountsApi.md#update_bank_account) | **PATCH** /bank-accounts/{bankAccountId} | Update bank account


# **backfill_bank_account**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankAccountBackfillResult backfill_bank_account(bank_account_id, bank_account_backfill_params)

Needs banking:admin: Backfill bank account history

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Imports historical bank transactions for this account from the provider over a date range, then runs matching against the account's full current card set. Unlike the `backfill` object on `PATCH /bank-accounts/{bankAccountId}` (which imports history for cards being added in that same request), this endpoint recovers a date window without touching card links. Each imported bank transaction sends `banktransaction.created` and each new match `transaction.match.created`.

Requires a backing connection. Starting a backfill while another sync already holds the account's connection returns `409 Conflict`; retry shortly.

For Mastercard accounts at US banks (`provider: mastercard`, `countryCode: USA`), `loadHistoric: true` additionally asks the provider to generate deep history (up to 2 years) for this account before the import runs. This is a billable provider operation and generation is asynchronous on the provider side: if the immediate import returns few rows, re-run the same window without the flag once generation completes (typically within minutes). Providers without a deep-history operation reject the flag with `400 Bad Request`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_backfill_params import BankAccountBackfillParams
from astrada.banking.models.bank_account_backfill_result import BankAccountBackfillResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'  # str
bank_account_backfill_params = {'startDate': '2026-06-13', 'endDate': '2026-06-27'}  # BankAccountBackfillParams

result = client.banking.bank_accounts.backfill_bank_account(bank_account_id, bank_account_backfill_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 
 **bank_account_backfill_params** | [**BankAccountBackfillParams**](BankAccountBackfillParams.md)| Date range to import. Both bounds are optional; send an empty object for the default window. | 

### Return type

[**BankAccountBackfillResult**](BankAccountBackfillResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Backfill completed |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**409** | The resource is not in a state that allows this request. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_account**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> delete_bank_account(bank_account_id)

Needs banking:admin: Delete bank account

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Deletes a bank account and all associated bank transactions, transaction matches, and card links.

Cards are not deleted. A `bank-feed` subscription created from this account is deactivated; a card enrolled by its number only loses its bank account. The account sends `bankaccount.state_changed` with reason `deleted`.

**Note:** This action is irreversible. Deleting the last account of a bank connection also removes the connection at the bank.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'  # str

client.banking.bank_accounts.delete_bank_account(bank_account_id)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Bank account deleted |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_account**
> BankAccount get_bank_account(bank_account_id)

Retrieve bank account

Returns detailed information about a specific bank account by its identifier.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account import BankAccount

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'  # str

result = client.banking.bank_accounts.get_bank_account(bank_account_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token does not hold the &#x60;banking:read&#x60; scope this route needs. |  -  |
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_enrolled_cards**
> BankAccountLinkCardsResult link_enrolled_cards(bank_account_link_cards_params)

Link enrolled cards to bank accounts (admin backfill)

Admin backfill/retry for immediate mask-linking: matches the subaccount's ENROLLED cards against its credit bank accounts by mask (an enrolled card's last 4 digits) and links each exact match. The same exactly-one-or-skip rules as completion-time linking apply: a mask matching multiple cards, or multiple accounts claiming a mask, links nothing (the scheduled mask sweep retries this every few hours). Idempotent: already-linked pairs are skipped. Intended for onboarding backfills (cards enrolled before the bank link) and recovery after a transient directory failure at completion. Emits no webhook; linked cardIds appear on subsequent bank-account reads.

The body takes `subaccountId` only; any other field is a `400`. The admin actions (minting cards for cardless accounts, the cardholder backfill) are on `POST /bank-accounts/maintenance` at `banking:admin`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_link_cards_params import BankAccountLinkCardsParams
from astrada.banking.models.bank_account_link_cards_result import BankAccountLinkCardsResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_link_cards_params = {'subaccountId': 'f297d659-c13d-4219-aeaa-e10a845140a5'}  # BankAccountLinkCardsParams

result = client.banking.bank_accounts.link_enrolled_cards(bank_account_link_cards_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_link_cards_params** | [**BankAccountLinkCardsParams**](BankAccountLinkCardsParams.md)|  | 

### Return type

[**BankAccountLinkCardsResult**](BankAccountLinkCardsResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Backfill executed. Maps each bank account that gained links to the card ids linked in this run (empty object when nothing matched). |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token does not hold the &#x60;banking:write&#x60; scope this route needs. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_accounts**
> BankAccountList list_bank_accounts(subaccount_id=subaccount_id, state=state, card_id=card_id, limit=limit, cursor=cursor)

List bank accounts

Returns a list of bank accounts under the account. Bank accounts are created automatically when a bank link enrollment is completed.

By default, `GET /bank-accounts` returns bank accounts ordered by the latest `createdAt`.

This endpoint supports cursor-based pagination.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_list import BankAccountList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
state = 'active'  # str (optional)
card_id = '8164683a-8d23-4421-9694-1a81fc9b9c37'  # str (optional)
limit = 250  # int (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)

result = client.banking.bank_accounts.list_bank_accounts(subaccount_id=subaccount_id, state=state, card_id=card_id, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | [optional] 
 **state** | **str**| Filter bank accounts by state | [optional] 
 **card_id** | **str**|  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 250]
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 

### Return type

[**BankAccountList**](BankAccountList.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token does not hold the &#x60;banking:read&#x60; scope this route needs. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_bank_account**
> BankAccountRefreshResult refresh_bank_account(bank_account_id)

Refresh bank account

Creates a new hosted link URL for the user to re-authenticate an account in `auth_required`. Any other state answers `400`. To ask the bank for new transactions, use `POST /bank-accounts/{bankAccountId}/transactions/refresh`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_refresh_result import BankAccountRefreshResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'  # str

result = client.banking.bank_accounts.refresh_bank_account(bank_account_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

[**BankAccountRefreshResult**](BankAccountRefreshResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Refresh triggered |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token does not hold the &#x60;banking:write&#x60; scope this route needs. |  -  |
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_bank_account_transactions**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankAccountTransactionsRefreshResult refresh_bank_account_transactions(bank_account_id)

Needs banking:admin: Refresh transactions

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Asks the data provider to check this account's institution **now**, instead of waiting for its own schedule (typically one to four checks a day). The call returns once the check has run, usually within seconds but occasionally 30 seconds or more. It imports nothing itself: anything the check finds arrives through the normal update path within moments.

**Billable per successful call.** Use it at moments that matter, not on a timer. Returns `400 Bad Request` when the account has no backing connection, or when its provider or institution doesn't support an on-demand refresh (e.g. some card issuers), and `502 Bad Gateway` when the provider's check fails.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_transactions_refresh_result import BankAccountTransactionsRefreshResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'  # str

result = client.banking.bank_accounts.refresh_bank_account_transactions(bank_account_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 

### Return type

[**BankAccountTransactionsRefreshResult**](BankAccountTransactionsRefreshResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The provider has run its check of the institution. &#x60;durationMs&#x60; is how long that check took, not an import; any changes it found arrive through the normal update path. |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |
**502** | The bank data provider failed to complete the request. Try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_bank_account_maintenance**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankAccountMaintenanceResult run_bank_account_maintenance(bank_account_maintenance_params)

Needs banking:admin: Bank account maintenance for a subaccount

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Admin maintenance over one subaccount. It first runs the same mask pass as `POST /bank-accounts/link-enrolled-cards`, then each action the request asks for. The actions create cards on the cards platform or rewrite stored rows, so this route needs `banking:admin`, while the mask pass alone stays on `link-enrolled-cards` at `banking:write`. The caller's account comes from its token: it can run maintenance on any subaccount of its own account, and a subaccount of another account simply matches nothing (an empty result, not a `403`).

Three optional actions, each off by default:

- `mint: true` runs the completion-time mint pass over the subaccount's credit bank accounts that a completed link left without a card (the same-last-4 American Express case), so each gains a bank-feed card. Idempotent: an account that already holds a minted card is skipped.
- `backfillJunctionLast4: true` fills, for the subaccount's card links, the last 4 each link answers to where it is still unknown, from the cards directory. Idempotent.
- `createCardholderCards: true` runs, now and for this subaccount only, what a scheduled job does every 30 minutes: it gives each cardholder behind a pooled American Express billing account (a supplementary card that is not its own Plaid account) a bank-feed card of their own, with the cardholder's name, so their transactions can be emitted on that card. It does nothing unless Astrada has switched the feature on for the subaccount; the switches are set by Astrada only, from inside the platform, and no request can set them. Idempotent: a cardholder who already has a card is never given another.

The actions run in the order above, after the mask pass. If the cards directory cannot be read, the mask pass links nothing and still returns `201`; each action then reads the directory again on its own and says so in its result (`directoryUnavailable`), or, for `mint` with accounts to screen, fails rather than mint unscreened. Any step that fails returns `400` and runs nothing after it (steps before it have done their work, and every step is idempotent, so the request can simply be repeated). Emits no webhook from banking; a card created here produces the cards platform's usual card-subscription events.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_maintenance_params import BankAccountMaintenanceParams
from astrada.banking.models.bank_account_maintenance_result import BankAccountMaintenanceResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_maintenance_params = {'subaccountId': 'f297d659-c13d-4219-aeaa-e10a845140a5'}  # BankAccountMaintenanceParams

result = client.banking.bank_accounts.run_bank_account_maintenance(bank_account_maintenance_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_maintenance_params** | [**BankAccountMaintenanceParams**](BankAccountMaintenanceParams.md)|  | 

### Return type

[**BankAccountMaintenanceResult**](BankAccountMaintenanceResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Maintenance executed. Maps each bank account that gained links to the card ids linked in this run (empty object when nothing matched). The other fields appear only for the actions the request asked for. |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_account**
> BankAccountUpdateResult update_bank_account(bank_account_id, bank_account_update_params)

Update bank account

Updates a bank account. Card links are detected automatically: a scheduled sweep re-checks each cardless credit account every few hours and links an enrolled card whose last 4 digits match the account's mask, without any API call. This endpoint is the manual override: use it to pre-link a card immediately, correct an assignment, or import history.

Each card in `cardIds` must belong to the same subaccount as the bank account. A card can only be linked to one bank account at a time; attempting to link a card that is already associated with another bank account will return a `409 Conflict` error.

A card that cannot take a bank-account link is also rejected with `409 Conflict` before any change is applied: one whose only enrollment is a bulk feed, or whose subscriptions are all in a dead, non-attachable state. The `message` names the card and says whether it is bulk-enrolled or has no live subscription. This body, like the "already linked" `409`, has no `code`. If the cards directory cannot be consulted, this screen is skipped (fail-open) rather than blocking the update.

`cardIds` is a full replacement. Send `cardIds: []` to clear explicit links (the scheduled mask sweep can re-link a matching card on its next run).

Cards Astrada created for the individual cardholders of a pooled American Express billing account are managed by the platform: a `cardIds` list without them does not remove them (they leave when the card is deactivated or the account is disconnected or deleted). An enrolled card that was linked for one such cardholder can be removed here, and stays removed: it is not linked again automatically.

Optionally include a `backfill` object with `startDate` and/or `endDate` to trigger a backfill of historical bank transactions for the specified date range. An automatically detected link re-matches the account's already-synced unmatched transactions around the new card's activity on its own; IMPORTING bank history from before the link (pulling older transactions from the provider) still happens only through this endpoint's `backfill`.

The current card set is always readable at `GET /bank-accounts/{bankAccountId}` (`cardIds`), and `GET /bank-accounts?cardId=` finds the account a card is linked to.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_account_update_params import BankAccountUpdateParams
from astrada.banking.models.bank_account_update_result import BankAccountUpdateResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_account_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'  # str
bank_account_update_params = {'cardIds': ['5dec2c49-0aa5-4683-a317-427eb5d115f3']}  # BankAccountUpdateParams

result = client.banking.bank_accounts.update_bank_account(bank_account_id, bank_account_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**|  | 
 **bank_account_update_params** | [**BankAccountUpdateParams**](BankAccountUpdateParams.md)| Bank account update request | 

### Return type

[**BankAccountUpdateResult**](BankAccountUpdateResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bank account updated |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token does not hold the &#x60;banking:write&#x60; scope this route needs. |  -  |
**404** | The resource was not found for this account. |  -  |
**409** | The resource is not in a state that allows this request. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

