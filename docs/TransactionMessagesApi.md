# astrada.TransactionMessagesApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_raw_transaction_message**](TransactionMessagesApi.md#get_raw_transaction_message) | **GET** /transaction-messages/{transactionMessageId}/raw | Retrieve the raw transaction message
[**get_transaction_message**](TransactionMessagesApi.md#get_transaction_message) | **GET** /transaction-messages/{transactionMessageId} | Retrieve transaction message


# **get_raw_transaction_message**
> RawTransactionMessage get_raw_transaction_message(transaction_message_id)

Retrieve the raw transaction message

Return a raw transaction message by the transaction message unique identifier.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.raw_transaction_message import RawTransactionMessage

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
transaction_message_id = '9340721f-bdce-4afa-bd9d-26cceb9d2176'  # str

result = client.transaction_messages.get_raw_transaction_message(transaction_message_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_message_id** | **str**|  | 

### Return type

[**RawTransactionMessage**](RawTransactionMessage.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw transaction message retrieved successfully |  -  |
**204** | The request has been successfully processed and there is no content to return |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_message**
> TransactionMessage get_transaction_message(transaction_message_id)

Retrieve transaction message

Return a transaction message by its unique identifier, including details about the transaction's type and relevant transactional data.

Transaction messages are also delivered embedded in the transaction payload: `transaction.created` and `transaction.updated` webhook payloads include a projection of every correlated message under `_embedded.messages[]`, each entry carrying its financial fields plus a per-message `superseded` marker. See [Event Types](https://docs.astrada.co/reference/event-types) for the full payload structure.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.transaction_message import TransactionMessage

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
transaction_message_id = '9340721f-bdce-4afa-bd9d-26cceb9d2176'  # str

result = client.transaction_messages.get_transaction_message(transaction_message_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_message_id** | **str**|  | 

### Return type

[**TransactionMessage**](TransactionMessage.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction message retrieved successfully |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

