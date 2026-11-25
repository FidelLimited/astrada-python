# CardSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**OffsetPageLinks**](OffsetPageLinks.md) |  | 
**embedded** | [**CardSubscriptionListEmbedded**](CardSubscriptionListEmbedded.md) |  | 
**total_items** | **int** | Total number of card subscriptions matching the search criteria | 

## Example

```python
from astrada.models.card_subscription_list import CardSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of CardSubscriptionList from a JSON string
card_subscription_list_instance = CardSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(CardSubscriptionList.to_json())

# convert the object into a dict
card_subscription_list_dict = card_subscription_list_instance.to_dict()
# create an instance of CardSubscriptionList from a dict
card_subscription_list_from_dict = CardSubscriptionList.from_dict(card_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


