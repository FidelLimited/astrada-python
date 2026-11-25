# BinLookupValidationProblem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**title** | **str** |  | 
**errors** | [**List[BinLookupValidationProblemItem]**](BinLookupValidationProblemItem.md) |  | [optional] 

## Example

```python
from astrada.models.bin_lookup_validation_problem import BinLookupValidationProblem

# TODO update the JSON string below
json = "{}"
# create an instance of BinLookupValidationProblem from a JSON string
bin_lookup_validation_problem_instance = BinLookupValidationProblem.from_json(json)
# print the JSON string representation of the object
print(BinLookupValidationProblem.to_json())

# convert the object into a dict
bin_lookup_validation_problem_dict = bin_lookup_validation_problem_instance.to_dict()
# create an instance of BinLookupValidationProblem from a dict
bin_lookup_validation_problem_from_dict = BinLookupValidationProblem.from_dict(bin_lookup_validation_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


