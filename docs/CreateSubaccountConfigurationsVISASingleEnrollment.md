# CreateSubaccountConfigurationsVISASingleEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_card_types** | **List[str]** | Card types blocked for Visa single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | [optional] 
**blocked_funding_card_types** | **List[str]** | Funding card types blocked for Visa single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | [optional] 

## Example

```python
from astrada.models.create_subaccount_configurations_visa_single_enrollment import CreateSubaccountConfigurationsVISASingleEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubaccountConfigurationsVISASingleEnrollment from a JSON string
create_subaccount_configurations_visa_single_enrollment_instance = CreateSubaccountConfigurationsVISASingleEnrollment.from_json(json)
# print the JSON string representation of the object
print(CreateSubaccountConfigurationsVISASingleEnrollment.to_json())

# convert the object into a dict
create_subaccount_configurations_visa_single_enrollment_dict = create_subaccount_configurations_visa_single_enrollment_instance.to_dict()
# create an instance of CreateSubaccountConfigurationsVISASingleEnrollment from a dict
create_subaccount_configurations_visa_single_enrollment_from_dict = CreateSubaccountConfigurationsVISASingleEnrollment.from_dict(create_subaccount_configurations_visa_single_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


