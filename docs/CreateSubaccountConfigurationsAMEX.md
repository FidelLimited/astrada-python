# CreateSubaccountConfigurationsAMEX


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**AmexCountriesOrWildcard**](AmexCountriesOrWildcard.md) |  | 
**single_enrollment** | [**CreateSubaccountConfigurationsAMEXSingleEnrollment**](CreateSubaccountConfigurationsAMEXSingleEnrollment.md) |  | [optional] 
**bulk_enrollment** | [**CreateSubaccountConfigurationsAMEXBulkEnrollment**](CreateSubaccountConfigurationsAMEXBulkEnrollment.md) |  | [optional] 

## Example

```python
from astrada.models.create_subaccount_configurations_amex import CreateSubaccountConfigurationsAMEX

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubaccountConfigurationsAMEX from a JSON string
create_subaccount_configurations_amex_instance = CreateSubaccountConfigurationsAMEX.from_json(json)
# print the JSON string representation of the object
print(CreateSubaccountConfigurationsAMEX.to_json())

# convert the object into a dict
create_subaccount_configurations_amex_dict = create_subaccount_configurations_amex_instance.to_dict()
# create an instance of CreateSubaccountConfigurationsAMEX from a dict
create_subaccount_configurations_amex_from_dict = CreateSubaccountConfigurationsAMEX.from_dict(create_subaccount_configurations_amex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


