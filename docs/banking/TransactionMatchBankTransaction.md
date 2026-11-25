# TransactionMatchBankTransaction

Summary of the matched bank transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | The transaction date. | [optional] 
**amount** | **float** | The transaction amount. | [optional] 
**currency** | **str** | The transaction currency. | [optional] 
**description** | **str** | The transaction description. | [optional] 
**merchant_name** | **str** | The merchant name. | [optional] 

## Example

```python
from astrada.banking.models.transaction_match_bank_transaction import TransactionMatchBankTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMatchBankTransaction from a JSON string
transaction_match_bank_transaction_instance = TransactionMatchBankTransaction.from_json(json)
# print the JSON string representation of the object
print(TransactionMatchBankTransaction.to_json())

# convert the object into a dict
transaction_match_bank_transaction_dict = transaction_match_bank_transaction_instance.to_dict()
# create an instance of TransactionMatchBankTransaction from a dict
transaction_match_bank_transaction_from_dict = TransactionMatchBankTransaction.from_dict(transaction_match_bank_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


