# NetworkBulkEnrollmentBinInfo

A snapshot of the issuer details shown to the person who submitted the kickoff, kept for display only. `null` when the request carried none. The fields use the `GET /bin-lookup` vocabulary. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_name** | **str** | The name of the issuing bank. | [optional] 
**issuer_country** | **str** | The country of the issuing bank, ISO 3166 alpha-3. | [optional] 
**type** | **str** | The card type, for example &#x60;COMMERCIAL&#x60;. | [optional] 
**funding_type** | **str** | The card funding type, for example &#x60;CREDIT&#x60;. | [optional] 

## Example

```python
from astrada.models.network_bulk_enrollment_bin_info import NetworkBulkEnrollmentBinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentBinInfo from a JSON string
network_bulk_enrollment_bin_info_instance = NetworkBulkEnrollmentBinInfo.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentBinInfo.to_json())

# convert the object into a dict
network_bulk_enrollment_bin_info_dict = network_bulk_enrollment_bin_info_instance.to_dict()
# create an instance of NetworkBulkEnrollmentBinInfo from a dict
network_bulk_enrollment_bin_info_from_dict = NetworkBulkEnrollmentBinInfo.from_dict(network_bulk_enrollment_bin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


