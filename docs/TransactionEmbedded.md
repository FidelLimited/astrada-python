# TransactionEmbedded

Related resources inlined on request with the `expand` query parameter (`?expand=cardSubscription,card,cardholder`). A key is present only when it was requested and the related resource exists, and it is never null. Each embedded body is identical to the one served by the resource's own endpoint. Absent entirely when `expand` is not sent. Embedded resources show their current values, not those at the time of the transaction, with one exception: `cardholder.corporate` is the cardholder's corporate as of the transaction's `transactionOccurrenceDate` (end of that UTC day), or its `createdAt` when that is null.  `cardSubscription` is the transaction's card subscription exactly as `GET /card-subscriptions/{subscriptionId}` serves it (not itself expanded): the card's subscription in the transaction's sub-account, that is the one from the transaction's network bulk feed when the transaction has a `networkBulkFeedId`, otherwise the card's current subscription, otherwise its most recent one. Fields that apply only to some subscriptions (for example network bulk feed ones) follow that endpoint's rules.  `card` is the transaction's card (`cardId`) exactly as `GET /cards/{cardId}` serves it (not itself expanded, so it never carries its own `_embedded.cardholder`). `cardholder` is that card's cardholder as `GET /cards/{cardId}/cardholder` serves it, except that `corporate` (`id`, `employeeId`, `alternativeEmployeeId`, `legalEntity`) is the value in effect at the transaction's date while every other field is current; absent when the card has no cardholder data. When `GET /cards/{cardId}` would respond `404` for the card (for example because all of its card subscriptions were deleted), neither `card` nor `cardholder` is present. When `cardId` is null, none of the three keys is present. Presence is decided on the card and cardholder as they are now.  Transaction webhooks can also carry `_embedded` (see [Event Types](https://docs.astrada.co/reference/event-types)). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_subscription** | [**CardSubscription**](CardSubscription.md) |  | [optional] 
**card** | [**Card**](Card.md) |  | [optional] 
**cardholder** | [**Cardholder**](Cardholder.md) |  | [optional] 

## Example

```python
from astrada.models.transaction_embedded import TransactionEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionEmbedded from a JSON string
transaction_embedded_instance = TransactionEmbedded.from_json(json)
# print the JSON string representation of the object
print(TransactionEmbedded.to_json())

# convert the object into a dict
transaction_embedded_dict = transaction_embedded_instance.to_dict()
# create an instance of TransactionEmbedded from a dict
transaction_embedded_from_dict = TransactionEmbedded.from_dict(transaction_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


