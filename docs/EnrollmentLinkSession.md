# EnrollmentLinkSession

A session started from an enrollment link, as the hosted page ran it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The session&#39;s identifier. | 
**state** | **str** | - &#x60;open&#x60;: started and not yet completed. - &#x60;completed&#x60;: the page reported the session&#39;s outcome. - &#x60;expired&#x60;: an open session past &#x60;expiresAt&#x60;. It can no longer complete.  | 
**started_at** | **datetime** |  | 
**expires_at** | **datetime** | 60 minutes after &#x60;startedAt&#x60;. | 
**completed_at** | **datetime** |  | [optional] 
**outcome** | [**EnrollmentLinkSessionOutcome**](EnrollmentLinkSessionOutcome.md) |  | [optional] 

## Example

```python
from astrada.models.enrollment_link_session import EnrollmentLinkSession

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkSession from a JSON string
enrollment_link_session_instance = EnrollmentLinkSession.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkSession.to_json())

# convert the object into a dict
enrollment_link_session_dict = enrollment_link_session_instance.to_dict()
# create an instance of EnrollmentLinkSession from a dict
enrollment_link_session_from_dict = EnrollmentLinkSession.from_dict(enrollment_link_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


