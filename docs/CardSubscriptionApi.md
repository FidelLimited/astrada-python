# astrada.CardSubscriptionApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_card_subscription**](CardSubscriptionApi.md#get_card_subscription) | **GET** /card-subscriptions/{subscriptionId} | Retrieve card subscription
[**list_card_subscriptions**](CardSubscriptionApi.md#list_card_subscriptions) | **GET** /card-subscriptions | List card subscriptions
[**update_card_subscription**](CardSubscriptionApi.md#update_card_subscription) | **PATCH** /card-subscriptions/{subscriptionId} | Update card subscription


# **get_card_subscription**
> CardSubscription get_card_subscription(subscription_id, expand=expand)

Retrieve card subscription

Returns detailed information about a specific card subscription by its identifier, including its data-sharing state.

Add `expand=card,cardholder` to embed the card and cardholder under `_embedded` in the same response instead of fetching them separately. Each embedded resource is the exact body its own endpoint serves and requires that endpoint's scope (`cards:read` for `card`, `cardholder:read` for `cardholder`).


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_subscription import CardSubscription

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subscription_id = 'eb2ded7e-11fa-46fc-bd3e-f5b1d56fd3b3'  # str
expand = ['card', 'cardholder']  # List[str] (optional)

result = client.card_subscription.get_card_subscription(subscription_id, expand=expand)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **expand** | [**List[str]**](str.md)| Comma-separated list of related resources to embed on each card subscription under &#x60;_embedded&#x60;, so one call returns the subscription together with its card and cardholder instead of a &#x60;GET /cards/{cardId}&#x60; and a &#x60;GET /cards/{cardId}/cardholder&#x60; per item.  - &#x60;card&#x60; embeds the card exactly as &#x60;GET /cards/{cardId}&#x60; serves it and requires the &#x60;cards:read&#x60; scope. - &#x60;cardholder&#x60; embeds the cardholder exactly as &#x60;GET /cards/{cardId}/cardholder&#x60; serves it and requires the   &#x60;cardholder:read&#x60; scope.  A request naming a resource its credentials cannot read is refused with &#x60;403&#x60;. When a related resource does not exist (for example a card without cardholder data), its key is absent from &#x60;_embedded&#x60;; &#x60;_links&#x60; are unchanged.  Send one comma-separated value (&#x60;expand&#x3D;card,cardholder&#x60;). A repeated &#x60;expand&#x60; key, an empty value or an unknown value is refused with &#x60;400&#x60;.  | [optional] 

### Return type

[**CardSubscription**](CardSubscription.md)

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

# **list_card_subscriptions**
> CardSubscriptionList list_card_subscriptions(subaccount_id=subaccount_id, card_id=card_id, bank_account_id=bank_account_id, state=state, network_bulk_feed_id=network_bulk_feed_id, company_id=company_id, legal_entity_id=legal_entity_id, legal_entity_name=legal_entity_name, limit=limit, offset=offset, expand=expand)

List card subscriptions

Returns all card subscriptions under the account, ordered by `createdAt` descending (most recently created first).

The `subaccountId`, `cardId`, `bankAccountId`, `state`, `networkBulkFeedId`, `companyId`, `legalEntityId` and `legalEntityName` filters are independent and combine additively; supplying more than one narrows the result set to subscriptions matching **all** of them.

`companyId`, `legalEntityId` and `legalEntityName` filter on the card's cardholder as it is now: `corporate.id`, `corporate.legalEntity.id` and `corporate.legalEntity.name` (see the [Glossary](https://docs.astrada.co/docs/glossary)). Each is an exact match; `legalEntityName` is case-sensitive, and each of `legalEntityId` and `legalEntityName` never matches a cardholder whose legal entity lacks that field, so copy it from the cardholder (`expand=cardholder` shows each cardholder's company and legal entity in the same response). For example, this returns the active subscriptions of one legal entity on one feed:

`GET /card-subscriptions?networkBulkFeedId=<feed>&legalEntityId=<id>&state=active`

These three filters read cardholder data, so they need the `cardholder:read` scope, like `expand=cardholder`. Without it the request returns `403`.

Filtering by `state` accepts any of the states a card subscription reports in its response payload:

- `pending`: enrolled from a network roster while the card is still inactive at the network. The subscription is fully enrolled and billable, but has not yet transacted.
- `active`: also returns subscriptions still completing activation, which already report their own `state` as `active`.
- `deactivated`, `expired`, `reqSCA`, `failed-to-create`: matched exactly.

This endpoint supports [offset-based pagination](https://docs.astrada.co/reference/pagination). Pagination links preserve any filters applied to the original request.

Use `expand` to embed each subscription's card and cardholder in the same response (`?expand=card,cardholder`) instead of calling `GET /cards/{cardId}` and `GET /cards/{cardId}/cardholder` per item. Each embedded resource appears under the item's `_embedded` with the exact body its own endpoint serves, and requires that endpoint's scope (`cards:read` for `card`, `cardholder:read` for `cardholder`). Pagination links preserve `expand` like any other parameter.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_subscription_list import CardSubscriptionList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
card_id = '8164683a-8d23-4421-9694-1a81fc9b9c37'  # str (optional)
bank_account_id = '2b9c1e77-5a3d-4c8b-9f21-6d0e4a7b8c90'  # str (optional)
state = 'active'  # str (optional)
network_bulk_feed_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
company_id = '10021528'  # str (optional)
legal_entity_id = '1000001'  # str (optional)
legal_entity_name = 'Astrada Life'  # str (optional)
limit = 25  # int (optional)
offset = 0  # int (optional)
expand = ['card', 'cardholder']  # List[str] (optional)

result = client.card_subscription.list_card_subscriptions(subaccount_id=subaccount_id, card_id=card_id, bank_account_id=bank_account_id, state=state, network_bulk_feed_id=network_bulk_feed_id, company_id=company_id, legal_entity_id=legal_entity_id, legal_entity_name=legal_entity_name, limit=limit, offset=offset, expand=expand)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | [optional] 
 **card_id** | **str**|  | [optional] 
 **bank_account_id** | **str**| Filter to subscriptions whose card materialized from this bank account (bank-derived subscriptions). | [optional] 
 **state** | **str**|  | [optional] 
 **network_bulk_feed_id** | **str**|  | [optional] 
 **company_id** | **str**| Only subscriptions whose card&#39;s cardholder currently has this company ID (&#x60;corporate.id&#x60;), not the value it had when the subscription was created. Exact match. Requires the &#x60;cardholder:read&#x60; scope.  | [optional] 
 **legal_entity_id** | **str**| Only subscriptions whose card&#39;s cardholder currently belongs to this legal entity (&#x60;corporate.legalEntity.id&#x60;), not the one it belonged to when the subscription was created. Exact match. A cardholder whose legal entity has no id never matches this filter; filter by &#x60;legalEntityName&#x60; instead. Requires the &#x60;cardholder:read&#x60; scope.  | [optional] 
 **legal_entity_name** | **str**| Only subscriptions whose card&#39;s cardholder currently belongs to a legal entity with this name (&#x60;corporate.legalEntity.name&#x60;), not the one it belonged to when the subscription was created. Exact, case-sensitive match. A cardholder whose legal entity has no name never matches this filter; filter by &#x60;legalEntityId&#x60; instead. URL-encode the value: a space is &#x60;%20&#x60; (or &#x60;+&#x60;), for example &#x60;legalEntityName&#x3D;Astrada%20Life&#x60;. Requires the &#x60;cardholder:read&#x60; scope.  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 25]
 **offset** | **int**| The offset to use for pagination. Identifies the position of the first item returned in the collection | [optional] [default to 0]
 **expand** | [**List[str]**](str.md)| Comma-separated list of related resources to embed on each card subscription under &#x60;_embedded&#x60;, so one call returns the subscription together with its card and cardholder instead of a &#x60;GET /cards/{cardId}&#x60; and a &#x60;GET /cards/{cardId}/cardholder&#x60; per item.  - &#x60;card&#x60; embeds the card exactly as &#x60;GET /cards/{cardId}&#x60; serves it and requires the &#x60;cards:read&#x60; scope. - &#x60;cardholder&#x60; embeds the cardholder exactly as &#x60;GET /cards/{cardId}/cardholder&#x60; serves it and requires the   &#x60;cardholder:read&#x60; scope.  A request naming a resource its credentials cannot read is refused with &#x60;403&#x60;. When a related resource does not exist (for example a card without cardholder data), its key is absent from &#x60;_embedded&#x60;; &#x60;_links&#x60; are unchanged.  Send one comma-separated value (&#x60;expand&#x3D;card,cardholder&#x60;). A repeated &#x60;expand&#x60; key, an empty value or an unknown value is refused with &#x60;400&#x60;.  | [optional] 

### Return type

[**CardSubscriptionList**](CardSubscriptionList.md)

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

# **update_card_subscription**
> CardSubscription update_card_subscription(subscription_id, card_subscription_update_params)

Update card subscription

Updates an existing card subscription, allowing changes to its data-sharing state. Subscriptions that were enrolled in bulk, and where `enrollmentType = 'network-bulk'` cannot be updated.

**Note:** setting a card subscription to a `deactivated` state is a final action that cannot be undone.

If the card also has a linked bank account, deactivating it stops that bank account's feed for the card too; to stop only the card network data, ask your Astrada contact.

When deactivating, you can send an optional `deactivationReason` to record why the card was deactivated.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_subscription import CardSubscription
from astrada.models.card_subscription_update_params import CardSubscriptionUpdateParams

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subscription_id = 'eb2ded7e-11fa-46fc-bd3e-f5b1d56fd3b3'  # str
card_subscription_update_params = {'state': 'deactivated', 'deactivationReason': 'cardholder_offboarded'}  # CardSubscriptionUpdateParams

result = client.card_subscription.update_card_subscription(subscription_id, card_subscription_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **card_subscription_update_params** | [**CardSubscriptionUpdateParams**](CardSubscriptionUpdateParams.md)|  | 

### Return type

[**CardSubscription**](CardSubscription.md)

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
**409** | Request conflict with the current state of the target resource |  -  |
**422** | The request is well formatted but it fails some business logic validation |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

