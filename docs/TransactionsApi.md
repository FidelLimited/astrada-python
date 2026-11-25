# astrada.TransactionsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{transactionId} | Retrieve transaction
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List transactions


# **get_transaction**
> Transaction get_transaction(transaction_id, expand=expand)

Retrieve transaction

Returns a transaction by its unique identifier, including details about the transaction's state and relevant transactional data.

Add `expand` to embed related resources under `_embedded` in the same response, for example
`expand=cardSubscription,card,cardholder`. Each embedded resource is the exact body its own endpoint
serves, shows its current values (not those at the time of the transaction) except
`cardholder.corporate`, which is resolved as of the transaction's date (see the `expand` parameter), and
requires that endpoint's scope: `card-subscriptions:read` for `cardSubscription`, `cards:read` for `card`,
`cardholder:read` for `cardholder`.

For the company and legal entity a card belonged to when the transaction happened, use `expand=cardholder`
and read `cardholder.corporate.id` and `cardholder.corporate.legalEntity`. They are the values in effect on
the transaction's `transactionOccurrenceDate` (through the end of that UTC day), or at the transaction's
`createdAt` when that is null, so a card that later moved to another company or legal entity keeps its
historical attribution on past transactions.
Transactions themselves do not carry a company identifier.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.transaction import Transaction

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
transaction_id = '9340721f-bdce-4afa-bd9d-26cceb9d2176'  # str
expand = ['cardSubscription', 'card', 'cardholder']  # List[str] (optional)

result = client.transactions.get_transaction(transaction_id, expand=expand)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **expand** | [**List[str]**](str.md)| Comma-separated list of related resources to embed on the transaction under &#x60;_embedded&#x60;, so one call returns the transaction together with its card subscription, card and cardholder instead of follow-up calls to &#x60;GET /card-subscriptions?cardId&#x3D;&#x60;, &#x60;GET /cards/{cardId}&#x60; and &#x60;GET /cards/{cardId}/cardholder&#x60;.  - &#x60;cardSubscription&#x60; embeds the card subscription exactly as &#x60;GET /card-subscriptions/{subscriptionId}&#x60;   serves it (without its own &#x60;_embedded&#x60;) and requires the &#x60;card-subscriptions:read&#x60; scope. - &#x60;card&#x60; embeds the transaction&#39;s card exactly as &#x60;GET /cards/{cardId}&#x60; serves it (without its own   &#x60;_embedded&#x60;) and requires the &#x60;cards:read&#x60; scope. - &#x60;cardholder&#x60; embeds the card&#39;s cardholder as &#x60;GET /cards/{cardId}/cardholder&#x60; serves it, with one   difference: &#x60;corporate&#x60; is the cardholder&#39;s corporate as of the transaction (see below). Requires the   &#x60;cardholder:read&#x60; scope.  Each value is checked separately: a request asking to expand a resource its credentials cannot read is refused with &#x60;403&#x60;.  The embedded subscription is the card&#39;s subscription in the transaction&#39;s sub-account: the one from the transaction&#39;s network bulk feed when the transaction has a &#x60;networkBulkFeedId&#x60;, otherwise the card&#39;s current subscription, otherwise its most recent one.  &#x60;cardSubscription&#x60; and &#x60;card&#x60; show their **current** values, not the values they had when the transaction happened. So does the cardholder, except for &#x60;cardholder.corporate&#x60;: its &#x60;id&#x60;, &#x60;employeeId&#x60;, &#x60;alternativeEmployeeId&#x60; and &#x60;legalEntity&#x60; are the values in effect on the transaction&#39;s &#x60;transactionOccurrenceDate&#x60; (through the end of that UTC day), or at the transaction&#39;s &#x60;createdAt&#x60; when &#x60;transactionOccurrenceDate&#x60; is null. A card that moved to another company or legal entity after the transaction therefore still shows the one it belonged to at the time. &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;email&#x60;, &#x60;postalCode&#x60;, &#x60;corporate.networkToken&#x60;, &#x60;createdAt&#x60; and &#x60;updatedAt&#x60; are the cardholder&#39;s current values. Changes are dated by when Astrada received them from the card network or through the API. For a transaction dated before Astrada started recording the card&#39;s corporate history, the earliest recorded values are returned instead. Either way, a value that was not set in the values returned is null, or for &#x60;legalEntity&#x60; absent.  A key is present only when it was requested and the related resource exists, and it is never null. A transaction with no card (&#x60;cardId&#x60; is null, for example a bank-sourced transaction with no linked card) has no &#x60;cardSubscription&#x60;, &#x60;card&#x60; or &#x60;cardholder&#x60;. A card without cardholder data has no &#x60;cardholder&#x60;. A card that &#x60;GET /cards/{cardId}&#x60; no longer returns (it responds &#x60;404&#x60;, for example because all of its card subscriptions were deleted) is not embedded: both &#x60;card&#x60; and &#x60;cardholder&#x60; are absent. &#x60;_links&#x60; are unchanged. Without &#x60;expand&#x60;, &#x60;_embedded&#x60; is absent. Whether &#x60;cardholder&#x60; is embedded is decided on the card and cardholder as they are now, not as of the transaction&#39;s date.  Send one comma-separated value (&#x60;expand&#x3D;cardSubscription,card,cardholder&#x60;). A repeated &#x60;expand&#x60; key, an empty value or an unknown value is refused with &#x60;400&#x60;.  | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction retrieved successfully |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> TransactionList list_transactions(transaction_message_id=transaction_message_id, subaccount_id=subaccount_id, cursor=cursor, card_id=card_id, network_bulk_feed_id=network_bulk_feed_id, company_id=company_id, legal_entity_id=legal_entity_id, legal_entity_name=legal_entity_name, limit=limit, order=order, expand=expand)

