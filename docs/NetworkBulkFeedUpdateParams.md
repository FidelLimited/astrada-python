# NetworkBulkFeedUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_start_date** | **date** | Transactions posted on or after this calendar date (&#x60;YYYY-MM-DD&#x60;, a valid date, not in the future) are taken in for this feed&#39;s deliveries, replacing the default window, which keeps only transactions posted on or after the date 15 days before each file&#39;s delivery date (in UTC). On a file that serves several subaccounts, the earliest window among them applies to the whole file. Currently supported for &#x60;SMARTDATA&#x60; feeds only. The comparison is calendar-day based in UTC: the network&#39;s posting date is a date-only field, so a value of e.g. &#x60;2026-06-30&#x60; includes every transaction whose posting date is 2026-06-30 or later, with no local-timezone adjustment.  | [optional] 
**expected_card_count** | **int** | The expected number of cards that will be enrolled under this bulk feed. | [optional] 

## Example

```python
from astrada.models.network_bulk_feed_update_params import NetworkBulkFeedUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkFeedUpdateParams from a JSON string
network_bulk_feed_update_params_instance = NetworkBulkFeedUpdateParams.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkFeedUpdateParams.to_json())

# convert the object into a dict
network_bulk_feed_update_params_dict = network_bulk_feed_update_params_instance.to_dict()
# create an instance of NetworkBulkFeedUpdateParams from a dict
network_bulk_feed_update_params_from_dict = NetworkBulkFeedUpdateParams.from_dict(network_bulk_feed_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


