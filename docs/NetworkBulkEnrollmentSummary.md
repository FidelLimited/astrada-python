# NetworkBulkEnrollmentSummary

The `200` body of `POST /network-bulk-enrollments` when the request's program already has an open kickoff that another request wrote. A program is the calling account, the `subaccountId`, the `network` and the first 8 digits of the `bin`. The summary names the open kickoff and leaves out its contact details: no names, emails, bank contact, `binInfo`, consent or outreach. `alreadyOpen` is always `true` here, and the full enrollment never carries it, a replay of your own `requestId` included. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**NetworkBulkEnrollmentSummaryLinks**](NetworkBulkEnrollmentSummaryLinks.md) |  | 
**already_open** | **bool** | Always &#x60;true&#x60;. Tells this summary apart from the full enrollment. | 
**id** | **str** | The unique identifier of the open kickoff. | 
**subaccount_id** | **str** | The subaccount of the open kickoff, the same as the request&#39;s. | 
**network** | **str** | The network of the open kickoff, the same as the request&#39;s. | 
**state** | **str** | The open kickoff&#39;s state. &#x60;requested&#x60;: it was created less than 90 days ago and no feed has been registered against it yet. &#x60;feed-created&#x60;: a feed was registered against it and that feed is live.  | 
**network_bulk_feed_id** | **str** | The live feed registered against the open kickoff. &#x60;null&#x60; while the kickoff is &#x60;requested&#x60;. | 
**request_id** | **str** | The &#x60;requestId&#x60; this request sent, or &#x60;null&#x60; when it sent none. It is never the &#x60;requestId&#x60; the open kickoff was stored under.  | 
**created_at** | **datetime** | When the open kickoff was created, in UTC, following ISO 8601 format. Its 90-day window counts from this time. | 

## Example

```python
from astrada.models.network_bulk_enrollment_summary import NetworkBulkEnrollmentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentSummary from a JSON string
network_bulk_enrollment_summary_instance = NetworkBulkEnrollmentSummary.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentSummary.to_json())

# convert the object into a dict
network_bulk_enrollment_summary_dict = network_bulk_enrollment_summary_instance.to_dict()
# create an instance of NetworkBulkEnrollmentSummary from a dict
network_bulk_enrollment_summary_from_dict = NetworkBulkEnrollmentSummary.from_dict(network_bulk_enrollment_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


