# TransactionMessageBankData

Bank-side provenance, present only on bank-sourced messages (null otherwise). Deliberately slim; the bank's merchant string, dates and amounts map into the canonical fields above; `bankTransactionId` is the stable join key back to the bank feed. It equals `banktransaction.created.id` and `transaction.match.created.matches[].id`, and resolves via `GET /bank-transactions/{id}` for the full bank record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Open banking provider that observed the bank transaction. &#x60;mastercard-open-finance&#x60; appears once the Mastercard rail is enabled for the subaccount; the payload shape is identical across providers. | 
**bank_transaction_id** | **str** | The bank transaction entity id; the canonical, lifecycle-stable join key across every bank-data surface. | 
**personal_finance_category** | [**TransactionMessageBankDataPersonalFinanceCategory**](TransactionMessageBankDataPersonalFinanceCategory.md) |  | [optional] 

## Example

```python
from astrada.models.transaction_message_bank_data import TransactionMessageBankData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMessageBankData from a JSON string
transaction_message_bank_data_instance = TransactionMessageBankData.from_json(json)
# print the JSON string representation of the object
print(TransactionMessageBankData.to_json())

# convert the object into a dict
transaction_message_bank_data_dict = transaction_message_bank_data_instance.to_dict()
# create an instance of TransactionMessageBankData from a dict
transaction_message_bank_data_from_dict = TransactionMessageBankData.from_dict(transaction_message_bank_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


