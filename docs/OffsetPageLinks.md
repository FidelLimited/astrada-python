# OffsetPageLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**first** | [**Link**](Link.md) |  | [optional] 
**next** | [**Link**](Link.md) |  | [optional] 
**prev** | [**Link**](Link.md) |  | [optional] 
**last** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.models.offset_page_links import OffsetPageLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OffsetPageLinks from a JSON string
offset_page_links_instance = OffsetPageLinks.from_json(json)
# print the JSON string representation of the object
print(OffsetPageLinks.to_json())

# convert the object into a dict
offset_page_links_dict = offset_page_links_instance.to_dict()
# create an instance of OffsetPageLinks from a dict
offset_page_links_from_dict = OffsetPageLinks.from_dict(offset_page_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


