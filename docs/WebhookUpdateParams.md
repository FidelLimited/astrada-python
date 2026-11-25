# WebhookUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**event_types** | **List[str]** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from astrada.models.webhook_update_params import WebhookUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUpdateParams from a JSON string
webhook_update_params_instance = WebhookUpdateParams.from_json(json)
# print the JSON string representation of the object
print(WebhookUpdateParams.to_json())

# convert the object into a dict
webhook_update_params_dict = webhook_update_params_instance.to_dict()
# create an instance of WebhookUpdateParams from a dict
webhook_update_params_from_dict = WebhookUpdateParams.from_dict(webhook_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


