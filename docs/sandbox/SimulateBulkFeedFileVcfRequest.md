# SimulateBulkFeedFileVcfRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_reference** | **str** | The Visa reference for the bulk feed. Pass the same value used to create the feed via &#x60;POST /network-bulk-feeds&#x60;: the full RPIC &#39;{region}_{processor}_{issuer}_{company}&#39;, such as &#39;1_123_45_6789&#39;; the region segment is ignored. The 3-segment PIC form &#39;{processor}_{issuer}_{company}&#39; is also accepted.  | 
**card_count** | **int** | Number of cards from the head of the sandbox test-card pool to include. These are the same cards every call; once enrolled in the subaccount they deduplicate. &#x60;cardCount + newCardCount&#x60; must be at least 1.  While a feed has not completed an ingestion (normally its first call), a call with &#x60;newCardCount&#x60; of &#x60;0&#x60; also adds one card the feed&#39;s subaccount has not seen before, so the feed can become active.  | [optional] [default to 5]
**new_card_count** | **int** | Number of not-yet-enrolled cards to draw from the sandbox new-card pool for this feed&#39;s subaccount. Each call enrolls this many new cards (with &#x60;cardsubscription.created&#x60; webhooks). Requires an active feed for the &#x60;networkReference&#x60;; returns &#x60;400&#x60; when none exists or when the subaccount has exhausted the pool.  | [optional] [default to 0]
**transactions_per_card** | **int** | Number of transactions generated for every included card, with fresh transaction references and recent dates on each call. Use &#x60;0&#x60; for a cards-only (starter) file.  | [optional] [default to 3]

## Example

```python
from astrada.sandbox.models.simulate_bulk_feed_file_vcf_request import SimulateBulkFeedFileVcfRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateBulkFeedFileVcfRequest from a JSON string
simulate_bulk_feed_file_vcf_request_instance = SimulateBulkFeedFileVcfRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateBulkFeedFileVcfRequest.to_json())

# convert the object into a dict
simulate_bulk_feed_file_vcf_request_dict = simulate_bulk_feed_file_vcf_request_instance.to_dict()
# create an instance of SimulateBulkFeedFileVcfRequest from a dict
simulate_bulk_feed_file_vcf_request_from_dict = SimulateBulkFeedFileVcfRequest.from_dict(simulate_bulk_feed_file_vcf_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


