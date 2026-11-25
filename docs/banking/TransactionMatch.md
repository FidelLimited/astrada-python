# TransactionMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**TransactionMatchLinks**](TransactionMatchLinks.md) |  | 
**id** | **str** | The unique identifier of the transaction match. | 
**account_id** | **str** | The unique identifier of the account that owns this match. | 
**subaccount_id** | **str** | The unique identifier of the subaccount associated with this match. | 
**card_transaction_id** | **str** | The identifier of the matched card transaction message (the message the bank posting was matched against, for example the authorization). It is the &#x60;id&#x60; carried by &#x60;transactionmessage.created&#x60; and appears in &#x60;_embedded.messages[].id&#x60; on the unified transaction; it is not the unified transaction&#39;s own &#x60;id&#x60;. | 
**bank_transaction_id** | **str** | The unique identifier of the matched bank transaction. | 
**confidence** | **str** | The confidence level of the match. - &#x60;HIGH&#x60;: Score &gt;&#x3D; 0.70 - &#x60;MEDIUM&#x60;: Score &gt;&#x3D; 0.50 - &#x60;LOW&#x60;: Score &gt;&#x3D; 0.20  | 
**score** | **float** | The numeric match score between 0 and 1, representing how closely the bank and card transactions match. | 
**card_transaction** | [**TransactionMatchCardTransaction**](TransactionMatchCardTransaction.md) |  | 
**bank_transaction** | [**TransactionMatchBankTransaction**](TransactionMatchBankTransaction.md) |  | 
**reasons** | [**List[TransactionMatchReason]**](TransactionMatchReason.md) | Breakdown of the scoring factors that contributed to the match score. | 
**created_at** | **datetime** | Date and time when this match was created, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.banking.models.transaction_match import TransactionMatch

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMatch from a JSON string
transaction_match_instance = TransactionMatch.from_json(json)
# print the JSON string representation of the object
print(TransactionMatch.to_json())

# convert the object into a dict
transaction_match_dict = transaction_match_instance.to_dict()
# create an instance of TransactionMatch from a dict
transaction_match_from_dict = TransactionMatch.from_dict(transaction_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


