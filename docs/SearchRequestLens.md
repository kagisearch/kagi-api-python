# SearchRequestLens

An inline description of a lens to apply to the search. Options supplied by the lens take pecedent over those supplied by the user in their search terms (e.g., `site:` operators), allowing you to restrict the scope of the search to return more relevant results in specific applications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sites_included** | **List[str]** | A list of domains to restrict the search to. | [optional] 
**sites_excluded** | **List[str]** | A list of domains to restrict the search to. | [optional] 
**keywords_included** | **List[str]** | A list of keywords to filter results on, such that every result *must* contain these terms. | [optional] 
**keywords_excluded** | **List[str]** | A list of keywords to filter results on, such that any result containing these terms is removed. | [optional] 
**file_type** | **str** | A specific file type to search for. (e.g., &#x60;pdf&#x60;) | [optional] 
**time_after** | **str** | Filters for web pages that have been updated or published *after* the given date (&#x60;YYYY-MM-DD&#x60;). | [optional] 
**time_before** | **str** | Filters for web pages that have been updated or published *before* the given date (&#x60;YYYY-MM-DD&#x60;). | [optional] 
**time_relative** | **str** | Filters for web pages that have been updated or published in the given interval, relative to today&#39;s date. | [optional] 
**search_region** | **str** | Requests results localized to a specific region. Can be any valid [ISO-3166-1 Alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements), or the special value &#x60;no_region&#x60;, that will try to get the most general results possible. | [optional] 

## Example

```python
from openapi_client.models.search_request_lens import SearchRequestLens

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestLens from a JSON string
search_request_lens_instance = SearchRequestLens.from_json(json)
# print the JSON string representation of the object
print(SearchRequestLens.to_json())

# convert the object into a dict
search_request_lens_dict = search_request_lens_instance.to_dict()
# create an instance of SearchRequestLens from a dict
search_request_lens_from_dict = SearchRequestLens.from_dict(search_request_lens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


