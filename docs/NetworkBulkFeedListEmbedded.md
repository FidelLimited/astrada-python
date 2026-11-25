# NetworkBulkFeedListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_bulk_feeds** | [**List[NetworkBulkFeeds]**](NetworkBulkFeeds.md) |  | 

## Example

```python
from astrada.models.network_bulk_feed_list_embedded import NetworkBulkFeedListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkFeedListEmbedded from a JSON string
network_bulk_feed_list_embedded_instance = NetworkBulkFeedListEmbedded.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkFeedListEmbedded.to_json())

# convert the object into a dict
network_bulk_feed_list_embedded_dict = network_bulk_feed_list_embedded_instance.to_dict()
# create an instance of NetworkBulkFeedListEmbedded from a dict
network_bulk_feed_list_embedded_from_dict = NetworkBulkFeedListEmbedded.from_dict(network_bulk_feed_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


