# NetworkBulkConfirmationCreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the open confirmation request. | 
**request_id** | **str** | The &#x60;requestId&#x60; this request sent. It is never the &#x60;requestId&#x60; the open request was stored under. | 
**subaccount_id** | **str** | The subaccount of the open request, the same as the request&#39;s. | 
**network** | **str** | The network of the open request, the same as the request&#39;s. | 
**bin** | **str** | The first 8 digits of the card, exactly as submitted. | 
**grade** | **str** | The bulk likelihood grade the client saw for this BIN, as sent on the create request. &#x60;unchecked&#x60; when the request had no grade because it could not be determined. | 
**bin_info** | [**NetworkBulkConfirmationBinInfo**](NetworkBulkConfirmationBinInfo.md) |  | 
**company** | [**NetworkBulkConfirmationCompany**](NetworkBulkConfirmationCompany.md) |  | 
**card_admin** | [**NetworkBulkConfirmationCardAdmin**](NetworkBulkConfirmationCardAdmin.md) |  | 
**bank_contact** | [**NetworkBulkBankContact**](NetworkBulkBankContact.md) |  | 
**state** | **str** | The state of the open request. &#x60;requested&#x60; is the only state for now. | 
**customer_reference_id** | **str** | An optional id passed by the customer to associate a context with the confirmation. &#x60;null&#x60; when not provided. | 
**created_at** | **datetime** | When the open request was created, in UTC, following ISO 8601 format. Its 30-day window counts from this time. | 
**already_open** | **bool** | Always &#x60;true&#x60;. Tells this summary apart from the full confirmation. | 

## Example

```python
from astrada.models.network_bulk_confirmation_create_result import NetworkBulkConfirmationCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmationCreateResult from a JSON string
network_bulk_confirmation_create_result_instance = NetworkBulkConfirmationCreateResult.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmationCreateResult.to_json())

# convert the object into a dict
network_bulk_confirmation_create_result_dict = network_bulk_confirmation_create_result_instance.to_dict()
# create an instance of NetworkBulkConfirmationCreateResult from a dict
network_bulk_confirmation_create_result_from_dict = NetworkBulkConfirmationCreateResult.from_dict(network_bulk_confirmation_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


