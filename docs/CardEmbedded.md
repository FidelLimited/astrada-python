# CardEmbedded

Related resources inlined on request with the `expand` query parameter (`?expand=cardholder`). The `cardholder` key is present only when it was requested and the cardholder exists; its body is identical to the one served by `GET /cards/{cardId}/cardholder`. Absent entirely when `expand` is not sent. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardholder** | [**Cardholder**](Cardholder.md) |  | [optional] 

## Example

```python
from astrada.models.card_embedded import CardEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CardEmbedded from a JSON string
card_embedded_instance = CardEmbedded.from_json(json)
# print the JSON string representation of the object
print(CardEmbedded.to_json())

# convert the object into a dict
card_embedded_dict = card_embedded_instance.to_dict()
# create an instance of CardEmbedded from a dict
card_embedded_from_dict = CardEmbedded.from_dict(card_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


