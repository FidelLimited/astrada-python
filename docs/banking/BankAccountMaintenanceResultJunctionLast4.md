# BankAccountMaintenanceResultJunctionLast4

Present only when `backfillJunctionLast4: true` was sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows_updated** | **int** | Links that gained a last 4 in this run. | 
**rows_unresolved** | **int** | Links still without one (the directory did not list the card). | 
**directory_unavailable** | **bool** | True when this action&#39;s own read of the cards directory failed (the mask pass does not fail on it); call again later. | 

## Example

```python
from astrada.banking.models.bank_account_maintenance_result_junction_last4 import BankAccountMaintenanceResultJunctionLast4

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountMaintenanceResultJunctionLast4 from a JSON string
bank_account_maintenance_result_junction_last4_instance = BankAccountMaintenanceResultJunctionLast4.from_json(json)
# print the JSON string representation of the object
print(BankAccountMaintenanceResultJunctionLast4.to_json())

# convert the object into a dict
bank_account_maintenance_result_junction_last4_dict = bank_account_maintenance_result_junction_last4_instance.to_dict()
# create an instance of BankAccountMaintenanceResultJunctionLast4 from a dict
bank_account_maintenance_result_junction_last4_from_dict = BankAccountMaintenanceResultJunctionLast4.from_dict(bank_account_maintenance_result_junction_last4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


