# SearchRequestPersonalizationsDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain pattern to personalize (e.g., \&quot;example.com\&quot;). Can also be a tld suffix like \&quot;.co.uk\&quot;. | 
**kind** | **str** | Handling mode for this domain pattern | 

## Example

```python
from kagi_client.models.search_request_personalizations_domains_inner import SearchRequestPersonalizationsDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestPersonalizationsDomainsInner from a JSON string
search_request_personalizations_domains_inner_instance = SearchRequestPersonalizationsDomainsInner.from_json(json)
# print the JSON string representation of the object
print(SearchRequestPersonalizationsDomainsInner.to_json())

# convert the object into a dict
search_request_personalizations_domains_inner_dict = search_request_personalizations_domains_inner_instance.to_dict()
# create an instance of SearchRequestPersonalizationsDomainsInner from a dict
search_request_personalizations_domains_inner_from_dict = SearchRequestPersonalizationsDomainsInner.from_dict(search_request_personalizations_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


