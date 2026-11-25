# BankTransactionWebhooksResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable summary of the operation. | 
**emitted** | **int** | Number of webhook events emitted. | 
**resent** | **int** | Number of webhooks resent. | 
**matched** | **int** | Number of transactions that were matched. | 
**skipped** | **int** | Number of transactions that were skipped. | 
**failed** | [**List[BankTransactionWebhookFailure]**](BankTransactionWebhookFailure.md) | Transactions that failed to process. | 
**dispatched** | **int** | Number of standalone bank-only emissions dispatched for still-unmatched transactions. Only present when &#x60;dispatchUnmatched&#x60; was requested (and on service versions that support the flag). | [optional] 
**dispatch_error** | **str** | Present when the standalone dispatch step failed after a successful re-match; the matching results above still stand. | [optional] 

## Example

```python
from astrada.banking.models.bank_transaction_webhooks_result import BankTransactionWebhooksResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionWebhooksResult from a JSON string
bank_transaction_webhooks_result_instance = BankTransactionWebhooksResult.from_json(json)
# print the JSON string representation of the object
print(BankTransactionWebhooksResult.to_json())

# convert the object into a dict
bank_transaction_webhooks_result_dict = bank_transaction_webhooks_result_instance.to_dict()
# create an instance of BankTransactionWebhooksResult from a dict
bank_transaction_webhooks_result_from_dict = BankTransactionWebhooksResult.from_dict(bank_transaction_webhooks_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


