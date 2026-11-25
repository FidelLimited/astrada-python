# BankAccountLinkCardsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked** | **Dict[str, List[str]]** | bankAccountId -&gt; cardIds linked in THIS run. | 

## Example

```python
from astrada.banking.models.bank_account_link_cards_result import BankAccountLinkCardsResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountLinkCardsResult from a JSON string
bank_account_link_cards_result_instance = BankAccountLinkCardsResult.from_json(json)
# print the JSON string representation of the object
print(BankAccountLinkCardsResult.to_json())

# convert the object into a dict
bank_account_link_cards_result_dict = bank_account_link_cards_result_instance.to_dict()
# create an instance of BankAccountLinkCardsResult from a dict
bank_account_link_cards_result_from_dict = BankAccountLinkCardsResult.from_dict(bank_account_link_cards_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


