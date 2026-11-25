# EnrollmentMethodsParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **str** | The card&#39;s Bank Identification Number (BIN), consisting of the first 6 to 11 digits of the card number. Providing more digits yields more precise results: for example, two cards that share the same 6-digit BIN may support different enrollment methods. Send as many digits as you have, up to 11. For Mastercard, 8 digits or fewer can match several card ranges; when those ranges disagree, &#x60;bulkLikelihood&#x60; is capped at &#x60;medium&#x60; (a &#x60;proven&#x60; BIN keeps &#x60;proven&#x60;), and at &#x60;medium&#x60; a Mastercard card is not offered &#x60;network-bulk&#x60;. | 
**subaccount_id** | **str** | The subaccount the card would enroll under. With it, the response adds &#x60;singleDecision&#x60; when the subaccount&#39;s controls can be run. It must be one of your account&#39;s subaccounts, otherwise the request gets &#x60;400&#x60;. With an enrollment link session&#39;s token it must be the session&#39;s own subaccount, otherwise the request gets &#x60;403&#x60;. | [optional] 

## Example

```python
from astrada.models.enrollment_methods_params import EnrollmentMethodsParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentMethodsParams from a JSON string
enrollment_methods_params_instance = EnrollmentMethodsParams.from_json(json)
# print the JSON string representation of the object
print(EnrollmentMethodsParams.to_json())

# convert the object into a dict
enrollment_methods_params_dict = enrollment_methods_params_instance.to_dict()
# create an instance of EnrollmentMethodsParams from a dict
enrollment_methods_params_from_dict = EnrollmentMethodsParams.from_dict(enrollment_methods_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


