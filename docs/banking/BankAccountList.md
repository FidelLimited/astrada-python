# BankAccountList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BankAccount]**](BankAccount.md) |  | 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | 

## Example

```python
from astrada.banking.models.bank_account_list import BankAccountList

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountList from a JSON string
bank_account_list_instance = BankAccountList.from_json(json)
# print the JSON string representation of the object
print(BankAccountList.to_json())

# convert the object into a dict
bank_account_list_dict = bank_account_list_instance.to_dict()
# create an instance of BankAccountList from a dict
bank_account_list_from_dict = BankAccountList.from_dict(bank_account_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


