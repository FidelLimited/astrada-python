# BankTransactionWebhookFailure

A transaction that failed to process, with why.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The transaction identifier that failed. | [optional] 
**error** | **str** | The error message describing why processing failed. | [optional] 

## Example

```python
from astrada.banking.models.bank_transaction_webhook_failure import BankTransactionWebhookFailure

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionWebhookFailure from a JSON string
bank_transaction_webhook_failure_instance = BankTransactionWebhookFailure.from_json(json)
# print the JSON string representation of the object
print(BankTransactionWebhookFailure.to_json())

# convert the object into a dict
bank_transaction_webhook_failure_dict = bank_transaction_webhook_failure_instance.to_dict()
# create an instance of BankTransactionWebhookFailure from a dict
bank_transaction_webhook_failure_from_dict = BankTransactionWebhookFailure.from_dict(bank_transaction_webhook_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


