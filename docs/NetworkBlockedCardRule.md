# NetworkBlockedCardRule

A platform rule that blocks enrollment of matching cards on one network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | The BIN &#x60;type&#x60; this rule blocks. | 
**funding_types** | **List[str]** | The BIN &#x60;fundingType&#x60; values this rule blocks. Omitted or empty means every funding type. | [optional] 

## Example

```python
from astrada.models.network_blocked_card_rule import NetworkBlockedCardRule

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBlockedCardRule from a JSON string
network_blocked_card_rule_instance = NetworkBlockedCardRule.from_json(json)
# print the JSON string representation of the object
print(NetworkBlockedCardRule.to_json())

# convert the object into a dict
network_blocked_card_rule_dict = network_blocked_card_rule_instance.to_dict()
# create an instance of NetworkBlockedCardRule from a dict
network_blocked_card_rule_from_dict = NetworkBlockedCardRule.from_dict(network_blocked_card_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


