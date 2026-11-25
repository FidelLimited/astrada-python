# SubaccountUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | [**CreateSubaccountConfigurations**](CreateSubaccountConfigurations.md) |  | [optional] 
**name** | **str** |  | [optional] 
**verification_policy** | [**VerificationPolicy**](VerificationPolicy.md) | Set or clear fields of the subaccount&#39;s card verification policy. Fields you send replace those fields and fields you leave out keep their value; the policy as a whole cannot be sent as &#x60;null&#x60;. Customers may set any level above LOW (MEDIUM, HIGH, HIGHEST), send a null level to clear the override, toggle the &#x60;sandbox&#x60; test flag, and set &#x60;failedAttemptLockout&#x60;. LOW is internal-only and is rejected on this endpoint.  | [optional] 
**enrollment_policy** | [**CustomerEnrollmentPolicy**](CustomerEnrollmentPolicy.md) |  | [optional] 

## Example

```python
from astrada.models.subaccount_update_params import SubaccountUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SubaccountUpdateParams from a JSON string
subaccount_update_params_instance = SubaccountUpdateParams.from_json(json)
# print the JSON string representation of the object
print(SubaccountUpdateParams.to_json())

# convert the object into a dict
subaccount_update_params_dict = subaccount_update_params_instance.to_dict()
# create an instance of SubaccountUpdateParams from a dict
subaccount_update_params_from_dict = SubaccountUpdateParams.from_dict(subaccount_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


