# SimulateTransactionRequest

Starts a new simulated transaction on an enrolled sandbox card by publishing a single transaction message. Every field other than `cardId` and `type` is optional and falls back to a default. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | The identifier of the enrolled card to transact against. The card must belong to the account of the access token; the subaccount and, unless &#x60;network&#x60; is given, the network are read from the card.  | 
**type** | **str** | The first message of the new transaction. - &#x60;authorization&#x60;: publishes an authorization request, creating a   &#x60;PENDING&#x60; transaction with &#x60;amount&#x60; on hold. - &#x60;settlement&#x60;: publishes a clearing with no prior authorization,   creating a &#x60;SETTLED&#x60; transaction with &#x60;amount&#x60; settled and nothing on   hold. A later &#x60;authorization&#x60; step on the transaction joins it.  | 
**amount** | **int** | Transaction amount in minor units of &#x60;currency&#x60; (for example &#x60;4500&#x60; for 45.00 USD). Defaults to &#x60;4500&#x60;.  | [optional] 
**currency** | **str** | ISO 4217 three-letter currency code of the transaction, case insensitive. Must be a currency transactions can be made in; fund codes and precious metals are rejected with &#x60;400&#x60;. Defaults to &#x60;USD&#x60;.  | [optional] 
**network** | **str** | Card network the message is published on. Defaults to the card&#39;s own network; the request is rejected with &#x60;400&#x60; when this field is omitted and the card has no network or one outside this list.  | [optional] 
**merchant** | [**SimulateTransactionRequestMerchant**](SimulateTransactionRequestMerchant.md) |  | [optional] 
**date_time** | **datetime** | Timestamp of the message, ISO 8601 with a timezone offset. Must not be in the future. Defaults to the time of the request.  | [optional] 

## Example

```python
from astrada.sandbox.models.simulate_transaction_request import SimulateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionRequest from a JSON string
simulate_transaction_request_instance = SimulateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionRequest.to_json())

# convert the object into a dict
simulate_transaction_request_dict = simulate_transaction_request_instance.to_dict()
# create an instance of SimulateTransactionRequest from a dict
simulate_transaction_request_from_dict = SimulateTransactionRequest.from_dict(simulate_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


