# BankLinkLastMintFailure

Present once a completion attempt was aborted because card creation (the `bank-feed` mint) failed for one or more discovered credit accounts. The link stays pending and completion is retried; a later successful completion clears this field (an expired link keeps its last failure). `transient` failures resolve on retry; a `permanent` one keeps aborting until investigated. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **datetime** | When the failed completion attempt happened, in UTC, following ISO 8601 format. | [optional] 
**kind** | **str** | Whether the underlying failure is expected to clear on retry. | [optional] 
**failed_account_count** | **int** | How many discovered credit accounts failed to mint on the attempt. | [optional] 

## Example

```python
from astrada.banking.models.bank_link_last_mint_failure import BankLinkLastMintFailure

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkLastMintFailure from a JSON string
bank_link_last_mint_failure_instance = BankLinkLastMintFailure.from_json(json)
# print the JSON string representation of the object
print(BankLinkLastMintFailure.to_json())

# convert the object into a dict
bank_link_last_mint_failure_dict = bank_link_last_mint_failure_instance.to_dict()
# create an instance of BankLinkLastMintFailure from a dict
bank_link_last_mint_failure_from_dict = BankLinkLastMintFailure.from_dict(bank_link_last_mint_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


