# BankAccountMaintenanceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked** | **Dict[str, List[str]]** | bankAccountId -&gt; cardIds linked in THIS run. | 
**minted** | [**Dict[str, BankAccountMaintenanceResultMintedValue]**](BankAccountMaintenanceResultMintedValue.md) | Present whenever &#x60;mint: true&#x60; was sent (&#x60;{}&#x60; when nothing was minted). bankAccountId -&gt; the card minted for it in THIS run. &#x60;linkedHere&#x60; is false when the card is held by a sibling account instead (a re-link of the same bank; the background re-home converges it).  | [optional] 
**skipped** | **Dict[str, str]** | Present whenever &#x60;mint: true&#x60; was sent (&#x60;{}&#x60; when nothing was skipped). bankAccountId -&gt; why the mint pass did not mint for it: &#x60;already_materialized&#x60; (the account already holds a minted card), &#x60;existing_enrolled_card&#x60; (its last 4 belongs to a card the customer enrolled directly) or &#x60;no_institution_id&#x60; (the connection never recorded its institution).  | [optional] 
**failures** | **Dict[str, str]** | Present whenever &#x60;mint: true&#x60; was sent (&#x60;{}&#x60; when no mint failed). bankAccountId -&gt; the failure. The pass is idempotent, so the request can simply be repeated.  | [optional] 
**junction_last4** | [**BankAccountMaintenanceResultJunctionLast4**](BankAccountMaintenanceResultJunctionLast4.md) |  | [optional] 
**cardholder_cards** | [**BankAccountMaintenanceResultCardholderCards**](BankAccountMaintenanceResultCardholderCards.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_account_maintenance_result import BankAccountMaintenanceResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountMaintenanceResult from a JSON string
bank_account_maintenance_result_instance = BankAccountMaintenanceResult.from_json(json)
# print the JSON string representation of the object
print(BankAccountMaintenanceResult.to_json())

# convert the object into a dict
bank_account_maintenance_result_dict = bank_account_maintenance_result_instance.to_dict()
# create an instance of BankAccountMaintenanceResult from a dict
bank_account_maintenance_result_from_dict = BankAccountMaintenanceResult.from_dict(bank_account_maintenance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


