# BankTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**BankTransactionLinks**](BankTransactionLinks.md) |  | 
**id** | **str** | The unique identifier of the bank transaction. | 
**account_id** | **str** | The unique identifier of the account that owns this transaction. | 
**subaccount_id** | **str** | The unique identifier of the subaccount associated with this transaction. | 
**bank_account_id** | **str** | The unique identifier of the bank account this transaction belongs to. | 
**card_id** | **str** | The card whose card transaction this bank transaction is matched to. Stamped when a match is persisted and cleared if a later forced rematch supersedes that match, so it is only ever non-null alongside &#x60;matchId&#x60;. Null while unmatched, including on accounts with linked cards: linking alone never attributes individual bank transactions.  | 
**match_id** | **str** | The identifier of the transaction match, if this bank transaction has been matched to a card transaction. | 
**var_date** | **date** | The date the transaction was posted, in YYYY-MM-DD format. | 
**amount** | **float** | The transaction amount. | 
**currency** | **str** | The currency of the transaction following ISO 4217 format. | 
**description** | **str** | The transaction description provided by the financial institution. | 
**merchant_name** | **str** | The name of the merchant. | 
**category** | **List[str]** | The transaction categories assigned by the provider. | 
**transaction_type** | **str** | The type of transaction. - &#x60;debit&#x60;: Money sent (outflow). - &#x60;credit&#x60;: Money received (inflow).  | 
**source** | **str** | The source of this transaction. - &#x60;PLAID&#x60;: Synced from a connected financial institution via Plaid. - &#x60;UPLOAD&#x60;: Imported from a manually uploaded bank statement. - &#x60;MASTERCARD_US&#x60;: Synced from a connected financial institution via Mastercard Open Finance US. Sandbox only. - &#x60;MASTERCARD_EU&#x60;: Synced from a connected financial institution via Mastercard Open Finance Europe. Sandbox only.  | 
**status** | **str** | The lifecycle stage of the bank movement, derived from its match pointer and settlement state. - &#x60;posted&#x60;: Synced, not yet matched. - &#x60;matched&#x60;: Paired to a card transaction without an early settlement of its own (e.g. connector off, or a below-HIGH match): the movement is represented by the card transaction&#39;s network settlement, and any standalone it previously emitted is netted to zero. - &#x60;settled&#x60;: A bank-only movement settled standalone on the unified feed. - &#x60;early_cleared&#x60;: A matched movement settled its card transaction early. - &#x60;superseded&#x60;: A previously bank-only movement was retracted or corrected.  | 
**settlement** | [**BankTransactionSettlement**](BankTransactionSettlement.md) |  | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.banking.models.bank_transaction import BankTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransaction from a JSON string
bank_transaction_instance = BankTransaction.from_json(json)
# print the JSON string representation of the object
print(BankTransaction.to_json())

# convert the object into a dict
bank_transaction_dict = bank_transaction_instance.to_dict()
# create an instance of BankTransaction from a dict
bank_transaction_from_dict = BankTransaction.from_dict(bank_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


