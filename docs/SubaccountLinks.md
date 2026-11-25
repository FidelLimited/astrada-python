# SubaccountLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**team_link** | [**Link**](Link.md) | Only on &#x60;GET /subaccounts/{subaccountId}&#x60;: &#x60;POST /subaccounts/{subaccountId}/team-link&#x60;, which creates a team link for the subaccount, the \&quot;Invite your team\&quot; action. Present when enrollment links are enabled for the account, the token holds &#x60;card-subscriptions:write&#x60; or &#x60;subaccounts:write&#x60;, and the subaccount&#39;s card enrollment is on (its &#x60;enrollmentPolicy.cardEnrollment&#x60; is not &#x60;false&#x60;). Never offered to an enrollment link session&#39;s token. If the check cannot be made, the link is left out and the read still succeeds.  | [optional] 

## Example

```python
from astrada.models.subaccount_links import SubaccountLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountLinks from a JSON string
subaccount_links_instance = SubaccountLinks.from_json(json)
# print the JSON string representation of the object
print(SubaccountLinks.to_json())

# convert the object into a dict
subaccount_links_dict = subaccount_links_instance.to_dict()
# create an instance of SubaccountLinks from a dict
subaccount_links_from_dict = SubaccountLinks.from_dict(subaccount_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


