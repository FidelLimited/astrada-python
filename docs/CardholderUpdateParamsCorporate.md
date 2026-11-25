# CardholderUpdateParamsCorporate

The corporate entity that this cardholder is associated with. `legalEntity` is set by the card network and cannot be changed here: it is ignored if sent, and the stored value is kept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The company ID to store on the cardholder, the same value a network bulk feed supplies. See &#x60;cardholder.corporate.id&#x60;. | [optional] 
**employee_id** | **str** | The unique identifier of the employee | [optional] 
**alternative_employee_id** | **str** | An alternative employee identifier, typically configured for specific enterprise integrations. | [optional] 

## Example

```python
from astrada.models.cardholder_update_params_corporate import CardholderUpdateParamsCorporate

# TODO update the JSON string below
json = "{}"
# create an instance of CardholderUpdateParamsCorporate from a JSON string
cardholder_update_params_corporate_instance = CardholderUpdateParamsCorporate.from_json(json)
# print the JSON string representation of the object
print(CardholderUpdateParamsCorporate.to_json())

# convert the object into a dict
cardholder_update_params_corporate_dict = cardholder_update_params_corporate_instance.to_dict()
# create an instance of CardholderUpdateParamsCorporate from a dict
cardholder_update_params_corporate_from_dict = CardholderUpdateParamsCorporate.from_dict(cardholder_update_params_corporate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


