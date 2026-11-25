# CreateSubaccountConfigurationsMASTERCARDSingleEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_card_types** | **List[str]** | Card types blocked for Mastercard single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | [optional] 
**blocked_funding_card_types** | **List[str]** | Funding card types blocked for Mastercard single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | [optional] 

## Example

```python
from astrada.models.create_subaccount_configurations_mastercard_single_enrollment import CreateSubaccountConfigurationsMASTERCARDSingleEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubaccountConfigurationsMASTERCARDSingleEnrollment from a JSON string
create_subaccount_configurations_mastercard_single_enrollment_instance = CreateSubaccountConfigurationsMASTERCARDSingleEnrollment.from_json(json)
# print the JSON string representation of the object
print(CreateSubaccountConfigurationsMASTERCARDSingleEnrollment.to_json())

# convert the object into a dict
create_subaccount_configurations_mastercard_single_enrollment_dict = create_subaccount_configurations_mastercard_single_enrollment_instance.to_dict()
# create an instance of CreateSubaccountConfigurationsMASTERCARDSingleEnrollment from a dict
create_subaccount_configurations_mastercard_single_enrollment_from_dict = CreateSubaccountConfigurationsMASTERCARDSingleEnrollment.from_dict(create_subaccount_configurations_mastercard_single_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


