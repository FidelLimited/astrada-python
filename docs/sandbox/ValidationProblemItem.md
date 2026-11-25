# ValidationProblemItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from astrada.sandbox.models.validation_problem_item import ValidationProblemItem

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationProblemItem from a JSON string
validation_problem_item_instance = ValidationProblemItem.from_json(json)
# print the JSON string representation of the object
print(ValidationProblemItem.to_json())

# convert the object into a dict
validation_problem_item_dict = validation_problem_item_instance.to_dict()
# create an instance of ValidationProblemItem from a dict
validation_problem_item_from_dict = ValidationProblemItem.from_dict(validation_problem_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


