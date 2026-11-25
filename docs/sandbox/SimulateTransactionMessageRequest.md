# SimulateTransactionMessageRequest

Publishes one more transaction message on an existing sandbox transaction. The message reuses the transaction's card, network, currency, merchant and network reference, so the new message joins the same transaction. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The message to publish. &#x60;amount&#x60; is in minor units of the transaction&#39;s currency; whether it is required depends on the type: - &#x60;authorization&#x60;: an additional authorization that increases the hold.   &#x60;amount&#x60; is required. - &#x60;adjustment&#x60;: replaces the current hold with &#x60;amount&#x60; (the new total).   &#x60;amount&#x60; is required. Rejected with &#x60;409&#x60; when nothing is on hold. - &#x60;reversal&#x60;: releases &#x60;amount&#x60; from the hold. Defaults to the full   remaining hold. Rejected with &#x60;409&#x60; when nothing is on hold or when   &#x60;amount&#x60; exceeds the hold. - &#x60;settlement&#x60;: clears &#x60;amount&#x60;, moving it from the hold to the settled   amount. Defaults to the remaining hold; required when nothing is on   hold. - &#x60;refund&#x60;: negative settlement linked to this transaction. Nets into it   while it is still PENDING or on accounts that correlate refunds;   otherwise (the default for API-created accounts) a SETTLED transaction   gets a separate refund transaction with its own &#x60;transaction.created&#x60;.   Defaults to the settled amount; required when nothing has been settled.  | 
**amount** | **int** | Amount in minor units of the transaction&#39;s currency. See &#x60;type&#x60; for which types require it and what it defaults to otherwise.  | [optional] 
**date_time** | **datetime** | Timestamp of the message, ISO 8601 with a timezone offset. Must not be in the future. Defaults to one second after the transaction&#39;s latest message, or to the time of the request if that is later; when the latest message is already ahead of the clock (an end-of-day message, see below), the time of the request. Set an earlier value to backdate a message (for example an authorization that joins a settlement-first transaction).  As in production, Visa settlements and reversals and Amex settlements are published with an end-of-day &#x60;dateTime&#x60;: the UTC date of this value at &#x60;23:59:59Z&#x60;.  | [optional] 

## Example

```python
from astrada.sandbox.models.simulate_transaction_message_request import SimulateTransactionMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionMessageRequest from a JSON string
simulate_transaction_message_request_instance = SimulateTransactionMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionMessageRequest.to_json())

# convert the object into a dict
simulate_transaction_message_request_dict = simulate_transaction_message_request_instance.to_dict()
# create an instance of SimulateTransactionMessageRequest from a dict
simulate_transaction_message_request_from_dict = SimulateTransactionMessageRequest.from_dict(simulate_transaction_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


