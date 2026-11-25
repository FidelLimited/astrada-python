# BankAccountBackfillParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start of the range in YYYY-MM-DD format. Defaults to 90 days before &#x60;endDate&#x60;. | [optional] 
**end_date** | **date** | End of the range in YYYY-MM-DD format. Defaults to today. | [optional] 
**load_historic** | **bool** | Mastercard accounts at US banks (&#x60;provider: mastercard&#x60;, &#x60;countryCode: USA&#x60;) only. Triggers the provider&#39;s billable deep-history generation (up to 2 years) for this account before the import. Generation is asynchronous; re-run the window without the flag if rows are missing. Providers without the capability return &#x60;400&#x60;. | [optional] 

## Example

```python
from astrada.banking.models.bank_account_backfill_params import BankAccountBackfillParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountBackfillParams from a JSON string
bank_account_backfill_params_instance = BankAccountBackfillParams.from_json(json)
# print the JSON string representation of the object
print(BankAccountBackfillParams.to_json())

# convert the object into a dict
bank_account_backfill_params_dict = bank_account_backfill_params_instance.to_dict()
# create an instance of BankAccountBackfillParams from a dict
bank_account_backfill_params_from_dict = BankAccountBackfillParams.from_dict(bank_account_backfill_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


