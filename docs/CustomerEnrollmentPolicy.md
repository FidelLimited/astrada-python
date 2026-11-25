# CustomerEnrollmentPolicy

The customer-writable subset of the enrollment policy: the three unified-SDK rails. All other fields (`linkAnotherCard`, `bankEnrollmentLocked`, and the deprecated `bulkEnrollmentEnabled`) are managed on the internal enrollment-policy endpoints and are ignored if sent here. The `200` names every ignored key, these and misspelled ones alike, in `ignoredFields`.  Fields are optional and nullable; absent fields leave the current value unchanged, explicit `null` clears the subaccount-level value. A cleared rail falls back to the account-level value when one is set; only when neither level sets the rail does it disappear from reads, letting the host page's client configuration and then the SDK's card-only default apply. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_enrollment** | **bool** | Whether the unified SDK offers manual card enrollment (PAN entry + 3DS verification).  | [optional] 
**bank_enrollment** | **str** | Whether the unified SDK offers bank linking. In SDK v2 the bank link is a route after the card number, not a separate tile: &#x60;on&#x60; offers it for every network that can link a bank (SDK v1 shows a chooser tile instead); &#x60;amex-only&#x60; keeps it reachable only via the American Express card number; &#x60;amex-visa&#x60; is the American Express route plus a Visa rule: a Visa card enrolls through &#x60;POST /card-subscriptions&#x60; only when it is classified as business, and the SDK sends every other Visa card to the bank route, except a debit or prepaid one (a temporary mode for programs whose Visa approval is pending: expect it to be retired once approval lands; do not build long-lived integrations on it); &#x60;off&#x60; disables it (American Express cards then can&#39;t enroll unless a bulk program qualifies).  Before setting &#x60;amex-visa&#x60;, confirm with your Astrada contact that the SDK release supporting it is live: older SDK bundles treat unknown rail values as &#x60;off&#x60;, which disables bank linking entirely, the existing American Express pivot included.  Astrada can lock the account&#39;s &#x60;bankEnrollment&#x60;: the subaccount&#39;s &#x60;enrollmentPolicy&#x60; then returns &#x60;bankEnrollmentLocked: true&#x60;. While it is locked, the account&#39;s value applies. The value you set here is kept, and has no effect until the lock is removed.  An &#x60;amex-visa&#x60; set on the account applies to every subaccount in the same way, without a lock: the subaccount&#39;s &#x60;enrollmentPolicy&#x60; returns &#x60;amex-visa&#x60; whatever value you set here. The value you set is kept, and has no effect while the account&#39;s value is &#x60;amex-visa&#x60;.  | [optional] 
**bulk_enrollment** | **str** | Whether the unified SDK offers network bulk-feed enrollment for bulk-capable programs. In SDK v2 the bulk flow is the kickoff form, reached from the program screen or the callout after the card number (SDK v1 shows a bulk wizard). &#x60;suggested&#x60; offers it next to a connect-this-card-now option; &#x60;forced&#x60; makes it the only path for bulk-capable cards; &#x60;off&#x60; skips bulk routing entirely (direct card form).  | [optional] 

## Example

```python
from astrada.models.customer_enrollment_policy import CustomerEnrollmentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerEnrollmentPolicy from a JSON string
customer_enrollment_policy_instance = CustomerEnrollmentPolicy.from_json(json)
# print the JSON string representation of the object
print(CustomerEnrollmentPolicy.to_json())

# convert the object into a dict
customer_enrollment_policy_dict = customer_enrollment_policy_instance.to_dict()
# create an instance of CustomerEnrollmentPolicy from a dict
customer_enrollment_policy_from_dict = CustomerEnrollmentPolicy.from_dict(customer_enrollment_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


