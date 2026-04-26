# SearchRequestPersonalizationsDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain to personalize (e.g., \&quot;example.com\&quot;). | [optional] 
**bias** | **float** | Bias value to apply to results from this domain. | [optional] 

## Example

```python
from openapi_client.models.search_request_personalizations_domains_inner import SearchRequestPersonalizationsDomainsInner

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


