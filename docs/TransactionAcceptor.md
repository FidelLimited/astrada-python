# TransactionAcceptor

The details relating to the acceptor (merchant) from the latest transaction message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | The acceptor&#39;s registered city. Defined by the acquirer/processor. | 
**country** | **str** | The acceptor&#39;s registered country following ISO 3166 alpha-3. | 
**mcc** | **str** | The Merchant Category Code provided by the acquirer/processor. Used to classify businesses by the types of goods provided or services rendered. | 
**state** | **str** | The acceptor&#39;s registered state (e.g. Michigan) as assigned by the acquirer/processor. | 

## Example

```python
from astrada.models.transaction_acceptor import TransactionAcceptor

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionAcceptor from a JSON string
transaction_acceptor_instance = TransactionAcceptor.from_json(json)
# print the JSON string representation of the object
print(TransactionAcceptor.to_json())

# convert the object into a dict
transaction_acceptor_dict = transaction_acceptor_instance.to_dict()
# create an instance of TransactionAcceptor from a dict
transaction_acceptor_from_dict = TransactionAcceptor.from_dict(transaction_acceptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


