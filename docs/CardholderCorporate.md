# CardholderCorporate

The company the cardholder belongs to, as the bank or card network supplies it in a network bulk feed, unless it was set with `PATCH /cards/{cardId}/cardholder`. See the [Glossary](https://docs.astrada.co/docs/glossary) for the terms used here.  On `GET /cards/{cardId}/cardholder` this is the current value. When the cardholder is embedded on a transaction (`expand=cardholder`, or the transaction webhooks), `corporate` is the value in effect on the transaction's `transactionOccurrenceDate` (through the end of that UTC day), or at the transaction's `createdAt` when that is null; the other cardholder fields stay current. The one exception inside `corporate` is `networkToken`, which is always the card's current value. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_employee_id** | **str** | An alternative employee identifier, typically configured for specific enterprise integrations. | [optional] 
**employee_id** | **str** | The unique identifier of the employee | [optional] 
**id** | **str** | The **company ID**: the identifier the bank or card network gives the cardholder&#39;s company in the network bulk feed. Every card from the same company carries the same value, so it is the field to group cards by company.  - **Visa (VCF and VBDS)**: the company ID, the &#x60;C&#x60; in the feed&#39;s RPIC network reference (&#x60;RegionId_ProcessorId_IssuerId_CompanyId&#x60;), always its last segment. For the feed &#x60;1_123_45_6789&#x60; (or the VCF PIC form &#x60;123_45_6789&#x60;), &#x60;corporate.id&#x60; is &#x60;6789&#x60;. - **Mastercard (SmartData)**: the company ID from the file, which Mastercard calls the corporation number. - **American Express**: the company ID, the 6-digit corporate ID (CID), such as &#x60;014640&#x60;. For a feed whose network reference is the CID, &#x60;corporate.id&#x60; is that same value.  &#x60;null&#x60; when the feed does not supply one. The legal entity within the company is in &#x60;legalEntity&#x60;.  | [optional] 
**legal_entity** | [**CardholderCorporateLegalEntity**](CardholderCorporateLegalEntity.md) |  | [optional] 
**network_token** | **str** | The network token the card network issued for the card, for a tokenized American Express card. It is the same token the network sends you in its own files, so it is a stable identifier for matching the cardholder to your records. On these cards the card&#39;s &#x60;first6digits&#x60; and &#x60;last4digits&#x60; are the token&#39;s digits, not the physical card&#39;s. Present only for tokenized American Express cards; absent otherwise, never null. Always the card&#39;s current value, also when the cardholder is embedded on a transaction. | [optional] [readonly] 

## Example

```python
from astrada.models.cardholder_corporate import CardholderCorporate

# TODO update the JSON string below
json = "{}"
# create an instance of CardholderCorporate from a JSON string
cardholder_corporate_instance = CardholderCorporate.from_json(json)
# print the JSON string representation of the object
print(CardholderCorporate.to_json())

# convert the object into a dict
cardholder_corporate_dict = cardholder_corporate_instance.to_dict()
# create an instance of CardholderCorporate from a dict
cardholder_corporate_from_dict = CardholderCorporate.from_dict(cardholder_corporate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


