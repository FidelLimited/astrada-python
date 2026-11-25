# EnrollmentLinkCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | **str** | - &#x60;api&#x60;: &#x60;POST /enrollment-links&#x60; with &#x60;subaccounts:write&#x60;. - &#x60;staff&#x60;: &#x60;POST /enrollment-links&#x60; with Astrada&#39;s &#x60;accounts:write&#x60;. - &#x60;sdk&#x60;: &#x60;POST /subaccounts/{subaccountId}/team-link&#x60;, the route for the SDK&#39;s   \&quot;Invite your team\&quot; ending.  | 
**client_id** | **str** | The client ID of the credential that created the link, when known. | [optional] 

## Example

```python
from astrada.models.enrollment_link_created_by import EnrollmentLinkCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkCreatedBy from a JSON string
enrollment_link_created_by_instance = EnrollmentLinkCreatedBy.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkCreatedBy.to_json())

# convert the object into a dict
enrollment_link_created_by_dict = enrollment_link_created_by_instance.to_dict()
# create an instance of EnrollmentLinkCreatedBy from a dict
enrollment_link_created_by_from_dict = EnrollmentLinkCreatedBy.from_dict(enrollment_link_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


