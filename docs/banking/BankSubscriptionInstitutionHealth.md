# BankSubscriptionInstitutionHealth

The bank data provider's health figures for this connection's bank. Null when the provider publishes none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **float** | The share of the provider&#39;s recent transaction updates for this bank that succeeded, from 0 to 1. | [optional] 
**error_institution** | **float** | The share that failed because of the bank, from 0 to 1. | [optional] 
**error_provider** | **float** | The share that failed because of the provider, from 0 to 1. | [optional] 
**refresh_interval** | **str** | Whether the provider is refreshing this bank on schedule (&#x60;NORMAL&#x60;), late (&#x60;DELAYED&#x60;) or not at all (&#x60;STOPPED&#x60;). | [optional] 
**incidents** | [**List[BankInstitutionIncident]**](BankInstitutionIncident.md) | The provider&#39;s published outages and maintenance for this bank. | [optional] 
**observed_at** | **datetime** | When Astrada read these figures, in UTC, following ISO 8601 format. | [optional] 

## Example

```python
from astrada.banking.models.bank_subscription_institution_health import BankSubscriptionInstitutionHealth

# TODO update the JSON string below
json = "{}"
# create an instance of BankSubscriptionInstitutionHealth from a JSON string
bank_subscription_institution_health_instance = BankSubscriptionInstitutionHealth.from_json(json)
# print the JSON string representation of the object
print(BankSubscriptionInstitutionHealth.to_json())

# convert the object into a dict
bank_subscription_institution_health_dict = bank_subscription_institution_health_instance.to_dict()
# create an instance of BankSubscriptionInstitutionHealth from a dict
bank_subscription_institution_health_from_dict = BankSubscriptionInstitutionHealth.from_dict(bank_subscription_institution_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


