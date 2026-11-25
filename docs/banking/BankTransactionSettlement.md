# BankTransactionSettlement

Settlement outcome on the unified transaction feed. Present when the movement has settled live; null otherwise (unmatched, connector off, or shadow-only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**emission_type** | **str** |  | 
**emitted_at** | **datetime** | When the settlement was emitted to the feed. | 
**superseded_at** | **datetime** | When the settlement was superseded or corrected, if applicable. | 

## Example

```python
from astrada.banking.models.bank_transaction_settlement import BankTransactionSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionSettlement from a JSON string
bank_transaction_settlement_instance = BankTransactionSettlement.from_json(json)
# print the JSON string representation of the object
print(BankTransactionSettlement.to_json())

# convert the object into a dict
bank_transaction_settlement_dict = bank_transaction_settlement_instance.to_dict()
# create an instance of BankTransactionSettlement from a dict
bank_transaction_settlement_from_dict = BankTransactionSettlement.from_dict(bank_transaction_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


