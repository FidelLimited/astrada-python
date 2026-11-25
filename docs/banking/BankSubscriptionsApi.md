# astrada.banking.BankSubscriptionsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bank_subscription**](BankSubscriptionsApi.md#get_bank_subscription) | **GET** /bank-subscriptions/{bankSubscriptionId} | Needs banking:admin: Retrieve bank subscription
[**get_bank_subscription_by_connection**](BankSubscriptionsApi.md#get_bank_subscription_by_connection) | **GET** /bank-subscriptions/by-connection/{connectionId} | Needs banking:admin: Retrieve bank subscription by connection
[**list_bank_subscriptions**](BankSubscriptionsApi.md#list_bank_subscriptions) | **GET** /bank-subscriptions | Needs banking:admin: List bank subscriptions


# **get_bank_subscription**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankSubscription get_bank_subscription(bank_subscription_id)

Needs banking:admin: Retrieve bank subscription

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Returns detailed information about a specific bank subscription by its identifier, including the connection state and webhook configuration.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_subscription import BankSubscription

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_subscription_id = 'b2c3d4e5-f6a7-8901-bcde-f12345678901'  # str

result = client.banking.bank_subscriptions.get_bank_subscription(bank_subscription_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_subscription_id** | **str**|  | 

### Return type

[**BankSubscription**](BankSubscription.md)

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
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_subscription_by_connection**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankSubscription get_bank_subscription_by_connection(connection_id)

Needs banking:admin: Retrieve bank subscription by connection

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Returns a bank subscription by its provider connection identifier (e.g. Plaid item ID).

This is useful when you have the provider's connection ID and need to look up the corresponding subscription.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_subscription import BankSubscription

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
connection_id = 'conn_abc123def456'  # str

result = client.banking.bank_subscriptions.get_bank_subscription_by_connection(connection_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**|  | 

### Return type

[**BankSubscription**](BankSubscription.md)

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
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_subscriptions**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankSubscriptionList list_bank_subscriptions(subaccount_id=subaccount_id, state=state, connection_id=connection_id, limit=limit, cursor=cursor)

Needs banking:admin: List bank subscriptions

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Returns a list of bank subscriptions (active connections to financial institutions) under the account.

Bank subscriptions are created automatically when a bank link enrollment is completed. Each subscription represents a connection to a single financial institution.

By default, `GET /bank-subscriptions` returns subscriptions ordered by the latest `createdAt`.

This endpoint supports cursor-based pagination.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_subscription_list import BankSubscriptionList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
state = 'active'  # str (optional)
connection_id = 'connection_id_example'  # str (optional)
limit = 250  # int (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)

result = client.banking.bank_subscriptions.list_bank_subscriptions(subaccount_id=subaccount_id, state=state, connection_id=connection_id, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | [optional] 
 **state** | **str**| Filter subscriptions by state | [optional] 
 **connection_id** | **str**| Filter subscriptions by provider connection identifier | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 250]
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 

### Return type

[**BankSubscriptionList**](BankSubscriptionList.md)

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
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

