# Conflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**title** | **str** |  | [optional] 
**current_value** | **str** | Current value for the property causing the conflict | [optional] 
**requested_value** | **str** | Requested value for the property causing the conflict | [optional] 

## Example

```python
from astrada.sandbox.models.conflict import Conflict

# TODO update the JSON string below
json = "{}"
# create an instance of Conflict from a JSON string
conflict_instance = Conflict.from_json(json)
# print the JSON string representation of the object
print(Conflict.to_json())

# convert the object into a dict
conflict_dict = conflict_instance.to_dict()
# create an instance of Conflict from a dict
conflict_from_dict = Conflict.from_dict(conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


