# EnrollmentMethodsResultBinInfo

Best-effort card metadata for the looked-up BIN, resolved server-side. Present only when the issuer name is known and omitted otherwise; the other fields are best-effort and may each be omitted even when `binInfo` is present. Lets integrators read this data without the `cards:read` scope that `GET /bin-lookup` requires (it rides on this endpoint's `enrollment-methods:write` scope); the SDK surfaces it on the bulk-enrollment success payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_name** | **str** | The issuing bank&#39;s name for this BIN. | 
**issuer_country** | **str** | The country of the issuing bank following ISO 3166-1 alpha-3, for example &#x60;USA&#x60;. Omitted when the reference data does not record it. | [optional] 
**type** | **str** | The card type (e.g., COMMERCIAL, CORPORATE, CONSUMER, SMALL_BUSINESS). Omitted when the reference data does not classify the BIN. | [optional] 
**funding_type** | **str** | The card funding type (e.g., prepaid, debit, credit). Omitted when the reference data does not classify the BIN. | [optional] 
**card_category** | **str** | The card&#39;s classification, with the values of &#x60;cardCategory&#x60; on &#x60;GET /bin-lookup&#x60;. More specific than &#x60;type&#x60;, and set for many BINs where &#x60;type&#x60; is omitted. &#x60;UNKNOWN&#x60; means the card data does not classify the BIN. Omitted when there is no value. For Mastercard it is present only when the response falls back to stored card data. | [optional] 

## Example

```python
from astrada.models.enrollment_methods_result_bin_info import EnrollmentMethodsResultBinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentMethodsResultBinInfo from a JSON string
enrollment_methods_result_bin_info_instance = EnrollmentMethodsResultBinInfo.from_json(json)
# print the JSON string representation of the object
print(EnrollmentMethodsResultBinInfo.to_json())

# convert the object into a dict
enrollment_methods_result_bin_info_dict = enrollment_methods_result_bin_info_instance.to_dict()
# create an instance of EnrollmentMethodsResultBinInfo from a dict
enrollment_methods_result_bin_info_from_dict = EnrollmentMethodsResultBinInfo.from_dict(enrollment_methods_result_bin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


