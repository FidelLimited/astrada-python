# SubaccountConfigurationAMEXSingleEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | List of countries supported for AMEX single enrollment | 
**blocked_card_types** | **List[str]** | Card types blocked for AMEX single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | 
**blocked_funding_card_types** | **List[str]** | Funding card types blocked for AMEX single enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | 

## Example

```python
from astrada.models.subaccount_configuration_amex_single_enrollment import SubaccountConfigurationAMEXSingleEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfigurationAMEXSingleEnrollment from a JSON string
subaccount_configuration_amex_single_enrollment_instance = SubaccountConfigurationAMEXSingleEnrollment.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfigurationAMEXSingleEnrollment.to_json())

# convert the object into a dict
subaccount_configuration_amex_single_enrollment_dict = subaccount_configuration_amex_single_enrollment_instance.to_dict()
# create an instance of SubaccountConfigurationAMEXSingleEnrollment from a dict
subaccount_configuration_amex_single_enrollment_from_dict = SubaccountConfigurationAMEXSingleEnrollment.from_dict(subaccount_configuration_amex_single_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


