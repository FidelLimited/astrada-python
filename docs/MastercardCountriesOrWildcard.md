# MastercardCountriesOrWildcard

Either an array of ISO 3166 alpha-3 country codes (the contracted regional areas for Mastercard), each listed once, or the string `\"*\"`, which inherits all countries from the parent account's MASTERCARD capabilities.  Accepted codes: `USA`, `CAN`, `GBR`, `IRL`, `SWE`, `DEU`, `NLD`, `DNK`, `ITA`, `POL`, `FIN`, `BEL`, `ESP`, `FRA`, `PRT`, `AUT`, `GRC`, `MLT`, `NOR`, `CHE`, `ISR`, `AUS`, `NZL`, `SGP`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from astrada.models.mastercard_countries_or_wildcard import MastercardCountriesOrWildcard

# TODO update the JSON string below
json = "{}"
# create an instance of MastercardCountriesOrWildcard from a JSON string
mastercard_countries_or_wildcard_instance = MastercardCountriesOrWildcard.from_json(json)
# print the JSON string representation of the object
print(MastercardCountriesOrWildcard.to_json())

# convert the object into a dict
mastercard_countries_or_wildcard_dict = mastercard_countries_or_wildcard_instance.to_dict()
# create an instance of MastercardCountriesOrWildcard from a dict
mastercard_countries_or_wildcard_from_dict = MastercardCountriesOrWildcard.from_dict(mastercard_countries_or_wildcard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


