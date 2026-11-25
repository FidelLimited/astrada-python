# BankAccountDisconnect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Set to &#x60;disconnected&#x60; to stop this account&#39;s feed and remove its card links while keeping the account, its transactions and its matches readable. With &#x60;cardId&#x60;, see that field: the account can keep feeding its other cards. This endpoint cannot set it back: a new bank link to the same bank creates a new bank account, and this one stays &#x60;disconnected&#x60;. When this is the connection&#39;s last active account, the connection at the bank is ended too. Disconnecting an account that is already disconnected, or one that was deleted, answers &#x60;200&#x60; and sends no webhook (an id that never existed still answers &#x60;404&#x60;). Use &#x60;DELETE /bank-accounts/{bankAccountId}&#x60; to remove the account and its transactions. | 
**reason** | **str** | Optional free-text reason recorded with the disconnect. Sent as &#x60;reason&#x60; on &#x60;bankaccount.state_changed&#x60;. Default &#x60;subscription_deactivated&#x60;. | [optional] 
**card_id** | **str** | Optional SCOPE for the disconnect. Omit for the historical account-scoped behaviour: the whole account is torn down and every card on it loses the feed. Supply the card that was deactivated to scope it to that card: its link is removed and the account keeps feeding any other cards attached to it. Disconnecting the last remaining card still tears the account down, so a single-card account behaves identically either way.  | [optional] 

## Example

```python
from astrada.banking.models.bank_account_disconnect import BankAccountDisconnect

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDisconnect from a JSON string
bank_account_disconnect_instance = BankAccountDisconnect.from_json(json)
# print the JSON string representation of the object
print(BankAccountDisconnect.to_json())

# convert the object into a dict
bank_account_disconnect_dict = bank_account_disconnect_instance.to_dict()
# create an instance of BankAccountDisconnect from a dict
bank_account_disconnect_from_dict = BankAccountDisconnect.from_dict(bank_account_disconnect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


