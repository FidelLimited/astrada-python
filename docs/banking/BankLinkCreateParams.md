# BankLinkCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A client-provided identifier for the bank link. Must be alphanumeric with hyphens and underscores only. | 
**subaccount_id** | **str** | The subaccount identifier to associate with this bank link. A subaccount that does not belong to the account is rejected with &#x60;404&#x60; (&#x60;SUBACCOUNT_NOT_FOUND&#x60;). | 
**filters** | [**BankLinkCreateParamsFilters**](BankLinkCreateParamsFilters.md) |  | [optional] 
**bin6** | **str** | First 6 digits captured client-side before an institution pivot (e.g. an American Express BIN typed into the card form before the SDK pivots to bank linking). Persisted with the link. Attached as the completion-time bank-derived card&#39;s &#x60;first6digits&#x60; when the completion has exactly one eligible candidate account.  | [optional] 
**provider** | **str** | Open-banking provider to create the link on. Omitted, the subaccount&#39;s configured default applies (system default: &#x60;plaid&#x60;). A provider outside the subaccount&#39;s configured allowlist, or one not enabled on the platform, is rejected with &#x60;400&#x60;. The provider is fixed at creation: every later operation on the link uses the value it was created with.  | [optional] 
**country_code** | **str** | ISO 3166-1 alpha-3 country of the institution to connect (e.g. &#x60;USA&#x60;, &#x60;DEU&#x60;). Omitted, the subaccount&#39;s configured default applies (system default: &#x60;USA&#x60;). Combined with &#x60;provider&#x60; to select the concrete integration; a country the selected provider does not support is rejected with &#x60;400&#x60;.  | [optional] 
**language** | **str** | Language of the hosted bank-linking screens, as a BCP 47 tag such as &#x60;en&#x60;, &#x60;en-US&#x60; or &#x60;fr-CA&#x60;. A tag that matches the pattern is accepted; any other value is rejected with &#x60;400&#x60;. For a Plaid link, the language part of the tag (&#x60;fr&#x60; for &#x60;fr-CA&#x60;) is used when Plaid supports it, Astrada has turned that language on, and no Link customization applies to the link (one it asks for, one from the bank-linking policy, or one Astrada sets for the environment). Otherwise the screens are in English and the request still succeeds. Plaid Link supports &#x60;da&#x60;, &#x60;nl&#x60;, &#x60;en&#x60;, &#x60;et&#x60;, &#x60;fr&#x60;, &#x60;de&#x60;, &#x60;hi&#x60;, &#x60;it&#x60;, &#x60;lv&#x60;, &#x60;lt&#x60;, &#x60;no&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;ro&#x60;, &#x60;es&#x60;, &#x60;sv&#x60; and &#x60;vi&#x60;. Plaid&#39;s Norwegian is &#x60;no&#x60;, so &#x60;nb&#x60; and &#x60;nb-NO&#x60; fall back to English. Other providers ignore this field. The language is kept with the link, so a refreshed hosted link uses it again.  | [optional] 
**persona** | **str** | Who the bank login belongs to. &#x60;cardholder&#x60;: a page for one person, such as an employee, who links their own bank login. &#x60;admin&#x60;: the company. Omitted, the link is a company link, as with &#x60;admin&#x60;, which is how every link behaved before this field existed.  The link&#39;s owner decides which cards its accounts can join: two bank accounts can count as the same card only when their links have the same owner. Cardholder links sent with the same &#x60;cardholderKey&#x60; share an owner, a cardholder link without a key is its own owner, and every company link has the company as its owner, so a cardholder link never joins a company link&#39;s card.  | [optional] 
**cardholder_key** | **str** | Your stable id for the person on the page, used only with &#x60;persona: cardholder&#x60;, so that all of their links share one owner. Optional: without it, each cardholder link is its own owner. A key sent with &#x60;persona: admin&#x60;, or with no &#x60;persona&#x60;, is ignored. Surrounding whitespace is trimmed, and 1 to 256 characters must remain. Astrada stores only a keyed hash of the key, never the key itself.  The key must be one that no other user can guess: an opaque value your backend issues for that person and gives only to their page, such as a random id, or an HMAC of their employee id made with your own secret. Never send an email address, an employee number or anything else another user could guess. A guessed key can join another person&#39;s card.  | [optional] 
**consent** | [**BankLinkConsent**](BankLinkConsent.md) |  | [optional] 

## Example

```python
from astrada.banking.models.bank_link_create_params import BankLinkCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkCreateParams from a JSON string
bank_link_create_params_instance = BankLinkCreateParams.from_json(json)
# print the JSON string representation of the object
print(BankLinkCreateParams.to_json())

# convert the object into a dict
bank_link_create_params_dict = bank_link_create_params_instance.to_dict()
# create an instance of BankLinkCreateParams from a dict
bank_link_create_params_from_dict = BankLinkCreateParams.from_dict(bank_link_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


