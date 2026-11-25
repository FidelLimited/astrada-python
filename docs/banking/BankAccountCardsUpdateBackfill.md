# BankAccountCardsUpdateBackfill

Optional backfill configuration to import historical bank transactions for the linked card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date for the backfill range in YYYY-MM-DD format. | [optional] 
**end_date** | **date** | End date for the backfill range in YYYY-MM-DD format. | [optional] 

## Example

```python
from astrada.banking.models.bank_account_cards_update_backfill import BankAccountCardsUpdateBackfill

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCardsUpdateBackfill from a JSON string
bank_account_cards_update_backfill_instance = BankAccountCardsUpdateBackfill.from_json(json)
# print the JSON string representation of the object
print(BankAccountCardsUpdateBackfill.to_json())

# convert the object into a dict
bank_account_cards_update_backfill_dict = bank_account_cards_update_backfill_instance.to_dict()
# create an instance of BankAccountCardsUpdateBackfill from a dict
bank_account_cards_update_backfill_from_dict = BankAccountCardsUpdateBackfill.from_dict(bank_account_cards_update_backfill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


