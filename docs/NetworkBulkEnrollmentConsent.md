# NetworkBulkEnrollmentConsent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_at** | **datetime** | When the consent was recorded, which is the server time of the create request, in UTC, following ISO 8601 format. | 
**version** | **str** | The version of the consent wording that was accepted, as sent by the client (for example &#x60;kickoff-consent-v1&#x60;). | 

## Example

```python
from astrada.models.network_bulk_enrollment_consent import NetworkBulkEnrollmentConsent

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentConsent from a JSON string
network_bulk_enrollment_consent_instance = NetworkBulkEnrollmentConsent.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentConsent.to_json())

# convert the object into a dict
network_bulk_enrollment_consent_dict = network_bulk_enrollment_consent_instance.to_dict()
# create an instance of NetworkBulkEnrollmentConsent from a dict
network_bulk_enrollment_consent_from_dict = NetworkBulkEnrollmentConsent.from_dict(network_bulk_enrollment_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


