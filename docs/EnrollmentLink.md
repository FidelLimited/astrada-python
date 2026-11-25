# EnrollmentLink

An enrollment link to the Astrada-hosted page where people enroll their own cards into one subaccount. The link's `url` is returned only by the request that creates it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | 
**id** | **str** | The link&#39;s identifier. | 
**kind** | **str** | - &#x60;cardholder&#x60;: a personal link for one employee. It allows up to 5 session starts and   is used up by the first session that completes something. - &#x60;team&#x60;: a link to share with a team. Every session start counts as a use, up to   &#x60;maxUses&#x60;.  | 
**subaccount_id** | **str** | The subaccount that cards enrolled through the link join. | 
**starting_point** | **str** | Where the hosted page starts. Only &#x60;card&#x60; is available now; links made before the field existed read as &#x60;card&#x60;. | 
**state** | **str** | - &#x60;active&#x60;: sessions can start. - &#x60;used&#x60;: a personal link whose session completed something. - &#x60;revoked&#x60;: revoked with &#x60;POST /enrollment-links/{linkId}/revoke&#x60; or by deleting its   subaccount. Team links revoked by the former five-active-link limit on   &#x60;POST /subaccounts/{subaccountId}/team-link&#x60; stay revoked. - &#x60;expired&#x60;: an active link past &#x60;expiresAt&#x60;.  | 
**expires_at** | **datetime** | After this time no session starts from the link. | 
**max_uses** | **int** | 1 on a personal link. On a team link, the session starts it allows. | 
**uses** | **int** | On a team link, the sessions started so far. On a personal link, 1 once it is used, otherwise 0. | 
**starts** | **int** | The sessions started from the link so far. | 
**customer_reference_id** | **str** | The reference given when the link was created. Absent when none was given. | [optional] 
**platform_name** | **str** | The platform name given when the link was created. Absent when none was given. The hosted page ignores it once the account has a brand profile.  | [optional] 
**organization_name** | **str** | The organization name given when the link was created. Absent when none was given. | [optional] 
**created_by** | [**EnrollmentLinkCreatedBy**](EnrollmentLinkCreatedBy.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**used_at** | **datetime** | When a personal link was used up. | [optional] 
**revoked_at** | **datetime** | When the link was revoked. | [optional] 

## Example

```python
from astrada.models.enrollment_link import EnrollmentLink

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLink from a JSON string
enrollment_link_instance = EnrollmentLink.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLink.to_json())

# convert the object into a dict
enrollment_link_dict = enrollment_link_instance.to_dict()
# create an instance of EnrollmentLink from a dict
enrollment_link_from_dict = EnrollmentLink.from_dict(enrollment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


