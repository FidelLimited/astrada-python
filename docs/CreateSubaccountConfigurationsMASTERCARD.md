# CreateSubaccountConfigurationsMASTERCARD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**MastercardCountriesOrWildcard**](MastercardCountriesOrWildcard.md) |  | 
**single_enrollment** | [**CreateSubaccountConfigurationsMASTERCARDSingleEnrollment**](CreateSubaccountConfigurationsMASTERCARDSingleEnrollment.md) |  | [optional] 
**bulk_enrollment** | [**CreateSubaccountConfigurationsMASTERCARDBulkEnrollment**](CreateSubaccountConfigurationsMASTERCARDBulkEnrollment.md) |  | [optional] 

## Example

```python
from astrada.models.create_subaccount_configurations_mastercard import CreateSubaccountConfigurationsMASTERCARD

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubaccountConfigurationsMASTERCARD from a JSON string
create_subaccount_configurations_mastercard_instance = CreateSubaccountConfigurationsMASTERCARD.from_json(json)
# print the JSON string representation of the object
print(CreateSubaccountConfigurationsMASTERCARD.to_json())

# convert the object into a dict
create_subaccount_configurations_mastercard_dict = create_subaccount_configurations_mastercard_instance.to_dict()
# create an instance of CreateSubaccountConfigurationsMASTERCARD from a dict
create_subaccount_configurations_mastercard_from_dict = CreateSubaccountConfigurationsMASTERCARD.from_dict(create_subaccount_configurations_mastercard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


