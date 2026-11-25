# SubaccountConfigurationVISASingleEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | List of countries supported for Visa single enrollment | 
**blocked_card_types** | **List[str]** | Card types blocked for Visa single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | 
**blocked_funding_card_types** | **List[str]** | Funding card types blocked for Visa single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | 

## Example

```python
from astrada.models.subaccount_configuration_visa_single_enrollment import SubaccountConfigurationVISASingleEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfigurationVISASingleEnrollment from a JSON string
subaccount_configuration_visa_single_enrollment_instance = SubaccountConfigurationVISASingleEnrollment.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfigurationVISASingleEnrollment.to_json())

# convert the object into a dict
subaccount_configuration_visa_single_enrollment_dict = subaccount_configuration_visa_single_enrollment_instance.to_dict()
# create an instance of SubaccountConfigurationVISASingleEnrollment from a dict
subaccount_configuration_visa_single_enrollment_from_dict = SubaccountConfigurationVISASingleEnrollment.from_dict(subaccount_configuration_visa_single_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


