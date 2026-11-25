# AmexCountriesOrWildcard

Either an array of ISO 3166 alpha-3 country codes (the contracted regional areas for American Express), each listed once, or the string `\"*\"`, which inherits all countries from the parent account's AMEX capabilities.  Accepted codes: `USA`, `CAN`, `GBR`, `ITA`, `SWE`, `AUS`, `NZL`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from astrada.models.amex_countries_or_wildcard import AmexCountriesOrWildcard

# TODO update the JSON string below
json = "{}"
# create an instance of AmexCountriesOrWildcard from a JSON string
amex_countries_or_wildcard_instance = AmexCountriesOrWildcard.from_json(json)
# print the JSON string representation of the object
print(AmexCountriesOrWildcard.to_json())

# convert the object into a dict
amex_countries_or_wildcard_dict = amex_countries_or_wildcard_instance.to_dict()
# create an instance of AmexCountriesOrWildcard from a dict
amex_countries_or_wildcard_from_dict = AmexCountriesOrWildcard.from_dict(amex_countries_or_wildcard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


