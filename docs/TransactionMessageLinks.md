# TransactionMessageLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**raw** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.models.transaction_message_links import TransactionMessageLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageLinks from a JSON string
transaction_message_links_instance = TransactionMessageLinks.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageLinks.to_json())

# convert the object into a dict
transaction_message_links_dict = transaction_message_links_instance.to_dict()
# create an instance of TransactionMessageLinks from a dict
transaction_message_links_from_dict = TransactionMessageLinks.from_dict(transaction_message_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


