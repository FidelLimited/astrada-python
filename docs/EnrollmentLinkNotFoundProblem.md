# EnrollmentLinkNotFoundProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from astrada.models.enrollment_link_not_found_problem import EnrollmentLinkNotFoundProblem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkNotFoundProblem from a JSON string
enrollment_link_not_found_problem_instance = EnrollmentLinkNotFoundProblem.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkNotFoundProblem.to_json())

# convert the object into a dict
enrollment_link_not_found_problem_dict = enrollment_link_not_found_problem_instance.to_dict()
# create an instance of EnrollmentLinkNotFoundProblem from a dict
enrollment_link_not_found_problem_from_dict = EnrollmentLinkNotFoundProblem.from_dict(enrollment_link_not_found_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


