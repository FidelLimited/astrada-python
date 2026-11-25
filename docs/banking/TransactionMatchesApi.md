# astrada.banking.TransactionMatchesApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_match**](TransactionMatchesApi.md#get_transaction_match) | **GET** /transaction-matches/{subaccountId}/{transactionMatchId} | Retrieve transaction match
[**list_transaction_matches**](TransactionMatchesApi.md#list_transaction_matches) | **GET** /transaction-matches/{subaccountId} | List transaction matches


# **get_transaction_match**
> TransactionMatch get_transaction_match(subaccount_id, transaction_match_id)

Retrieve transaction match

Returns detailed information about a specific transaction match, including the confidence level, numeric score, and a breakdown of the scoring factors.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.transaction_match import TransactionMatch

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str
transaction_match_id = 'c3d4e5f6-a7b8-9012-cdef-123456789012'  # str

result = client.banking.transaction_matches.get_transaction_match(subaccount_id, transaction_match_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 
 **transaction_match_id** | **str**|  | 

### Return type

[**TransactionMatch**](TransactionMatch.md)

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

# **list_transaction_matches**
> TransactionMatchList list_transaction_matches(subaccount_id, bank_account_id=bank_account_id, card_id=card_id, bank_transaction_id=bank_transaction_id, card_transaction_id=card_transaction_id, min_confidence=min_confidence, start_date=start_date, end_date=end_date, limit=limit, cursor=cursor)

List transaction matches

Returns a list of transaction matches for a subaccount. Each match represents a link between a bank transaction and a card transaction, along with a confidence score and the reasoning behind the match.

By default, matches are filtered to `MEDIUM` confidence and above. Use the `minConfidence` parameter to adjust the threshold.

By default, `GET /transaction-matches/{subaccountId}` returns matches ordered by the latest `createdAt`.

This endpoint supports cursor-based pagination.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.transaction_match_list import TransactionMatchList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str
bank_account_id = '2b9c1e77-5a3d-4c8b-9f21-6d0e4a7b8c90'  # str (optional)
card_id = '8164683a-8d23-4421-9694-1a81fc9b9c37'  # str (optional)
bank_transaction_id = '7f2a9c4e-3b1d-4e8f-a5c7-6d0e2f9b8a3c'  # str (optional)
card_transaction_id = 'a9b8c7d6-e5f4-3a2b-1c0d-9e8f7a6b5c4d'  # str (optional)
min_confidence = 'MEDIUM'  # str (optional)
start_date = '2025-10-01'  # date (optional)
end_date = '2025-10-31'  # date (optional)
limit = 250  # int (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)

result = client.banking.transaction_matches.list_transaction_matches(subaccount_id, bank_account_id=bank_account_id, card_id=card_id, bank_transaction_id=bank_transaction_id, card_transaction_id=card_transaction_id, min_confidence=min_confidence, start_date=start_date, end_date=end_date, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 
 **bank_account_id** | **str**| Filter to subscriptions whose card materialized from this bank account (bank-derived subscriptions). | [optional] 
 **card_id** | **str**|  | [optional] 
 **bank_transaction_id** | **str**| Filter by bank transaction identifier | [optional] 
 **card_transaction_id** | **str**| Filter by card transaction identifier | [optional] 
 **min_confidence** | **str**| Filter transaction matches by minimum confidence level. Defaults to &#x60;MEDIUM&#x60;, which returns HIGH and MEDIUM matches. | [optional] [default to MEDIUM]
 **start_date** | **date**| Filter results from this date (inclusive), in YYYY-MM-DD format | [optional] 
 **end_date** | **date**| Filter results up to this date (inclusive), in YYYY-MM-DD format | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 250]
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 

### Return type

[**TransactionMatchList**](TransactionMatchList.md)

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
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

