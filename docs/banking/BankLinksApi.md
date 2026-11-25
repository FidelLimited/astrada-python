# astrada.banking.BankLinksApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank_link**](BankLinksApi.md#create_bank_link) | **POST** /bank-links | Create bank link
[**delete_bank_link**](BankLinksApi.md#delete_bank_link) | **DELETE** /bank-links/{bankLinkId} | Needs banking:admin: Delete bank link
[**get_bank_link**](BankLinksApi.md#get_bank_link) | **GET** /bank-links/{bankLinkId} | Retrieve bank link
[**list_bank_links**](BankLinksApi.md#list_bank_links) | **GET** /bank-links | List bank links
[**sync_bank_link**](BankLinksApi.md#sync_bank_link) | **POST** /bank-links/{bankLinkId}/sync | Needs banking:admin: Sync bank link
[**update_bank_link**](BankLinksApi.md#update_bank_link) | **PATCH** /bank-links/{bankLinkId} | Complete bank link


# **create_bank_link**
> BankLink create_bank_link(bank_link_create_params)

Create bank link

Creates a new bank link to initiate a bank enrollment. The response includes a `hostedLink` URL where the user can connect their bank account via Plaid.

The hosted link expires after 4 hours. If the link expires before the user completes enrollment, retrieve the bank link via `GET /bank-links/{bankLinkId}` to get a refreshed URL.

Creating a bank link with an ID that already exists for the account will return a `409 Conflict` error, unless the existing link has expired.

A refused create returns a JSON body with `statusCode` and `message`. These errors also carry a `code`, a stable name to branch on so that you never match on `message` text (the `409` above has no `code`):

- `404` `SUBACCOUNT_NOT_FOUND`: `subaccountId` is not one of the account's subaccounts. Nothing is created. The message is `Subaccount not found for this account`.
- `403` `BANK_ENROLLMENT_DISABLED`: a create is refused when the account has locked bank enrollment (`enrollmentPolicy.bankEnrollmentLocked` is `true` on the subaccount) and the subaccount's `enrollmentPolicy.bankEnrollment` value does not allow a bank link for this card. Otherwise the check does not refuse. Nothing is created. The message is `Bank linking is not enabled for this card on this account`. The body also has a `reason`: `bank-enrollment-off` when the setting is `off`, `network-not-allowed` when it does not allow the card's network, and `network-unknown` when it limits the networks and the request does not show the card's network. The card's network comes from the request: American Express when the link uses the `amex_only` customization, otherwise `bin6` (a first digit of `4` is Visa, `2` or `5` is Mastercard, and any other digit, a `3` included, is unknown). Without `bin6` it is unknown.
- `403` `MASTERCARD_CLIENT_NOT_PROVISIONED` and `PLAID_EC_NOT_PROVISIONED`: the account is not set up for bank linking on that provider yet. The messages are `This account is not set up for Mastercard bank linking yet` and `This account is not set up for Plaid bank linking yet`.
- `403` `PLAID_CUSTOMIZATION_NOT_PROVISIONED`: Plaid refused the Link customization this link asked for, because the account's Plaid client cannot use it, and no fallback applied. Nothing is created. The message is `This account is not fully set up for Plaid bank linking yet`. A customization other than `amex_only` (one set by the bank-linking policy's `plaidLinkCustomizationName`) answers this at once. When Plaid refuses `amex_only`, from `filters.linkCustomizationName` or from the policy, the create is retried once with the environment's pinned customization in its place, or with no customization when the environment pins none. If Plaid accepts the retry, the link is created as usual: its hosted session opens without the `amex_only` customization, and its completion is still held to American Express institutions. For `amex_only`, only a refused retry answers this error. Astrada fixes it in the account's Plaid setup, so sending the same request again does not help.
- `400` `INVALID_LINK_FILTERS`: `filters` asks for more than the account's bank-linking policy allows, or for a customization that is not allowed.
- `400` `PROVIDER_NOT_ENABLED_FOR_ACCOUNT`: `provider` is not enabled for the account.
- `400` `PROVIDER_NOT_SUPPORTED_FOR_COUNTRY`: no provider supports `countryCode` for the chosen `provider`.
- `503` `BANK_FEED_OWNER_NOT_CONFIGURED`: `persona: cardholder` in an environment where cardholder links are not set up yet. Nothing is created; a link without `persona: cardholder` still works. The message is `Cardholder bank linking is not available yet`.

A body that breaks the field formats (for example an empty `accountTypes` or a lower-case `countryCode`) answers `400` with message `Bad Request` and an `errors` list naming each field, and no `code`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_link import BankLink
from astrada.banking.models.bank_link_create_params import BankLinkCreateParams

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_link_create_params = {'id': 'enrollment_abc123', 'subaccountId': '50cced63-ee4e-4ff7-a469-aaa989f220f2'}  # BankLinkCreateParams

result = client.banking.bank_links.create_bank_link(bank_link_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_link_create_params** | [**BankLinkCreateParams**](BankLinkCreateParams.md)| Bank link creation request | 

### Return type

[**BankLink**](BankLink.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bank link created |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The request was refused for one of two reasons: - The token does not hold the &#x60;banking:write&#x60; scope. The message names the scope, and there is no &#x60;code&#x60;. - The account is not set up for this bank link. The answer carries one of the &#x60;403&#x60; codes in this operation&#39;s description, and its message names no scope.  |  -  |
**404** | The resource was not found for this account. |  -  |
**409** | The resource is not in a state that allows this request. |  -  |
**500** | The service failed while handling the request. |  -  |
**503** | Cardholder bank links are not set up in this environment yet (&#x60;BANK_FEED_OWNER_NOT_CONFIGURED&#x60;). Nothing was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_link**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> delete_bank_link(bank_link_id)

Needs banking:admin: Delete bank link

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Deletes a bank link and all associated resources, including the bank subscription, bank accounts, and bank transactions.

Cards are not deleted. A `bank-feed` subscription created at completion is deactivated; a card enrolled by its number only loses its bank account. Each still-active account sends `bankaccount.state_changed`, and each changed subscription sends `cardsubscription.updated`.

**Note:** This action is irreversible and will revoke access to the connected financial institution.


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
bank_link_id = 'enrollment_792dcb7d'  # str

client.banking.bank_links.delete_bank_link(bank_link_id)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_link_id** | **str**| The client-provided identifier of the bank link. | 

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
**204** | Bank link deleted |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**409** | The resource is not in a state that allows this request. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_link**
> BankLink get_bank_link(bank_link_id)

Retrieve bank link

Returns detailed information about a specific bank link by its identifier.

If the bank link is in `pending` state and the hosted link URL has expired, this endpoint will automatically refresh the URL and return the updated link.

Once the user has finished the hosted flow, a read of the link answers `completed`: the link completes without a `PATCH` from you.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_link import BankLink

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_link_id = 'enrollment_792dcb7d'  # str

result = client.banking.bank_links.get_bank_link(bank_link_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_link_id** | **str**| The client-provided identifier of the bank link. | 

### Return type

[**BankLink**](BankLink.md)

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
**404** | The resource was not found for this account. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_links**
> BankLinkList list_bank_links(subaccount_id=subaccount_id, state=state, limit=limit, cursor=cursor)

List bank links

Returns a list of bank links under the account.

By default, `GET /bank-links` returns bank links ordered by the latest `createdAt`.

This endpoint supports cursor-based pagination.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_link_list import BankLinkList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '2fd4d402-b759-479c-87a6-58d85e345356'  # str (optional)
state = 'completed'  # str (optional)
limit = 250  # int (optional)
cursor = 'ZXhhbXBsZQ=='  # str (optional)

result = client.banking.bank_links.list_bank_links(subaccount_id=subaccount_id, state=state, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | [optional] 
 **state** | **str**| Filter bank links by state | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 250]
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 

### Return type

[**BankLinkList**](BankLinkList.md)

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

# **sync_bank_link**
> **Needs banking:admin.** If your API client does not have the `banking:admin` scope, the API answers 403 and this raises `astrada.ScopeRequiredError`; ask Astrada to enable it if you need this operation.

> BankLinkSyncResult sync_bank_link(bank_link_id, bank_link_sync_params=bank_link_sync_params)

Needs banking:admin: Sync bank link

Needs the `banking:admin` scope. If your API client does not have it, the API answers `403 Forbidden`; ask Astrada to enable it if you need this operation.

Triggers a manual sync of transactions for the bank link's associated subscription. This fetches the latest transactions from the financial institution.

Transaction syncs also occur automatically via provider webhooks and scheduled jobs. Use this endpoint to force an immediate sync when needed.

While another sync of the same connection is running, this call answers `200` and syncs nothing; send it again shortly. When the bank is temporarily unavailable it answers `503`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_link_sync_params import BankLinkSyncParams
from astrada.banking.models.bank_link_sync_result import BankLinkSyncResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_link_id = 'enrollment_792dcb7d'  # str
bank_link_sync_params = {'webhooks': ['banktransaction.created'], 'force': False}  # BankLinkSyncParams (optional)

result = client.banking.bank_links.sync_bank_link(bank_link_id, bank_link_sync_params=bank_link_sync_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_link_id** | **str**| The client-provided identifier of the bank link. | 
 **bank_link_sync_params** | [**BankLinkSyncParams**](BankLinkSyncParams.md)| Optional sync configuration | [optional] 

### Return type

[**BankLinkSyncResult**](BankLinkSyncResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sync triggered |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Needs the &#x60;banking:admin&#x60; scope. Your API client does not have it; ask Astrada to enable it if you need this operation.  |  -  |
**404** | The resource was not found for this account. |  -  |
**409** | The resource is not in a state that allows this request. |  -  |
**500** | The service failed while handling the request. |  -  |
**503** | The bank is temporarily unavailable. Nothing was synced; try again later. The message comes from the bank data provider and can change, so do not parse it.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_link**
> BankLink update_bank_link(bank_link_id, bank_link_update_params)

Complete bank link

Completes a bank link enrollment, transitioning it from `pending` to `completed` state. The request body must contain `state: "completed"`.

When a bank link is completed, the system exchanges the enrollment credentials with the provider, creates a bank subscription (connection), and discovers the associated bank accounts.

A link that is no longer `pending` answers `409`; read it with `GET /bank-links/{bankLinkId}`.

The PATCH response echoes the bank link record only. The discovered `bankAccounts` (with each account's `cardIds` and any minted `cards`) are returned by `GET /bank-links/{bankLinkId}`, not by this PATCH.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.banking.models.bank_link import BankLink
from astrada.banking.models.bank_link_update_params import BankLinkUpdateParams

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bank_link_id = 'enrollment_792dcb7d'  # str
bank_link_update_params = {'state': 'completed'}  # BankLinkUpdateParams

result = client.banking.bank_links.update_bank_link(bank_link_id, bank_link_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_link_id** | **str**| The client-provided identifier of the bank link. | 
 **bank_link_update_params** | [**BankLinkUpdateParams**](BankLinkUpdateParams.md)| Bank link completion request | 

### Return type

[**BankLink**](BankLink.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bank link completed |  -  |
**400** | The request was refused. &#x60;message&#x60;, and &#x60;code&#x60; where present, say why. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token does not hold the &#x60;banking:write&#x60; scope this route needs. |  -  |
**404** | The resource was not found for this account. |  -  |
**409** | The resource is not in a state that allows this request. |  -  |
**500** | The service failed while handling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

