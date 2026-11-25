# NetworkBulkConfirmationCreateParamsBinInfo

Optional. The issuer details shown to the person who asked for the confirmation, in the `GET /bin-lookup` vocabulary. Stored as a display snapshot only; every field is optional. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_name** | **str** | The name of the issuing bank. | [optional] 
**issuer_country** | **str** | The country of the issuing bank, ISO 3166-1 alpha-3. | [optional] 
**type** | **str** | The card type, for example &#x60;COMMERCIAL&#x60;. | [optional] 
**funding_type** | **str** | The card funding type, for example &#x60;CREDIT&#x60;. | [optional] 

## Example

```python
from astrada.models.network_bulk_confirmation_create_params_bin_info import NetworkBulkConfirmationCreateParamsBinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmationCreateParamsBinInfo from a JSON string
network_bulk_confirmation_create_params_bin_info_instance = NetworkBulkConfirmationCreateParamsBinInfo.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmationCreateParamsBinInfo.to_json())

# convert the object into a dict
network_bulk_confirmation_create_params_bin_info_dict = network_bulk_confirmation_create_params_bin_info_instance.to_dict()
# create an instance of NetworkBulkConfirmationCreateParamsBinInfo from a dict
network_bulk_confirmation_create_params_bin_info_from_dict = NetworkBulkConfirmationCreateParamsBinInfo.from_dict(network_bulk_confirmation_create_params_bin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


