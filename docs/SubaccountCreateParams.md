# SubaccountCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the subaccount | 
**configurations** | [**CreateSubaccountConfigurations**](CreateSubaccountConfigurations.md) |  | 

## Example

```python
from astrada.models.subaccount_create_params import SubaccountCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountCreateParams from a JSON string
subaccount_create_params_instance = SubaccountCreateParams.from_json(json)
# print the JSON string representation of the object
print(SubaccountCreateParams.to_json())

# convert the object into a dict
subaccount_create_params_dict = subaccount_create_params_instance.to_dict()
# create an instance of SubaccountCreateParams from a dict
subaccount_create_params_from_dict = SubaccountCreateParams.from_dict(subaccount_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


