# CardVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**CardVerificationLinks**](CardVerificationLinks.md) |  | 
**id** | **str** | The unique identifier of the Verification entity. | 
**subaccount_id** | **str** | The unique identifier of the subaccount related to this entity. | 
**card_id** | **str** | The unique identifier of the card related to this entity. | 
**type** | **str** | Verification Step Type | 
**current_step_id** | **str** | The identifier of the next step the client should execute. &#x60;null&#x60; when the verification has no follow-up step; typically because the issuer supports frictionless authentication, or because the card did not require interactive 3DS. When &#x60;null&#x60;, &#x60;state&#x60; will be &#x60;completed&#x60; on the creation response and clients should not call any &#x60;/steps/...&#x60; endpoint.  On retrieved/listed verifications, &#x60;currentStepId&#x60; is also &#x60;null&#x60; with &#x60;state: failed&#x60; when the card was declined synchronously at creation (the creation call returned &#x60;400&#x60;, and the attempt is persisted as a failed verification with its &#x60;failureReason&#x60;).  For the HIGHEST tier, a frictionless 3DS outcome does NOT complete the verification: it returns &#x60;stripe-holds-pending&#x60; (the cardholder must initiate two small verification holds via &#x60;/steps/place-holds&#x60;), which then advances to &#x60;stripe-amount-confirm&#x60; (the cardholder reads the two amounts back via &#x60;/steps/amount-confirm&#x60;).  | [optional] 
**state** | **str** | Current Verification state | 
**client_secret** | **str** | Stripe SetupIntent or PaymentIntent client secret, used by the client to run &#x60;stripe.handleNextAction&#x60;. Returned whenever the verification is on the Stripe 3DS step; on the creation response (&#x60;POST /card-verifications/3ds&#x60;) and on the retrieve response (&#x60;GET /card-verifications/3ds/{verificationId}&#x60;) while &#x60;currentStepId&#x60; is &#x60;stripe-3ds&#x60;. | [optional] 
**stripe_publishable_key** | **str** | Stripe publishable key to initialize Stripe.js on the client. Returned alongside &#x60;clientSecret&#x60; (creation response and retrieve response while &#x60;currentStepId&#x60; is &#x60;stripe-3ds&#x60;). | [optional] 
**authentication_flow** | **str** | The 3DS authentication flow attested by the issuer, surfaced at the terminal state. &#x60;challenge&#x60; &#x3D; the cardholder actively authenticated; &#x60;frictionless&#x60; &#x3D; the issuer approved without interaction; &#x60;null&#x60; &#x3D; 3DS was not engaged (e.g. a low-risk automatic skip).  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) | Normalized, customer-facing reason the verification failed. Present only when &#x60;state&#x60; is &#x60;failed&#x60;; read it to triage the failure (category, retryability, and the issuer&#39;s message). See the &#x60;FailureReason&#x60; schema.  | [optional] 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.models.card_verification import CardVerification

# TODO update the JSON string below
json = "{}"
# create an instance of CardVerification from a JSON string
card_verification_instance = CardVerification.from_json(json)
# print the JSON string representation of the object
print(CardVerification.to_json())

# convert the object into a dict
card_verification_dict = card_verification_instance.to_dict()
# create an instance of CardVerification from a dict
card_verification_from_dict = CardVerification.from_dict(card_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


