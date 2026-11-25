# TransactionListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[Transaction]**](Transaction.md) |  | 

## Example

```python
from astrada.models.transaction_list_embedded import TransactionListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionListEmbedded from a JSON string
transaction_list_embedded_instance = TransactionListEmbedded.from_json(json)
# print the JSON string representation of the object
print(TransactionListEmbedded.to_json())

# convert the object into a dict
transaction_list_embedded_dict = transaction_list_embedded_instance.to_dict()
# create an instance of TransactionListEmbedded from a dict
transaction_list_embedded_from_dict = TransactionListEmbedded.from_dict(transaction_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


