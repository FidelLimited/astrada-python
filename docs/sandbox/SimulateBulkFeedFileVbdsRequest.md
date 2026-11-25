# SimulateBulkFeedFileVbdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_reference** | **str** | The Visa RPIC identifier for the bulk feed, made of the Visa region, processor, issuer and company segments joined by &#39;_&#39; (&#39;{region}_{processor}_{issuer}_{company}&#39;), such as &#39;1_12345_67890_54321&#39;. Must match the feed created via &#x60;POST /network-bulk-feeds&#x60;.  | 
**card_count** | **int** | Number of cards from the head of the sandbox card pool to include. These are the same cards every call; once enrolled in the subaccount they deduplicate. &#x60;cardCount + newCardCount&#x60; must be at least 1.  | [optional] [default to 5]
**new_card_count** | **int** | Number of not-yet-enrolled cards to draw from the sandbox pool for this feed&#39;s subaccount. Each call enrolls this many new cards (with &#x60;cardsubscription.created&#x60; webhooks). Requires an active feed for the &#x60;networkReference&#x60;; returns &#x60;400&#x60; when none exists or when the subaccount has exhausted the pool.  | [optional] [default to 0]
**transactions_per_card** | **int** | Number of settlements generated for every included card, with fresh transaction ids and recent dates on each call. Use &#x60;0&#x60; for a cards-only delivery.  | [optional] [default to 3]

## Example

```python
from astrada.sandbox.models.simulate_bulk_feed_file_vbds_request import SimulateBulkFeedFileVbdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateBulkFeedFileVbdsRequest from a JSON string
simulate_bulk_feed_file_vbds_request_instance = SimulateBulkFeedFileVbdsRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateBulkFeedFileVbdsRequest.to_json())

# convert the object into a dict
simulate_bulk_feed_file_vbds_request_dict = simulate_bulk_feed_file_vbds_request_instance.to_dict()
# create an instance of SimulateBulkFeedFileVbdsRequest from a dict
simulate_bulk_feed_file_vbds_request_from_dict = SimulateBulkFeedFileVbdsRequest.from_dict(simulate_bulk_feed_file_vbds_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


