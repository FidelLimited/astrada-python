# SimulateTransactionAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | The id of the transaction message that was published. Once it has been processed, use &#x60;GET /transaction-messages/{transactionMessageId}&#x60; to retrieve it, or &#x60;GET /transactions?transactionMessageId&#x3D;&#x60; to find the transaction it created or updated.  | 

## Example

```python
from astrada.sandbox.models.simulate_transaction_accepted import SimulateTransactionAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionAccepted from a JSON string
simulate_transaction_accepted_instance = SimulateTransactionAccepted.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionAccepted.to_json())

# convert the object into a dict
simulate_transaction_accepted_dict = simulate_transaction_accepted_instance.to_dict()
# create an instance of SimulateTransactionAccepted from a dict
simulate_transaction_accepted_from_dict = SimulateTransactionAccepted.from_dict(simulate_transaction_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


