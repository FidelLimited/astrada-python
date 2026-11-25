# CreateSubaccountConfigurationsAMEXSingleEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_card_types** | **List[str]** | Card types blocked for AMEX single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | [optional] 
**blocked_funding_card_types** | **List[str]** | Funding card types blocked for AMEX single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | [optional] 

## Example

```python
from astrada.models.create_subaccount_configurations_amex_single_enrollment import CreateSubaccountConfigurationsAMEXSingleEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubaccountConfigurationsAMEXSingleEnrollment from a JSON string
create_subaccount_configurations_amex_single_enrollment_instance = CreateSubaccountConfigurationsAMEXSingleEnrollment.from_json(json)
# print the JSON string representation of the object
print(CreateSubaccountConfigurationsAMEXSingleEnrollment.to_json())

# convert the object into a dict
create_subaccount_configurations_amex_single_enrollment_dict = create_subaccount_configurations_amex_single_enrollment_instance.to_dict()
# create an instance of CreateSubaccountConfigurationsAMEXSingleEnrollment from a dict
create_subaccount_configurations_amex_single_enrollment_from_dict = CreateSubaccountConfigurationsAMEXSingleEnrollment.from_dict(create_subaccount_configurations_amex_single_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


