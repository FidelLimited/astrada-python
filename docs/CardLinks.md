# CardLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**cardholder** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.models.card_links import CardLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CardLinks from a JSON string
card_links_instance = CardLinks.from_json(json)
# print the JSON string representation of the object
print(CardLinks.to_json())

# convert the object into a dict
card_links_dict = card_links_instance.to_dict()
# create an instance of CardLinks from a dict
card_links_from_dict = CardLinks.from_dict(card_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


