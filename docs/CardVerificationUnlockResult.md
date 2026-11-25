# CardVerificationUnlockResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlocked** | **bool** | Always &#x60;true&#x60; on success. | 
**cleared** | **bool** | Whether an active lock actually existed and was cleared. &#x60;false&#x60; when the card had no active lock (the idempotent no-op case).  | 

## Example

```python
from astrada.models.card_verification_unlock_result import CardVerificationUnlockResult

# TODO update the JSON string below
json = "{}"
# create an instance of CardVerificationUnlockResult from a JSON string
card_verification_unlock_result_instance = CardVerificationUnlockResult.from_json(json)
# print the JSON string representation of the object
print(CardVerificationUnlockResult.to_json())

# convert the object into a dict
card_verification_unlock_result_dict = card_verification_unlock_result_instance.to_dict()
# create an instance of CardVerificationUnlockResult from a dict
card_verification_unlock_result_from_dict = CardVerificationUnlockResult.from_dict(card_verification_unlock_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


