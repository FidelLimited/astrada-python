# ValidationProblem

A `400 Bad Request` body. `errors`, when present, lists each problem found in the request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**title** | **str** | A short summary of the status, &#x60;Bad Request&#x60; on this response. | 
**errors** | [**List[ValidationProblemItem]**](ValidationProblemItem.md) |  | [optional] 

## Example

```python
from astrada.sandbox.models.validation_problem import ValidationProblem

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationProblem from a JSON string
validation_problem_instance = ValidationProblem.from_json(json)
# print the JSON string representation of the object
print(ValidationProblem.to_json())

# convert the object into a dict
validation_problem_dict = validation_problem_instance.to_dict()
# create an instance of ValidationProblem from a dict
validation_problem_from_dict = ValidationProblem.from_dict(validation_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


