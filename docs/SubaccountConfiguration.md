# SubaccountConfiguration

Subaccount network and regional configurations which determine the available networks and geographies during card enrollment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visa** | [**SubaccountConfigurationVISA**](SubaccountConfigurationVISA.md) |  | [optional] 
**mastercard** | [**SubaccountConfigurationMASTERCARD**](SubaccountConfigurationMASTERCARD.md) |  | [optional] 
**amex** | [**SubaccountConfigurationAMEX**](SubaccountConfigurationAMEX.md) |  | [optional] 

## Example

```python
from astrada.models.subaccount_configuration import SubaccountConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfiguration from a JSON string
subaccount_configuration_instance = SubaccountConfiguration.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfiguration.to_json())

# convert the object into a dict
subaccount_configuration_dict = subaccount_configuration_instance.to_dict()
# create an instance of SubaccountConfiguration from a dict
subaccount_configuration_from_dict = SubaccountConfiguration.from_dict(subaccount_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


