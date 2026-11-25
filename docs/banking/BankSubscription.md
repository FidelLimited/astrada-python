# BankSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the bank subscription. | 
**account_id** | **str** | The unique identifier of the account that owns this subscription. | 
**subaccount_id** | **str** | The unique identifier of the subaccount associated with this subscription. | 
**connection_id** | **str** | The provider&#39;s unique connection identifier (e.g. Plaid item ID). | 
**provider** | **str** | The banking data provider for this subscription. - &#x60;PLAID&#x60;: Connected through Plaid. - &#x60;MASTERCARD_US&#x60;: Connected through Mastercard Open Finance US. Sandbox only. - &#x60;MASTERCARD_EU&#x60;: Connected through Mastercard Open Finance Europe. Sandbox only.  | 
**institution_name** | **str** | The name of the connected financial institution. | 
**state** | **str** | Current state of the subscription. - &#x60;active&#x60;: The connection is functioning normally. - &#x60;error&#x60;: The connection has encountered an error. - &#x60;auth_required&#x60;: The connection requires user re-authentication. - &#x60;disconnected&#x60;: The connection has been disconnected.  | 
**webhook** | [**BankSubscriptionWebhook**](BankSubscriptionWebhook.md) |  | 
**sync_cursor** | **str** | The current transaction sync cursor for this subscription. | 
**last_synced_at** | **datetime** | Last successful sync of this connection, in UTC, following ISO 8601 format. Null until the first sync. | [optional] 
**auth_error_first_seen_at** | **datetime** | When a sync first found that the bank needs the user to sign in again, in UTC, following ISO 8601 format. Null when no such error is open. | [optional] 
**institution_last_checked_at** | **datetime** | When the bank data provider last reached the bank for this connection, in UTC, following ISO 8601 format. Null when the provider gives no such time. | [optional] 
**institution_last_failed_at** | **datetime** | When the bank data provider last failed to reach the bank for this connection, in UTC, following ISO 8601 format. Null when the provider gives no such time. | [optional] 
**institution_health** | [**BankSubscriptionInstitutionHealth**](BankSubscriptionInstitutionHealth.md) |  | [optional] 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.banking.models.bank_subscription import BankSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of BankSubscription from a JSON string
bank_subscription_instance = BankSubscription.from_json(json)
# print the JSON string representation of the object
print(BankSubscription.to_json())

# convert the object into a dict
bank_subscription_dict = bank_subscription_instance.to_dict()
# create an instance of BankSubscription from a dict
bank_subscription_from_dict = BankSubscription.from_dict(bank_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


