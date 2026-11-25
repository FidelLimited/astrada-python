# NetworkBulkBankContactParams

Optional. The company's relationship contact at the issuing bank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from astrada.models.network_bulk_bank_contact_params import NetworkBulkBankContactParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkBankContactParams from a JSON string
network_bulk_bank_contact_params_instance = NetworkBulkBankContactParams.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkBankContactParams.to_json())

# convert the object into a dict
network_bulk_bank_contact_params_dict = network_bulk_bank_contact_params_instance.to_dict()
# create an instance of NetworkBulkBankContactParams from a dict
network_bulk_bank_contact_params_from_dict = NetworkBulkBankContactParams.from_dict(network_bulk_bank_contact_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