List transactions

Returns a list of all transactions under the account.

By default, `GET /transactions` returns transactions ordered by the latest `createdAt`. You can combine the different filters as documented.

This endpoint supports [cursor-based pagination](https://docs.astrada.co/reference/pagination).

Add `expand` to embed each transaction's related resources under `_embedded` in the same response,
for example `expand=cardSubscription,card,cardholder`. Each embedded resource is the exact body its own
endpoint serves, shows its current values (not those at the time of the transaction) except
`cardholder.corporate`, which is resolved as of the transaction's date (see the `expand` parameter), and
requires that endpoint's scope: `card-subscriptions:read` for `cardSubscription`, `cards:read` for `card`,
`cardholder:read` for `cardholder`. Transactions without a given related resource simply omit that key.
Pagination links preserve `expand`.

For the company and legal entity a card belonged to when the transaction happened, use `expand=cardholder`
and read `cardholder.corporate.id` and `cardholder.corporate.legalEntity`. They are the values in effect on
the transaction's `transactionOccurrenceDate` (through the end of that UTC day), or at the transaction's
`createdAt` when that is null, so a card that later moved to another company or legal entity keeps its
historical attribution on past transactions.
Transactions themselves do not carry a company identifier.

To list the transactions of one company or legal entity, filter with `companyId`, `legalEntityId` or
`legalEntityName`. They match the cardholder's `corporate.id`, `corporate.legalEntity.id` and
`corporate.legalEntity.name` on the transaction date: the values `expand=cardholder` returns on each
transaction, not the cardholder's current ones (see the [Glossary](https://docs.astrada.co/docs/glossary)).
Each is an exact, case-sensitive match, so copy the value from a transaction's `expand=cardholder`.
The filters use the same as-of resolution as `expand=cardholder`, including the earliest recorded values
for a transaction dated before Astrada started recording the card's corporate history. A transaction
whose card has no cardholder data, or whose card `GET /cards/{cardId}` no longer returns, does not match, just
as `expand` embeds no `cardholder` for it.
They combine with each other and with `transactionMessageId`, `cardId`, `subaccountId` and
`networkBulkFeedId`: supplying more than one returns only the transactions matching **all** of them.
The one exception: `cardId` and `networkBulkFeedId` cannot be sent together, and the request answers `400`.
Transactions without a card never match. For example, this returns one legal entity's transactions on
one feed:

`GET /transactions?networkBulkFeedId=<feed>&legalEntityId=<id>`

URL-encode the values. In `legalEntityName` a space is `%20` (or `+`), and a literal `+` is read as a
space, so send a `+` in the name as `%2B`. Send each filter once. Leading and trailing spaces are
ignored. A value that is empty or only spaces, or longer than 255 characters, is refused with `400`.

With any of these filters a page can hold fewer than `limit` transactions, even none, while
`_links.next` is present. Keep following `_links.next` until it is absent.

These three filters read cardholder data, so they need the `cardholder:read` scope, like
`expand=cardholder`. Without it the request returns `403`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.transaction_list import TransactionList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
transaction_message_id = '9a88aa0e-c1d3-4e70-b5e1-45ab64eb5aac'  # str (optional)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)
card_id = '8164683a-8d23-4421-9694-1a81fc9b9c37'  # str (optional)
network_bulk_feed_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
company_id = '10021528'  # str (optional)
legal_entity_id = '1000001'  # str (optional)
legal_entity_name = 'Astrada Life'  # str (optional)
limit = 25  # int (optional)
order = 'desc'  # str (optional)
expand = ['cardSubscription', 'card', 'cardholder']  # List[str] (optional)

result = client.transactions.list_transactions(transaction_message_id=transaction_message_id, subaccount_id=subaccount_id, cursor=cursor, card_id=card_id, network_bulk_feed_id=network_bulk_feed_id, company_id=company_id, legal_entity_id=legal_entity_id, legal_entity_name=legal_entity_name, limit=limit, order=order, expand=expand)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_message_id** | **str**|  | [optional] 
 **subaccount_id** | **str**|  | [optional] 
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 
 **card_id** | **str**|  | [optional] 
 **network_bulk_feed_id** | **str**|  | [optional] 
 **company_id** | **str**| Only transactions whose card&#39;s cardholder had this company ID (&#x60;corporate.id&#x60;) on the transaction date (the value &#x60;expand&#x3D;cardholder&#x60; returns on that transaction; the &#x60;expand&#x60; parameter defines the date), not the cardholder&#39;s current company. Exact, case-sensitive match. Requires the &#x60;cardholder:read&#x60; scope.  | [optional] 
 **legal_entity_id** | **str**| Only transactions whose card&#39;s cardholder belonged to this legal entity (&#x60;corporate.legalEntity.id&#x60;) on the transaction date (the value &#x60;expand&#x3D;cardholder&#x60; returns on that transaction; the &#x60;expand&#x60; parameter defines the date), not the legal entity it belongs to now. Exact, case-sensitive match. Requires the &#x60;cardholder:read&#x60; scope.  | [optional] 
 **legal_entity_name** | **str**| Only transactions whose card&#39;s cardholder belonged to a legal entity with this name (&#x60;corporate.legalEntity.name&#x60;) on the transaction date (the value &#x60;expand&#x3D;cardholder&#x60; returns on that transaction; the &#x60;expand&#x60; parameter defines the date), not the legal entity it belongs to now. Exact, case-sensitive match. URL-encode the value: a space is &#x60;%20&#x60; (or &#x60;+&#x60;), for example &#x60;legalEntityName&#x3D;Astrada%20Life&#x60;. A literal &#x60;+&#x60; is read as a space, so send a &#x60;+&#x60; in the name as &#x60;%2B&#x60;. Requires the &#x60;cardholder:read&#x60; scope.  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 25]
 **order** | **str**|  | [optional] [default to desc]
 **expand** | [**List[str]**](str.md)| Comma-separated list of related resources to embed on the transaction under &#x60;_embedded&#x60;, so one call returns the transaction together with its card subscription, card and cardholder instead of follow-up calls to &#x60;GET /card-subscriptions?cardId&#x3D;&#x60;, &#x60;GET /cards/{cardId}&#x60; and &#x60;GET /cards/{cardId}/cardholder&#x60;.  - &#x60;cardSubscription&#x60; embeds the card subscription exactly as &#x60;GET /card-subscriptions/{subscriptionId}&#x60;   serves it (without its own &#x60;_embedded&#x60;) and requires the &#x60;card-subscriptions:read&#x60; scope. - &#x60;card&#x60; embeds the transaction&#39;s card exactly as &#x60;GET /cards/{cardId}&#x60; serves it (without its own   &#x60;_embedded&#x60;) and requires the &#x60;cards:read&#x60; scope. - &#x60;cardholder&#x60; embeds the card&#39;s cardholder as &#x60;GET /cards/{cardId}/cardholder&#x60; serves it, with one   difference: &#x60;corporate&#x60; is the cardholder&#39;s corporate as of the transaction (see below). Requires the   &#x60;cardholder:read&#x60; scope.  Each value is checked separately: a request asking to expand a resource its credentials cannot read is refused with &#x60;403&#x60;.  The embedded subscription is the card&#39;s subscription in the transaction&#39;s sub-account: the one from the transaction&#39;s network bulk feed when the transaction has a &#x60;networkBulkFeedId&#x60;, otherwise the card&#39;s current subscription, otherwise its most recent one.  &#x60;cardSubscription&#x60; and &#x60;card&#x60; show their **current** values, not the values they had when the transaction happened. So does the cardholder, except for &#x60;cardholder.corporate&#x60;: its &#x60;id&#x60;, &#x60;employeeId&#x60;, &#x60;alternativeEmployeeId&#x60; and &#x60;legalEntity&#x60; are the values in effect on the transaction&#39;s &#x60;transactionOccurrenceDate&#x60; (through the end of that UTC day), or at the transaction&#39;s &#x60;createdAt&#x60; when &#x60;transactionOccurrenceDate&#x60; is null. A card that moved to another company or legal entity after the transaction therefore still shows the one it belonged to at the time. &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;email&#x60;, &#x60;postalCode&#x60;, &#x60;corporate.networkToken&#x60;, &#x60;createdAt&#x60; and &#x60;updatedAt&#x60; are the cardholder&#39;s current values. Changes are dated by when Astrada received them from the card network or through the API. For a transaction dated before Astrada started recording the card&#39;s corporate history, the earliest recorded values are returned instead. Either way, a value that was not set in the values returned is null, or for &#x60;legalEntity&#x60; absent.  A key is present only when it was requested and the related resource exists, and it is never null. A transaction with no card (&#x60;cardId&#x60; is null, for example a bank-sourced transaction with no linked card) has no &#x60;cardSubscription&#x60;, &#x60;card&#x60; or &#x60;cardholder&#x60;. A card without cardholder data has no &#x60;cardholder&#x60;. A card that &#x60;GET /cards/{cardId}&#x60; no longer returns (it responds &#x60;404&#x60;, for example because all of its card subscriptions were deleted) is not embedded: both &#x60;card&#x60; and &#x60;cardholder&#x60; are absent. &#x60;_links&#x60; are unchanged. Without &#x60;expand&#x60;, &#x60;_embedded&#x60; is absent. Whether &#x60;cardholder&#x60; is embedded is decided on the card and cardholder as they are now, not as of the transaction&#39;s date.  Send one comma-separated value (&#x60;expand&#x3D;cardSubscription,card,cardholder&#x60;). A repeated &#x60;expand&#x60; key, an empty value or an unknown value is refused with &#x60;400&#x60;.  | [optional] 

### Return type

[**TransactionList**](TransactionList.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transactions retrieved successfully |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

