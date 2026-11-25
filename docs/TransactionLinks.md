# TransactionLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[Link]**](Link.md) |  | 
**card** | [**Link**](Link.md) |  | [optional] 
**var_self** | [**Link**](Link.md) |  | [optional] 
**subaccount** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.models.transaction_links import TransactionLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionLinks from a JSON string
transaction_links_instance = TransactionLinks.from_json(json)
# print the JSON string representation of the object
print(TransactionLinks.to_json())

# convert the object into a dict
transaction_links_dict = transaction_links_instance.to_dict()
# create an instance of TransactionLinks from a dict
transaction_links_from_dict = TransactionLinks.from_dict(transaction_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


