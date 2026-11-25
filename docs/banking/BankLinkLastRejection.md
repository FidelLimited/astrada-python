# BankLinkLastRejection

Present while `state` is `pending` after a completion attempt was refused because the connected institution is not allowed for this link (for example, a non-Amex institution on an Amex-restricted link). The link can still be completed by reconnecting with an allowed institution; a successful completion clears this field. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_name** | **str** | Display name of the refused institution. | [optional] 
**at** | **datetime** | When the refusal happened, in UTC, following ISO 8601 format. | [optional] 

## Example

```python
from astrada.banking.models.bank_link_last_rejection import BankLinkLastRejection

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkLastRejection from a JSON string
bank_link_last_rejection_instance = BankLinkLastRejection.from_json(json)
# print the JSON string representation of the object
print(BankLinkLastRejection.to_json())

# convert the object into a dict
bank_link_last_rejection_dict = bank_link_last_rejection_instance.to_dict()
# create an instance of BankLinkLastRejection from a dict
bank_link_last_rejection_from_dict = BankLinkLastRejection.from_dict(bank_link_last_rejection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


