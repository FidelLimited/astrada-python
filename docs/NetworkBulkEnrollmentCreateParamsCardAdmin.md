# NetworkBulkEnrollmentCreateParamsCardAdmin

The card program administrator. Astrada keeps this person engaged throughout onboarding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from astrada.models.network_bulk_enrollment_create_params_card_admin import NetworkBulkEnrollmentCreateParamsCardAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentCreateParamsCardAdmin from a JSON string
network_bulk_enrollment_create_params_card_admin_instance = NetworkBulkEnrollmentCreateParamsCardAdmin.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentCreateParamsCardAdmin.to_json())

# convert the object into a dict
network_bulk_enrollment_create_params_card_admin_dict = network_bulk_enrollment_create_params_card_admin_instance.to_dict()
# create an instance of NetworkBulkEnrollmentCreateParamsCardAdmin from a dict
network_bulk_enrollment_create_params_card_admin_from_dict = NetworkBulkEnrollmentCreateParamsCardAdmin.from_dict(network_bulk_enrollment_create_params_card_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


