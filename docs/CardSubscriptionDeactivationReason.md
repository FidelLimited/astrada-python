# CardSubscriptionDeactivationReason

Why a card subscription was deactivated, as given by the customer in the deactivation request.  - `card_lost`: the cardholder lost the card. - `card_stolen`: the card was stolen. - `card_replaced`: the card was reissued or replaced with a new card number. - `card_closed`: the issuer or bank closed the card or its account. - `cardholder_offboarded`: the cardholder no longer works for the business. - `organization_offboarded`: the business no longer uses your platform. - `suspected_fraud`: the card is suspected of fraudulent use. - `duplicate_enrollment`: the card was enrolled more than once. - `no_longer_needed`: the card no longer needs to share data. - `other`: any other reason.  New values may be added later. Handle a value you don't recognize as `other`. 

## Enum

* `CARD_LOST` (value: `'card_lost'`)

* `CARD_STOLEN` (value: `'card_stolen'`)

* `CARD_REPLACED` (value: `'card_replaced'`)

* `CARD_CLOSED` (value: `'card_closed'`)

* `CARDHOLDER_OFFBOARDED` (value: `'cardholder_offboarded'`)

* `ORGANIZATION_OFFBOARDED` (value: `'organization_offboarded'`)

* `SUSPECTED_FRAUD` (value: `'suspected_fraud'`)

* `DUPLICATE_ENROLLMENT` (value: `'duplicate_enrollment'`)

* `NO_LONGER_NEEDED` (value: `'no_longer_needed'`)

* `OTHER` (value: `'other'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


