# TransactionMessageBankDataPersonalFinanceCategory

Provider categorization of the bank transaction; the one bank-only datum with no card-side equivalent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary category (e.g. FOOD_AND_DRINK). | [optional] 
**detailed** | **str** | Detailed category (e.g. FOOD_AND_DRINK_RESTAURANT). | [optional] 

## Example

```python
from astrada.models.transaction_message_bank_data_personal_finance_category import TransactionMessageBankDataPersonalFinanceCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageBankDataPersonalFinanceCategory from a JSON string
transaction_message_bank_data_personal_finance_category_instance = TransactionMessageBankDataPersonalFinanceCategory.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageBankDataPersonalFinanceCategory.to_json())

# convert the object into a dict
transaction_message_bank_data_personal_finance_category_dict = transaction_message_bank_data_personal_finance_category_instance.to_dict()
# create an instance of TransactionMessageBankDataPersonalFinanceCategory from a dict
transaction_message_bank_data_personal_finance_category_from_dict = TransactionMessageBankDataPersonalFinanceCategory.from_dict(transaction_message_bank_data_personal_finance_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


