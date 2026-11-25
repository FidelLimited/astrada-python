# NetworkBulkFeedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**OffsetPageLinks**](OffsetPageLinks.md) |  | 
**embedded** | [**NetworkBulkFeedListEmbedded**](NetworkBulkFeedListEmbedded.md) |  | 
**total_items** | **int** | Total number of network bulk feeds | 

## Example

```python
from astrada.models.network_bulk_feed_list import NetworkBulkFeedList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkFeedList from a JSON string
network_bulk_feed_list_instance = NetworkBulkFeedList.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkFeedList.to_json())

# convert the object into a dict
network_bulk_feed_list_dict = network_bulk_feed_list_instance.to_dict()
# create an instance of NetworkBulkFeedList from a dict
network_bulk_feed_list_from_dict = NetworkBulkFeedList.from_dict(network_bulk_feed_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


