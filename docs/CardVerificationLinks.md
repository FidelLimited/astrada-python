# CardVerificationLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) | The link to this verification resource. | 
**steps** | [**Link**](Link.md) | The link to this verification&#39;s steps (&#x60;/card-verifications/3ds/{verificationId}/steps&#x60;). | 
**current_step** | [**Link**](Link.md) | The link to the step the client should execute next. Absent once the verification reaches a terminal &#x60;state&#x60; (&#x60;completed&#x60; or &#x60;failed&#x60;).  | [optional] 

## Example

```python
from astrada.models.card_verification_links import CardVerificationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CardVerificationLinks from a JSON string
card_verification_links_instance = CardVerificationLinks.from_json(json)
# print the JSON string representation of the object
print(CardVerificationLinks.to_json())

# convert the object into a dict
card_verification_links_dict = card_verification_links_instance.to_dict()
# create an instance of CardVerificationLinks from a dict
card_verification_links_from_dict = CardVerificationLinks.from_dict(card_verification_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


