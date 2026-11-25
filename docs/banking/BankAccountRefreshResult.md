# BankAccountRefreshResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The bank account identifier. | 
**hosted_link** | **str** | A hosted URL for the user to complete re-authentication. | 
**expires_at** | **datetime** | When the hosted link expires. | 

## Example

```python
from astrada.banking.models.bank_account_refresh_result import BankAccountRefreshResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountRefreshResult from a JSON string
bank_account_refresh_result_instance = BankAccountRefreshResult.from_json(json)
# print the JSON string representation of the object
print(BankAccountRefreshResult.to_json())

# convert the object into a dict
bank_account_refresh_result_dict = bank_account_refresh_result_instance.to_dict()
# create an instance of BankAccountRefreshResult from a dict
bank_account_refresh_result_from_dict = BankAccountRefreshResult.from_dict(bank_account_refresh_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


