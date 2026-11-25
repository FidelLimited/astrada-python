# EnrollmentLinkCreateValidationProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 
**code** | **str** |  | [optional] 
**errors** | [**List[ValidationProblemItem]**](ValidationProblemItem.md) |  | [optional] 

## Example

```python
from astrada.models.enrollment_link_create_validation_problem import EnrollmentLinkCreateValidationProblem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkCreateValidationProblem from a JSON string
enrollment_link_create_validation_problem_instance = EnrollmentLinkCreateValidationProblem.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkCreateValidationProblem.to_json())

# convert the object into a dict
enrollment_link_create_validation_problem_dict = enrollment_link_create_validation_problem_instance.to_dict()
# create an instance of EnrollmentLinkCreateValidationProblem from a dict
enrollment_link_create_validation_problem_from_dict = EnrollmentLinkCreateValidationProblem.from_dict(enrollment_link_create_validation_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


