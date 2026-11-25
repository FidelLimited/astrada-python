# TransactionMatchLinks

HAL-style links to related resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**card_transaction** | [**Link**](Link.md) |  | 
**bank_transaction** | [**Link**](Link.md) |  | 
**card** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from astrada.banking.models.transaction_match_links import TransactionMatchLinks

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMatchLinks from a JSON string
transaction_match_links_instance = TransactionMatchLinks.from_json(json)
# print the JSON string representation of the object
print(TransactionMatchLinks.to_json())

# convert the object into a dict
transaction_match_links_dict = transaction_match_links_instance.to_dict()
# create an instance of TransactionMatchLinks from a dict
transaction_match_links_from_dict = TransactionMatchLinks.from_dict(transaction_match_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


