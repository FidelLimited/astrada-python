# astrada.sandbox.SandboxSimulationApi

All URIs are relative to *https://api.sandbox.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simulate_bulk_feed_file_gl**](SandboxSimulationApi.md#simulate_bulk_feed_file_gl) | **POST** /simulate/ingestion/amex-gl | Simulate an American Express bulk file (sandbox only)
[**simulate_bulk_feed_file_smartdata**](SandboxSimulationApi.md#simulate_bulk_feed_file_smartdata) | **POST** /simulate/ingestion/smartdata | Simulate a Mastercard bulk file (sandbox only)
[**simulate_bulk_feed_file_vbds**](SandboxSimulationApi.md#simulate_bulk_feed_file_vbds) | **POST** /simulate/ingestion/vbds | Simulate a pulled Visa bulk feed delivery (sandbox only)
[**simulate_bulk_feed_file_vcf**](SandboxSimulationApi.md#simulate_bulk_feed_file_vcf) | **POST** /simulate/ingestion/vcf | Simulate a Visa bulk file (sandbox only)
[**simulate_transaction**](SandboxSimulationApi.md#simulate_transaction) | **POST** /simulate/transactions | Simulate a transaction (sandbox only)
[**simulate_transaction_message**](SandboxSimulationApi.md#simulate_transaction_message) | **POST** /simulate/transactions/{transactionId} | Simulate a transaction message (sandbox only)
[**simulate_transaction_scenario**](SandboxSimulationApi.md#simulate_transaction_scenario) | **POST** /simulate/transaction/scenario | Simulate a transaction scenario (sandbox only)


# **simulate_bulk_feed_file_gl**
> simulate_bulk_feed_file_gl(simulate_bulk_feed_file_gl_request)

Simulate an American Express bulk file (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Creates a simulated American Express bulk-enrollment file, plus a
companion settlement file when `transactionsPerCard` is above `0`, and
processes it as if American Express had delivered it. The call returns
`202 Accepted` at once; enrolled cards appear as card subscriptions when
processing finishes, and their settlements follow shortly after.

A bulk feed must already exist for the `networkReference`, created with
`POST /network-bulk-feeds`.

`cardCount` replays the fixed head of the sandbox account pool (encrypted
feeds; for tokenized feeds see below): the same accounts every call, so once
enrolled in a subaccount they deduplicate (no new
`cardsubscription.created`), exactly like a file that is delivered twice.
`newCardCount` draws accounts the subaccount has never seen from a
reserved pool, so every call enrolls that many new cards. All included
cards get `transactionsPerCard` transactions with fresh ids and recent
dates, so repeat calls always produce `transaction.*` webhooks.

For a feed registered `tokenized` (see `panFormat` on
`POST /network-bulk-feeds`), `cardCount` draws American Express network
tokens instead of raw card numbers, and `newCardCount` is not supported
(there is no tokenized new-card pool).


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_bulk_feed_file_gl_request import SimulateBulkFeedFileGlRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
simulate_bulk_feed_file_gl_request = {'networkReference': 'R12345', 'cardCount': 5}  # SimulateBulkFeedFileGlRequest

client.sandbox.simulate_bulk_feed_file_gl(simulate_bulk_feed_file_gl_request)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_bulk_feed_file_gl_request** | [**SimulateBulkFeedFileGlRequest**](SimulateBulkFeedFileGlRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The simulated file was created and is processed asynchronously. The response has no body.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**413** | Content Too Large |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_bulk_feed_file_smartdata**
> simulate_bulk_feed_file_smartdata(simulate_bulk_feed_file_smartdata_request)

Simulate a Mastercard bulk file (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Creates a simulated Mastercard bulk-enrollment file and processes it as if
Mastercard had delivered it. The call returns `202 Accepted` at once;
enrolled cards appear as card subscriptions when processing finishes.

A bulk feed must already exist for the `networkReference`, created with
`POST /network-bulk-feeds`.

`cardCount` replays the fixed head of the sandbox test-card pool: the same
cards every call, so once enrolled in a subaccount they deduplicate (no new
`cardsubscription.created`), exactly like a file that is delivered twice.
`newCardCount` draws cards the subaccount has never seen from a reserved
pool, so every call enrolls that many new cards. All included cards get
`transactionsPerCard` transactions with fresh references and recent dates,
so repeat calls always produce `transaction.*` webhooks.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_bulk_feed_file_smartdata_request import SimulateBulkFeedFileSmartdataRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
simulate_bulk_feed_file_smartdata_request = {'networkReference': 'G1234567', 'cardCount': 5}  # SimulateBulkFeedFileSmartdataRequest

client.sandbox.simulate_bulk_feed_file_smartdata(simulate_bulk_feed_file_smartdata_request)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_bulk_feed_file_smartdata_request** | [**SimulateBulkFeedFileSmartdataRequest**](SimulateBulkFeedFileSmartdataRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The simulated file was created and is processed asynchronously. The response has no body.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**413** | Content Too Large |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_bulk_feed_file_vbds**
> simulate_bulk_feed_file_vbds(simulate_bulk_feed_file_vbds_request)

Simulate a pulled Visa bulk feed delivery (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Simulates one delivery on a Visa bulk feed of `type: VBDS`, the kind
Astrada pulls from Visa instead of receiving a file. The delivery enrolls
cards and, when `transactionsPerCard` is above `0`, adds settlements for
them. The call returns `202 Accepted` at once; enrolled cards appear as
card subscriptions when processing finishes.

A bulk feed must already exist for the `networkReference`, created with
`POST /network-bulk-feeds`; otherwise the call returns `400`.

`cardCount` replays the fixed head of the sandbox card pool: the same
cards every call, so once enrolled in a subaccount they deduplicate (no
new `cardsubscription.created`), exactly like a delivery that arrives
twice. `newCardCount` draws cards the subaccount has never seen from a
reserved pool, so every call enrolls that many new cards. All included
cards get `transactionsPerCard` transactions with fresh ids and recent
dates, so repeat calls always produce `transaction.*` webhooks.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_bulk_feed_file_vbds_request import SimulateBulkFeedFileVbdsRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
simulate_bulk_feed_file_vbds_request = {'networkReference': '1_12345_67890_54321', 'cardCount': 5}  # SimulateBulkFeedFileVbdsRequest

client.sandbox.simulate_bulk_feed_file_vbds(simulate_bulk_feed_file_vbds_request)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_bulk_feed_file_vbds_request** | [**SimulateBulkFeedFileVbdsRequest**](SimulateBulkFeedFileVbdsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The simulated delivery was queued and is processed asynchronously. The response has no body.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**413** | Content Too Large |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_bulk_feed_file_vcf**
> simulate_bulk_feed_file_vcf(simulate_bulk_feed_file_vcf_request)

Simulate a Visa bulk file (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Creates a simulated Visa bulk-enrollment file (a feed of `type: VCF`) and
processes it as if Visa had delivered it. The call returns
`202 Accepted` at once; enrolled cards appear as card subscriptions when
processing finishes.

A bulk feed must already exist for the `networkReference`, created with
`POST /network-bulk-feeds`.

`cardCount` replays the fixed head of the sandbox test-card pool: the same
cards every call, so once enrolled in a subaccount they deduplicate (no new
`cardsubscription.created`), exactly like a file that is delivered twice.
`newCardCount` draws cards the subaccount has never seen from a reserved
pool, so every call enrolls that many new cards. All included cards get
`transactionsPerCard` transactions with fresh references and recent dates,
so repeat calls always produce `transaction.*` webhooks.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_bulk_feed_file_vcf_request import SimulateBulkFeedFileVcfRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
simulate_bulk_feed_file_vcf_request = {'networkReference': '1_123_45_6789', 'cardCount': 5}  # SimulateBulkFeedFileVcfRequest

client.sandbox.simulate_bulk_feed_file_vcf(simulate_bulk_feed_file_vcf_request)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_bulk_feed_file_vcf_request** | [**SimulateBulkFeedFileVcfRequest**](SimulateBulkFeedFileVcfRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The simulated file was created and is processed asynchronously. The response has no body.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**413** | Content Too Large |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_transaction**
> SimulateTransactionAccepted simulate_transaction(simulate_transaction_request)

Simulate a transaction (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Starts a new simulated transaction on an enrolled card by publishing one
transaction message, an authorization or a settlement, as if a card
network had sent it. Follow it with
`POST /simulate/transactions/{transactionId}` to add further messages to
the transaction.

Besides `simulation:write`, the access token needs `cards:read`: the card
is read from the public API to resolve its subaccount and network.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_transaction_accepted import SimulateTransactionAccepted
from astrada.sandbox.models.simulate_transaction_request import SimulateTransactionRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
simulate_transaction_request = {'cardId': '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c', 'type': 'authorization', 'amount': 4500}  # SimulateTransactionRequest

result = client.sandbox.simulate_transaction(simulate_transaction_request)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_transaction_request** | [**SimulateTransactionRequest**](SimulateTransactionRequest.md)|  | 

### Return type

[**SimulateTransactionAccepted**](SimulateTransactionAccepted.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The transaction message was published and is processed asynchronously. The transaction it creates is delivered through the &#x60;transaction.created&#x60; webhook and can be found with &#x60;GET /transactions?transactionMessageId&#x3D;&#x60;.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**502** | The card could not be read from the sandbox API. Retry the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_transaction_message**
> SimulateTransactionAccepted simulate_transaction_message(transaction_id, simulate_transaction_message_request)

Simulate a transaction message (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Publishes one more transaction message (authorization, adjustment,
reversal, settlement or refund) on an existing sandbox transaction. The
transaction can have been created by `POST /simulate/transactions` or by
the scenario endpoint; take its id from the `transaction.created` webhook
or from `GET /transactions?transactionMessageId=`.

Besides `simulation:write`, the access token needs `transactions:read`
and `transaction-messages:read`: the transaction and its messages are read
from the public API to carry over the network reference and the current
hold and settled amounts.

`adjustment` and `reversal` are checked against the hold Astrada has
processed so far and rejected with `409` when there is nothing to adjust
or reverse. The check is best effort: a step published immediately after
another may see the earlier state.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_transaction_accepted import SimulateTransactionAccepted
from astrada.sandbox.models.simulate_transaction_message_request import SimulateTransactionMessageRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
transaction_id = '9340721f-bdce-4afa-bd9d-26cceb9d2176'  # str
simulate_transaction_message_request = {'type': 'settlement'}  # SimulateTransactionMessageRequest

result = client.sandbox.simulate_transaction_message(transaction_id, simulate_transaction_message_request)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 
 **simulate_transaction_message_request** | [**SimulateTransactionMessageRequest**](SimulateTransactionMessageRequest.md)|  | 

### Return type

[**SimulateTransactionAccepted**](SimulateTransactionAccepted.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The transaction message was published and is processed asynchronously. The updated transaction is delivered through the &#x60;transaction.updated&#x60; webhook.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**409** | Request conflict with the current state of the target resource |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |
**502** | The transaction could not be read from the sandbox API. Retry the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_transaction_scenario**
> SimulateTransactionScenarioAccepted simulate_transaction_scenario(simulate_transaction_scenario_request)

Simulate a transaction scenario (sandbox only)

Works in the sandbox only (`https://api.sandbox.astrada.co`). Production
has no such call.

Runs a predefined transaction scenario, such as a purchase followed by a
refund, on an enrolled card. The call publishes every transaction message
of the scenario as if a card network had sent them and returns `202
Accepted` with their ids. The transactions arrive asynchronously through
the `transaction.created` and `transaction.updated` webhooks.

The call does not look the card up first: well-formed ids return `202`
even when they do not name an enrolled card of your account. If no
transaction appears, check that `cardId` is enrolled in `subaccountId`.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.sandbox.models.simulate_transaction_scenario_accepted import SimulateTransactionScenarioAccepted
from astrada.sandbox.models.simulate_transaction_scenario_request import SimulateTransactionScenarioRequest

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
simulate_transaction_scenario_request = (  # SimulateTransactionScenarioRequest
    {'scenario': 'simple_purchase',
     'cardId': '24c4f90d-ab3b-4f6e-8a1d-d251a4fcf34c',
     'subaccountId': 'f297d659-c13d-4219-aeaa-e10a845140a5',
     'amount': 1500,
     'currency': 'USD'}
)

result = client.sandbox.simulate_transaction_scenario(simulate_transaction_scenario_request)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_transaction_scenario_request** | [**SimulateTransactionScenarioRequest**](SimulateTransactionScenarioRequest.md)|  | 

### Return type

[**SimulateTransactionScenarioAccepted**](SimulateTransactionScenarioAccepted.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. The transaction messages were published and are processed asynchronously.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

