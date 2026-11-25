# BinLookupWarning

A note about the answer, with a code to branch on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A stable code for programs to branch on. New codes may be added; ignore codes you don&#39;t recognize.  | 
**message** | **str** | A human-readable explanation. The wording may change. | 

## Example

```python
from astrada.models.bin_lookup_warning import BinLookupWarning

# TODO update the JSON string below
json = "{}"
# create an instance of BinLookupWarning from a JSON string
bin_lookup_warning_instance = BinLookupWarning.from_json(json)
# print the JSON string representation of the object
print(BinLookupWarning.to_json())

# convert the object into a dict
bin_lookup_warning_dict = bin_lookup_warning_instance.to_dict()
# create an instance of BinLookupWarning from a dict
bin_lookup_warning_from_dict = BinLookupWarning.from_dict(bin_lookup_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


