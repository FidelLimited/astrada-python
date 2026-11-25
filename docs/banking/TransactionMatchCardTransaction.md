# TransactionMatchCardTransaction

Summary of the matched card transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | The card identifier associated with the matched card transaction. | [optional] 
**var_date** | **str** | The transaction date. | [optional] 
**amount** | **float** | The transaction amount. | [optional] 
**currency** | **str** | The transaction currency. | [optional] 
**descriptor** | **str** | The merchant descriptor. | [optional] 

## Example

```python
from astrada.banking.models.transaction_match_card_transaction import TransactionMatchCardTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMatchCardTransaction from a JSON string
transaction_match_card_transaction_instance = TransactionMatchCardTransaction.from_json(json)
# print the JSON string representation of the object
print(TransactionMatchCardTransaction.to_json())

# convert the object into a dict
transaction_match_card_transaction_dict = transaction_match_card_transaction_instance.to_dict()
# create an instance of TransactionMatchCardTransaction from a dict
transaction_match_card_transaction_from_dict = TransactionMatchCardTransaction.from_dict(transaction_match_card_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


