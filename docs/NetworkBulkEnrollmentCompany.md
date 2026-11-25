# NetworkBulkEnrollmentCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | The legal name of the company whose card program is being enrolled. | 

## Example

```python
from astrada.models.network_bulk_enrollment_company import NetworkBulkEnrollmentCompany

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentCompany from a JSON string
network_bulk_enrollment_company_instance = NetworkBulkEnrollmentCompany.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentCompany.to_json())

# convert the object into a dict
network_bulk_enrollment_company_dict = network_bulk_enrollment_company_instance.to_dict()
# create an instance of NetworkBulkEnrollmentCompany from a dict
network_bulk_enrollment_company_from_dict = NetworkBulkEnrollmentCompany.from_dict(network_bulk_enrollment_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


