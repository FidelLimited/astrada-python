# VisaCountriesOrWildcard

Either an array of ISO 3166 alpha-3 country codes (the contracted regional areas for Visa), each listed once, or the string `\"*\"`, which inherits all countries from the parent account's VISA capabilities.  Accepted codes: `USA`, `CAN`, `IRL`, `DEU`, `CZE`, `SWE`, `NLD`, `LTU`, `GBR`, `SVN`, `LUX`, `POL`, `SVK`, `HUN`, `ITA`, `ROU`, `FIN`, `DNK`, `MLT`, `LVA`, `GRC`, `AUT`, `HRV`, `CHE`, `NOR`, `ISL`, `FRA`, `ESP`, `ISR`, `SMR`, `VAT`, `AND`, `GIB`, `AUS`, `NZL`, `PRT`, `BEL`, `SGP`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from astrada.models.visa_countries_or_wildcard import VisaCountriesOrWildcard

# TODO update the JSON string below
json = "{}"
# create an instance of VisaCountriesOrWildcard from a JSON string
visa_countries_or_wildcard_instance = VisaCountriesOrWildcard.from_json(json)
# print the JSON string representation of the object
print(VisaCountriesOrWildcard.to_json())

# convert the object into a dict
visa_countries_or_wildcard_dict = visa_countries_or_wildcard_instance.to_dict()
# create an instance of VisaCountriesOrWildcard from a dict
visa_countries_or_wildcard_from_dict = VisaCountriesOrWildcard.from_dict(visa_countries_or_wildcard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


