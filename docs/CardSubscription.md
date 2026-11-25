# CardSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**CardSubscriptionLinks**](CardSubscriptionLinks.md) |  | 
**embedded** | [**CardSubscriptionEmbedded**](CardSubscriptionEmbedded.md) |  | [optional] 
**id** | **str** | The unique identifier of this subscription entity. | 
**account_id** | **str** | The unique identifier of the account related to this entity. | [optional] 
**subaccount_id** | **str** | The unique identifier of the subaccount related to this entity. | 
**card_id** | **str** | The unique identifier of the card related to this entity. | 
**customer_reference_id** | **str** | An optional id in UUID format passed by the customer to associate a context with the subscription. | [optional] 
**state** | **str** | State of the subscription. &#x60;active&#x60; and &#x60;pending&#x60; subscriptions are both considered enrolled in Astrada&#39;s platform. A &#x60;pending&#x60; subscription is enrolled from a network roster while the card is still inactive at the network (e.g. Mastercard Smart Data &#x60;I&#x60; status): it is customer-visible but has not yet received a transaction. It exits only by promotion to &#x60;active&#x60; (a later roster &#x60;active&#x60; record or the card&#39;s first clearing transaction), explicit deactivation, or expiry. Virtual cards are excluded from &#x60;pending&#x60; enrollment.  | 
**deactivation_reason** | [**CardSubscriptionDeactivationReason**](CardSubscriptionDeactivationReason.md) | The reason given when this subscription was deactivated. Only present on a deactivated subscription that was given a reason; the field is left out otherwise. New values may be added, so treat an unknown value as &#x60;other&#x60;.  | [optional] 
**effective_date** | **datetime** | Date and time when this card subscription will be activated and start receiving data, in UTC, following ISO 8601 format. | 
**expiration_date** | **datetime** | Date and time when this card subscription will become expired and stop receiving data, in UTC, following ISO 8601 format. | 
**network_bulk_feed_id** | **str** | The unique identifier of the network bulk feed associated with this card subscription. Present when the &#x60;enrollmentType&#x60; is &#x60;network-bulk&#x60;, null otherwise. | [optional] 
**bank_account_id** | **str** | The bank account this subscription&#39;s card was originally materialized from; present only when &#x60;enrollmentType&#x60; is &#x60;bank-feed&#x60; (the analog of &#x60;networkBulkFeedId&#x60; for bank-connected enrollments). This is provenance and does not re-point if a re-link later attaches the card to a successor account; the current link surface is the bank account&#39;s &#x60;cardIds&#x60;. | [optional] 
**enrollment_type** | **str** | The flow that led to the creation of the card subscription. &#x60;cardholder-single&#x60; refers to enrollments where cardholders themselves are responsible for inputting card data and where a single card is attempted at a time. &#x60;network-bulk&#x60; refers to enrollments where card data will be captured by Astrada using network data sources (eg Mastercard Smart Data) and where many cards may be attempted at once. &#x60;bank-feed&#x60; refers to cards materialized from a bank connection (e.g. American Express via the hosted bank-linking flow); the bank-side analog of &#x60;network-bulk&#x60;, with &#x60;bankAccountId&#x60; as the back-reference. | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.models.card_subscription import CardSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of CardSubscription from a JSON string
card_subscription_instance = CardSubscription.from_json(json)
# print the JSON string representation of the object
print(CardSubscription.to_json())

# convert the object into a dict
card_subscription_dict = card_subscription_instance.to_dict()
# create an instance of CardSubscription from a dict
card_subscription_from_dict = CardSubscription.from_dict(card_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


