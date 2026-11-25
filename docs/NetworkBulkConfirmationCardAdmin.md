# NetworkBulkConfirmationCardAdmin

The card program administrator. Astrada emails this person with the answer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from astrada.models.network_bulk_confirmation_card_admin import NetworkBulkConfirmationCardAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkConfirmationCardAdmin from a JSON string
network_bulk_confirmation_card_admin_instance = NetworkBulkConfirmationCardAdmin.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkConfirmationCardAdmin.to_json())

# convert the object into a dict
network_bulk_confirmation_card_admin_dict = network_bulk_confirmation_card_admin_instance.to_dict()
# create an instance of NetworkBulkConfirmationCardAdmin from a dict
network_bulk_confirmation_card_admin_from_dict = NetworkBulkConfirmationCardAdmin.from_dict(network_bulk_confirmation_card_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


