# astrada.NetworkBulkEnrollmentsApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_bulk_confirmation**](NetworkBulkEnrollmentsApi.md#create_network_bulk_confirmation) | **POST** /network-bulk-confirmations | Create network bulk confirmation
[**create_network_bulk_enrollment**](NetworkBulkEnrollmentsApi.md#create_network_bulk_enrollment) | **POST** /network-bulk-enrollments | Create network bulk enrollment
[**get_network_bulk_enrollment**](NetworkBulkEnrollmentsApi.md#get_network_bulk_enrollment) | **GET** /network-bulk-enrollments/{networkBulkEnrollmentId} | Retrieve a network bulk enrollment
[**get_open_network_bulk_enrollment**](NetworkBulkEnrollmentsApi.md#get_open_network_bulk_enrollment) | **GET** /network-bulk-enrollments/open | Check for an open network bulk enrollment


# **create_network_bulk_confirmation**
> NetworkBulkConfirmationCreateResult create_network_bulk_confirmation(network_bulk_confirmation_create_params)

Create network bulk confirmation

Asks Astrada to confirm that a card program can join a network bulk feed. Astrada
checks with the issuing bank and the network by hand, then emails the card program
admin with the answer. Unlike `POST /network-bulk-enrollments`, this is not a kickoff:
it does not start outreach to the bank and can never be linked to a feed. A validation
failure or an unknown subaccount answers `400`, as for the kickoff.

A program has one open confirmation request at a time. A program is the calling account,
the `subaccountId`, the `network` and the `bin`. Every stored request is open for 30 days
from its `createdAt`, as nothing closes a request yet. When the program already has an
open request that another request wrote, this request stores nothing and answers `200`
with that request's summary (`alreadyOpen: true`), whatever new `requestId` it sent. No
second request reaches Astrada. Two requests for one program sent at the same time store
one request between them.

Once a request is 30 days old it stops holding its program: nothing is written to it, and
the next request for the program is stored with `201` and reaches Astrada again.

The route answers these errors as `application/problem+json`, with `title` and `detail`:

| Status | When | `detail` |
| --- | --- | --- |
| `400` | The body does not pass validation. `errors` lists each field that failed. | `Request parameters are invalid` |
| `400` | `subaccountId` is not a subaccount of the calling account. | `The subaccount {subaccountId} was not found` |
| `403` | The token holds neither `network-bulk-enrollments:write` nor `network-bulk-feeds:write`. | `You do not have permission to access the requested resource` |
| `500` | The request could not be completed. | `An unexpected error occurred` or `The server encountered an unexpected condition that prevented it from fulfilling the request` |


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_confirmation_create_params import NetworkBulkConfirmationCreateParams
from astrada.models.network_bulk_confirmation_create_result import NetworkBulkConfirmationCreateResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_bulk_confirmation_create_params = (  # NetworkBulkConfirmationCreateParams
    {'requestId': 'c3f1a7e2-5b94-4d0a-8e6f-2a9d4b7c1e35',
     'subaccountId': '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c',
     'network': 'MASTERCARD',
     'bin': '51075500',
     'grade': 'high',
     'binInfo': {'issuerName': 'Jack Henry And Associates',
                 'issuerCountry': 'USA',
                 'type': 'COMMERCIAL',
                 'fundingType': 'CREDIT'},
     'company': {'legalName': 'Vertex Industries, Inc.'},
     'cardAdmin': {'name': 'Dana Whitfield', 'email': 'dana.whitfield@vertexind.com'},
     'bankContact': {'name': 'Sam Lee', 'email': 'sam.lee@bank.example'},
     'customerReferenceId': 'ledgerly-customer-8842'}
)

result = client.network_bulk_enrollments.create_network_bulk_confirmation(network_bulk_confirmation_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_bulk_confirmation_create_params** | [**NetworkBulkConfirmationCreateParams**](NetworkBulkConfirmationCreateParams.md)|  | 

### Return type

[**NetworkBulkConfirmationCreateResult**](NetworkBulkConfirmationCreateResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A stored confirmation request, returned unchanged, in one of two shapes:  - A confirmation with this &#x60;requestId&#x60; already exists: the full confirmation, as your   request wrote it. - The program already has an open request that another request wrote: its summary,   marked &#x60;alreadyOpen: true&#x60;, with the &#x60;requestId&#x60; this request sent. Names, emails,   bank contact, &#x60;binInfo&#x60; and &#x60;grade&#x60; are left out.  Both are plain JSON with no &#x60;_links&#x60;.  |  -  |
**201** | Resource created. The program had no open request, so this request wrote one. Served as plain JSON rather than HAL, since a confirmation has no GET and so carries no &#x60;_links&#x60;. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_bulk_enrollment**
> NetworkBulkEnrollmentCreateResult create_network_bulk_enrollment(network_bulk_enrollment_create_params)

Create network bulk enrollment

Starts a bulk enrollment kickoff for a whole card program. The request records the
company, the card program admin, an optional bank contact and program size, and the
admin's consent, and Astrada's onboarding team takes it from there with the issuing
bank. The Unified Enrollment SDK calls this endpoint when an admin sends the bulk
kickoff form (in SDK v1, with `bulkFlow: "kickoff"`); you can also call it directly.

Nothing is enrolled yet at this point. Once the bank has issued the network
reference, register the feed with `POST /network-bulk-feeds` and pass this
enrollment's `id` as `networkBulkEnrollmentId`; the enrollment then moves to
`feed-created` and links to the feed.

The subaccount must belong to the calling account. The BIN's bulk eligibility is not
re-checked here. A validation failure or an unknown subaccount answers `400`.

A program has one open kickoff at a time. A program is the calling account, the
`subaccountId`, the `network` and the first 8 digits of the `bin`; a `bin` shorter than
8 digits matches only a kickoff with exactly the same digits. A kickoff is open while it
is `requested` and was created less than 90 days ago, or while it is `feed-created` and
its feed is live (not `failed` or `deactivated`, and not deleted), at any age. When the
program already has an open kickoff that another request wrote, this request stores no
second kickoff and answers `200` with that kickoff's summary (`alreadyOpen: true`),
whatever new `requestId` it sent, or none. Astrada keeps the card admin named in this
request with the open kickoff, so its onboarding team knows who else is waiting, and the
open kickoff stays the only one they work on. A repeat of the same `requestId` is kept once.
`GET /network-bulk-enrollments/open` answers the same question before the form.
Two kickoffs for one program sent at the same time store one kickoff between them.

The 90 days count from the kickoff's `createdAt`. Once a `requested` kickoff is 90 days
old it stops holding its program: nothing is written to it, it keeps its state and can
still be read, and the next kickoff for the program is created with `201`. A `cancelled`
kickoff, or one whose feed failed, was deactivated or was deleted, does not hold its
program either.

Requires the `network-bulk-enrollments:write` scope. Tokens that only hold
`network-bulk-feeds:write` are still accepted, so existing integrations keep working.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_enrollment_create_params import NetworkBulkEnrollmentCreateParams
from astrada.models.network_bulk_enrollment_create_result import NetworkBulkEnrollmentCreateResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_bulk_enrollment_create_params = (  # NetworkBulkEnrollmentCreateParams
    {'requestId': '3f8a1c52-7d4e-4b19-9c06-5e2b8d7a9f14',
     'subaccountId': '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c',
     'network': 'MASTERCARD',
     'bin': '51075500',
     'binInfo': {'issuerName': 'Example Bank',
                 'issuerCountry': 'USA',
                 'type': 'COMMERCIAL',
                 'fundingType': 'CREDIT'},
     'company': {'legalName': 'Vertex Industries, Inc.'},
     'cardAdmin': {'name': 'Dana Whitfield', 'email': 'dana.whitfield@vertexind.com'},
     'bankContact': {'name': 'Sam Lee', 'email': 'sam.lee@bank.example'},
     'cardCountBand': '251-1000',
     'cardCount': 400,
     'outreach': 'astrada',
     'consent': {'accepted': True, 'version': 'kickoff-consent-v2'},
     'customerReferenceId': 'ledgerly-customer-8842'}
)

result = client.network_bulk_enrollments.create_network_bulk_enrollment(network_bulk_enrollment_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_bulk_enrollment_create_params** | [**NetworkBulkEnrollmentCreateParams**](NetworkBulkEnrollmentCreateParams.md)|  | 

### Return type

[**NetworkBulkEnrollmentCreateResult**](NetworkBulkEnrollmentCreateResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A stored kickoff, returned unchanged, in one of two shapes:  - An enrollment with this &#x60;requestId&#x60; already exists: the full enrollment, as your   request wrote it. - The program already has an open kickoff that another request wrote: its summary,   marked &#x60;alreadyOpen: true&#x60;, with the &#x60;requestId&#x60; this request sent (&#x60;null&#x60; when it   sent none) and only the &#x60;self&#x60; link. Names, emails, bank contact, &#x60;binInfo&#x60;, consent   and outreach are left out.  |  -  |
**201** | Resource created. The program had no open kickoff, so this request wrote one. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_bulk_enrollment**
> NetworkBulkEnrollment get_network_bulk_enrollment(network_bulk_enrollment_id)

Retrieve a network bulk enrollment

Returns a network bulk enrollment by its identifier. Once a feed has been registered
with this enrollment's id on `POST /network-bulk-feeds`, the representation carries
`networkBulkFeedId` and a `networkBulkFeed` link. An enrollment that belongs to
another account answers `404`.

Requires the `network-bulk-enrollments:read` scope. Tokens that only hold
`network-bulk-feeds:read` are still accepted, so existing integrations keep working.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_enrollment import NetworkBulkEnrollment

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
network_bulk_enrollment_id = '9c1f0c4e-2f0e-4a9c-9a1b-0c1d2e3f4a5b'  # str

result = client.network_bulk_enrollments.get_network_bulk_enrollment(network_bulk_enrollment_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_bulk_enrollment_id** | **str**|  | 

### Return type

[**NetworkBulkEnrollment**](NetworkBulkEnrollment.md)

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

# **get_open_network_bulk_enrollment**
> NetworkBulkEnrollmentOpen get_open_network_bulk_enrollment(subaccount_id, network, bin)

Check for an open network bulk enrollment

Answers whether a card program already has an open bulk enrollment kickoff, before anyone
fills in the kickoff form. The Unified Enrollment SDK calls it while it looks up a card, and
shows "Already under way" instead of the program screen when the program has one; you can
also call it directly.

A program is the calling account, the `subaccountId`, the `network` and the card's first 8
digits (`bin`). The rule is the one `POST /network-bulk-enrollments` uses: a kickoff is open
while it is `requested` and was created less than 90 days ago, or while it is `feed-created`
and its feed is live, at any age. The account comes from the token, never from the query.

The answer carries only the open kickoff's `enrollmentId`, `state` and `requestedAt`. A
`bin` of more or fewer than 8 digits, a missing or unknown parameter, or an `accountId` in
the query answers `400`.

Requires the `network-bulk-enrollments:write` scope, the one the kickoff itself takes.
Tokens that only hold `network-bulk-feeds:write` are also accepted. A token with only a read
scope answers `403`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.network_bulk_enrollment_open import NetworkBulkEnrollmentOpen

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '3f2b8c1e-6a4d-4e2f-9b7a-1c5d8e9f0a2b'  # str
network = 'AMEX'  # str
bin = '41111111'  # str

result = client.network_bulk_enrollments.get_open_network_bulk_enrollment(subaccount_id, network, bin)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**| The subaccount of the card program. Must belong to the calling account to find anything. | 
 **network** | **str**| The card&#39;s network. | 
 **bin** | **str**| Exactly the card&#39;s first 8 digits. | 

### Return type

[**NetworkBulkEnrollmentOpen**](NetworkBulkEnrollmentOpen.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the program has an open kickoff. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

