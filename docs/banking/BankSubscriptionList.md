# BankSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BankSubscription]**](BankSubscription.md) |  | 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | 

## Example

```python
from astrada.banking.models.bank_subscription_list import BankSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of BankSubscriptionList from a JSON string
bank_subscription_list_instance = BankSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(BankSubscriptionList.to_json())

# convert the object into a dict
bank_subscription_list_dict = bank_subscription_list_instance.to_dict()
# create an instance of BankSubscriptionList from a dict
bank_subscription_list_from_dict = BankSubscriptionList.from_dict(bank_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


