# BankLinkUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The target state for the bank link. Only &#x60;completed&#x60; is accepted. | 
**consent** | [**BankLinkConsent**](BankLinkConsent.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_link_update_params import BankLinkUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkUpdateParams from a JSON string
bank_link_update_params_instance = BankLinkUpdateParams.from_json(json)
# print the JSON string representation of the object
print(BankLinkUpdateParams.to_json())

# convert the object into a dict
bank_link_update_params_dict = bank_link_update_params_instance.to_dict()
# create an instance of BankLinkUpdateParams from a dict
bank_link_update_params_from_dict = BankLinkUpdateParams.from_dict(bank_link_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


