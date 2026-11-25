# BankTransactionLinks

HAL-style links to related resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**bank_account** | [**Link**](Link.md) |  | 
**card** | [**Link**](Link.md) |  | [optional] 
**match** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_transaction_links import BankTransactionLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionLinks from a JSON string
bank_transaction_links_instance = BankTransactionLinks.from_json(json)
# print the JSON string representation of the object
print(BankTransactionLinks.to_json())

# convert the object into a dict
bank_transaction_links_dict = bank_transaction_links_instance.to_dict()
# create an instance of BankTransactionLinks from a dict
bank_transaction_links_from_dict = BankTransactionLinks.from_dict(bank_transaction_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


