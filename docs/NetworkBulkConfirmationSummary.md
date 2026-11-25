# NetworkBulkConfirmationSummary

The `200` body of `POST /network-bulk-confirmations` when the request's program already has an open confirmation request that another request wrote. A program is the calling account, the `subaccountId`, the `network` and the `bin`. The summary names the open request and leaves out its contact details: no names, emails, bank contact, `binInfo` or `grade`. It is plain JSON with no `_links`, as a confirmation has no GET. `alreadyOpen` is always `true` here, and the full confirmation never carries it, a replay of your own `requestId` included. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**already_open** | **bool** | Always &#x60;true&#x60;. Tells this summary apart from the full confirmation. | 
**id** | **str** | The unique identifier of the open confirmation request. | 
**request_id** | **str** | The &#x60;requestId&#x60; this request sent. It is never the &#x60;requestId&#x60; the open request was stored under. | 
**subaccount_id** | **str** | The subaccount of the open request, the same as the request&#39;s. | 
**network** | **str** | The network of the open request, the same as the request&#39;s. | 
**state** | **str** | The state of the open request. &#x60;requested&#x60; is the only state for now. | 
**created_at** | **datetime** | When the open request was created, in UTC, following ISO 8601 format. Its 30-day window counts from this time. | 

## Example

```python
from astrada.models.network_bulk_confirmation_summary import NetworkBulkConfirmationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmationSummary from a JSON string
network_bulk_confirmation_summary_instance = NetworkBulkConfirmationSummary.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmationSummary.to_json())

# convert the object into a dict
network_bulk_confirmation_summary_dict = network_bulk_confirmation_summary_instance.to_dict()
# create an instance of NetworkBulkConfirmationSummary from a dict
network_bulk_confirmation_summary_from_dict = NetworkBulkConfirmationSummary.from_dict(network_bulk_confirmation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


