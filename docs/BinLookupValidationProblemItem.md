# BinLookupValidationProblemItem

One problem found in a BIN lookup request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** | The part of the request the problem is about. | [optional] 
**title** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from astrada.models.bin_lookup_validation_problem_item import BinLookupValidationProblemItem

# TODO update the JSON string below
json = "{}"
# create an instance of BinLookupValidationProblemItem from a JSON string
bin_lookup_validation_problem_item_instance = BinLookupValidationProblemItem.from_json(json)
# print the JSON string representation of the object
print(BinLookupValidationProblemItem.to_json())

# convert the object into a dict
bin_lookup_validation_problem_item_dict = bin_lookup_validation_problem_item_instance.to_dict()
# create an instance of BinLookupValidationProblemItem from a dict
bin_lookup_validation_problem_item_from_dict = BinLookupValidationProblemItem.from_dict(bin_lookup_validation_problem_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


