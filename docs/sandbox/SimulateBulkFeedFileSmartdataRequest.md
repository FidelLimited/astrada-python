# SimulateBulkFeedFileSmartdataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_reference** | **str** | The Mastercard Delivery ID for the bulk feed, such as &#39;G1234567&#39;. Must match the feed created via &#x60;POST /network-bulk-feeds&#x60;.  | 
**card_count** | **int** | Number of cards from the head of the sandbox test-card pool to include. These are the same cards every call; once enrolled in the subaccount they deduplicate. &#x60;cardCount + newCardCount&#x60; must be at least 1.  | [optional] [default to 5]
**new_card_count** | **int** | Number of not-yet-enrolled cards to draw from the sandbox new-card pool for this feed&#39;s subaccount. Each call enrolls this many new cards (with &#x60;cardsubscription.created&#x60; webhooks). Requires an active feed for the &#x60;networkReference&#x60;; returns &#x60;400&#x60; when none exists or when the subaccount has exhausted the pool.  | [optional] [default to 0]
**transactions_per_card** | **int** | Number of transactions generated for every included card, with fresh transaction references and recent dates on each call. Use &#x60;0&#x60; for a cards-only (starter) file.  | [optional] [default to 3]

## Example

```python
from astrada.sandbox.models.simulate_bulk_feed_file_smartdata_request import SimulateBulkFeedFileSmartdataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateBulkFeedFileSmartdataRequest from a JSON string
simulate_bulk_feed_file_smartdata_request_instance = SimulateBulkFeedFileSmartdataRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateBulkFeedFileSmartdataRequest.to_json())

# convert the object into a dict
simulate_bulk_feed_file_smartdata_request_dict = simulate_bulk_feed_file_smartdata_request_instance.to_dict()
# create an instance of SimulateBulkFeedFileSmartdataRequest from a dict
simulate_bulk_feed_file_smartdata_request_from_dict = SimulateBulkFeedFileSmartdataRequest.from_dict(simulate_bulk_feed_file_smartdata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


