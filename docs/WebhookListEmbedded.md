# WebhookListEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Webhook]**](Webhook.md) |  | [optional] 

## Example

```python
from astrada.models.webhook_list_embedded import WebhookListEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookListEmbedded from a JSON string
webhook_list_embedded_instance = WebhookListEmbedded.from_json(json)
# print the JSON string representation of the object
print(WebhookListEmbedded.to_json())

# convert the object into a dict
webhook_list_embedded_dict = webhook_list_embedded_instance.to_dict()
# create an instance of WebhookListEmbedded from a dict
webhook_list_embedded_from_dict = WebhookListEmbedded.from_dict(webhook_list_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


