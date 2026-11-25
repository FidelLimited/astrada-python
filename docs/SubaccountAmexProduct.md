# SubaccountAmexProduct

The American Express data Astrada has turned on for your account, the same on every subaccount. Only Astrada sets it; `null` means neither is on. `clearing` is transactions from American Express's card file; `realTimeAuth` is American Express authorizations as they happen (US only, by approval). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clearing** | [**SubaccountAmexProductClearing**](SubaccountAmexProductClearing.md) |  | [optional] 
**real_time_auth** | [**SubaccountAmexProductRealTimeAuth**](SubaccountAmexProductRealTimeAuth.md) |  | [optional] 

## Example

```python
from astrada.models.subaccount_amex_product import SubaccountAmexProduct

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountAmexProduct from a JSON string
subaccount_amex_product_instance = SubaccountAmexProduct.from_json(json)
# print the JSON string representation of the object
print(SubaccountAmexProduct.to_json())

# convert the object into a dict
subaccount_amex_product_dict = subaccount_amex_product_instance.to_dict()
# create an instance of SubaccountAmexProduct from a dict
subaccount_amex_product_from_dict = SubaccountAmexProduct.from_dict(subaccount_amex_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


