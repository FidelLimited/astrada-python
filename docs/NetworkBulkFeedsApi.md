# astrada.NetworkBulkFeedsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_bulk_feed**](NetworkBulkFeedsApi.md#create_network_bulk_feed) | **POST** /network-bulk-feeds | Create network bulk feed
[**get_network_bulk_feed**](NetworkBulkFeedsApi.md#get_network_bulk_feed) | **GET** /network-bulk-feeds/{networkBulkFeedId} | Retrieve a network bulk feed
[**list_network_bulk_feeds**](NetworkBulkFeedsApi.md#list_network_bulk_feeds) | **GET** /network-bulk-feeds | List network bulk feed
[**update_network_bulk_feed**](NetworkBulkFeedsApi.md#update_network_bulk_feed) | **PATCH** /network-bulk-feeds/{networkBulkFeedId} | Update a network bulk feed


# **create_network_bulk_feed**
> NetworkBulkFeeds create_network_bulk_feed(network_bulk_feed_create_params)

Create network bulk feed

Registers a new feed for network bulk.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_feed_create_params import NetworkBulkFeedCreateParams
from astrada.models.network_bulk_feeds import NetworkBulkFeeds

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_bulk_feed_create_params = (  # NetworkBulkFeedCreateParams
    {'networkReference': 'R123456',
     'network': 'AMEX',
     'subaccountId': '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'}
)

result = client.network_bulk_feeds.create_network_bulk_feed(network_bulk_feed_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_bulk_feed_create_params** | [**NetworkBulkFeedCreateParams**](NetworkBulkFeedCreateParams.md)|  | 

### Return type

[**NetworkBulkFeeds**](NetworkBulkFeeds.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**409** | The network bulk feed already exists. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_bulk_feed**
> NetworkBulkFeeds get_network_bulk_feed(network_bulk_feed_id)

Retrieve a network bulk feed

Returns detailed information about a specific network bulk feed by its identifier.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_feeds import NetworkBulkFeeds

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_bulk_feed_id = 'eb2ded7e-11fa-46fc-bd3e-f5b1d56fd3b3'  # str

result = client.network_bulk_feeds.get_network_bulk_feed(network_bulk_feed_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_bulk_feed_id** | **str**|  | 

### Return type

[**NetworkBulkFeeds**](NetworkBulkFeeds.md)

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

# **list_network_bulk_feeds**
> NetworkBulkFeedList list_network_bulk_feeds(network_reference=network_reference, subaccount_id=subaccount_id, limit=limit, offset=offset)

List network bulk feed

Returns all network bulk feeds under the account.

By default, `GET /network-bulk-feeds` returns network bulk feeds ordered by the latest `createdAt`.

This endpoint supports [offset-based pagination](https://docs.astrada.co/reference/pagination).


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_feed_list import NetworkBulkFeedList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_reference = 'G1234567'  # str (optional)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
limit = 50  # int (optional)
offset = 0  # int (optional)

result = client.network_bulk_feeds.list_network_bulk_feeds(network_reference=network_reference, subaccount_id=subaccount_id, limit=limit, offset=offset)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_reference** | **str**| Filters the returned feeds to an exact match on the feed&#39;s network reference. The network reference format depends on the card network (see the schema below).  | [optional] 
 **subaccount_id** | **str**|  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 50]
 **offset** | **int**| The offset to use for pagination. Identifies the position of the first item returned in the collection | [optional] [default to 0]

### Return type

[**NetworkBulkFeedList**](NetworkBulkFeedList.md)

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

# **update_network_bulk_feed**
> NetworkBulkFeeds update_network_bulk_feed(network_bulk_feed_id, network_bulk_feed_update_params)

Update a network bulk feed

Updates a network bulk feed. Supports setting `transactionStartDate`
(currently for `SMARTDATA` feeds only; other feed types are rejected with
a 422) and `expectedCardCount`. At least one field must be provided;
`transactionStartDate` cannot be unset (`null` is rejected).

Setting `transactionStartDate` widens the feed's ingestion window:
transactions posted on or after the date are ingested for the feed's
deliveries, replacing the default 15-day window.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_feed_update_params import NetworkBulkFeedUpdateParams
from astrada.models.network_bulk_feeds import NetworkBulkFeeds

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_bulk_feed_id = 'eb2ded7e-11fa-46fc-bd3e-f5b1d56fd3b3'  # str
network_bulk_feed_update_params = {'transactionStartDate': '2026-07-01'}  # NetworkBulkFeedUpdateParams

result = client.network_bulk_feeds.update_network_bulk_feed(network_bulk_feed_id, network_bulk_feed_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_bulk_feed_id** | **str**|  | 
 **network_bulk_feed_update_params** | [**NetworkBulkFeedUpdateParams**](NetworkBulkFeedUpdateParams.md)|  | 

### Return type

[**NetworkBulkFeeds**](NetworkBulkFeeds.md)

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
**422** | The request is well formatted but it fails some business logic validation |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

