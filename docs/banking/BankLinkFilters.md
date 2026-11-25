# BankLinkFilters

The account filtering actually applied to this link, after resolution against the account's bank-linking policy. Echoes what the hosted session will offer; absent on links created before filtering existed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | **List[str]** | Account types selectable in the hosted session. | [optional] 
**link_customization_name** | **str** | The Plaid Link customization this link asked for: the request&#39;s &#x60;filters.linkCustomizationName&#x60;, or else the bank-linking policy&#39;s &#x60;plaidLinkCustomizationName&#x60;. Absent when neither applies. When Plaid refused &#x60;amex_only&#x60; and the create was retried without it, this still reads &#x60;amex_only&#x60;, and the link&#39;s completion is still held to American Express institutions.  | [optional] 

## Example

```python
from astrada.banking.models.bank_link_filters import BankLinkFilters

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkFilters from a JSON string
bank_link_filters_instance = BankLinkFilters.from_json(json)
# print the JSON string representation of the object
print(BankLinkFilters.to_json())

# convert the object into a dict
bank_link_filters_dict = bank_link_filters_instance.to_dict()
# create an instance of BankLinkFilters from a dict
bank_link_filters_from_dict = BankLinkFilters.from_dict(bank_link_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


