# EnrollmentLinkConflictProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from astrada.models.enrollment_link_conflict_problem import EnrollmentLinkConflictProblem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkConflictProblem from a JSON string
enrollment_link_conflict_problem_instance = EnrollmentLinkConflictProblem.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkConflictProblem.to_json())

# convert the object into a dict
enrollment_link_conflict_problem_dict = enrollment_link_conflict_problem_instance.to_dict()
# create an instance of EnrollmentLinkConflictProblem from a dict
enrollment_link_conflict_problem_from_dict = EnrollmentLinkConflictProblem.from_dict(enrollment_link_conflict_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


