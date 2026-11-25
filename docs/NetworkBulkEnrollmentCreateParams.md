# NetworkBulkEnrollmentCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Optional. Your idempotency key for this enrollment, unique per account. Repeating the request with a &#x60;requestId&#x60; that was already used returns the stored enrollment, whole and unchanged, with &#x60;200&#x60; instead of creating a second one with &#x60;201&#x60;. A request without a &#x60;requestId&#x60; is never a replay: it creates a new enrollment unless its program already has an open kickoff, which answers &#x60;200&#x60; with that kickoff&#39;s summary.  | [optional] 
**subaccount_id** | **str** | The subaccount the card program enrolls into. Must belong to the calling account. | 
**network** | **str** | The network of the card program. | 
**bin** | **str** | The leading 6 to 11 digits of the card that opened the kickoff. | 
**bin_info** | [**NetworkBulkEnrollmentCreateParamsBinInfo**](NetworkBulkEnrollmentCreateParamsBinInfo.md) |  | [optional] 
**company** | [**NetworkBulkCompanyParams**](NetworkBulkCompanyParams.md) |  | 
**card_admin** | [**NetworkBulkEnrollmentCreateParamsCardAdmin**](NetworkBulkEnrollmentCreateParamsCardAdmin.md) |  | 
**bank_contact** | [**NetworkBulkBankContactParams**](NetworkBulkBankContactParams.md) |  | [optional] 
**card_count_band** | **str** | Optional. The estimated number of cards in the program, as a band. An estimate helps the bank size the file. | [optional] 
**card_count** | **int** | Optional. The estimated number of cards in the program. When sent, it decides the stored &#x60;cardCountBand&#x60;, even if &#x60;cardCountBand&#x60; is also sent. | [optional] 
**outreach** | **str** | Who contacts the bank. &#x60;astrada&#x60;: Astrada reaches out to the bank, copying the company and the card admin. &#x60;self&#x60;: the company emails the bank itself and copies onboarding@astrada.co so Astrada can guide the setup.  | 
**consent** | [**NetworkBulkEnrollmentCreateParamsConsent**](NetworkBulkEnrollmentCreateParamsConsent.md) |  | 
**customer_reference_id** | **str** | Optional. Your own id for this enrollment, echoed back on the resource. | [optional] 

## Example

```python
from astrada.models.network_bulk_enrollment_create_params import NetworkBulkEnrollmentCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentCreateParams from a JSON string
network_bulk_enrollment_create_params_instance = NetworkBulkEnrollmentCreateParams.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentCreateParams.to_json())

# convert the object into a dict
network_bulk_enrollment_create_params_dict = network_bulk_enrollment_create_params_instance.to_dict()
# create an instance of NetworkBulkEnrollmentCreateParams from a dict
network_bulk_enrollment_create_params_from_dict = NetworkBulkEnrollmentCreateParams.from_dict(network_bulk_enrollment_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


