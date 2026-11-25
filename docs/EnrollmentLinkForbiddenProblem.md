# EnrollmentLinkForbiddenProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 
**code** | **str** |  | [optional] 

## Example

```python
from astrada.models.enrollment_link_forbidden_problem import EnrollmentLinkForbiddenProblem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkForbiddenProblem from a JSON string
enrollment_link_forbidden_problem_instance = EnrollmentLinkForbiddenProblem.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkForbiddenProblem.to_json())

# convert the object into a dict
enrollment_link_forbidden_problem_dict = enrollment_link_forbidden_problem_instance.to_dict()
# create an instance of EnrollmentLinkForbiddenProblem from a dict
enrollment_link_forbidden_problem_from_dict = EnrollmentLinkForbiddenProblem.from_dict(enrollment_link_forbidden_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


