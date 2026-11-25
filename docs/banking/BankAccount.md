# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**BankAccountLinks**](BankAccountLinks.md) |  | 
**id** | **str** | The unique identifier of the bank account. | 
**account_id** | **str** | The unique identifier of the account that owns this bank account. | 
**subaccount_id** | **str** | The unique identifier of the subaccount associated with this bank account. | 
**bank_link_id** | **str** | The identifier of the bank link that created this account. Null for accounts that predate persisted link attribution. | [optional] 
**external_id** | **str** | The provider account ID for the connected account. | 
**card_ids** | **List[str]** | The identifiers of cards linked to this bank account for transaction matching, always current. A card links when its last 4 digits match this account&#39;s mask (the same rule applied at bank-link completion and by a scheduled sweep that re-checks each cardless credit account every few hours), or when set manually via PATCH. Cards must belong to the same subaccount. | 
**no_link_reason** | **str** | Why this credit account has no card. Present ONLY while the account is still cardless; once any card links, the field disappears, so it can never contradict &#x60;cardIds&#x60;. See the identically-named field on the bank link response for the full meaning of each value.  | [optional] 
**cards** | [**List[BankFeedCard]**](BankFeedCard.md) | Cards MATERIALIZED from this bank account (&#x60;bank-feed&#x60; enrollments minted at bank-link completion for credit accounts whose mask matched no already-enrolled card). Distinct from &#x60;cardIds&#x60;, which is the link surface: a mask-matched card appears in &#x60;cardIds&#x60; only, while a minted card appears in both. Empty for depository and mask-matched-only accounts.  | 
**institution_name** | **str** | The name of the connected financial institution. | 
**institution_id** | **str** | The provider identifier of the connected institution (Plaid &#x60;ins_*&#x60;). Null for connections made before this field was captured. | [optional] 
**name** | **str** | The display name of the bank account (e.g. \&quot;Checking\&quot;, \&quot;Savings\&quot;). | 
**mask** | **str** | The last 4 digits of the account number. For &#x60;credit&#x60; accounts this is the card number&#39;s last 4; the per-card identity for bank-connected (e.g. American Express) card enrollments. Not guaranteed to be per-card when the institution combines multiple cards into a single account. | [optional] 
**type** | **str** | The normalized type of bank account. (Correction: the service has always returned normalized values; the previous &#x60;depository&#x60;/&#x60;credit&#x60; enum understated live behavior. Codegen consumers should regenerate.) | 
**subtype** | **str** | The raw provider account subtype (e.g. Plaid &#x60;credit card&#x60;, &#x60;checking&#x60;). Null when the provider did not supply one or for accounts connected before this field was captured. | [optional] 
**currency** | **str** | The currency of the account following ISO 4217 format. | 
**state** | **str** | Current state of the bank account. - &#x60;active&#x60;: The account is connected and functioning normally. - &#x60;auth_required&#x60;: The account requires re-authentication. - &#x60;disconnected&#x60;: The account has been disconnected from the provider.  | 
**subscription_state** | **str** | The health of the underlying aggregator connection backing this account. The account &#x60;state&#x60; above can read &#x60;active&#x60; while the connection has errored or needs re-auth, so this field can read \&quot;active but dead\&quot;. Null if no subscription is linked.  | [optional] 
**last_synced_at** | **datetime** | Last successful sync of the backing connection, in UTC, following ISO 8601 format. Pairs with &#x60;subscriptionState&#x60; as the freshness signal. Null until the first sync. | [optional] 
**created_at** | **datetime** | Date and time when this resource was created, in UTC, following ISO 8601 format. | 
**updated_at** | **datetime** | Date and time when this resource was last updated, in UTC, following ISO 8601 format. | 

## Example

```python
from astrada.banking.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


