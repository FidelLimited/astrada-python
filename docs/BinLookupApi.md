# astrada.BinLookupApi

All URIs are relative to *https://api.astrada.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_bin**](BinLookupApi.md#lookup_bin) | **GET** /bin-lookup | Lookup card information by BIN


# **lookup_bin**
> BinLookup lookup_bin(bin)

Lookup card information by BIN

Retrieve card information such as network, type, and issuing bank by providing the card's
BIN (Bank Identification Number): the first 6 to 11 digits of the card number. Never send
the full card number; more than 11 digits is rejected with `400`.

The card details are found under the first 6 digits. One 6-digit BIN can be shared by
issuers in several countries, so for a Mastercard card looked up with 6 to 11 digits,
Astrada also runs a more precise issuer-country check on the digits sent. That check can
return a different `issuerCountry`, `issuerRegion` and `issuerName` than the first 6
digits alone would. Send more digits (up to 11) for a more precise issuer country; never
send the full card number.

When the digits sent match card ranges in more than one country, the response keeps the
6-digit values and adds `issuerCountryAmbiguous`, `issuerCountryCandidates`, and a
`warnings` entry with code `ISSUER_COUNTRY_NOT_CONFIRMED`. In every other case none of
these three fields is present.

Lookups for every other network are unaffected. If the precise check gives no answer, the
request still succeeds with the 6-digit values. In sandbox the precise check is not run,
so sandbox responses never include these fields.


### Example

* OAuth Authentication (main-auth):
```python
import os

import astrada
from astrada.models.bin_lookup import BinLookup

client = astrada.Astrada(
    account_id=os.environ["ASTRADA_ACCOUNT_ID"],
    client_id=os.environ["ASTRADA_CLIENT_ID"],
    client_secret=os.environ["ASTRADA_CLIENT_SECRET"],
    environment="sandbox",  # or "production"
)
bin = '55891900000'  # str

result = client.bin_lookup.lookup_bin(bin)
print(result)
```


### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bin** | **str**| The first 6 to 11 digits of the card number. Send digits only, and never the full card number. Input that is shorter than 6 digits, longer than 11 digits, or contains anything other than digits is rejected with &#x60;400&#x60;; longer input is not truncated.  For a Mastercard card, send more digits (up to 11) for a more precise issuer country. 11 digits gives the most precise answer.  | 

### Return type

[**BinLookup**](BinLookup.md)

### Authorization

[main-auth](../README.md#main-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | The &#x60;bin&#x60; is not 6 to 11 digits (too short, too long, or not digits only).  |  -  |
**401** | Authentication credentials were either missing or incorrect |  -  |
**403** | Authentication credentials used do not have have permissions to perform the request |  -  |
**404** | The requested resource was not found on the server |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

