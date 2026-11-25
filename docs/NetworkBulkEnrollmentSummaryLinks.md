# NetworkBulkEnrollmentSummaryLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) | The open kickoff (&#x60;/network-bulk-enrollments/{id}&#x60;). A token with &#x60;network-bulk-enrollments:read&#x60; or &#x60;network-bulk-feeds:read&#x60; can follow it to the full enrollment; any other token gets &#x60;403&#x60;.  | 

## Example

```python
from astrada.models.network_bulk_enrollment_summary_links import NetworkBulkEnrollmentSummaryLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentSummaryLinks from a JSON string
network_bulk_enrollment_summary_links_instance = NetworkBulkEnrollmentSummaryLinks.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentSummaryLinks.to_json())

# convert the object into a dict
network_bulk_enrollment_summary_links_dict = network_bulk_enrollment_summary_links_instance.to_dict()
# create an instance of NetworkBulkEnrollmentSummaryLinks from a dict
network_bulk_enrollment_summary_links_from_dict = NetworkBulkEnrollmentSummaryLinks.from_dict(network_bulk_enrollment_summary_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


