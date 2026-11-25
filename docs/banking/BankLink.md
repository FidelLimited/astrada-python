# BankLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**BankLinkLinks**](BankLinkLinks.md) |  | 
**id** | **str** | The client-provided identifier of the bank link. Must be alphanumeric with hyphens and underscores only. | 
**account_id** | **str** | The unique identifier of the account that owns this bank link. | 
**subaccount_id** | **str** | The unique identifier of the subaccount associated with this bank link. | 
**state** | **str** | Current state of the bank link. - &#x60;pending&#x60;: The link has been created and is awaiting user enrollment. - &#x60;completed&#x60;: The user has successfully connected their bank account. - &#x60;expired&#x60;: The link has expired without being completed.  | 
**provider** | **str** | Open-banking provider this link was created on. Fixed at creation: every later operation on the link uses this value. Links created before provider selection existed are &#x60;plaid&#x60;.  | [optional] 
**hosted_link** | **str** | The hosted URL where the user can complete the bank enrollment. This link expires after 4 hours and is automatically refreshed when retrieved via GET. | 
**link_expires_at** | **datetime** | Date and time when the hosted link expires, in UTC, following ISO 8601 format. | 
**completed_at** | **datetime** | Date and time when the bank link enrollment was completed, in UTC, following ISO 8601 format. Only present when state is &#x60;completed&#x60;. | [optional] 
**last_rejection** | [**BankLinkLastRejection**](BankLinkLastRejection.md) |  | [optional] 
**last_mint_failure** | [**BankLinkLastMintFailure**](BankLinkLastMintFailure.md) |  | [optional] 
**filters** | [**BankLinkFilters**](BankLinkFilters.md) |  | [optional] 
**bank_accounts** | [**List[BankLinkBankAccount]**](BankLinkBankAccount.md) | Summary of bank accounts created from this link. Only present when state is &#x60;completed&#x60; and accounts exist. | [optional] 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.banking.models.bank_link import BankLink

# TODO update the JSON string below
json = "{}"
# create an instance of BankLink from a JSON string
bank_link_instance = BankLink.from_json(json)
# print the JSON string representation of the object
print(BankLink.to_json())

# convert the object into a dict
bank_link_dict = bank_link_instance.to_dict()
# create an instance of BankLink from a dict
bank_link_from_dict = BankLink.from_dict(bank_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


