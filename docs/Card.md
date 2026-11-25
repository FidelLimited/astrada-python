# Card


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**CardLinks**](CardLinks.md) |  | 
**embedded** | [**CardEmbedded**](CardEmbedded.md) |  | [optional] 
**id** | **str** | The unique identifier of this card entity. | 
**subaccount_id** | **str** | The unique identifier of the subaccount related to this entity. | 
**expiry_month** | **int** | The month that the card will expire in MM format. | 
**expiry_year** | **int** | The year that the card will expire in YYYY format. | 
**first6digits** | **str** | The first 6 digits of the card number (PAN). Nullable for bank-derived cards (created from a bank connection, where the full PAN is never seen); populated when known (e.g. the SDK captured the BIN before pivoting to the bank flow) and attached when the card is later PAN-enrolled (upgrade-in-place keeps the same card id).  | [optional] 
**last4digits** | **str** | The last 4 digits of the card number (PAN). | 
**network** | **str** | The card network that processes payments for this card. &#x60;amex&#x60; and &#x60;null&#x60; occur only on bank-derived cards: Amex-institution connections mint &#x60;amex&#x60;; other institutions cannot reveal the network from bank data, so it stays &#x60;null&#x60; until the card is PAN-enrolled (upgrade-in-place).  | [optional] 
**country** | **str** | The country of issuance for this card following ISO 3166 alpha-3. | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print(Card.to_json())

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_from_dict = Card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


