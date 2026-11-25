# EnrollmentLinkListValidationProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 
**code** | **str** |  | [optional] 
**errors** | [**List[ValidationProblemItem]**](ValidationProblemItem.md) |  | [optional] 

## Example

```python
from astrada.models.enrollment_link_list_validation_problem import EnrollmentLinkListValidationProblem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkListValidationProblem from a JSON string
enrollment_link_list_validation_problem_instance = EnrollmentLinkListValidationProblem.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkListValidationProblem.to_json())

# convert the object into a dict
enrollment_link_list_validation_problem_dict = enrollment_link_list_validation_problem_instance.to_dict()
# create an instance of EnrollmentLinkListValidationProblem from a dict
enrollment_link_list_validation_problem_from_dict = EnrollmentLinkListValidationProblem.from_dict(enrollment_link_list_validation_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


