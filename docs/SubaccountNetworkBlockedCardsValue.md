# SubaccountNetworkBlockedCardsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**single_enrollment** | [**List[NetworkBlockedCardRule]**](NetworkBlockedCardRule.md) | Rules applied to single (SDK or API) enrollment on this network. | [optional] 
**bulk_enrollment** | [**List[NetworkBlockedCardRule]**](NetworkBlockedCardRule.md) | Rules applied to bulk enrollment on this network. | [optional] 

## Example

```python
from astrada.models.subaccount_network_blocked_cards_value import SubaccountNetworkBlockedCardsValue

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountNetworkBlockedCardsValue from a JSON string
subaccount_network_blocked_cards_value_instance = SubaccountNetworkBlockedCardsValue.from_json(json)
# print the JSON string representation of the object
print(SubaccountNetworkBlockedCardsValue.to_json())

# convert the object into a dict
subaccount_network_blocked_cards_value_dict = subaccount_network_blocked_cards_value_instance.to_dict()
# create an instance of SubaccountNetworkBlockedCardsValue from a dict
subaccount_network_blocked_cards_value_from_dict = SubaccountNetworkBlockedCardsValue.from_dict(subaccount_network_blocked_cards_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


