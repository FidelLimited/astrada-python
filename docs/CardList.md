# CardList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**OffsetPageLinks**](OffsetPageLinks.md) |  | 
**embedded** | [**CardListEmbedded**](CardListEmbedded.md) |  | 
**total_items** | **int** | Total number of cards matching the search criteria | 

## Example

```python
from astrada.models.card_list import CardList

# TODO update the JSON string below
json = "{}"
# create an instance of CardList from a JSON string
card_list_instance = CardList.from_json(json)
# print the JSON string representation of the object
print(CardList.to_json())

# convert the object into a dict
card_list_dict = card_list_instance.to_dict()
# create an instance of CardList from a dict
card_list_from_dict = CardList.from_dict(card_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


