# ConsentPolicy

Which consent records `POST /card-subscriptions` accepts for this subaccount. Astrada sets it, on the account as a default and on the subaccount as an override; there is no route to change it. The value is the effective one: each field comes from the subaccount when it sets one, otherwise from the account, except that an account `mode` of `off` turns the mode off for every subaccount. Absent (never `null`) when neither level sets a field.  A subaccount with no `consentPolicy` behaves as `log` with every channel allowed. Which mode a new or existing account starts in: [When consent is required](https://docs.astrada.co/docs/direct-api-card-enrollment-integration#when-consent-is-required). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_channels** | **List[str]** | The channels a consent may come from. A consent from any other channel fails with &#x60;consent_channel_not_allowed&#x60;. | [optional] 
**mode** | **str** | &#x60;off&#x60; records nothing, &#x60;log&#x60; records without refusing, &#x60;enforce&#x60; refuses a missing or failing consent. What each mode answers: [When consent is required](https://docs.astrada.co/docs/direct-api-card-enrollment-integration#when-consent-is-required).  | [optional] 

## Example

```python
from astrada.models.consent_policy import ConsentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentPolicy from a JSON string
consent_policy_instance = ConsentPolicy.from_json(json)
# print the JSON string representation of the object
print(ConsentPolicy.to_json())

# convert the object into a dict
consent_policy_dict = consent_policy_instance.to_dict()
# create an instance of ConsentPolicy from a dict
consent_policy_from_dict = ConsentPolicy.from_dict(consent_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


