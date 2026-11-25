# NetworkBulkEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**NetworkBulkEnrollmentLinks**](NetworkBulkEnrollmentLinks.md) |  | 
**id** | **str** | The unique identifier of this network bulk enrollment. | 
**subaccount_id** | **str** | The unique identifier of the subaccount the card program enrolls into. | 
**network** | **str** | The network of the card program. | 
**bin** | **str** | The leading 6 to 11 digits of the card that opened the kickoff, exactly as submitted. | 
**bin_info** | [**NetworkBulkEnrollmentBinInfo**](NetworkBulkEnrollmentBinInfo.md) |  | 
**company** | [**NetworkBulkEnrollmentCompany**](NetworkBulkEnrollmentCompany.md) |  | 
**card_admin** | [**NetworkBulkEnrollmentCardAdmin**](NetworkBulkEnrollmentCardAdmin.md) |  | 
**bank_contact** | [**NetworkBulkBankContact**](NetworkBulkBankContact.md) |  | 
**card_count_band** | **str** | The estimated number of cards in the program, as a band. &#x60;null&#x60; when not provided. | 
**outreach** | **str** | Who contacts the bank. &#x60;astrada&#x60;: Astrada reaches out to the bank, copying the company and the card admin. &#x60;self&#x60;: the company emails the bank itself and copies onboarding@astrada.co so Astrada can guide the setup.  | 
**consent** | [**NetworkBulkEnrollmentConsent**](NetworkBulkEnrollmentConsent.md) |  | 
**state** | **str** | &#x60;requested&#x60; until a network bulk feed is registered with this enrollment&#39;s id, then &#x60;feed-created&#x60;. Astrada does not set &#x60;cancelled&#x60; today. A kickoff that is never followed by a feed keeps &#x60;requested&#x60;, also after its 90 days (see &#x60;POST /network-bulk-enrollments&#x60;).  | 
**network_bulk_feed_id** | **str** | The network bulk feed registered with this enrollment&#39;s id on &#x60;POST /network-bulk-feeds&#x60;. &#x60;null&#x60; until then. | 
**customer_reference_id** | **str** | An optional id passed by the customer to associate a context with the enrollment. &#x60;null&#x60; when not provided. | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.models.network_bulk_enrollment import NetworkBulkEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkEnrollment from a JSON string
network_bulk_enrollment_instance = NetworkBulkEnrollment.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkEnrollment.to_json())

# convert the object into a dict
network_bulk_enrollment_dict = network_bulk_enrollment_instance.to_dict()
# create an instance of NetworkBulkEnrollment from a dict
network_bulk_enrollment_from_dict = NetworkBulkEnrollment.from_dict(network_bulk_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


