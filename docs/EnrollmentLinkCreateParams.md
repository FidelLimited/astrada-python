# EnrollmentLinkCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaccount_id** | **str** | The subaccount that cards enrolled through the link join. It must be one of your subaccounts. | 
**kind** | **str** | &#x60;cardholder&#x60; for a personal link, &#x60;team&#x60; for a team link. | 
**customer_reference_id** | **str** | Your reference for the link, such as the employee a personal link is for. It must be a UUID, as &#x60;customerReferenceId&#x60; on &#x60;POST /card-subscriptions&#x60; is; any other value answers &#x60;400&#x60;. A session from the link can create card subscriptions only with this reference.  | [optional] 
**platform_name** | **str** | The platform&#39;s name, shown on the hosted page. Letters, digits, spaces and &#x60;. , &amp; &#39; ’ ( ) - _ + ! # @&#x60; only, with at least one letter or digit; surrounding spaces are trimmed. Default: your account&#39;s name. A name that is a well-known brand, such as a card network or a large bank, answers &#x60;400&#x60; &#x60;LINK_NAME_NOT_ALLOWED&#x60;. Once Astrada has set a brand profile for your account, the hosted pages show its name and ignore this one.  | [optional] 
**organization_name** | **str** | The employer&#39;s name, shown on the hosted page. The same characters as &#x60;platformName&#x60;, and the same &#x60;LINK_NAME_NOT_ALLOWED&#x60; refusal. Default: none; the hosted page then names only the platform.  | [optional] 
**starting_point** | **str** | Where the hosted page starts. Only &#x60;card&#x60; is available now; any other value answers &#x60;400&#x60;.  | [optional] [default to 'card']
**expires_in_hours** | **int** | How long the link can start sessions. Default: 168 (7 days) for a personal link, 336 (14 days) for a team link.  | [optional] 
**max_uses** | **int** | Team links only: the session starts the link allows. Default: 50. On a personal link it answers &#x60;400&#x60;.  | [optional] 

## Example

```python
from astrada.models.enrollment_link_create_params import EnrollmentLinkCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkCreateParams from a JSON string
enrollment_link_create_params_instance = EnrollmentLinkCreateParams.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkCreateParams.to_json())

# convert the object into a dict
enrollment_link_create_params_dict = enrollment_link_create_params_instance.to_dict()
# create an instance of EnrollmentLinkCreateParams from a dict
enrollment_link_create_params_from_dict = EnrollmentLinkCreateParams.from_dict(enrollment_link_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


