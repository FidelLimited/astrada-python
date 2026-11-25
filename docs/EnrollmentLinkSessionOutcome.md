# EnrollmentLinkSessionOutcome

What the hosted page reported when the session completed. A session completes something when it reports at least one id.  The ids are as the page sent them: nothing checks them against the card or bank APIs. The `cardsubscription` webhooks are the source of truth for what was enrolled. When the link has a `customerReferenceId`, the card subscriptions created through it carry that reference. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_ids** | **List[str]** | Card subscriptions the page reports it created. | [optional] 
**card_ids** | **List[str]** | Cards the page reports it enrolled. | [optional] 
**bank_link_ids** | **List[str]** | Bank links the page reports it completed. | [optional] 
**summary** | **Dict[str, int]** | Up to 10 counts the page reports. Each name is 1 to 40 letters and digits and starts with a letter.  | [optional] 

## Example

```python
from astrada.models.enrollment_link_session_outcome import EnrollmentLinkSessionOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkSessionOutcome from a JSON string
enrollment_link_session_outcome_instance = EnrollmentLinkSessionOutcome.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkSessionOutcome.to_json())

# convert the object into a dict
enrollment_link_session_outcome_dict = enrollment_link_session_outcome_instance.to_dict()
# create an instance of EnrollmentLinkSessionOutcome from a dict
enrollment_link_session_outcome_from_dict = EnrollmentLinkSessionOutcome.from_dict(enrollment_link_session_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


