# SubaccountUpdateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**SubaccountLinks**](SubaccountLinks.md) |  | 
**account_id** | **str** | The unique identifier of the account related to this entity. | 
**id** | **str** | The unique identifier of this subaccount entity. | 
**name** | **str** | The name of this subaccount entity. | 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 
**configurations** | [**SubaccountConfiguration**](SubaccountConfiguration.md) |  | 
**verification_policy** | [**VerificationPolicy**](VerificationPolicy.md) | The subaccount&#39;s card verification policy.  - Copied from the account when the subaccount is created; &#x60;PATCH&#x60; changes it field by field. - The tier and &#x60;sandbox&#x60; use only this value (in the sandbox environment, &#x60;sandbox&#x60; counts as &#x60;true&#x60; for every subaccount). - &#x60;failedAttemptLockout&#x60; falls back to the account&#39;s while the subaccount&#39;s policy, or its &#x60;failedAttemptLockout&#x60;, is &#x60;null&#x60;.  | [optional] 
**enforce_issuer_country** | **bool** | Whether card enrollment is restricted to issuer countries within the account&#39;s capabilities. Account-level setting, resolved onto the subaccount at read time; there is no subaccount-level override, so the subaccount never stores its own value. Absent on the subaccount list; &#x60;false&#x60; when the account has not enabled it.  | [optional] 
**network_blocked_cards** | [**Dict[str, SubaccountNetworkBlockedCardsValue]**](SubaccountNetworkBlockedCardsValue.md) | Platform-level enrollment rules resolved from the network configuration at read time. Applied before the subaccount&#39;s own block lists and not configurable per account or subaccount. Keyed by network (&#x60;VISA&#x60;, &#x60;MASTERCARD&#x60;, &#x60;AMEX&#x60;); a network with no rules is omitted. A rule matches a card when &#x60;cardType&#x60; equals the BIN&#39;s &#x60;type&#x60; and &#x60;fundingTypes&#x60; contains the BIN&#39;s &#x60;fundingType&#x60;. An omitted or empty &#x60;fundingTypes&#x60; matches every funding type. Enrolling a matching card fails with &#x60;card_subscription.network_blocking_card&#x60;.  | [optional] [readonly] 
**amex_product** | [**SubaccountAmexProduct**](SubaccountAmexProduct.md) |  | [optional] 
**enrollment_policy** | [**SubaccountEnrollmentPolicy**](SubaccountEnrollmentPolicy.md) | Enrollment policy. Fields are the EFFECTIVE values: the unified-SDK rails (&#x60;cardEnrollment&#x60;, &#x60;bankEnrollment&#x60;, &#x60;bulkEnrollment&#x60;) and the deprecated &#x60;bulkEnrollmentEnabled&#x60; resolve as subaccount-overrides-account, and are SPARSE; only explicitly-configured fields appear; &#x60;linkAnotherCard&#x60; resolves live to &#x60;false&#x60; when either level stores an explicit &#x60;false&#x60; (absent everywhere &#x3D; enabled, field omitted). &#x60;bankEnrollmentLocked&#x60; is read-only: it appears, as &#x60;true&#x60;, only while the account has locked &#x60;bankEnrollment&#x60;, and &#x60;bankEnrollment&#x60; is then the account&#39;s value. &#x60;null&#x60; means the subaccount stores no policy and neither a rail nor &#x60;linkAnotherCard&#x60; is set at the account level (account-level admin snapshot fields do not surface through a &#x60;null&#x60; here).  | [optional] 
**plaid_end_customer** | [**PlaidEndCustomer**](PlaidEndCustomer.md) | Plaid End-Customer routing. &#x60;enabled&#x60; is the EFFECTIVE value; resolved from the parent account. This object is account-level only: there is no subaccount-level override, so the subaccount never stores its own value. &#x60;null&#x60; means the account has Plaid End-Customer routing disabled.  | [optional] 
**bank_linking_policy** | [**BankLinkingPolicy**](BankLinkingPolicy.md) | Admin-managed bank-linking policy. Fields are the EFFECTIVE values; per-field live resolution against the parent account (subaccount field if set, else account, else &#x60;null&#x60;). A whole-&#x60;null&#x60; policy means neither level has one set. The credit-only system default (&#x60;accountTypes: [credit]&#x60;) is applied downstream at bank-link creation, not materialized in this read.  | [optional] 
**consent_policy** | [**ConsentPolicy**](ConsentPolicy.md) | The effective consent policy, set by Astrada. A subaccount with no &#x60;consentPolicy&#x60; behaves as &#x60;log&#x60; with every channel allowed, and an account &#x60;mode&#x60; of &#x60;off&#x60; turns the mode off for every subaccount. Which mode a new or existing account starts in: [When consent is required](https://docs.astrada.co/docs/direct-api-card-enrollment-integration#when-consent-is-required).  | [optional] 
**ignored_fields** | **List[str]** | The keys of the request&#39;s &#x60;enrollmentPolicy&#x60; that this endpoint ignored, each written as &#x60;enrollmentPolicy.&lt;key&gt;&#x60;: every key other than &#x60;cardEnrollment&#x60;, &#x60;bankEnrollment&#x60; and &#x60;bulkEnrollment&#x60;, such as a misspelled key or a field Astrada manages. Nothing is stored for them, and the accepted keys are applied as usual. Absent when no key was ignored.  | [optional] 

## Example

```python
from astrada.models.subaccount_update_result import SubaccountUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountUpdateResult from a JSON string
subaccount_update_result_instance = SubaccountUpdateResult.from_json(json)
# print the JSON string representation of the object
print(SubaccountUpdateResult.to_json())

# convert the object into a dict
subaccount_update_result_dict = subaccount_update_result_instance.to_dict()
# create an instance of SubaccountUpdateResult from a dict
subaccount_update_result_from_dict = SubaccountUpdateResult.from_dict(subaccount_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


