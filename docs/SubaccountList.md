# SubaccountList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**SubaccountListEmbedded**](SubaccountListEmbedded.md) |  | 
**links** | [**PageLinks**](PageLinks.md) |  | 

## Example

```python
from astrada.models.subaccount_list import SubaccountList

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountList from a JSON string
subaccount_list_instance = SubaccountList.from_json(json)
# print the JSON string representation of the object
print(SubaccountList.to_json())

# convert the object into a dict
subaccount_list_dict = subaccount_list_instance.to_dict()
# create an instance of SubaccountList from a dict
subaccount_list_from_dict = SubaccountList.from_dict(subaccount_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


