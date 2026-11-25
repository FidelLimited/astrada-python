# CardSubscriptionLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**card** | [**Link**](Link.md) |  | 
**verifications** | [**Link**](Link.md) | The link to this card&#39;s 3-D Secure verifications (&#x60;/card-verifications/3ds?cardId&#x3D;&#x60;). Useful when a subscription is stuck at &#x60;reqSCA&#x60; to inspect why verification failed.  | [optional] 
**network_bulk_feed** | [**Link**](Link.md) | The link to the network bulk feed associated with this card subscription, if applicable. This link may be present when the &#x60;enrollmentType&#x60; is &#x60;network-bulk&#x60;. It will not be present for subscriptions created through the &#x60;cardholder-single&#x60; flow.  | [optional] 
**bank_account** | [**Link**](Link.md) | The link to the bank account this subscription&#39;s card was materialized from (&#x60;/bank-accounts/{bankAccountId}&#x60;). Present only when the &#x60;enrollmentType&#x60; is &#x60;bank-feed&#x60;; the bank-connected analog of &#x60;networkBulkFeed&#x60;. Not present for &#x60;cardholder-single&#x60; or &#x60;network-bulk&#x60; subscriptions.  | [optional] 

## Example

```python
from astrada.models.card_subscription_links import CardSubscriptionLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CardSubscriptionLinks from a JSON string
card_subscription_links_instance = CardSubscriptionLinks.from_json(json)
# print the JSON string representation of the object
print(CardSubscriptionLinks.to_json())

# convert the object into a dict
card_subscription_links_dict = card_subscription_links_instance.to_dict()
# create an instance of CardSubscriptionLinks from a dict
card_subscription_links_from_dict = CardSubscriptionLinks.from_dict(card_subscription_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


