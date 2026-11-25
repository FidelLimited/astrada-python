# BankAccountMaintenanceResultMintedValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** |  | 
**subscription_id** | **str** |  | 
**linked_here** | **bool** |  | 

## Example

```python
from astrada.banking.models.bank_account_maintenance_result_minted_value import BankAccountMaintenanceResultMintedValue

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountMaintenanceResultMintedValue from a JSON string
bank_account_maintenance_result_minted_value_instance = BankAccountMaintenanceResultMintedValue.from_json(json)
# print the JSON string representation of the object
print(BankAccountMaintenanceResultMintedValue.to_json())

# convert the object into a dict
bank_account_maintenance_result_minted_value_dict = bank_account_maintenance_result_minted_value_instance.to_dict()
# create an instance of BankAccountMaintenanceResultMintedValue from a dict
bank_account_maintenance_result_minted_value_from_dict = BankAccountMaintenanceResultMintedValue.from_dict(bank_account_maintenance_result_minted_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


