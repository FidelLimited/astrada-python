# SimulateTransactionScenarioAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[SimulateTransactionScenarioTransaction]**](SimulateTransactionScenarioTransaction.md) | The transactions created by the scenario. Each entry lists the ids of the transaction messages published for that transaction; use &#x60;GET /transaction-messages/{transactionMessageId}&#x60; to retrieve each message once it has been processed.  | 

## Example

```python
from astrada.sandbox.models.simulate_transaction_scenario_accepted import SimulateTransactionScenarioAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionScenarioAccepted from a JSON string
simulate_transaction_scenario_accepted_instance = SimulateTransactionScenarioAccepted.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionScenarioAccepted.to_json())

# convert the object into a dict
simulate_transaction_scenario_accepted_dict = simulate_transaction_scenario_accepted_instance.to_dict()
# create an instance of SimulateTransactionScenarioAccepted from a dict
simulate_transaction_scenario_accepted_from_dict = SimulateTransactionScenarioAccepted.from_dict(simulate_transaction_scenario_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


