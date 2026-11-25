# NetworkBulkConfirmationBinInfo

A snapshot of the issuer details shown to the person who asked for the confirmation, kept for display only. `null` when the request carried none. The fields use the `GET /bin-lookup` vocabulary. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_name** | **str** | The name of the issuing bank. | [optional] 
**issuer_country** | **str** | The country of the issuing bank, ISO 3166-1 alpha-3. | [optional] 
**type** | **str** | The card type, for example &#x60;COMMERCIAL&#x60;. | [optional] 
**funding_type** | **str** | The card funding type, for example &#x60;CREDIT&#x60;. | [optional] 

## Example

```python
from astrada.models.network_bulk_confirmation_bin_info import NetworkBulkConfirmationBinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmationBinInfo from a JSON string
network_bulk_confirmation_bin_info_instance = NetworkBulkConfirmationBinInfo.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmationBinInfo.to_json())

# convert the object into a dict
network_bulk_confirmation_bin_info_dict = network_bulk_confirmation_bin_info_instance.to_dict()
# create an instance of NetworkBulkConfirmationBinInfo from a dict
network_bulk_confirmation_bin_info_from_dict = NetworkBulkConfirmationBinInfo.from_dict(network_bulk_confirmation_bin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


