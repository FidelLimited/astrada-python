# CardVerificationUnlockParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Identifier of the card whose attempt lockout to clear. | 

## Example

```python
from astrada.models.card_verification_unlock_params import CardVerificationUnlockParams

# TODO update the JSON string below
json = "{}"
# create an instance of CardVerificationUnlockParams from a JSON string
card_verification_unlock_params_instance = CardVerificationUnlockParams.from_json(json)
# print the JSON string representation of the object
print(CardVerificationUnlockParams.to_json())

# convert the object into a dict
card_verification_unlock_params_dict = card_verification_unlock_params_instance.to_dict()
# create an instance of CardVerificationUnlockParams from a dict
card_verification_unlock_params_from_dict = CardVerificationUnlockParams.from_dict(card_verification_unlock_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


