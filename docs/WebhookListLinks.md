# WebhookListLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | [optional] 
**next** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.models.webhook_list_links import WebhookListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookListLinks from a JSON string
webhook_list_links_instance = WebhookListLinks.from_json(json)
# print the JSON string representation of the object
print(WebhookListLinks.to_json())

# convert the object into a dict
webhook_list_links_dict = webhook_list_links_instance.to_dict()
# create an instance of WebhookListLinks from a dict
webhook_list_links_from_dict = WebhookListLinks.from_dict(webhook_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


