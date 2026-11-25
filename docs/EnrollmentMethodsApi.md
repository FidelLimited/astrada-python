# astrada.EnrollmentMethodsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_enrollment_methods**](EnrollmentMethodsApi.md#get_enrollment_methods) | **POST** /enrollment-methods | List the available enrollment methods given a card BIN


# **get_enrollment_methods**
> EnrollmentMethodsResult get_enrollment_methods(enrollment_methods_params)

List the available enrollment methods given a card BIN

List the available enrollment methods given a card BIN.

The Unified Enrollment SDK v2 calls this endpoint for each card: when a person presses **Continue** on the card number screen, with the first 8 to 11 digits they typed (8 by default), and on an employee page that opens on the card form, once 8 digits are typed there. It sends the session's `subaccountId` with the digits, and asks again with the digits alone when that answers `400` or `403`. It routes the session from the answer together with `GET /bin-lookup`. The SDK token therefore needs `enrollment-methods:write`. If your own backend calls it, send up to 11 digits for the most precise answer.

Send `subaccountId` to ask whether that subaccount can enroll this card one at a time with `POST /card-subscriptions`. The response then adds `singleDecision`, from the single-enrollment controls that create runs for the subaccount, and `singleEligible` and `availableEnrollmentMethods` follow it. Create also checks the `country` sent with the card; this request has no country, so `singleDecision` does not cover that check. Without `subaccountId`, the response is about the card alone and no subaccount is read.

When Mastercard's live card data is temporarily unavailable, the response falls back to Astrada's stored card data instead of failing, and `binInfo` comes from that stored data. `bulkLikelihood` is then capped at `medium`, except for BINs with proven bulk history, which stay `proven`, so `network-bulk` is then offered only for those proven BINs. When nothing decides the grade, `bulkLikelihood` is omitted and `unavailable` lists it; `singleEligible` is then `true` and `availableEnrollmentMethods` is `["cardholder-single"]`, unless `singleDecision` refuses the card. Retry later for a full answer.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.enrollment_methods_params import EnrollmentMethodsParams
from astrada.models.enrollment_methods_result import EnrollmentMethodsResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
enrollment_methods_params = {'bin': '42424242'}  # EnrollmentMethodsParams

result = client.enrollment_methods.get_enrollment_methods(enrollment_methods_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_methods_params** | [**EnrollmentMethodsParams**](EnrollmentMethodsParams.md)| Enrollment methods payload | 

### Return type

[**EnrollmentMethodsResult**](EnrollmentMethodsResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | The request failed validation, for example a &#x60;bin&#x60; that is not 6 to 11 digits or a &#x60;subaccountId&#x60; that is not a UUID. A &#x60;subaccountId&#x60; that is not one of your account&#39;s subaccounts also gets &#x60;400&#x60;, with the detail &#x60;Given subaccount is not valid&#x60;. |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**413** | Content Too Large |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

