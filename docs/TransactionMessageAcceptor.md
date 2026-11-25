# TransactionMessageAcceptor

The details relating to the acceptor (merchant) that initiated the transaction message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirer_id** | **str** | The identifier of the acquirer/processor used by the acceptor as assigned by the network. | 
**city** | **str** | The acceptor&#39;s registered city. Defined by the acquirer/processor. | 
**country** | **str** | The acceptor&#39;s registered country following ISO 3166 alpha-3. | [optional] 
**id** | **str** | The identifier of the payment acceptor (merchant) as assigned by the acquirer/processor. | 
**mcc** | **str** | The Merchant Category Code provided by the acquirer/processor. Used to classify businesses by the types of goods provided or services rendered. | 
**name** | **str** | The acceptor (merchant) name. | 
**state** | **str** | The acceptor&#39;s registered state (e.g. Michigan) as assigned by the acquirer/processor. | 

## Example

```python
from astrada.models.transaction_message_acceptor import TransactionMessageAcceptor

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageAcceptor from a JSON string
transaction_message_acceptor_instance = TransactionMessageAcceptor.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageAcceptor.to_json())

# convert the object into a dict
transaction_message_acceptor_dict = transaction_message_acceptor_instance.to_dict()
# create an instance of TransactionMessageAcceptor from a dict
transaction_message_acceptor_from_dict = TransactionMessageAcceptor.from_dict(transaction_message_acceptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


