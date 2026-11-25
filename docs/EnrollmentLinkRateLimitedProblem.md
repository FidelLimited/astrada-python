# EnrollmentLinkRateLimitedProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**detail** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from astrada.models.enrollment_link_rate_limited_problem import EnrollmentLinkRateLimitedProblem

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkRateLimitedProblem from a JSON string
enrollment_link_rate_limited_problem_instance = EnrollmentLinkRateLimitedProblem.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkRateLimitedProblem.to_json())

# convert the object into a dict
enrollment_link_rate_limited_problem_dict = enrollment_link_rate_limited_problem_instance.to_dict()
# create an instance of EnrollmentLinkRateLimitedProblem from a dict
enrollment_link_rate_limited_problem_from_dict = EnrollmentLinkRateLimitedProblem.from_dict(enrollment_link_rate_limited_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


