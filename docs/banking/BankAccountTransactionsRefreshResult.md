# BankAccountTransactionsRefreshResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The bank account identifier. | 
**requested_at** | **datetime** | When the check was requested. | 
**duration_ms** | **int** | How long the provider took to run the check. | 

## Example

```python
from astrada.banking.models.bank_account_transactions_refresh_result import BankAccountTransactionsRefreshResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountTransactionsRefreshResult from a JSON string
bank_account_transactions_refresh_result_instance = BankAccountTransactionsRefreshResult.from_json(json)
# print the JSON string representation of the object
print(BankAccountTransactionsRefreshResult.to_json())

# convert the object into a dict
bank_account_transactions_refresh_result_dict = bank_account_transactions_refresh_result_instance.to_dict()
# create an instance of BankAccountTransactionsRefreshResult from a dict
bank_account_transactions_refresh_result_from_dict = BankAccountTransactionsRefreshResult.from_dict(bank_account_transactions_refresh_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


