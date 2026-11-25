# CreateSubaccountConfigurationsVISA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**VisaCountriesOrWildcard**](VisaCountriesOrWildcard.md) |  | 
**single_enrollment** | [**CreateSubaccountConfigurationsVISASingleEnrollment**](CreateSubaccountConfigurationsVISASingleEnrollment.md) |  | [optional] 
**bulk_enrollment** | [**CreateSubaccountConfigurationsVISABulkEnrollment**](CreateSubaccountConfigurationsVISABulkEnrollment.md) |  | [optional] 

## Example

```python
from astrada.models.create_subaccount_configurations_visa import CreateSubaccountConfigurationsVISA

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubaccountConfigurationsVISA from a JSON string
create_subaccount_configurations_visa_instance = CreateSubaccountConfigurationsVISA.from_json(json)
# print the JSON string representation of the object
print(CreateSubaccountConfigurationsVISA.to_json())

# convert the object into a dict
create_subaccount_configurations_visa_dict = create_subaccount_configurations_visa_instance.to_dict()
# create an instance of CreateSubaccountConfigurationsVISA from a dict
create_subaccount_configurations_visa_from_dict = CreateSubaccountConfigurationsVISA.from_dict(create_subaccount_configurations_visa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


