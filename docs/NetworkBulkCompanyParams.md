# NetworkBulkCompanyParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | The company&#39;s legal name, exactly as it reads on the card agreement. | 

## Example

```python
from astrada.models.network_bulk_company_params import NetworkBulkCompanyParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkCompanyParams from a JSON string
network_bulk_company_params_instance = NetworkBulkCompanyParams.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkCompanyParams.to_json())

# convert the object into a dict
network_bulk_company_params_dict = network_bulk_company_params_instance.to_dict()
# create an instance of NetworkBulkCompanyParams from a dict
network_bulk_company_params_from_dict = NetworkBulkCompanyParams.from_dict(network_bulk_company_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


