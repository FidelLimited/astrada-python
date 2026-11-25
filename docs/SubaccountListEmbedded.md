# SubaccountListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaccounts** | [**List[Subaccount]**](Subaccount.md) |  | 

## Example

```python
from astrada.models.subaccount_list_embedded import SubaccountListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountListEmbedded from a JSON string
subaccount_list_embedded_instance = SubaccountListEmbedded.from_json(json)
# print the JSON string representation of the object
print(SubaccountListEmbedded.to_json())

# convert the object into a dict
subaccount_list_embedded_dict = subaccount_list_embedded_instance.to_dict()
# create an instance of SubaccountListEmbedded from a dict
subaccount_list_embedded_from_dict = SubaccountListEmbedded.from_dict(subaccount_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


