# SimulateBulkFeedFileGlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_reference** | **str** | The Amex Recipient ID for the bulk feed, in the format &#39;R{RecipientId}&#39;, such as &#39;R12345&#39;, or the 6-digit Company ID the feed was created with. Must match the feed created via &#x60;POST /network-bulk-feeds&#x60;.  | 
**card_count** | **int** | Number of cards to include. For an &#x60;encrypted&#x60; feed these are drawn from the head of the sandbox account pool: the same accounts every call; once enrolled in the subaccount they deduplicate. For a &#x60;tokenized&#x60; feed they are drawn from the enrollable 374290-BIN Amex token pool (two tokens). Requesting more than the tokenized pool holds does not error: the call still returns &#x60;202&#x60; and under-delivers (only the enrollable tokens are written), so do not build a retry on an expected &#x60;400&#x60;. When omitted, defaults to 3 for encrypted feeds and to the whole enrollable token pool for tokenized feeds. When &#x60;cardCount&#x60; is sent, &#x60;cardCount + newCardCount&#x60; must be at least 1.  | [optional] 
**new_card_count** | **int** | Number of not-yet-enrolled accounts to draw from the sandbox pool for this feed&#39;s subaccount. Each call enrolls this many new cards (with &#x60;cardsubscription.created&#x60; webhooks). Requires an active feed for the &#x60;networkReference&#x60;; returns &#x60;400&#x60; when none exists or when the subaccount has exhausted the pool. Not supported on &#x60;tokenized&#x60; feeds: a value greater than 0 on a tokenized feed returns &#x60;400&#x60; (there is no tokenized new-card pool).  | [optional] [default to 0]
**transactions_per_card** | **int** | Number of settlements generated for every included card (written as a companion settlement file), with fresh transaction ids and recent dates on each call. Use &#x60;0&#x60; for a cards-only file.  | [optional] [default to 3]

## Example

```python
from astrada.sandbox.models.simulate_bulk_feed_file_gl_request import SimulateBulkFeedFileGlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateBulkFeedFileGlRequest from a JSON string
simulate_bulk_feed_file_gl_request_instance = SimulateBulkFeedFileGlRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateBulkFeedFileGlRequest.to_json())

# convert the object into a dict
simulate_bulk_feed_file_gl_request_dict = simulate_bulk_feed_file_gl_request_instance.to_dict()
# create an instance of SimulateBulkFeedFileGlRequest from a dict
simulate_bulk_feed_file_gl_request_from_dict = SimulateBulkFeedFileGlRequest.from_dict(simulate_bulk_feed_file_gl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


