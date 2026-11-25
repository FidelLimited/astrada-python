# NetworkBulkEnrollmentCreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**NetworkBulkEnrollmentSummaryLinks**](NetworkBulkEnrollmentSummaryLinks.md) |  | 
**id** | **str** | The unique identifier of the open kickoff. | 
**subaccount_id** | **str** | The subaccount of the open kickoff, the same as the request&#39;s. | 
**network** | **str** | The network of the open kickoff, the same as the request&#39;s. | 
**bin** | **str** | The leading 6 to 11 digits of the card that opened the kickoff, exactly as submitted. | 
**bin_info** | [**NetworkBulkEnrollmentBinInfo**](NetworkBulkEnrollmentBinInfo.md) |  | 
**company** | [**NetworkBulkEnrollmentCompany**](NetworkBulkEnrollmentCompany.md) |  | 
**card_admin** | [**NetworkBulkEnrollmentCardAdmin**](NetworkBulkEnrollmentCardAdmin.md) |  | 
**bank_contact** | [**NetworkBulkBankContact**](NetworkBulkBankContact.md) |  | 
**card_count_band** | **str** | The estimated number of cards in the program, as a band. &#x60;null&#x60; when not provided. | 
**outreach** | **str** | Who contacts the bank. &#x60;astrada&#x60;: Astrada reaches out to the bank, copying the company and the card admin. &#x60;self&#x60;: the company emails the bank itself and copies onboarding@astrada.co so Astrada can guide the setup.  | 
**consent** | [**NetworkBulkEnrollmentConsent**](NetworkBulkEnrollmentConsent.md) |  | 
**state** | **str** | The open kickoff&#39;s state. &#x60;requested&#x60;: it was created less than 90 days ago and no feed has been registered against it yet. &#x60;feed-created&#x60;: a feed was registered against it and that feed is live.  | 
**network_bulk_feed_id** | **str** | The live feed registered against the open kickoff. &#x60;null&#x60; while the kickoff is &#x60;requested&#x60;. | 
**customer_reference_id** | **str** | An optional id passed by the customer to associate a context with the enrollment. &#x60;null&#x60; when not provided. | 
**created_at** | **datetime** | When the open kickoff was created, in UTC, following ISO 8601 format. Its 90-day window counts from this time. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 
**already_open** | **bool** | Always &#x60;true&#x60;. Tells this summary apart from the full enrollment. | 
**request_id** | **str** | The &#x60;requestId&#x60; this request sent, or &#x60;null&#x60; when it sent none. It is never the &#x60;requestId&#x60; the open kickoff was stored under.  | 

## Example

```python
from astrada.models.network_bulk_enrollment_create_result import NetworkBulkEnrollmentCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollmentCreateResult from a JSON string
network_bulk_enrollment_create_result_instance = NetworkBulkEnrollmentCreateResult.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollmentCreateResult.to_json())

# convert the object into a dict
network_bulk_enrollment_create_result_dict = network_bulk_enrollment_create_result_instance.to_dict()
# create an instance of NetworkBulkEnrollmentCreateResult from a dict
network_bulk_enrollment_create_result_from_dict = NetworkBulkEnrollmentCreateResult.from_dict(network_bulk_enrollment_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


