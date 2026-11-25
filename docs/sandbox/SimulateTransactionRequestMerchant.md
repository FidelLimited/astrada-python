# SimulateTransactionRequestMerchant

The merchant (card acceptor) on the message. Defaults to a fixed sandbox coffee-shop merchant in the United States. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Merchant name, emitted as the transaction descriptor. | 
**mcc** | **str** | Four-digit merchant category code. | 
**city** | **str** | Merchant city. | [optional] 
**country** | **str** | Merchant country as an ISO 3166-1 alpha-3 code (for example &#x60;USA&#x60;, &#x60;GBR&#x60;, &#x60;FRA&#x60;), case insensitive; any other value is rejected with &#x60;400&#x60;. Defaults to &#x60;USA&#x60;.  | [optional] 

## Example

```python
from astrada.sandbox.models.simulate_transaction_request_merchant import SimulateTransactionRequestMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateTransactionRequestMerchant from a JSON string
simulate_transaction_request_merchant_instance = SimulateTransactionRequestMerchant.from_json(json)
# print the JSON string representation of the object
print(SimulateTransactionRequestMerchant.to_json())

# convert the object into a dict
simulate_transaction_request_merchant_dict = simulate_transaction_request_merchant_instance.to_dict()
# create an instance of SimulateTransactionRequestMerchant from a dict
simulate_transaction_request_merchant_from_dict = SimulateTransactionRequestMerchant.from_dict(simulate_transaction_request_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


