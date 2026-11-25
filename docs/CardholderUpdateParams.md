# CardholderUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subaccount_id** | **str** | The unique identifier of the subaccount related to the card | 
**first_name** | **str** | The first name of the cardholder | [optional] 
**last_name** | **str** | The last name of the cardholder | [optional] 
**email** | **str** | Cardholder email address | [optional] 
**postal_code** | **str** | Cardholder postal code. Format varies by country; no validation or normalization is applied. | [optional] 
**corporate** | [**CardholderUpdateParamsCorporate**](CardholderUpdateParamsCorporate.md) |  | [optional] 

## Example

```python
from astrada.models.cardholder_update_params import CardholderUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of CardholderUpdateParams from a JSON string
cardholder_update_params_instance = CardholderUpdateParams.from_json(json)
# print the JSON string representation of the object
print(CardholderUpdateParams.to_json())

# convert the object into a dict
cardholder_update_params_dict = cardholder_update_params_instance.to_dict()
# create an instance of CardholderUpdateParams from a dict
cardholder_update_params_from_dict = CardholderUpdateParams.from_dict(cardholder_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


