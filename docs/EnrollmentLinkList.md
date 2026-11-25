# EnrollmentLinkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**EnrollmentLinkListEmbedded**](EnrollmentLinkListEmbedded.md) |  | 
**links** | [**PageLinks**](PageLinks.md) |  | 

## Example

```python
from astrada.models.enrollment_link_list import EnrollmentLinkList

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkList from a JSON string
enrollment_link_list_instance = EnrollmentLinkList.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkList.to_json())

# convert the object into a dict
enrollment_link_list_dict = enrollment_link_list_instance.to_dict()
# create an instance of EnrollmentLinkList from a dict
enrollment_link_list_from_dict = EnrollmentLinkList.from_dict(enrollment_link_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


