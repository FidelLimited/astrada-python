# BankInstitutionIncident

An outage or maintenance the bank data provider published for the bank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The provider&#39;s title for the incident. | [optional] 
**started_at** | **str** | When the incident started, as the provider published it. | [optional] 
**ended_at** | **str** | When the incident ended, as the provider published it. Null while it is open. | [optional] 
**status** | **str** | The status on the provider&#39;s latest update to the incident. | [optional] 
**update** | **str** | The text of the provider&#39;s latest update to the incident. | [optional] 

## Example

```python
from astrada.banking.models.bank_institution_incident import BankInstitutionIncident

# TODO update the JSON string below
json = "{}"
# create an instance of BankInstitutionIncident from a JSON string
bank_institution_incident_instance = BankInstitutionIncident.from_json(json)
# print the JSON string representation of the object
print(BankInstitutionIncident.to_json())

# convert the object into a dict
bank_institution_incident_dict = bank_institution_incident_instance.to_dict()
# create an instance of BankInstitutionIncident from a dict
bank_institution_incident_from_dict = BankInstitutionIncident.from_dict(bank_institution_incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


