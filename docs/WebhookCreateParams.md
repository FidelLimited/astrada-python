# WebhookCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**description** | **str** |  | [optional] 
**event_types** | **List[str]** |  | 
**subaccount_id** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from astrada.models.webhook_create_params import WebhookCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateParams from a JSON string
webhook_create_params_instance = WebhookCreateParams.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateParams.to_json())

# convert the object into a dict
webhook_create_params_dict = webhook_create_params_instance.to_dict()
# create an instance of WebhookCreateParams from a dict
webhook_create_params_from_dict = WebhookCreateParams.from_dict(webhook_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


