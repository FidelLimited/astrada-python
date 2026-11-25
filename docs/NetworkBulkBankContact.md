# NetworkBulkBankContact

The company's relationship contact at the issuing bank. `null` when not provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from astrada.models.network_bulk_bank_contact import NetworkBulkBankContact

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkBankContact from a JSON string
network_bulk_bank_contact_instance = NetworkBulkBankContact.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkBankContact.to_json())

# convert the object into a dict
network_bulk_bank_contact_dict = network_bulk_bank_contact_instance.to_dict()
# create an instance of NetworkBulkBankContact from a dict
network_bulk_bank_contact_from_dict = NetworkBulkBankContact.from_dict(network_bulk_bank_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


