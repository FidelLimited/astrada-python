# FailureReasonAcsReferences

3DS ACS reference identifiers, when returned by the issuer; useful when escalating to the issuer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_transaction_id** | **str** |  | [optional] 
**acs_reference_number** | **str** |  | [optional] 
**ds_transaction_id** | **str** |  | [optional] 

## Example

```python
from astrada.models.failure_reason_acs_references import FailureReasonAcsReferences

# TODO update the JSON string below
json = "{}"
# create an instance of FailureReasonAcsReferences from a JSON string
failure_reason_acs_references_instance = FailureReasonAcsReferences.from_json(json)
# print the JSON string representation of the object
print(FailureReasonAcsReferences.to_json())

# convert the object into a dict
failure_reason_acs_references_dict = failure_reason_acs_references_instance.to_dict()
# create an instance of FailureReasonAcsReferences from a dict
failure_reason_acs_references_from_dict = FailureReasonAcsReferences.from_dict(failure_reason_acs_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


