# CardSubscriptionListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_subscriptions** | [**List[CardSubscription]**](CardSubscription.md) |  | 

## Example

```python
from astrada.models.card_subscription_list_embedded import CardSubscriptionListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CardSubscriptionListEmbedded from a JSON string
card_subscription_list_embedded_instance = CardSubscriptionListEmbedded.from_json(json)
# print the JSON string representation of the object
print(CardSubscriptionListEmbedded.to_json())

# convert the object into a dict
card_subscription_list_embedded_dict = card_subscription_list_embedded_instance.to_dict()
# create an instance of CardSubscriptionListEmbedded from a dict
card_subscription_list_embedded_from_dict = CardSubscriptionListEmbedded.from_dict(card_subscription_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


