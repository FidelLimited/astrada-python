# TeamLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The link&#39;s identifier. | 
**url** | **str** | The link to share. Its secret follows &#x60;#&#x60;, and only this response returns it. | 
**expires_at** | **datetime** | After this time no session starts from the link. | 
**max_uses** | **int** | The session starts the link allows. | 

## Example

```python
from astrada.models.team_link import TeamLink

# TODO update the JSON string below
json = "{}"
# create an instance of TeamLink from a JSON string
team_link_instance = TeamLink.from_json(json)
# print the JSON string representation of the object
print(TeamLink.to_json())

# convert the object into a dict
team_link_dict = team_link_instance.to_dict()
# create an instance of TeamLink from a dict
team_link_from_dict = TeamLink.from_dict(team_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


