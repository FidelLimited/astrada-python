# CardSubscriptionEmbedded

Related resources inlined on request with the `expand` query parameter (`?expand=card,cardholder`). A key is present only when it was requested and the related resource exists; each embedded body is identical to the one served by the resource's own endpoint. Absent entirely when `expand` is not sent. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**Card**](Card.md) |  | [optional] 
**cardholder** | [**Cardholder**](Cardholder.md) |  | [optional] 

## Example

```python
from astrada.models.card_subscription_embedded import CardSubscriptionEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CardSubscriptionEmbedded from a JSON string
card_subscription_embedded_instance = CardSubscriptionEmbedded.from_json(json)
# print the JSON string representation of the object
print(CardSubscriptionEmbedded.to_json())

# convert the object into a dict
card_subscription_embedded_dict = card_subscription_embedded_instance.to_dict()
# create an instance of CardSubscriptionEmbedded from a dict
card_subscription_embedded_from_dict = CardSubscriptionEmbedded.from_dict(card_subscription_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


