# RawTransactionMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**RawTransactionMessageLinks**](RawTransactionMessageLinks.md) |  | 
**raw** | **object** | The raw payload from the network that originated the underlying transaction message (will vary by network and message). | 

## Example

```python
from astrada.models.raw_transaction_message import RawTransactionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of RawTransactionMessage from a JSON string
raw_transaction_message_instance = RawTransactionMessage.from_json(json)
# print the JSON string representation of the object
print(RawTransactionMessage.to_json())

# convert the object into a dict
raw_transaction_message_dict = raw_transaction_message_instance.to_dict()
# create an instance of RawTransactionMessage from a dict
raw_transaction_message_from_dict = RawTransactionMessage.from_dict(raw_transaction_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


