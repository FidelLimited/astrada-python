# BankFeedCard

A card created from a bank account at bank-link completion (a `bank-feed` enrollment), with its subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The minted card&#39;s identifier on the cards platform. | 
**subscription_id** | **str** | The bank-feed card subscription created by the mint. | 
**last4digits** | **str** | The card number&#39;s last 4; equals this account&#39;s mask by construction. | 
**network** | **str** | The card network when the institution implies it (e.g. &#x60;amex&#x60;); null until a PAN enrollment upgrades the card in place. | 
**enrollment_type** | **str** | Always &#x60;bank-feed&#x60;; the enrollment transport this card was materialized through. | 

## Example

```python
from astrada.banking.models.bank_feed_card import BankFeedCard

# TODO update the JSON string below
json = "{}"
# create an instance of BankFeedCard from a JSON string
bank_feed_card_instance = BankFeedCard.from_json(json)
# print the JSON string representation of the object
print(BankFeedCard.to_json())

# convert the object into a dict
bank_feed_card_dict = bank_feed_card_instance.to_dict()
# create an instance of BankFeedCard from a dict
bank_feed_card_from_dict = BankFeedCard.from_dict(bank_feed_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


