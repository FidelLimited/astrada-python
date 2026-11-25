# CardListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[Card]**](Card.md) |  | 

## Example

```python
from astrada.models.card_list_embedded import CardListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CardListEmbedded from a JSON string
card_list_embedded_instance = CardListEmbedded.from_json(json)
# print the JSON string representation of the object
print(CardListEmbedded.to_json())

# convert the object into a dict
card_list_embedded_dict = card_list_embedded_instance.to_dict()
# create an instance of CardListEmbedded from a dict
card_list_embedded_from_dict = CardListEmbedded.from_dict(card_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


