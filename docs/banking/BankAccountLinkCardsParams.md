# BankAccountLinkCardsParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaccount_id** | **str** | The subaccount whose enrolled cards and bank accounts to match. | 

## Example

```python
from astrada.banking.models.bank_account_link_cards_params import BankAccountLinkCardsParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountLinkCardsParams from a JSON string
bank_account_link_cards_params_instance = BankAccountLinkCardsParams.from_json(json)
# print the JSON string representation of the object
print(BankAccountLinkCardsParams.to_json())

# convert the object into a dict
bank_account_link_cards_params_dict = bank_account_link_cards_params_instance.to_dict()
# create an instance of BankAccountLinkCardsParams from a dict
bank_account_link_cards_params_from_dict = BankAccountLinkCardsParams.from_dict(bank_account_link_cards_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


