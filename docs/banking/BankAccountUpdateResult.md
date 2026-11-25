# BankAccountUpdateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The bank account identifier. | 
**card_ids** | **List[str]** | The linked card identifiers. | 
**state** | **str** | The current state of the bank account. | 
**updated_at** | **datetime** | When the bank account was last updated. | 
**backfill** | [**BankAccountUpdateResultBackfill**](BankAccountUpdateResultBackfill.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_account_update_result import BankAccountUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountUpdateResult from a JSON string
bank_account_update_result_instance = BankAccountUpdateResult.from_json(json)
# print the JSON string representation of the object
print(BankAccountUpdateResult.to_json())

# convert the object into a dict
bank_account_update_result_dict = bank_account_update_result_instance.to_dict()
# create an instance of BankAccountUpdateResult from a dict
bank_account_update_result_from_dict = BankAccountUpdateResult.from_dict(bank_account_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


