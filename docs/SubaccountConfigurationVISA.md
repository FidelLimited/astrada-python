# SubaccountConfigurationVISA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | List of contracted regional areas for Visa | 
**single_enrollment** | [**SubaccountConfigurationVISASingleEnrollment**](SubaccountConfigurationVISASingleEnrollment.md) |  | 
**bulk_enrollment** | [**SubaccountConfigurationVISABulkEnrollment**](SubaccountConfigurationVISABulkEnrollment.md) |  | 

## Example

```python
from astrada.models.subaccount_configuration_visa import SubaccountConfigurationVISA

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfigurationVISA from a JSON string
subaccount_configuration_visa_instance = SubaccountConfigurationVISA.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfigurationVISA.to_json())

# convert the object into a dict
subaccount_configuration_visa_dict = subaccount_configuration_visa_instance.to_dict()
# create an instance of SubaccountConfigurationVISA from a dict
subaccount_configuration_visa_from_dict = SubaccountConfigurationVISA.from_dict(subaccount_configuration_visa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


