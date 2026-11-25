# astrada.EnrollmentLinksApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_enrollment_link**](EnrollmentLinksApi.md#create_enrollment_link) | **POST** /enrollment-links | Create enrollment link
[**create_team_link**](EnrollmentLinksApi.md#create_team_link) | **POST** /subaccounts/{subaccountId}/team-link | Create team link
[**get_enrollment_link**](EnrollmentLinksApi.md#get_enrollment_link) | **GET** /enrollment-links/{linkId} | Retrieve enrollment link
[**list_enrollment_links**](EnrollmentLinksApi.md#list_enrollment_links) | **GET** /enrollment-links | List enrollment links
[**revoke_enrollment_link**](EnrollmentLinksApi.md#revoke_enrollment_link) | **POST** /enrollment-links/{linkId}/revoke | Revoke enrollment link


# **create_enrollment_link**
> EnrollmentLinkCreateResult create_enrollment_link(enrollment_link_create_params)

Create enrollment link

Creates an enrollment link for one of your subaccounts. The link opens a page on
Astrada's SDK host where the person who has it enrolls their own cards into that
subaccount.

- A personal link (`kind: cardholder`) is for one employee. It allows up to 5 session
  starts and is used up by the first session that completes something.
- A team link (`kind: team`) is for sharing. Each session start counts as a use, up to
  `maxUses`.

The response's `url` carries the link's secret after `#`. This response is the only
one that returns it, and it is sent with `Cache-Control: no-store`. Astrada stores only
a hash of the secret. In sandbox the `url` starts with
`https://sdk.sandbox.astrada.co/unified/v2/enroll.html#`.

Requires `subaccounts:write`.

Refusals carry a `code`:

- `404` `SUBACCOUNT_NOT_FOUND`: `subaccountId` is not one of your subaccounts.
- `409` `ENROLLMENT_LINKS_NOT_ENABLED`: enrollment links are not enabled for your
  account.
- `409` `CARD_ENROLLMENT_OFF`: card enrollment is off for the subaccount (its
  `enrollmentPolicy.cardEnrollment` is `false`). The hosted page offers card enrollment
  only, so a link would have nothing to enroll. This check runs before the daily limit
  is counted, so a refused request does not use it up.
- `400` `LINK_NAME_NOT_ALLOWED`: `organizationName` or `platformName` is a
  well-known brand name, such as a card network or a large bank, matched ignoring case,
  accents and punctuation. Astrada and Plaid are also refused inside a longer name.
- `429` `RATE_LIMITED`: your account has created 2,000 links today (UTC), team links
  made with `POST /subaccounts/{subaccountId}/team-link` included.

A link made before card enrollment was turned off starts no session while card
enrollment stays off: `POST /enrollment-link-sessions/preview` and
`POST /enrollment-link-sessions` answer `409` `CARD_ENROLLMENT_OFF`, and no start is
counted.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.enrollment_link_create_params import EnrollmentLinkCreateParams
from astrada.models.enrollment_link_create_result import EnrollmentLinkCreateResult

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
enrollment_link_create_params = (  # EnrollmentLinkCreateParams
    {'subaccountId': '6f1c2a3b-4d5e-4f60-8a7b-9c0d1e2f3a4b',
     'kind': 'cardholder',
     'customerReferenceId': '2b7e9d14-5c3a-4f8e-9b21-0d6c4a8e7f35',
     'platformName': 'Ledgerly',
     'organizationName': 'Vertex Industries'}
)

result = client.enrollment_links.create_enrollment_link(enrollment_link_create_params)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_link_create_params** | [**EnrollmentLinkCreateParams**](EnrollmentLinkCreateParams.md)|  | 

### Return type

[**EnrollmentLinkCreateResult**](EnrollmentLinkCreateResult.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The link, with its &#x60;url&#x60;. |  -  |
**400** | The body failed validation, and &#x60;errors&#x60; names the field. Or &#x60;organizationName&#x60; or &#x60;platformName&#x60; is a well-known brand name, with &#x60;code&#x60; &#x60;LINK_NAME_NOT_ALLOWED&#x60;.  |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token holds none of the scopes the route accepts, or it is an enrollment link session&#39;s token, which no scope lets manage links. A missing scope answers without a &#x60;code&#x60;. A link session token that holds an accepted scope answers with &#x60;code&#x60; &#x60;LINK_SESSION_FORBIDDEN&#x60;.  |  -  |
**404** | The subaccount is not one of your account&#39;s subaccounts. Nothing is created.  |  -  |
**409** | The link was not created, and nothing is stored. &#x60;code&#x60; says why:  - &#x60;ENROLLMENT_LINKS_NOT_ENABLED&#x60;: enrollment links are not enabled for the account.   Astrada enables them per account. - &#x60;CARD_ENROLLMENT_OFF&#x60;: card enrollment is off for the subaccount (its   &#x60;enrollmentPolicy.cardEnrollment&#x60; is &#x60;false&#x60;). The hosted page offers card enrollment   only, so a link would have nothing to enroll.  |  -  |
**429** | A rate limit was reached. The operation&#39;s description names its limits. Retry later.  |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team_link**
> TeamLink create_team_link(subaccount_id)

Create team link

Creates a team link for the subaccount: the route for the SDK's "Invite your team"
ending, which calls it with the SDK token's `card-subscriptions:write`. An API client
may call it with `subaccounts:write`. No body.

`_links.team-link` on `GET /subaccounts/{subaccountId}` points here when the route is
available to the caller.

The link has the team defaults: it expires after 14 days and allows 50 session starts.
The response holds only what the SDK screen shows, and is sent with
`Cache-Control: no-store`. Every call makes a new link. A new link does not revoke an
older one: each link ends at its own expiry, when its session starts are used up, or
when it is revoked. Revoke a link you no longer want shared with
`POST /enrollment-links/{linkId}/revoke`.

Refusals carry a `code`:

- `403` `LINK_SESSION_FORBIDDEN`: the token is an enrollment link session's. It holds
  `card-subscriptions:write` too, but cannot make links.
- `404` `SUBACCOUNT_NOT_FOUND`: the subaccount is not one of your account's.
- `409` `ENROLLMENT_LINKS_NOT_ENABLED`: enrollment links are not enabled for your
  account.
- `409` `CARD_ENROLLMENT_OFF`: card enrollment is off for the subaccount (its
  `enrollmentPolicy.cardEnrollment` is `false`). The hosted page offers card enrollment
  only, so a link would have nothing to enroll. This check runs before the daily limits
  are counted, so a refused request does not use them up.
- `429` `RATE_LIMITED`: 20 links were made here for the subaccount today (UTC), or your
  account has created 2,000 links today.

A link made before card enrollment was turned off starts no session while card
enrollment stays off: `POST /enrollment-link-sessions/preview` and
`POST /enrollment-link-sessions` answer `409` `CARD_ENROLLMENT_OFF`, and no start is
counted.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.team_link import TeamLink

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c'  # str

result = client.enrollment_links.create_team_link(subaccount_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**|  | 

### Return type

[**TeamLink**](TeamLink.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The team link. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token holds none of the scopes the route accepts, or it is an enrollment link session&#39;s token, which no scope lets manage links. A missing scope answers without a &#x60;code&#x60;. A link session token that holds an accepted scope answers with &#x60;code&#x60; &#x60;LINK_SESSION_FORBIDDEN&#x60;.  |  -  |
**404** | The subaccount is not one of your account&#39;s subaccounts. Nothing is created.  |  -  |
**409** | The link was not created, and nothing is stored. &#x60;code&#x60; says why:  - &#x60;ENROLLMENT_LINKS_NOT_ENABLED&#x60;: enrollment links are not enabled for the account.   Astrada enables them per account. - &#x60;CARD_ENROLLMENT_OFF&#x60;: card enrollment is off for the subaccount (its   &#x60;enrollmentPolicy.cardEnrollment&#x60; is &#x60;false&#x60;). The hosted page offers card enrollment   only, so a link would have nothing to enroll.  |  -  |
**429** | A rate limit was reached. The operation&#39;s description names its limits. Retry later.  |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_link**
> EnrollmentLinkDetail get_enrollment_link(link_id)

Retrieve enrollment link

Returns one of your enrollment links with its sessions, oldest first, without its
`url`. With the `cardsubscription` webhooks, this is how you see what happened on the
hosted page.

Each session's `outcome` holds the ids the hosted page reported. Nothing checks them
against the card or bank APIs: the `cardsubscription` webhooks are the source of truth
for what was enrolled.

Requires `subaccounts:write`. A link that is not one of yours answers `404` with
`code` `ENROLLMENT_LINK_NOT_FOUND`. A link and its sessions are kept for 90 days after
`expiresAt`, then answer `404`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.enrollment_link_detail import EnrollmentLinkDetail

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
link_id = '1d0a6c52-8f3e-4b7a-9c21-5e4d3b2a1f09'  # str

result = client.enrollment_links.get_enrollment_link(link_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**| The enrollment link&#39;s identifier, the &#x60;id&#x60; returned when the link was created. | 

### Return type

[**EnrollmentLinkDetail**](EnrollmentLinkDetail.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The link and its sessions. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token holds none of the scopes the route accepts, or it is an enrollment link session&#39;s token, which no scope lets manage links. A missing scope answers without a &#x60;code&#x60;. A link session token that holds an accepted scope answers with &#x60;code&#x60; &#x60;LINK_SESSION_FORBIDDEN&#x60;.  |  -  |
**404** | No link with this id belongs to your account. Another account&#39;s link answers the same.  |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_enrollment_links**
> EnrollmentLinkList list_enrollment_links(subaccount_id, state=state, limit=limit, cursor=cursor)

List enrollment links

Lists the enrollment links of one of your subaccounts, newest first, without their
`url`.

A page holds at most `limit` links and can hold fewer, even none, while more remain.
Keep following `_links.next` until a response has no `_links.next`. Use its `href` as
it is: it keeps your `subaccountId`, `state` and `limit`.

A subaccount that has no links, or that is not one of yours, gives an empty list.

Requires `subaccounts:write`, so link details such as references and counts never
reach a browser SDK token.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.enrollment_link_list import EnrollmentLinkList

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
subaccount_id = '6f1c2a3b-4d5e-4f60-8a7b-9c0d1e2f3a4b'  # str
state = 'active'  # str (optional)
limit = 50  # int (optional)
cursor = 'standin'  # str (optional)

result = client.enrollment_links.list_enrollment_links(subaccount_id, state=state, limit=limit, cursor=cursor)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subaccount_id** | **str**| The subaccount whose links to list. | 
 **state** | **str**| Only links in this state. &#x60;active&#x60; and &#x60;expired&#x60; are told apart by &#x60;expiresAt&#x60;. | [optional] 
 **limit** | **int**| The most links a page holds. | [optional] [default to 50]
 **cursor** | **str**| Where the page starts, as set in &#x60;_links.next&#x60;. A cursor from another subaccount&#39;s listing, or one that does not decode, answers &#x60;400&#x60; &#x60;INVALID_CURSOR&#x60;.  | [optional] 

### Return type

[**EnrollmentLinkList**](EnrollmentLinkList.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of links. |  -  |
**400** | A query parameter is not valid, and &#x60;errors&#x60; names it. Or the cursor is not one this listing gave out, with &#x60;code&#x60; &#x60;INVALID_CURSOR&#x60;.  |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token holds none of the scopes the route accepts, or it is an enrollment link session&#39;s token, which no scope lets manage links. A missing scope answers without a &#x60;code&#x60;. A link session token that holds an accepted scope answers with &#x60;code&#x60; &#x60;LINK_SESSION_FORBIDDEN&#x60;.  |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_enrollment_link**
> EnrollmentLink revoke_enrollment_link(link_id)

Revoke enrollment link

Revokes one of your enrollment links. No body. An active link, an expired one
included, becomes `revoked`: no session starts from it again, and its open sessions
fail their next token refresh, so their access ends within one access token lifetime
(at most 300 seconds). A link that is already used or revoked is returned as it is.

Requires `subaccounts:write`. A link that is not one of yours answers `404` with
`code` `ENROLLMENT_LINK_NOT_FOUND`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.enrollment_link import EnrollmentLink

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
link_id = '1d0a6c52-8f3e-4b7a-9c21-5e4d3b2a1f09'  # str

result = client.enrollment_links.revoke_enrollment_link(link_id)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **str**| The enrollment link&#39;s identifier, the &#x60;id&#x60; returned when the link was created. | 

### Return type

[**EnrollmentLink**](EnrollmentLink.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The link as it is now. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | The token holds none of the scopes the route accepts, or it is an enrollment link session&#39;s token, which no scope lets manage links. A missing scope answers without a &#x60;code&#x60;. A link session token that holds an accepted scope answers with &#x60;code&#x60; &#x60;LINK_SESSION_FORBIDDEN&#x60;.  |  -  |
**404** | No link with this id belongs to your account. Another account&#39;s link answers the same.  |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

