# BankAccountLinks

HAL-style links to related resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**transactions** | [**Link**](Link.md) |  | 
**bank_link** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_account_links import BankAccountLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountLinks from a JSON string
bank_account_links_instance = BankAccountLinks.from_json(json)
# print the JSON string representation of the object
print(BankAccountLinks.to_json())

# convert the object into a dict
bank_account_links_dict = bank_account_links_instance.to_dict()
# create an instance of BankAccountLinks from a dict
bank_account_links_from_dict = BankAccountLinks.from_dict(bank_account_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


