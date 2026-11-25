# NetworkBulkFeedCreateCommon

The fields every network's bulk feed create body shares. Some apply to one network only; the API rejects them with a 400 for any other network or feed type:  | Field | Applies to | |---|---| | `networkReference`, `subaccountId`, `networkBulkEnrollmentId`, `expectedCardCount` | Every network | | `transactionStartDate` | `MASTERCARD` (type `SMARTDATA`) | | `cardCount`, `newCards` | `VISA` with type `VBDS` or no `type`, sandbox only | | `panFormat` | `AMEX` (type `GL`), sandbox only | 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_reference** | **str** | The identifier associated with the card network&#39;s bulk enrollment feed. Its format depends on the network. For Amex, the Recipient ID in the format &#39;R{RecipientId}&#39;, such as &#39;R123456&#39;, or the 6-digit Amex corporate ID (CID), such as &#39;014640&#39;. For Mastercard, the Delivery ID, such as &#39;G1234567&#39;; its format is not checked. For Visa-VBDS, the RPIC: four numeric parts joined by underscores, &#39;RegionId_ProcessorId_IssuerId_CompanyId&#39;, such as &#39;1_123_45_6789&#39;. For Visa-VCF, the same RPIC &#39;RegionId_ProcessorId_IssuerId_CompanyId&#39;, such as &#39;1_123_45_6789&#39; (the region segment is ignored), or the 3-segment PIC form &#39;ProcessorId_IssuerId_CompanyId&#39;, such as &#39;123_45_6789&#39;. For Visa, a part that is not all digits is refused with &#x60;400&#x60;, naming the part. Spaces around each part and leading zeros are removed before the reference is stored. For more details on our bulk enrollment process, refer to [this guide](https://docs.astrada.co/docs/network-bulk-enrollment).  | 
**subaccount_id** | **str** | The subaccount identifier | 
**network_bulk_enrollment_id** | **str** | Optional. The network bulk enrollment (&#x60;POST /network-bulk-enrollments&#x60;) this feed fulfils. The enrollment must exist on this account, its &#x60;subaccountId&#x60; and &#x60;network&#x60; must equal the body&#39;s, and its &#x60;state&#x60; must be &#x60;requested&#x60; or &#x60;feed-created&#x60; (re-registering after a failed feed is allowed). Any mismatch is rejected with a 400 whose &#x60;detail&#x60; reads &#x60;networkBulkEnrollmentId does not match this subaccount and network&#x60;. When the feed is created, the enrollment&#39;s &#x60;networkBulkFeedId&#x60; is set and its state moves to &#x60;feed-created&#x60;; the link lives on the enrollment, so the feed representation is unchanged. A duplicate feed still answers 409 and leaves the enrollment untouched.  | [optional] 
**expected_card_count** | **int** | The expected number of cards that will be enrolled under this bulk feed. Optional. When provided, the value is echoed back on the response and on the &#x60;networkbulkfeed.statechanged&#x60; webhook payload.  | [optional] 
**transaction_start_date** | **date** | Optional. Transactions posted on or after this calendar date (&#x60;YYYY-MM-DD&#x60;, a valid date, not in the future) are taken in for this feed&#39;s deliveries, replacing the default window, which keeps only transactions posted on or after the date 15 days before each file&#39;s delivery date (in UTC). On a file that serves several subaccounts, the earliest window among them applies to the whole file. Currently supported for &#x60;SMARTDATA&#x60; feeds only; requests containing this field for any other feed type are rejected with a 400. When unset, the 15-day window applies. Also settable later via &#x60;PATCH /network-bulk-feeds/{networkBulkFeedId}&#x60;. The comparison is calendar-day based in UTC: the network&#39;s posting date is a date-only field, so a value of e.g. &#x60;2026-06-30&#x60; includes every transaction whose posting date is 2026-06-30 or later, with no local-timezone adjustment.  | [optional] 
**card_count** | **int** | Sandbox only. The number of synthetic Visa cards to create when this bulk feed is created in the sandbox environment. The cards are drawn from the head of Astrada&#39;s published sandbox Visa test-card pool: the same cards every feed, deduplicated once enrolled (matching the &#x60;cardCount&#x60; field on the &#x60;SimulateBulkFeedFile*&#x60; operations). Only valid for pulled Visa feeds: &#x60;type: VBDS&#x60;, or a &#x60;VISA&#x60; feed sent without &#x60;type&#x60;. Requests containing this field outside the sandbox environment, or for any other feed type, are rejected with a 400. When omitted on such a feed in sandbox, 5 starter cards are created.  | [optional] 
**new_cards** | **int** | Deprecated alias of &#x60;cardCount&#x60;; use &#x60;cardCount&#x60; instead. When both fields are provided, &#x60;cardCount&#x60; takes precedence. Same constraints and behavior.  | [optional] 
**pan_format** | **str** | Sandbox only. Selects how card numbers arrive for this feed: &#x60;encrypted&#x60; (raw PAN) or &#x60;tokenized&#x60; (Amex network token / &#x60;tokenizedId&#x60;). Only valid for &#x60;type: GL&#x60; (AMEX) feeds. Requests containing this field outside the sandbox environment, or for any non-GL feed type, are rejected with a 400. When omitted, the feed defaults to &#x60;encrypted&#x60;.  | [optional] 

## Example

```python
from astrada.models.network_bulk_feed_create_common import NetworkBulkFeedCreateCommon

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkBulkFeedCreateCommon from a JSON string
network_bulk_feed_create_common_instance = NetworkBulkFeedCreateCommon.from_json(json)
# print the JSON string representation of the object
print(NetworkBulkFeedCreateCommon.to_json())

# convert the object into a dict
network_bulk_feed_create_common_dict = network_bulk_feed_create_common_instance.to_dict()
# create an instance of NetworkBulkFeedCreateCommon from a dict
network_bulk_feed_create_common_from_dict = NetworkBulkFeedCreateCommon.from_dict(network_bulk_feed_create_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


