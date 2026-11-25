# TransactionMatchReason

One scoring factor of a match and what it added to the score.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The matching factor type. | [optional] 
**score** | **float** | The individual score for this factor. | [optional] 
**card_value** | **str** | The value from the card transaction used for comparison. May be a string or numeric value. | [optional] 
**bank_value** | **str** | The value from the bank transaction used for comparison. May be a string or numeric value. | [optional] 
**diff** | **float** | The numeric difference between the card and bank values. | [optional] 
**message** | **str** | Human-readable explanation of the score for this factor. | [optional] 

## Example

```python
from astrada.banking.models.transaction_match_reason import TransactionMatchReason

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMatchReason from a JSON string
transaction_match_reason_instance = TransactionMatchReason.from_json(json)
# print the JSON string representation of the object
print(TransactionMatchReason.to_json())

# convert the object into a dict
transaction_match_reason_dict = transaction_match_reason_instance.to_dict()
# create an instance of TransactionMatchReason from a dict
transaction_match_reason_from_dict = TransactionMatchReason.from_dict(transaction_match_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


