# Problem

An error body in the problem details format (`application/problem+json`). Every error response without its own fields uses it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**detail** | **str** |  | 
**title** | **str** | A short summary of the status, for example &#x60;Unauthorized&#x60;, &#x60;Forbidden&#x60;, &#x60;Not Found&#x60; or &#x60;Internal Server Error&#x60;. Each response&#39;s example shows its value.  | 

## Example

```python
from astrada.banking.models.problem import Problem

# TODO update the JSON string below
json = "{}"
# create an instance of Problem from a JSON string
problem_instance = Problem.from_json(json)
# print the JSON string representation of the object
print(Problem.to_json())

# convert the object into a dict
problem_dict = problem_instance.to_dict()
# create an instance of Problem from a dict
problem_from_dict = Problem.from_dict(problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


