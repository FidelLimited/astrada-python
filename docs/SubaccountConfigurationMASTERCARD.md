# SubaccountConfigurationMASTERCARD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | List of contracted regional areas for Mastercard | 
**single_enrollment** | [**SubaccountConfigurationMASTERCARDSingleEnrollment**](SubaccountConfigurationMASTERCARDSingleEnrollment.md) |  | 
**bulk_enrollment** | [**SubaccountConfigurationMASTERCARDBulkEnrollment**](SubaccountConfigurationMASTERCARDBulkEnrollment.md) |  | 

## Example

```python
from astrada.models.subaccount_configuration_mastercard import SubaccountConfigurationMASTERCARD

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfigurationMASTERCARD from a JSON string
subaccount_configuration_mastercard_instance = SubaccountConfigurationMASTERCARD.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfigurationMASTERCARD.to_json())

# convert the object into a dict
subaccount_configuration_mastercard_dict = subaccount_configuration_mastercard_instance.to_dict()
# create an instance of SubaccountConfigurationMASTERCARD from a dict
subaccount_configuration_mastercard_from_dict = SubaccountConfigurationMASTERCARD.from_dict(subaccount_configuration_mastercard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


