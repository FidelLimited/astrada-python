# CardVerificationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | 
**embedded** | [**CardVerificationListEmbedded**](CardVerificationListEmbedded.md) |  | 
**total_items** | **int** |  | 

## Example

```python
from astrada.models.card_verification_list import CardVerificationList

# TODO update the JSON string below
json = "{}"
# create an instance of CardVerificationList from a JSON string
card_verification_list_instance = CardVerificationList.from_json(json)
# print the JSON string representation of the object
print(CardVerificationList.to_json())

# convert the object into a dict
card_verification_list_dict = card_verification_list_instance.to_dict()
# create an instance of CardVerificationList from a dict
card_verification_list_from_dict = CardVerificationList.from_dict(card_verification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


