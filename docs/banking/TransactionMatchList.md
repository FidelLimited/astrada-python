# TransactionMatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TransactionMatch]**](TransactionMatch.md) |  | 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | 

## Example

```python
from astrada.banking.models.transaction_match_list import TransactionMatchList

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMatchList from a JSON string
transaction_match_list_instance = TransactionMatchList.from_json(json)
# print the JSON string representation of the object
print(TransactionMatchList.to_json())

# convert the object into a dict
transaction_match_list_dict = transaction_match_list_instance.to_dict()
# create an instance of TransactionMatchList from a dict
transaction_match_list_from_dict = TransactionMatchList.from_dict(transaction_match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


