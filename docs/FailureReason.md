# FailureReason

Normalized, customer-facing reason a card verification failed. Present only when the verification `state` is `failed`. `category`, `description` and `retryable` are always present; `issuerMessage` and `acsReferences` appear only when the issuer returned them (typically on a frictionless decline; when the issuer renders its own challenge UI no per-attempt message is available). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Stable, provider-agnostic failure category an integrator can branch on without enumerating raw issuer codes.  | 
**description** | **str** | Human-readable explanation of the failure, safe to relay to the cardholder. | 
**retryable** | **bool** | Whether the cardholder can retry now and plausibly succeed. | 
**issuer_message** | **str** | The issuer&#39;s own cardholder-facing message, when provided (frictionless declines only). | [optional] 
**code** | **str** | Raw provider reason code (e.g. a 3DS &#x60;transStatusReason&#x60; or a Stripe &#x60;decline_code&#x60;), surfaced for support escalation.  | [optional] 
**provider_message** | **str** | The payment provider&#39;s cardholder-safe message for the specific failure code (e.g. \&quot;Your card does not support this type of purchase.\&quot;). Finer-grained than the category-level &#x60;description&#x60;; absent when the provider supplied none.  | [optional] 
**advice_code** | **str** | The issuer&#39;s advice code on authorization declines, verbatim from the payment provider. Documented values: &#x60;try_again_later&#x60;, &#x60;do_not_try_again&#x60;, &#x60;confirm_card_data&#x60;; values the provider introduces later pass through unchanged. Absent when the issuer gave no advice (e.g. 3-D Secure authentication failures).  | [optional] 
**acs_references** | [**FailureReasonAcsReferences**](FailureReasonAcsReferences.md) |  | [optional] 

## Example

```python
from astrada.models.failure_reason import FailureReason

# TODO update the JSON string below
json = "{}"
# create an instance of FailureReason from a JSON string
failure_reason_instance = FailureReason.from_json(json)
# print the JSON string representation of the object
print(FailureReason.to_json())

# convert the object into a dict
failure_reason_dict = failure_reason_instance.to_dict()
# create an instance of FailureReason from a dict
failure_reason_from_dict = FailureReason.from_dict(failure_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


