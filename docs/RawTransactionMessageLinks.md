# RawTransactionMessageLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**message** | [**Link**](Link.md) |  | 

## Example

```python
from astrada.models.raw_transaction_message_links import RawTransactionMessageLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RawTransactionMessageLinks from a JSON string
raw_transaction_message_links_instance = RawTransactionMessageLinks.from_json(json)
# print the JSON string representation of the object
print(RawTransactionMessageLinks.to_json())

# convert the object into a dict
raw_transaction_message_links_dict = raw_transaction_message_links_instance.to_dict()
# create an instance of RawTransactionMessageLinks from a dict
raw_transaction_message_links_from_dict = RawTransactionMessageLinks.from_dict(raw_transaction_message_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


