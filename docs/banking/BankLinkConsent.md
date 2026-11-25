# BankLinkConsent

The bank-link consent record. The Unified Enrollment SDK sets it on channel `sdk-unified`, naming the Astrada consent text of the bank-connect screen the person saw. Integrators do not send it. Astrada relays it to each card subscription the bank link creates, where it is recorded and never refused. A consent without `textVersionId` is accepted but not kept. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Always &#x60;sdk-unified&#x60;. | 
**text_version_id** | **str** | The id of the bank-connect consent text the SDK showed, such as &#x60;sdk-unified:bank-consent.plaid.bank.en@v1&#x60;. | [optional] 
**text_hash** | **str** | &#x60;sha256:&#x60; and the lowercase hex SHA-256 of the text named by &#x60;textVersionId&#x60;, compared with the registered text when sent. | [optional] 
**sdk_version** | **str** | The SDK release that collected the consent. | [optional] 
**variables** | **Dict[str, str]** | &#x60;companyName&#x60; and &#x60;providerName&#x60;, as the screen showed them. For a Plaid link, Astrada adds &#x60;plaidLinkSessionId&#x60; when it relays the record.  | [optional] 

## Example

```python
from astrada.banking.models.bank_link_consent import BankLinkConsent

# TODO update the JSON string below
json = "{}"
# create an instance of BankLinkConsent from a JSON string
bank_link_consent_instance = BankLinkConsent.from_json(json)
# print the JSON string representation of the object
print(BankLinkConsent.to_json())

# convert the object into a dict
bank_link_consent_dict = bank_link_consent_instance.to_dict()
# create an instance of BankLinkConsent from a dict
bank_link_consent_from_dict = BankLinkConsent.from_dict(bank_link_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


