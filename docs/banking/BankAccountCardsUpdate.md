# BankAccountCardsUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_ids** | **List[str]** | The identifiers of cards to link to this bank account for transaction matching. Send an empty array to unlink all cards. Each card must belong to the same subaccount. | 
**backfill** | [**BankAccountCardsUpdateBackfill**](BankAccountCardsUpdateBackfill.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_account_cards_update import BankAccountCardsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountCardsUpdate from a JSON string
bank_account_cards_update_instance = BankAccountCardsUpdate.from_json(json)
# print the JSON string representation of the object
print(BankAccountCardsUpdate.to_json())

# convert the object into a dict
bank_account_cards_update_dict = bank_account_cards_update_instance.to_dict()
# create an instance of BankAccountCardsUpdate from a dict
bank_account_cards_update_from_dict = BankAccountCardsUpdate.from_dict(bank_account_cards_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


