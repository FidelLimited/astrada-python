# EnrollmentMethodsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_enrollment_methods** | **List[str]** | The enrollment methods this card can use: &#x60;network-bulk&#x60; when &#x60;bulkLikelihood&#x60; is present and not &#x60;none&#x60; (for Visa and Mastercard cards, only &#x60;high&#x60; or &#x60;proven&#x60;), and &#x60;cardholder-single&#x60; when &#x60;singleEligible&#x60; is &#x60;true&#x60;. Empty when neither applies, for example for a card from a country Astrada doesn&#39;t cover for its network. | 
**bulk_likelihood** | **str** | Graded likelihood that network-bulk enrollment will succeed for this BIN. A country-coverage veto forces &#x60;none&#x60;. Omitted when it could not be determined for this request; &#x60;unavailable&#x60; then lists it. &#x60;none&#x60; is only returned when it was established, never because the data was unavailable. Whether &#x60;network-bulk&#x60; is offered is in &#x60;availableEnrollmentMethods&#x60;: for Visa and Mastercard cards it needs &#x60;high&#x60; or &#x60;proven&#x60;. | [optional] 
**single_eligible** | **bool** | Whether cardholder-single enrollment is supported for this BIN. When the response has &#x60;singleDecision&#x60;, it equals &#x60;singleDecision.allowed&#x60;. | [optional] 
**single_decision** | [**EnrollmentMethodsResultSingleDecision**](EnrollmentMethodsResultSingleDecision.md) |  | [optional] 
**bin_info** | [**EnrollmentMethodsResultBinInfo**](EnrollmentMethodsResultBinInfo.md) |  | [optional] 
**unavailable** | **List[str]** | Response fields whose value could not be determined for this request, for example when live card data was temporarily unavailable and the stored card data doesn&#39;t decide the grade. Today it can only contain &#x60;bulkLikelihood&#x60;; more values may be added, so ignore any you don&#39;t recognize. Omitted when every field was determined. | [optional] 

## Example

```python
from astrada.models.enrollment_methods_result import EnrollmentMethodsResult

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentMethodsResult from a JSON string
enrollment_methods_result_instance = EnrollmentMethodsResult.from_json(json)
# print the JSON string representation of the object
print(EnrollmentMethodsResult.to_json())

# convert the object into a dict
enrollment_methods_result_dict = enrollment_methods_result_instance.to_dict()
# create an instance of EnrollmentMethodsResult from a dict
enrollment_methods_result_from_dict = EnrollmentMethodsResult.from_dict(enrollment_methods_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


