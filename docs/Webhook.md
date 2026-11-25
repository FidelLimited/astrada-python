# Webhook

Astrada's Webhook resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SelfLinks**](SelfLinks.md) |  | 
**id** | **str** |  | 
**url** | **str** |  | 
**description** | **str** |  | 
**event_types** | **List[str]** |  | 
**subaccount_id** | **str** |  | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 
**enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from astrada.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


