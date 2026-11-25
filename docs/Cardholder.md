# Cardholder

The person a card belongs to: their name, email address and postal code, and their company details in `corporate`. A card has at most one cardholder, and not every card has one. Which fields are filled depends on how the card was enrolled:  - **Card entered by number** (the card form, or `POST /card-subscriptions`): since 10 November 2026,   created with the card subscription, before the bank's check, from the `cardholderName` sent. When created it   holds only `firstName` and `lastName`; `email`, `postalCode` and the ids in `corporate` (`id`,   `employeeId`, `alternativeEmployeeId`) are `null`. A blank `cardholderName` gives no cardholder, and a   card entered by number before 10 November 2026 got none when it was entered. - **Network bulk feed**: created from the network's file when it carries cardholder data, with the fields   that file carries. Which fields those are differs by network. - **Bank sign-in**: the cardholders a bank sign-in creates are on some American Express cards only, and   hold no company details when created. See   [American Express cards](https://docs.astrada.co/docs/bank-linking#which-kind-of-account-is-it).  Read it with `GET /cards/{cardId}/cardholder` (scope `cardholder:read`), or inline with `expand=cardholder` on a card, a card subscription or a transaction. A card that has a cardholder carries a `cardholder` link in its `_links`. For a card without one, `GET /cards/{cardId}/cardholder` answers `404`, and `expand` on the card or its card subscription leaves the `cardholder` key out; for a transaction, see `expand` on `GET /transactions/{transactionId}`. In the sandbox, once a card's card subscriptions are deleted, the cardholder answers `404` too. [Cards](https://docs.astrada.co/docs/cards#cardholder) lists the fields and what each way of enrolling fills. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | 
**corporate** | [**CardholderCorporate**](CardholderCorporate.md) |  | 
**first_name** | **str** | The first name of the cardholder. When created for a card entered by number, every word of the &#x60;cardholderName&#x60; sent but the last; &#x60;null&#x60; when that name is one word. | [optional] 
**last_name** | **str** | The last name of the cardholder. When created for a card entered by number, the last word of the &#x60;cardholderName&#x60; sent. | [optional] 
**email** | **str** | Cardholder email address | [optional] 
**postal_code** | **str** | Cardholder postal code as provided by the card network. Format varies by country; no validation or normalization is applied. | [optional] 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.models.cardholder import Cardholder

# TODO update the JSON string below
json = "{}"
# create an instance of Cardholder from a JSON string
cardholder_instance = Cardholder.from_json(json)
# print the JSON string representation of the object
print(Cardholder.to_json())

# convert the object into a dict
cardholder_dict = cardholder_instance.to_dict()
# create an instance of Cardholder from a dict
cardholder_from_dict = Cardholder.from_dict(cardholder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


