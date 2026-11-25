# astrada.banking.BankTransactionsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bank_transaction**](BankTransactionsApi.md#get_bank_transaction) | **GET** /bank-transactions/{subaccountId}/{transactionId} | Retrieve bank transaction
[**list_bank_transactions**](BankTransactionsApi.md#list_bank_transactions) | **GET** /bank-transactions/{subaccountId} | List bank transactions
[**trigger_bank_transaction_webhooks**](BankTransactionsApi.md#trigger_bank_transaction_webhooks) | **POST** /bank-transactions/{subaccountId}/webhooks | Needs banking:admin: Trigger bank transaction webhooks


# **get_bank_transaction**
> BankTransaction get_bank_transaction(subaccount_id, transaction_id)

Retrieve bank transaction

Returns detailed information about a specific bank transaction by its identifier, including match status and transaction metadata.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_transaction import BankTransaction

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str
transaction_id = '9340721f-bdce-4afa-bd9d-26cceb9d2176'  # str

result = client.banking.bank_transactions.get_bank_transaction(subaccount_id, transaction_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 
 **transaction_id** | **str**|  | 

### Return type

[**BankTransaction**](BankTransaction.md)

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

# **list_bank_transactions**
> BankTransactionList list_bank_transactions(subaccount_id, bank_account_id=bank_account_id, card_id=card_id, start_date=start_date, end_date=end_date, min_amount=min_amount, max_amount=max_amount, transaction_type=transaction_type, matched=matched, source=source, limit=limit, cursor=cursor)

List bank transactions

Returns a list of bank transactions for a subaccount. Bank transactions are synced from connected financial institutions. A movement may briefly appear as its pending posting until the posted transaction replaces it (the pending row is then removed from the feed).

By default, `GET /bank-transactions/{subaccountId}` returns transactions ordered by the latest `date`.

This endpoint supports cursor-based pagination and various filters including date range, amount range, and match status.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_transaction_list import BankTransactionList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str
bank_account_id = '2b9c1e77-5a3d-4c8b-9f21-6d0e4a7b8c90'  # str (optional)
card_id = '8164683a-8d23-4421-9694-1a81fc9b9c37'  # str (optional)
start_date = '2025-10-01'  # date (optional)
end_date = '2025-10-31'  # date (optional)
min_amount = 10  # float (optional)
max_amount = 500  # float (optional)
transaction_type = 'debit'  # str (optional)
matched = 'true'  # str (optional)
source = 'PLAID'  # str (optional)
limit = 250  # int (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)

result = client.banking.bank_transactions.list_bank_transactions(subaccount_id, bank_account_id=bank_account_id, card_id=card_id, start_date=start_date, end_date=end_date, min_amount=min_amount, max_amount=max_amount, transaction_type=transaction_type, matched=matched, source=source, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 
 **bank_account_id** | **str**| Filter to subscriptions whose card materialized from this bank account (bank-derived subscriptions). | [optional] 
 **card_id** | **str**|  | [optional] 
 **start_date** | **date**| Filter results from this date (inclusive), in YYYY-MM-DD format | [optional] 
 **end_date** | **date**| Filter results up to this date (inclusive), in YYYY-MM-DD format | [optional] 
 **min_amount** | **float**| Filter transactions with an amount greater than or equal to this value | [optional] 
 **max_amount** | **float**| Filter transactions with an amount less than or equal to this value | [optional] 
 **transaction_type** | **str**| Filter bank transactions by transaction type | [optional] 
 **matched** | **str**| Filter bank transactions by match status. Set to &#x60;true&#x60; to return only matched transactions, or &#x60;false&#x60; for unmatched. | [optional] 
 **source** | **str**| Filter transactions by source. | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 250]
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 

### Return type

[**BankTransactionList**](BankTransactionList.md)

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

# **trigger_bank_transaction_webhooks**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankTransactionWebhooksResult trigger_bank_transaction_webhooks(subaccount_id, bank_transaction_webhooks_params)

Needs banking:admin: Trigger bank transaction webhooks

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Manually triggers webhook delivery for specified bank transactions. This can be used to re-emit webhooks that may have been missed or to force re-matching of transactions.

You can specify which webhook event types to emit: `banktransaction.created` for transaction data or `transaction.match.created` for match results.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_transaction_webhooks_params import BankTransactionWebhooksParams
from astrada.banking.models.bank_transaction_webhooks_result import BankTransactionWebhooksResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str
bank_transaction_webhooks_params = (  # BankTransactionWebhooksParams
    {'ids': ['7f2a9c4e-3b1d-4e8f-a5c7-6d0e2f9b8a3c'],
     'webhooks': ['banktransaction.created', 'transaction.match.created'],
     'forceRematch': False}
)

result = client.banking.bank_transactions.trigger_bank_transaction_webhooks(subaccount_id, bank_transaction_webhooks_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 
 **bank_transaction_webhooks_params** | [**BankTransactionWebhooksParams**](BankTransactionWebhooksParams.md)| Webhook trigger request | 

### Return type

[**BankTransactionWebhooksResult**](BankTransactionWebhooksResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhooks triggered |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

