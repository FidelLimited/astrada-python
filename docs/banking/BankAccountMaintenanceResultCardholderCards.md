# BankAccountMaintenanceResultCardholderCards

Present only when `createCardholderCards: true` was sent. Counts only; no cardholder name is ever returned. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | False when card creation is not switched on for the subaccount; nothing was created. | 
**route_enabled** | **bool** | True when each cardholder&#39;s transactions are emitted on their own card. | 
**accounts** | **int** | Pooled American Express billing accounts served. | 
**suffixes_seen** | **int** | Distinct cardholders (by the card&#39;s last 4) seen in those accounts&#39; transactions. | 
**created** | **int** | Cardholder cards created in this run. | 
**linked_enrolled** | **int** | Cards the cardholder had already enrolled, linked instead of creating one. | 
**named** | **int** | Cards whose cardholder name was written in this run. | 
**relinked** | **int** | Cardholder cards found on another bank account of the subaccount after a re-link, left where they are and counted (the background re-home moves them). | 
**failed** | **int** | Cards that could not be created this run; the next run tries again. | 
**skipped** | **Dict[str, int]** | Reason -&gt; count of cardholders given no card of their own (their transactions stay on the account&#39;s main card). Reasons: &#x60;no_primary&#x60;, &#x60;ambiguous_primary&#x60;, &#x60;bulk_owned&#x60;, &#x60;ambiguous_enrolled&#x60;, and the permanent &#x60;deactivated&#x60;, &#x60;not_active&#x60;, &#x60;unlinked&#x60; and &#x60;foreign_reuse&#x60;. Only reasons with a count appear.  | 
**directory_unavailable** | **bool** | True when this action&#39;s own read of the cards directory failed; no card was created this run. | 

## Example

```python
from astrada.banking.models.bank_account_maintenance_result_cardholder_cards import BankAccountMaintenanceResultCardholderCards

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountMaintenanceResultCardholderCards from a JSON string
bank_account_maintenance_result_cardholder_cards_instance = BankAccountMaintenanceResultCardholderCards.from_json(json)
# print the JSON string representation of the object
print(BankAccountMaintenanceResultCardholderCards.to_json())

# convert the object into a dict
bank_account_maintenance_result_cardholder_cards_dict = bank_account_maintenance_result_cardholder_cards_instance.to_dict()
# create an instance of BankAccountMaintenanceResultCardholderCards from a dict
bank_account_maintenance_result_cardholder_cards_from_dict = BankAccountMaintenanceResultCardholderCards.from_dict(bank_account_maintenance_result_cardholder_cards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


