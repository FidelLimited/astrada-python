# NetworkBulkEnrollmentCreateParamsConsent

The card admin's approval for the company and Astrada to start bulk enrollment with the bank, including contacting the bank on the company's behalf.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Must be &#x60;true&#x60;. The request is rejected with a 400 otherwise. | 
**version** | **str** | Your own id for the consent wording that was accepted, for example &#x60;kickoff-consent-v2&#x60;. Stored as an opaque string. | 

## Example

```python
from astrada.models.network_bulk_enrollment_create_params_consent import NetworkBulkEnrollmentCreateParamsConsent

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentCreateParamsConsent from a JSON string
network_bulk_enrollment_create_params_consent_instance = NetworkBulkEnrollmentCreateParamsConsent.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentCreateParamsConsent.to_json())

# convert the object into a dict
network_bulk_enrollment_create_params_consent_dict = network_bulk_enrollment_create_params_consent_instance.to_dict()
# create an instance of NetworkBulkEnrollmentCreateParamsConsent from a dict
network_bulk_enrollment_create_params_consent_from_dict = NetworkBulkEnrollmentCreateParamsConsent.from_dict(network_bulk_enrollment_create_params_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


