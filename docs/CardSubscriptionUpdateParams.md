# CardSubscriptionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**deactivation_reason** | [**CardSubscriptionDeactivationReason**](CardSubscriptionDeactivationReason.md) | Optional reason for the deactivation. Only accepted together with &#x60;state: deactivated&#x60;; sending it on its own returns &#x60;400&#x60;. Returned in the &#x60;deactivationReason&#x60; field of the card subscription.  | [optional] 

## Example

```python
from astrada.models.card_subscription_update_params import CardSubscriptionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of CardSubscriptionUpdateParams from a JSON string
card_subscription_update_params_instance = CardSubscriptionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(CardSubscriptionUpdateParams.to_json())

# convert the object into a dict
card_subscription_update_params_dict = card_subscription_update_params_instance.to_dict()
# create an instance of CardSubscriptionUpdateParams from a dict
card_subscription_update_params_from_dict = CardSubscriptionUpdateParams.from_dict(card_subscription_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


