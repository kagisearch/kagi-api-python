# SearchRequestFilters

Filters to apply to search results for more targeted queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | Filter results to a specific region using an ISO-3166-1 Alpha-2 country code. See https://help.kagi.com/api/regions for supported codes. | [optional] 
**after** | **str** | Filter for results published/updated after this date. Must be in ISO 8601 format (YYYY-MM-DD). | [optional] 
**before** | **str** | Filter for results published/updated before this date. Must be in ISO 8601 format (YYYY-MM-DD). | [optional] 

## Example

```python
from openapi_client.models.search_request_filters import SearchRequestFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestFilters from a JSON string
search_request_filters_instance = SearchRequestFilters.from_json(json)
# print the JSON string representation of the object
print(SearchRequestFilters.to_json())

# convert the object into a dict
search_request_filters_dict = search_request_filters_instance.to_dict()
# create an instance of SearchRequestFilters from a dict
search_request_filters_from_dict = SearchRequestFilters.from_dict(search_request_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


