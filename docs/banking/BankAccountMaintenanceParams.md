# BankAccountMaintenanceParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaccount_id** | **str** | The subaccount to run maintenance over. | 
**mint** | **bool** | After the mask pass, also mint a bank-feed card for each of the subaccount&#39;s eligible credit bank accounts that holds no card. Accounts that already hold a minted card are skipped.  | [optional] [default to False]
**backfill_junction_last4** | **bool** | After the mask pass, also fill each of the subaccount&#39;s card links with the last 4 it answers to, where still unknown, from the cards directory.  | [optional] [default to False]
**create_cardholder_cards** | **bool** | After the mask pass, also create and name the bank-feed cards of the cardholders behind the subaccount&#39;s pooled American Express billing accounts, as the scheduled job does. Does nothing unless Astrada has switched the feature on for the subaccount.  | [optional] [default to False]

## Example

```python
from astrada.banking.models.bank_account_maintenance_params import BankAccountMaintenanceParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountMaintenanceParams from a JSON string
bank_account_maintenance_params_instance = BankAccountMaintenanceParams.from_json(json)
# print the JSON string representation of the object
print(BankAccountMaintenanceParams.to_json())

# convert the object into a dict
bank_account_maintenance_params_dict = bank_account_maintenance_params_instance.to_dict()
# create an instance of BankAccountMaintenanceParams from a dict
bank_account_maintenance_params_from_dict = BankAccountMaintenanceParams.from_dict(bank_account_maintenance_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


