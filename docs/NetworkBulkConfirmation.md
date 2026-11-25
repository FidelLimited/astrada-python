# NetworkBulkConfirmation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of this network bulk confirmation. | 
**request_id** | **str** | The idempotency key sent on the create request, unique per account. | 
**subaccount_id** | **str** | The unique identifier of the subaccount the card program belongs to. | 
**network** | **str** | The network of the card program. | 
**bin** | **str** | The first 8 digits of the card, exactly as submitted. | 
**grade** | **str** | The bulk likelihood grade the client saw for this BIN, as sent on the create request. &#x60;unchecked&#x60; when the request had no grade because it could not be determined. | 
**bin_info** | [**NetworkBulkConfirmationBinInfo**](NetworkBulkConfirmationBinInfo.md) |  | 
**company** | [**NetworkBulkConfirmationCompany**](NetworkBulkConfirmationCompany.md) |  | 
**card_admin** | [**NetworkBulkConfirmationCardAdmin**](NetworkBulkConfirmationCardAdmin.md) |  | 
**bank_contact** | [**NetworkBulkBankContact**](NetworkBulkBankContact.md) |  | 
**state** | **str** | The state of the confirmation. &#x60;requested&#x60; is the only state for now. | 
**customer_reference_id** | **str** | An optional id passed by the customer to associate a context with the confirmation. &#x60;null&#x60; when not provided. | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.models.network_bulk_confirmation import NetworkBulkConfirmation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmation from a JSON string
network_bulk_confirmation_instance = NetworkBulkConfirmation.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmation.to_json())

# convert the object into a dict
network_bulk_confirmation_dict = network_bulk_confirmation_instance.to_dict()
# create an instance of NetworkBulkConfirmation from a dict
network_bulk_confirmation_from_dict = NetworkBulkConfirmation.from_dict(network_bulk_confirmation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


