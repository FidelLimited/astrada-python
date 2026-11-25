# astrada.CardVerificationApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_card_verification**](CardVerificationApi.md#get_card_verification) | **GET** /card-verifications/3ds/{verificationId} | Retrieve 3DS verification
[**list_card_verifications**](CardVerificationApi.md#list_card_verifications) | **GET** /card-verifications/3ds | List a card&#39;s 3DS verifications
[**unlock_card_verification_attempts**](CardVerificationApi.md#unlock_card_verification_attempts) | **POST** /card-verifications/unlock | Unlock a card&#39;s verification attempt lockout


# **get_card_verification**
> CardVerification get_card_verification(verification_id)

Retrieve 3DS verification

Returns the current status and detailed information of a specific 3DS verification by its identifier.

### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_verification import CardVerification

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
verification_id = '9cac38a2-6584-4c1f-92fd-85223774979b'  # str

result = client.card_verification.get_card_verification(verification_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_id** | **str**|  | 

### Return type

[**CardVerification**](CardVerification.md)

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

# **list_card_verifications**
> CardVerificationList list_card_verifications(card_id, state=state)

List a card's 3DS verifications

List the 3DS verifications for a card, most recent first. Use the optional `state`
filter (e.g. `state=failed`) to retrieve only failed verifications; each failed
verification carries a `failureReason` explaining why it failed. This includes
cards declined synchronously at creation (the `POST` returned `400`): those
attempts are persisted as failed verifications with `currentStepId: null`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_verification_list import CardVerificationList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
card_id = '8164683a-8d23-4421-9694-1a81fc9b9c37'  # str
state = 'completed'  # str (optional)

result = client.card_verification.list_card_verifications(card_id, state=state)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**|  | 
 **state** | **str**| Optional filter to retrieve only verifications in the given state. | [optional] 

### Return type

[**CardVerificationList**](CardVerificationList.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_card_verification_attempts**
> CardVerificationUnlockResult unlock_card_verification_attempts(card_verification_unlock_params)

Unlock a card's verification attempt lockout

Clear the cross-network verification **attempt lockout** for a card,
identified by its `cardId`. This re-enables verification attempts for the
card after it has been throttled by too many recent hard failures; the
account-scoped, cross-network throttle that protects the non-HIGHEST tiers
(Visa/Stripe, Mastercard/TNS). Idempotent: unlocking a card that has no
active lock succeeds and clears nothing. The HIGHEST per-fingerprint lockout
is **not** affected by this endpoint.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.card_verification_unlock_params import CardVerificationUnlockParams
from astrada.models.card_verification_unlock_result import CardVerificationUnlockResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
card_verification_unlock_params = {'cardId': '00cdba2d-01f0-46bb-b34a-c76d9699e991'}  # CardVerificationUnlockParams

result = client.card_verification.unlock_card_verification_attempts(card_verification_unlock_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_verification_unlock_params** | [**CardVerificationUnlockParams**](CardVerificationUnlockParams.md)|  | 

### Return type

[**CardVerificationUnlockResult**](CardVerificationUnlockResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The card&#39;s attempt lockout was cleared, or the card had no active lock (idempotent).  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

