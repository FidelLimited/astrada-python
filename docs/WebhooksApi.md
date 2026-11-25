# astrada.WebhooksApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Delete webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Retrieve webhook
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /webhooks | List webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /webhooks/{webhookId} | Update webhook


# **create_webhook**
> WebhookCreateResult create_webhook(webhook_create_params)

Create webhook

Registers a new webhook for capturing event notifications.

A `subaccountId` that is not one of your subaccounts is refused with `400` "Request parameters are invalid", and its `errors` list holds "Given subaccount does not exist".


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.webhook_create_params import WebhookCreateParams
from astrada.models.webhook_create_result import WebhookCreateResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
webhook_create_params = (  # WebhookCreateParams
    {'url': 'https://example-api.com/path',
     'description': 'Example of Webhook description',
     'eventTypes': ['transactionmessage.created'],
     'subaccountId': 'f297d659-c13d-4219-aeaa-e10a845140a5'}
)

result = client.webhooks.create_webhook(webhook_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_create_params** | [**WebhookCreateParams**](WebhookCreateParams.md)|  | 

### Return type

[**WebhookCreateResult**](WebhookCreateResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(webhook_id)

Delete webhook

Remove a configured webhook by its identifier. Results in the resource being deleted and no longer available.

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
webhook_id = '3c750084-a60f-478c-ab91-c53567d11fac'  # str

client.webhooks.delete_webhook(webhook_id)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Retrieve webhook

Returns detailed information about a specific webhook by its identifier, including its configuration and event subscription details.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.webhook import Webhook

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
webhook_id = '3c750084-a60f-478c-ab91-c53567d11fac'  # str

result = client.webhooks.get_webhook(webhook_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhookList list_webhooks(subaccount_id=subaccount_id, limit=limit, cursor=cursor)

List webhooks

Returns all webhooks configured under the account, optionally filtered by subaccount, including details on the events each webhook is subscribed to.

This endpoint supports [cursor-based pagination](https://docs.astrada.co/reference/pagination).


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.webhook_list import WebhookList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
limit = 25  # int (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)

result = client.webhooks.list_webhooks(subaccount_id=subaccount_id, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 25]
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> Webhook update_webhook(webhook_id, webhook_update_params)

Update webhook

Updates the configuration of an existing webhook, allowing changes to the event subscriptions or notification URL.

Only `url`, `description`, `eventTypes` and `enabled` can be sent. Any other field, `subaccountId` included, is refused with `400`: a webhook's subaccount can't be changed.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.webhook import Webhook
from astrada.models.webhook_update_params import WebhookUpdateParams

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
webhook_id = '3c750084-a60f-478c-ab91-c53567d11fac'  # str
webhook_update_params = (  # WebhookUpdateParams
    {'description': 'standin',
     'enabled': True,
     'eventTypes': ['cardsubscription.created'],
     'url': 'https://example.com/path'}
)

result = client.webhooks.update_webhook(webhook_id, webhook_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_update_params** | [**WebhookUpdateParams**](WebhookUpdateParams.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

