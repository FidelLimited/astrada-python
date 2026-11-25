# BankAccountUpdateResultBackfill

The result of the backfill, when the request asked for one and added at least one card. If fetching history from the bank data provider fails, matching still runs on the bank transactions already stored, and this object is returned with counts for those. It is left out when a later step fails (reading the stored or card transactions, or matching); the update itself still stands. The fields mean the same as on `POST /bank-accounts/{bankAccountId}/backfill`, except that matching here only looks for the cards this request added. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions_processed** | **int** | Unmatched bank transactions in the window that matching looked at, whether imported by this call or already stored. | [optional] 
**matches_found** | **int** | Matches found against the cards this request added. | [optional] 

## Example

```python
from astrada.banking.models.bank_account_update_result_backfill import BankAccountUpdateResultBackfill

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountUpdateResultBackfill from a JSON string
bank_account_update_result_backfill_instance = BankAccountUpdateResultBackfill.from_json(json)
# print the JSON string representation of the object
print(BankAccountUpdateResultBackfill.to_json())

# convert the object into a dict
bank_account_update_result_backfill_dict = bank_account_update_result_backfill_instance.to_dict()
# create an instance of BankAccountUpdateResultBackfill from a dict
bank_account_update_result_backfill_from_dict = BankAccountUpdateResultBackfill.from_dict(bank_account_update_result_backfill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


