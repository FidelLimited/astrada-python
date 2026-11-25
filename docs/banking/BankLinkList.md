# BankLinkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BankLink]**](BankLink.md) |  | 
**pagination** | [**CursorPagination**](CursorPagination.md) |  | 

## Example

```python
from astrada.banking.models.bank_link_list import BankLinkList

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkList from a JSON string
bank_link_list_instance = BankLinkList.from_json(json)
# print the JSON string representation of the object
print(BankLinkList.to_json())

# convert the object into a dict
bank_link_list_dict = bank_link_list_instance.to_dict()
# create an instance of BankLinkList from a dict
bank_link_list_from_dict = BankLinkList.from_dict(bank_link_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


