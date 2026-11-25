# BankLinkSyncResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable confirmation message. | [optional] 

## Example

```python
from astrada.banking.models.bank_link_sync_result import BankLinkSyncResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkSyncResult from a JSON string
bank_link_sync_result_instance = BankLinkSyncResult.from_json(json)
# print the JSON string representation of the object
print(BankLinkSyncResult.to_json())

# convert the object into a dict
bank_link_sync_result_dict = bank_link_sync_result_instance.to_dict()
# create an instance of BankLinkSyncResult from a dict
bank_link_sync_result_from_dict = BankLinkSyncResult.from_dict(bank_link_sync_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


