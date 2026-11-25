# EnrollmentLinkListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_links** | [**List[EnrollmentLink]**](EnrollmentLink.md) |  | 

## Example

```python
from astrada.models.enrollment_link_list_embedded import EnrollmentLinkListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentLinkListEmbedded from a JSON string
enrollment_link_list_embedded_instance = EnrollmentLinkListEmbedded.from_json(json)
# print the JSON string representation of the object
print(EnrollmentLinkListEmbedded.to_json())

# convert the object into a dict
enrollment_link_list_embedded_dict = enrollment_link_list_embedded_instance.to_dict()
# create an instance of EnrollmentLinkListEmbedded from a dict
enrollment_link_list_embedded_from_dict = EnrollmentLinkListEmbedded.from_dict(enrollment_link_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


