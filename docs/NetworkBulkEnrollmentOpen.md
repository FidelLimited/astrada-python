# NetworkBulkEnrollmentOpen

Whether the card program has an open kickoff, the answer of `GET /network-bulk-enrollments/open`. When it has none, the body is `{ \"open\": false }` and nothing else. When it has one, the body carries only that kickoff's `enrollmentId`, `state` and `requestedAt`: no names, emails, bank contact, `binInfo`, consent or outreach, as the kickoff may have been sent by someone else. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open** | **bool** | Whether the program has an open kickoff, by the same rule &#x60;POST /network-bulk-enrollments&#x60; uses. | 
**enrollment_id** | **str** | The open kickoff&#39;s identifier, the &#x60;id&#x60; that &#x60;POST /network-bulk-enrollments&#x60; answers with when it finds the same kickoff. Present only when &#x60;open&#x60; is &#x60;true&#x60;.  | [optional] 
**state** | **str** | The open kickoff&#39;s state. &#x60;requested&#x60;: it was created less than 90 days ago and no feed is registered yet. &#x60;feed-created&#x60;: its feed is registered and live. Present only when &#x60;open&#x60; is &#x60;true&#x60;.  | [optional] 
**requested_at** | **datetime** | When the open kickoff was created, in UTC, following ISO 8601 format. Present only when &#x60;open&#x60; is &#x60;true&#x60;.  | [optional] 

## Example

```python
from astrada.models.network_bulk_enrollment_open import NetworkBulkEnrollmentOpen

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentOpen from a JSON string
network_bulk_enrollment_open_instance = NetworkBulkEnrollmentOpen.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentOpen.to_json())

# convert the object into a dict
network_bulk_enrollment_open_dict = network_bulk_enrollment_open_instance.to_dict()
# create an instance of NetworkBulkEnrollmentOpen from a dict
network_bulk_enrollment_open_from_dict = NetworkBulkEnrollmentOpen.from_dict(network_bulk_enrollment_open_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


