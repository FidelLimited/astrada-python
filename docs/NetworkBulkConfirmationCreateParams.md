# NetworkBulkConfirmationCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Your idempotency key for this confirmation, unique per account. Repeating the request with a &#x60;requestId&#x60; that was already used returns the stored confirmation, whole and unchanged, with &#x60;200&#x60; instead of creating a second one with &#x60;201&#x60;. A new &#x60;requestId&#x60; for a program that already has an open request answers &#x60;200&#x60; with that request&#39;s summary.  | 
**subaccount_id** | **str** | The subaccount the card program belongs to. Must belong to the calling account; an unknown subaccount answers &#x60;400&#x60;. | 
**network** | **str** | The network of the card program. | 
**bin** | **str** | Exactly the first 8 digits of the card number. Never send the full card number. | 
**grade** | **str** | The bulk likelihood grade your client saw for this BIN, as returned in &#x60;bulkLikelihood&#x60; by &#x60;POST /enrollment-methods&#x60;. Send it whenever that response had one. Leave it out (or send &#x60;unchecked&#x60;) only when the response had no &#x60;bulkLikelihood&#x60; because it could not be determined; the request is then stored as &#x60;unchecked&#x60;. | [optional] 
**bin_info** | [**NetworkBulkConfirmationCreateParamsBinInfo**](NetworkBulkConfirmationCreateParamsBinInfo.md) |  | [optional] 
**company** | [**NetworkBulkCompanyParams**](NetworkBulkCompanyParams.md) |  | 
**card_admin** | [**NetworkBulkConfirmationCreateParamsCardAdmin**](NetworkBulkConfirmationCreateParamsCardAdmin.md) |  | 
**bank_contact** | [**NetworkBulkBankContactParams**](NetworkBulkBankContactParams.md) |  | [optional] 
**customer_reference_id** | **str** | Optional. Your own id for this confirmation, echoed back on the resource. | [optional] 

## Example

```python
from astrada.models.network_bulk_confirmation_create_params import NetworkBulkConfirmationCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmationCreateParams from a JSON string
network_bulk_confirmation_create_params_instance = NetworkBulkConfirmationCreateParams.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmationCreateParams.to_json())

# convert the object into a dict
network_bulk_confirmation_create_params_dict = network_bulk_confirmation_create_params_instance.to_dict()
# create an instance of NetworkBulkConfirmationCreateParams from a dict
network_bulk_confirmation_create_params_from_dict = NetworkBulkConfirmationCreateParams.from_dict(network_bulk_confirmation_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


