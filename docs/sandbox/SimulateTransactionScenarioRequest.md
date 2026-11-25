# SimulateTransactionScenarioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario** | **str** | The predefined scenario to simulate. | 
**card_id** | **str** | The identifier of the enrolled card to transact against. | 
**subaccount_id** | **str** | The subaccount identifier the card belongs to. | 
**amount** | **int** | Optional transaction amount in minor units (cents). When omitted, the scenario&#39;s default amount is used.  | [optional] 
**currency** | **str** | Optional ISO 4217 three-letter currency code, case insensitive. A code that is not a currency transactions can be made in is rejected with &#x60;400&#x60;. When omitted, the scenario&#39;s default currency is used.  | [optional] 
**network** | **str** | Optional card network override, so one scenario can be run against any network. When omitted, the scenario&#39;s own default network is used.  | [optional] 
**source** | **str** | Optional ingestion-source tag applied to every message the scenario emits, so simulated activity can be attributed to a given network feed. When omitted, defaults to the scenario&#39;s own source if it sets one (the &#x60;amex_auth_*&#x60; scenarios default to &#x60;amexrta&#x60;), else &#x60;tns&#x60;, or &#x60;amexgl&#x60; when the resolved network is AMEX.  | [optional] 

## Example

```python
from astrada.sandbox.models.simulate_transaction_scenario_request import SimulateTransactionScenarioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionScenarioRequest from a JSON string
simulate_transaction_scenario_request_instance = SimulateTransactionScenarioRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionScenarioRequest.to_json())

# convert the object into a dict
simulate_transaction_scenario_request_dict = simulate_transaction_scenario_request_instance.to_dict()
# create an instance of SimulateTransactionScenarioRequest from a dict
simulate_transaction_scenario_request_from_dict = SimulateTransactionScenarioRequest.from_dict(simulate_transaction_scenario_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


