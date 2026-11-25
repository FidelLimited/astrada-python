# SubaccountConfigurationVISABulkEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | List of countries supported for Visa bulk enrollment | 
**blocked_card_types** | **List[str]** | Card types blocked for Visa bulk enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | 
**blocked_funding_card_types** | **List[str]** | Funding card types blocked for Visa bulk enrollment. The account&#39;s defaults for this network and enrollment mode are always added, so the stored list can include values that were not sent. | 

## Example

```python
from astrada.models.subaccount_configuration_visa_bulk_enrollment import SubaccountConfigurationVISABulkEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountConfigurationVISABulkEnrollment from a JSON string
subaccount_configuration_visa_bulk_enrollment_instance = SubaccountConfigurationVISABulkEnrollment.from_json(json)
# print the JSON string representation of the object
print(SubaccountConfigurationVISABulkEnrollment.to_json())

# convert the object into a dict
subaccount_configuration_visa_bulk_enrollment_dict = subaccount_configuration_visa_bulk_enrollment_instance.to_dict()
# create an instance of SubaccountConfigurationVISABulkEnrollment from a dict
subaccount_configuration_visa_bulk_enrollment_from_dict = SubaccountConfigurationVISABulkEnrollment.from_dict(subaccount_configuration_visa_bulk_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


