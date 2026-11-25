# BankLinkSyncParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks** | **List[str]** | The events this sync sends. Default (field left out) is both. An empty array sends neither; transactions are still stored and matched. Names outside this list are ignored, not refused. | [optional] 
**force** | **bool** | Set to &#x60;true&#x60; to force a full sync even if no new transactions are detected. With &#x60;true&#x60;:  - Stored transactions: every transaction already stored for the link is gone over again, and &#x60;banktransaction.created&#x60; is sent again for each when &#x60;webhooks&#x60; allows it. - Existing matches: scored again, and &#x60;transaction.match.created&#x60; sent again, only when &#x60;webhooks&#x60; lists &#x60;transaction.match.created&#x60;. With &#x60;webhooks&#x60; left out they are kept and not sent again. - Unmatched transactions: whatever &#x60;webhooks&#x60; lists, a stored transaction with no match yet goes through matching, and a new match is sent when &#x60;webhooks&#x60; allows it.  | [optional] [default to False]

## Example

```python
from astrada.banking.models.bank_link_sync_params import BankLinkSyncParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkSyncParams from a JSON string
bank_link_sync_params_instance = BankLinkSyncParams.from_json(json)
# print the JSON string representation of the object
print(BankLinkSyncParams.to_json())

# convert the object into a dict
bank_link_sync_params_dict = bank_link_sync_params_instance.to_dict()
# create an instance of BankLinkSyncParams from a dict
bank_link_sync_params_from_dict = BankLinkSyncParams.from_dict(bank_link_sync_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


