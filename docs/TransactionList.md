# TransactionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PageLinks**](PageLinks.md) |  | 
**embedded** | [**TransactionListEmbedded**](TransactionListEmbedded.md) |  | 

## Example

```python
from astrada.models.transaction_list import TransactionList

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionList from a JSON string
transaction_list_instance = TransactionList.from_json(json)
# print the JSON string representation of the object
print(TransactionList.to_json())

# convert the object into a dict
transaction_list_dict = transaction_list_instance.to_dict()
# create an instance of TransactionList from a dict
transaction_list_from_dict = TransactionList.from_dict(transaction_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


