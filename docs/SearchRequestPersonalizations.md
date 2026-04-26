# SearchRequestPersonalizations

Personalization rules to customize search result ranking. Allows specifying domain biases and regex-based replacements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[SearchRequestPersonalizationsDomainsInner]**](SearchRequestPersonalizationsDomainsInner.md) | Domain-level personalization rules (maximum 1000 rules). Each rule can boost or lower the ranking of results from specific domains. | [optional] 
**regexes** | [**List[SearchRequestPersonalizationsRegexesInner]**](SearchRequestPersonalizationsRegexesInner.md) | Regex-based personalization rules (maximum 1000 rules, max 1000 bytes per pattern). | [optional] 

## Example

```python
from openapi_client.models.search_request_personalizations import SearchRequestPersonalizations

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestPersonalizations from a JSON string
search_request_personalizations_instance = SearchRequestPersonalizations.from_json(json)
# print the JSON string representation of the object
print(SearchRequestPersonalizations.to_json())

# convert the object into a dict
search_request_personalizations_dict = search_request_personalizations_instance.to_dict()
# create an instance of SearchRequestPersonalizations from a dict
search_request_personalizations_from_dict = SearchRequestPersonalizations.from_dict(search_request_personalizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


