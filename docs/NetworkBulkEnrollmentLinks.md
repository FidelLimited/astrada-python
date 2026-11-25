# NetworkBulkEnrollmentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**network_bulk_feed** | [**Link**](Link.md) | The network bulk feed registered against this enrollment (&#x60;/network-bulk-feeds/{networkBulkFeedId}&#x60;). Present once &#x60;state&#x60; is &#x60;feed-created&#x60;, absent before that.  | [optional] 

## Example

```python
from astrada.models.network_bulk_enrollment_links import NetworkBulkEnrollmentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentLinks from a JSON string
network_bulk_enrollment_links_instance = NetworkBulkEnrollmentLinks.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentLinks.to_json())

# convert the object into a dict
network_bulk_enrollment_links_dict = network_bulk_enrollment_links_instance.to_dict()
# create an instance of NetworkBulkEnrollmentLinks from a dict
network_bulk_enrollment_links_from_dict = NetworkBulkEnrollmentLinks.from_dict(network_bulk_enrollment_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


