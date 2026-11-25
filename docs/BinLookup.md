# BinLookup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **str** | The 6-digit Bank Identification Number (BIN) the answer was found under. It is always the first 6 digits of the &#x60;bin&#x60; you sent, even when you sent more; the rest of your input is never echoed back.  | 
**network** | **str** | The card network (e.g., VISA, MASTERCARD, AMERICAN_EXPRESS). American Express is &#x60;AMERICAN_EXPRESS&#x60; here; other endpoints spell it &#x60;AMEX&#x60;. | 
**type** | **str** | The card type (e.g., COMMERCIAL, CORPORATE, CONSUMER, SMALL_BUSINESS ) | [optional] 
**funding_type** | **str** | The card funding type (e.g., prepaid, debit, credit) | 
**card_category** | **str** | The card&#39;s commercial classification, carried through from the BIN reference dataset. More specific than &#x60;type&#x60;: it separates &#x60;FLEET&#x60;, &#x60;PURCHASING&#x60; and &#x60;GIFT&#x60; cards that &#x60;type&#x60; reports as &#x60;COMMERCIAL&#x60; or &#x60;CORPORATE&#x60;, and it is populated for many BINs where &#x60;type&#x60; is absent. &#x60;UNKNOWN&#x60; means the reference data does not classify the BIN; treat it as \&quot;not determined\&quot;, not as \&quot;consumer\&quot;.  | [optional] 
**card_funding_type** | **str** | How the card is funded, carried through from the BIN reference dataset. Broader than &#x60;fundingType&#x60;: it separates &#x60;CHARGE&#x60; cards (which &#x60;fundingType&#x60; reports as &#x60;CREDIT&#x60;) and &#x60;GIFT&#x60; cards (which &#x60;fundingType&#x60; reports as &#x60;PREPAID&#x60; or &#x60;DEBIT&#x60;). &#x60;UNKNOWN&#x60; means the reference data does not classify the BIN.  | [optional] 
**issuer_name** | **str** | The name of the issuing bank. For a Mastercard card, this can be more specific to the digits sent than the 6-digit BIN&#39;s issuer name (see &#x60;issuerCountry&#x60;).  | [optional] 
**issuer_country** | **str** | The country of the issuing bank following ISO 3166 alpha-3. May be &#x60;null&#x60; when the BIN is known but the reference data does not record its issuing country (an unknown BIN returns 404, not &#x60;null&#x60;).  For a Mastercard card, this is checked against the digits sent and can differ from what the first 6 digits alone would give, because one BIN can be shared by issuers in several countries. Send more digits (up to 11) for a more precise issuer country; never send the full card number.  | [optional] 
**issuer_country_ambiguous** | **bool** | Present, and always &#x60;true&#x60;, only when the digits sent match card ranges in more than one country. &#x60;issuerCountry&#x60; is then the 6-digit BIN&#39;s value and may not be this card&#39;s country; &#x60;issuerCountryCandidates&#x60; lists the possible countries and &#x60;warnings&#x60; explains what to do. With fewer than 11 digits, sending more can resolve it. Omitted in every other case.  | [optional] 
**issuer_country_candidates** | **List[str]** | The possible issuer countries (ISO 3166 alpha-3, sorted, at least two) when the digits sent match card ranges in more than one country. Present only together with &#x60;issuerCountryAmbiguous: true&#x60;.  | [optional] 
**issuer_region** | **str** | The region of the issuing bank, derived from the issuer country. &#x60;EU&#x60; covers Europe and &#x60;MEA&#x60; covers the Middle East &amp; Africa. These are separate buckets; there is no combined &#x60;EMEA&#x60; value. &#x60;UNKNOWN&#x60; means the issuer country is missing or not mapped to a region; treat it as \&quot;not determined\&quot;. It always matches the returned &#x60;issuerCountry&#x60;.  | [optional] 
**warnings** | [**List[BinLookupWarning]**](BinLookupWarning.md) | Notes about the answer that a caller may want to act on. Present only when there is something to report, and never empty. Branch on &#x60;code&#x60;; &#x60;message&#x60; is for people and may change.  Today the only code is &#x60;ISSUER_COUNTRY_NOT_CONFIRMED&#x60;, sent together with &#x60;issuerCountryAmbiguous: true&#x60; when the digits sent match card ranges in more than one country. With fewer than 11 digits, sending more digits (up to 11) may confirm the issuer country. With 11 digits, the issuer country could not be confirmed.  | [optional] 

## Example

```python
from astrada.models.bin_lookup import BinLookup

# TODO update the JSON string below
json = "{}"
# create an instance of BinLookup from a JSON string
bin_lookup_instance = BinLookup.from_json(json)
# print the JSON string representation of the object
print(BinLookup.to_json())

# convert the object into a dict
bin_lookup_dict = bin_lookup_instance.to_dict()
# create an instance of BinLookup from a dict
bin_lookup_from_dict = BinLookup.from_dict(bin_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


