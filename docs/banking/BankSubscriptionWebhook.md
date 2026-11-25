# BankSubscriptionWebhook

Webhook configuration for this subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL where webhook events will be delivered. | 
**status** | **str** | The current status of the webhook configuration. - &#x60;pending&#x60;: The webhook URL has been set but not yet confirmed by the provider. - &#x60;confirmed&#x60;: The provider has acknowledged the webhook URL. - &#x60;none&#x60;: No webhook URL has been configured.  | 

## Example

```python
from astrada.banking.models.bank_subscription_webhook import BankSubscriptionWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of BankSubscriptionWebhook from a JSON string
bank_subscription_webhook_instance = BankSubscriptionWebhook.from_json(json)
# print the JSON string representation of the object
print(BankSubscriptionWebhook.to_json())

# convert the object into a dict
bank_subscription_webhook_dict = bank_subscription_webhook_instance.to_dict()
# create an instance of BankSubscriptionWebhook from a dict
bank_subscription_webhook_from_dict = BankSubscriptionWebhook.from_dict(bank_subscription_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


