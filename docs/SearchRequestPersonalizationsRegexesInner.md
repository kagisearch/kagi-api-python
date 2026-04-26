# SearchRequestPersonalizationsRegexesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regex** | **str** | The regex pattern to match. | [optional] 
**replacement** | **str** | The replacement string to apply when the pattern matches. | [optional] 

## Example

```python
from openapi_client.models.search_request_personalizations_regexes_inner import SearchRequestPersonalizationsRegexesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestPersonalizationsRegexesInner from a JSON string
search_request_personalizations_regexes_inner_instance = SearchRequestPersonalizationsRegexesInner.from_json(json)
# print the JSON string representation of the object
print(SearchRequestPersonalizationsRegexesInner.to_json())

# convert the object into a dict
search_request_personalizations_regexes_inner_dict = search_request_personalizations_regexes_inner_instance.to_dict()
# create an instance of SearchRequestPersonalizationsRegexesInner from a dict
search_request_personalizations_regexes_inner_from_dict = SearchRequestPersonalizationsRegexesInner.from_dict(search_request_personalizations_regexes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


