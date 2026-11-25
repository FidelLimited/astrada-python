# astrada.CardApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_card**](CardApi.md#get_card) | **GET** /cards/{cardId} | Retrieve card
[**get_cardholder**](CardApi.md#get_cardholder) | **GET** /cards/{cardId}/cardholder | Retrieve cardholder information
[**list_cards**](CardApi.md#list_cards) | **GET** /cards | List cards
[**update_cardholder**](CardApi.md#update_cardholder) | **PATCH** /cards/{cardId}/cardholder | Update cardholder information


# **get_card**
> Card get_card(card_id, expand=expand)

Retrieve card

Returns detailed information about a specific card by its identifier.

Add `expand=cardholder` to embed the cardholder under `_embedded` in the same response instead
of calling `GET /cards/{cardId}/cardholder` separately. The embedded body is the exact body that
endpoint serves and requires its `cardholder:read` scope.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card import Card

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
card_id = '6d18f5bb-b9d6-4237-97c2-44b1bdb71d6b'  # str
expand = ['cardholder']  # List[str] (optional)

result = client.card.get_card(card_id, expand=expand)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**|  | 
 **expand** | [**List[str]**](str.md)| Embed the card&#39;s related &#x60;cardholder&#x60; resource under &#x60;_embedded&#x60; so one call returns the card together with its cardholder instead of a follow-up &#x60;GET /cards/{cardId}/cardholder&#x60;.  - &#x60;cardholder&#x60; embeds the cardholder exactly as &#x60;GET /cards/{cardId}/cardholder&#x60; serves it and   requires the &#x60;cardholder:read&#x60; scope.  A request asking to expand a resource its credentials cannot read is refused with &#x60;403&#x60; (&#x60;Missing scope &#39;cardholder:read&#39;&#x60;). When the card has no cardholder, the &#x60;cardholder&#x60; key is absent from &#x60;_embedded&#x60;; &#x60;_links&#x60; are unchanged.  Send &#x60;expand&#x3D;cardholder&#x60;. A repeated &#x60;expand&#x60; key, an empty value or an unknown value is refused with &#x60;400&#x60;.  | [optional] 

### Return type

[**Card**](Card.md)

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

# **get_cardholder**
> Cardholder get_cardholder(card_id)

Retrieve cardholder information

Returns the card's current cardholder information. Answers `404` when the card has no cardholder.

For the company and legal entity the card belonged to at the time of a given transaction, use
`expand=cardholder` on that transaction instead: `GET /transactions/{transactionId}?expand=cardholder`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.cardholder import Cardholder

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
card_id = '6d18f5bb-b9d6-4237-97c2-44b1bdb71d6b'  # str

result = client.card.get_cardholder(card_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**|  | 

### Return type

[**Cardholder**](Cardholder.md)

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

# **list_cards**
> CardList list_cards(country=country, expiry_month=expiry_month, expiry_year=expiry_year, subaccount_id=subaccount_id, network_bulk_feed_id=network_bulk_feed_id, expand=expand, limit=limit, offset=offset)

List cards

Returns a list of all cards linked to the account.

By default, `GET /cards` returns cards ordered by the latest updatedAt. You can combine the different filters as documented.

Use `networkBulkFeedId` to filter the list to cards enrolled through a given network bulk feed. An unknown feed id returns an empty page. It combines with `expand=cardholder`.

Use `expand=cardholder` to embed each card's cardholder under `_embedded` in the same response instead of calling `GET /cards/{cardId}/cardholder` per item. The embedded body is the exact body that endpoint serves and requires its `cardholder:read` scope. Pagination links preserve `expand` like any other parameter.

This endpoint supports [offset-based pagination](https://docs.astrada.co/reference/pagination).


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_list import CardList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
country = 'USA'  # str (optional)
expiry_month = 6  # int (optional)
expiry_year = 2024  # int (optional)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
network_bulk_feed_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
expand = ['cardholder']  # List[str] (optional)
limit = 25  # int (optional)
offset = 0  # int (optional)

result = client.card.list_cards(country=country, expiry_month=expiry_month, expiry_year=expiry_year, subaccount_id=subaccount_id, network_bulk_feed_id=network_bulk_feed_id, expand=expand, limit=limit, offset=offset)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The card country of issuance following ISO 3166 alpha-3 | [optional] 
 **expiry_month** | **int**| The card expiration month | [optional] 
 **expiry_year** | **int**| The card expiration year | [optional] 
 **subaccount_id** | **str**|  | [optional] 
 **network_bulk_feed_id** | **str**|  | [optional] 
 **expand** | [**List[str]**](str.md)| Embed the card&#39;s related &#x60;cardholder&#x60; resource under &#x60;_embedded&#x60; so one call returns the card together with its cardholder instead of a follow-up &#x60;GET /cards/{cardId}/cardholder&#x60;.  - &#x60;cardholder&#x60; embeds the cardholder exactly as &#x60;GET /cards/{cardId}/cardholder&#x60; serves it and   requires the &#x60;cardholder:read&#x60; scope.  A request asking to expand a resource its credentials cannot read is refused with &#x60;403&#x60; (&#x60;Missing scope &#39;cardholder:read&#39;&#x60;). When the card has no cardholder, the &#x60;cardholder&#x60; key is absent from &#x60;_embedded&#x60;; &#x60;_links&#x60; are unchanged.  Send &#x60;expand&#x3D;cardholder&#x60;. A repeated &#x60;expand&#x60; key, an empty value or an unknown value is refused with &#x60;400&#x60;.  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 25]
 **offset** | **int**| The offset to use for pagination. Identifies the position of the first item returned in the collection | [optional] [default to 0]

### Return type

[**CardList**](CardList.md)

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

# **update_cardholder**
> Cardholder update_cardholder(card_id, cardholder_update_params)

Update cardholder information

Updates cardholder information for a specific card. Use this endpoint to simulate cardholder data that would typically be received through a Network Bulk Feed. This is useful for testing your integration against bulk-enrolled cards without waiting for actual network feed data.

**Note:** This endpoint requires the `cardholder:write` scope and must be directly enabled by Astrada.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.cardholder import Cardholder
from astrada.models.cardholder_update_params import CardholderUpdateParams

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
card_id = '6d18f5bb-b9d6-4237-97c2-44b1bdb71d6b'  # str
cardholder_update_params = (  # CardholderUpdateParams
    {'corporate': {'alternativeEmployeeId': 'standin', 'employeeId': 'standin', 'id': 'standin'},
     'email': 'someone@example.com',
     'firstName': 'standin',
     'lastName': 'standin',
     'postalCode': 'standin',
     'subaccountId': '3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b'}
)

result = client.card.update_cardholder(card_id, cardholder_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**|  | 
 **cardholder_update_params** | [**CardholderUpdateParams**](CardholderUpdateParams.md)|  | 

### Return type

[**Cardholder**](Cardholder.md)

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

