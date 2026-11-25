# SimulateTransactionScenarioTransaction

One transaction the scenario created, with the ids of its published messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_ids** | **List[str]** |  | 

## Example

```python
from astrada.sandbox.models.simulate_transaction_scenario_transaction import SimulateTransactionScenarioTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionScenarioTransaction from a JSON string
simulate_transaction_scenario_transaction_instance = SimulateTransactionScenarioTransaction.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionScenarioTransaction.to_json())

# convert the object into a dict
simulate_transaction_scenario_transaction_dict = simulate_transaction_scenario_transaction_instance.to_dict()
# create an instance of SimulateTransactionScenarioTransaction from a dict
simulate_transaction_scenario_transaction_from_dict = SimulateTransactionScenarioTransaction.from_dict(simulate_transaction_scenario_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


