# BankTransactionWebhooksParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of bank transaction identifiers to emit webhooks for. Must contain at least one ID. | 
**webhooks** | **List[str]** | The types of webhook events to emit. Leave it out and only &#x60;banktransaction.created&#x60; is sent. | [optional] 
**force_rematch** | **bool** | Set to &#x60;true&#x60; to re-run the matching algorithm for the named transactions before emitting webhooks. Transactions that already have a match are genuinely re-scored: the existing match id is preserved when the pairing survives, updated when a better pairing exists, and removed when the movement no longer matches. | [optional] [default to False]
**dispatch_unmatched** | **bool** | After the re-match, emit the standalone bank-only feed entry for each named transaction the matcher left unmatched (idempotent per transaction; already-emitted standalones are skipped). Requires &#x60;forceRematch: true&#x60; and &#x60;webhooks&#x60; to include &#x60;transaction.match.created&#x60;; the request is rejected with &#x60;400&#x60; otherwise, because only a same-run re-match can distinguish a genuinely unmatched movement from a duplicate of an already-settled purchase. | [optional] [default to False]

## Example

```python
from astrada.banking.models.bank_transaction_webhooks_params import BankTransactionWebhooksParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionWebhooksParams from a JSON string
bank_transaction_webhooks_params_instance = BankTransactionWebhooksParams.from_json(json)
# print the JSON string representation of the object
print(BankTransactionWebhooksParams.to_json())

# convert the object into a dict
bank_transaction_webhooks_params_dict = bank_transaction_webhooks_params_instance.to_dict()
# create an instance of BankTransactionWebhooksParams from a dict
bank_transaction_webhooks_params_from_dict = BankTransactionWebhooksParams.from_dict(bank_transaction_webhooks_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


