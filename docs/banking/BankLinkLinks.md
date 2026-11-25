# BankLinkLinks

HAL-style links to related resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**bank_accounts** | [**List[Link]**](Link.md) | Links to the bank accounts created from this link. Only present when state is &#x60;completed&#x60; and accounts exist. | [optional] 

## Example

```python
from astrada.banking.models.bank_link_links import BankLinkLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkLinks from a JSON string
bank_link_links_instance = BankLinkLinks.from_json(json)
# print the JSON string representation of the object
print(BankLinkLinks.to_json())

# convert the object into a dict
bank_link_links_dict = bank_link_links_instance.to_dict()
# create an instance of BankLinkLinks from a dict
bank_link_links_from_dict = BankLinkLinks.from_dict(bank_link_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


