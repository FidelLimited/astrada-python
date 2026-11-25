# astrada.sandbox.SubaccountsApi

All URIs are relative to *https://api.sandbox.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subaccount**](SubaccountsApi.md#delete_subaccount) | **DELETE** /subaccounts/{subaccountId} | Delete subaccount (sandbox only)


# **delete_subaccount**
> delete_subaccount(subaccount_id)

Delete subaccount (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`), for
clearing test data between runs. Production has no delete call: there
you deactivate card subscriptions with `PATCH`.

Deletes a subaccount and everything under it, and cannot be undone. Its
bank links (with their bank accounts, bank transactions and matches) go
first, then every card subscription, card, cardholder, stored token,
transaction, network bulk feed and webhook of the subaccount.

The call returns when the delete has finished: `204` when it is done,
`502` when a step failed. Retrying a failed delete is always safe:
completed steps are skipped on replay.


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
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str

client.sandbox.delete_subaccount(subaccount_id)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 

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
**204** | The request has been successfully processed and there is no content to return |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**502** | The cascade delete did not complete; retrying the request resumes it |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

