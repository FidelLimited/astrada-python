# BankAccountBackfillResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The bank account identifier. | 
**transactions_processed** | **int** | Unmatched bank transactions in the window that matching looked at, whether imported by this call or already stored. | 
**matches_found** | **int** | Matches found against the account&#39;s linked cards during the backfill. | 

## Example

```python
from astrada.banking.models.bank_account_backfill_result import BankAccountBackfillResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountBackfillResult from a JSON string
bank_account_backfill_result_instance = BankAccountBackfillResult.from_json(json)
# print the JSON string representation of the object
print(BankAccountBackfillResult.to_json())

# convert the object into a dict
bank_account_backfill_result_dict = bank_account_backfill_result_instance.to_dict()
# create an instance of BankAccountBackfillResult from a dict
bank_account_backfill_result_from_dict = BankAccountBackfillResult.from_dict(bank_account_backfill_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


