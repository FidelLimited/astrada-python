# SubaccountConfigurationAMEX


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | List of contracted regional areas for American Express | 
**single_enrollment** | [**SubaccountConfigurationAMEXSingleEnrollment**](SubaccountConfigurationAMEXSingleEnrollment.md) |  | 
**bulk_enrollment** | [**SubaccountConfigurationAMEXBulkEnrollment**](SubaccountConfigurationAMEXBulkEnrollment.md) |  | 

## Example

```python
from astrada.models.subaccount_configuration_amex import SubaccountConfigurationAMEX

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfigurationAMEX from a JSON string
subaccount_configuration_amex_instance = SubaccountConfigurationAMEX.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfigurationAMEX.to_json())

# convert the object into a dict
subaccount_configuration_amex_dict = subaccount_configuration_amex_instance.to_dict()
# create an instance of SubaccountConfigurationAMEX from a dict
subaccount_configuration_amex_from_dict = SubaccountConfigurationAMEX.from_dict(subaccount_configuration_amex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


