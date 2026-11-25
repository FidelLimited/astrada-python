# PageLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**next** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.models.page_links import PageLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PageLinks from a JSON string
page_links_instance = PageLinks.from_json(json)
# print the JSON string representation of the object
print(PageLinks.to_json())

# convert the object into a dict
page_links_dict = page_links_instance.to_dict()
# create an instance of PageLinks from a dict
page_links_from_dict = PageLinks.from_dict(page_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


