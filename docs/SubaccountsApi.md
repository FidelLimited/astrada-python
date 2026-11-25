# astrada.SubaccountsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subaccount**](SubaccountsApi.md#create_subaccount) | **POST** /subaccounts | Create subaccount
[**get_subaccount**](SubaccountsApi.md#get_subaccount) | **GET** /subaccounts/{subaccountId} | Retrieve subaccount
[**list_subaccounts**](SubaccountsApi.md#list_subaccounts) | **GET** /subaccounts | List subaccounts
[**update_subaccount**](SubaccountsApi.md#update_subaccount) | **PATCH** /subaccounts/{subaccountId} | Update subaccount configurations


# **create_subaccount**
> Subaccount create_subaccount(subaccount_create_params=subaccount_create_params)

Create subaccount

Creates a new subaccount, allowing you to set network and regional configurations.

Each network's `countries` can be set to either an array of specific ISO 3166 alpha-3 country codes, or the string `"*"` to inherit all countries from the parent account's capabilities for that network.

When using `"*"`, the subaccount will automatically reflect the parent account's current country list. If the parent account's capabilities change, subaccounts configured with `"*"` will inherit the updated countries.

The single and bulk enrollment configurations are optional. Countries are set per network: each one's country list is the network's `countries`, limited to the countries the account allows for that way of enrolling.
The supported card types for single and bulk enrollment is CONSUMER, while the supported funding card types is DEBIT. If not provided, the block rules for both card types will default to the parent account's default block rule for that network and enrollment level. A list you send is combined with the account's defaults, so it can add blocks but never remove one of the account's defaults. Visa consumer debit and prepaid cards are blocked at the network level regardless of these settings; see `networkBlockedCards` on the subaccount.

To set the default rule on the parent account, please reach out to your account manager or support.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.subaccount import Subaccount
from astrada.models.subaccount_create_params import SubaccountCreateParams

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_create_params = (  # SubaccountCreateParams (optional)
    {'name': 'Subaccount A',
     'configurations': {'VISA': {'countries': ['USA', 'CAN']},
                        'MASTERCARD': {'countries': ['USA']}}}
)

result = client.subaccounts.create_subaccount(subaccount_create_params=subaccount_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_create_params** | [**SubaccountCreateParams**](SubaccountCreateParams.md)|  | [optional] 

### Return type

[**Subaccount**](Subaccount.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New subaccount created successfully. The body is the same effective read model &#x60;GET /subaccounts/{subaccountId}&#x60; returns (&#x60;enrollmentPolicy&#x60;, &#x60;bankLinkingPolicy&#x60;, &#x60;plaidEndCustomer&#x60; and &#x60;enforceIssuerCountry&#x60; resolved against the parent account, and &#x60;networkBlockedCards&#x60; resolved from the platform network configuration), not the raw create-time snapshot. Account-level and platform-level settings therefore appear here even though the new subaccount stores no value for them.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccount**
> Subaccount get_subaccount(subaccount_id)

Retrieve subaccount

Returns detailed information about a specific subaccount by its identifier, including configuration details and associated data.

`_links.team-link` appears when enrollment links are enabled for the account, the token holds `card-subscriptions:write` or `subaccounts:write`, and the subaccount's card enrollment is on (its `enrollmentPolicy.cardEnrollment` is not `false`). It points to `POST /subaccounts/{subaccountId}/team-link`, which creates a team link for the subaccount. An enrollment link session's token never gets it.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.subaccount import Subaccount

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str

result = client.subaccounts.get_subaccount(subaccount_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 

### Return type

[**Subaccount**](Subaccount.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the subaccount giving the accountId and subaccountId |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subaccounts**
> SubaccountList list_subaccounts(cursor=cursor, limit=limit)

List subaccounts

Returns a list of all subaccounts associated with the account.

This endpoint supports [cursor-based pagination](https://docs.astrada.co/reference/pagination).


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.subaccount_list import SubaccountList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
cursor = 'ZXhhbXBsZQ=='  # str (optional)
limit = 25  # int (optional)

result = client.subaccounts.list_subaccounts(cursor=cursor, limit=limit)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor to use for pagination. Identifies your place on the list | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 25]

### Return type

[**SubaccountList**](SubaccountList.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subaccounts list retrieved successfully |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subaccount**
> SubaccountUpdateResult update_subaccount(subaccount_id, subaccount_update_params)

Update subaccount configurations

Update a subaccount name and configurations.
All updated configurations are validated against the capabilities of the main account to ensure compliance.
It is possible to add new networks and/or regions but it is not possible to remove any configurations that were previously set.
`configurations` replaces the whole object: send every network the subaccount has (a network left out is refused with `Delete a configuration is not supported.`), and every block list you want to keep (a block list left out goes back to the account's default).

Each network's `countries` can be set to either an array of specific ISO 3166 alpha-3 country codes, or the string `"*"` to inherit all countries from the parent account's capabilities for that network.

When using `"*"`, the subaccount will automatically reflect the parent account's current country list. If the parent account's capabilities change, subaccounts configured with `"*"` will inherit the updated countries.

The single and bulk enrollment configurations are optional. Countries are set per network: each one's country list is the network's `countries`, limited to the countries the account allows for that way of enrolling. The supported card types for single and bulk enrollment is CONSUMER, while the supported funding card types is DEBIT. If not provided, the block rules for both card types will default to the parent account's default block rule for that network and enrollment level. A list you send is combined with the account's defaults, so it can add blocks but never remove one of the account's defaults. Visa consumer debit and prepaid cards are blocked at the network level regardless of these settings; see `networkBlockedCards` on the subaccount.

To set the default rule on the parent account, please reach out to your account manager or support.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.subaccount_update_params import SubaccountUpdateParams
from astrada.models.subaccount_update_result import SubaccountUpdateResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str
subaccount_update_params = {'name': 'New name'}  # SubaccountUpdateParams

result = client.subaccounts.update_subaccount(subaccount_id, subaccount_update_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 
 **subaccount_update_params** | [**SubaccountUpdateParams**](SubaccountUpdateParams.md)|  | 

### Return type

[**SubaccountUpdateResult**](SubaccountUpdateResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specified subaccount updated successfully. The body is the same effective read model &#x60;GET /subaccounts/{subaccountId}&#x60; returns (&#x60;enrollmentPolicy&#x60;, &#x60;bankLinkingPolicy&#x60;, &#x60;plaidEndCustomer&#x60; and &#x60;enforceIssuerCountry&#x60; resolved against the parent account, and &#x60;networkBlockedCards&#x60; resolved from the platform network configuration), so it may include account-level and platform-level settings that were not part of the request and that the subaccount stores no value for.  When the request&#39;s &#x60;enrollmentPolicy&#x60; holds keys this endpoint does not accept, the body also carries &#x60;ignoredFields&#x60;, which names each of them. Unknown keys outside &#x60;enrollmentPolicy&#x60; are ignored and not listed.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

