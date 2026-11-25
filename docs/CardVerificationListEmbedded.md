# CardVerificationListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_verifications** | [**List[CardVerification]**](CardVerification.md) |  | 

## Example

```python
from astrada.models.card_verification_list_embedded import CardVerificationListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CardVerificationListEmbedded from a JSON string
card_verification_list_embedded_instance = CardVerificationListEmbedded.from_json(json)
# print the JSON string representation of the object
print(CardVerificationListEmbedded.to_json())

# convert the object into a dict
card_verification_list_embedded_dict = card_verification_list_embedded_instance.to_dict()
# create an instance of CardVerificationListEmbedded from a dict
card_verification_list_embedded_from_dict = CardVerificationListEmbedded.from_dict(card_verification_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


