# SearchRequestExtract

Configuration for extracting page content from search results. When provided, the API will fetch and extract the content from the specified number of result pages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of search results to extract content from. Must be between 1 and 10. | [optional] 
**timeout** | **float** | Timeout in seconds for extraction of each page. If omitted, uses the default timeout. | [optional] 

## Example

```python
from openapi_client.models.search_request_extract import SearchRequestExtract

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestExtract from a JSON string
search_request_extract_instance = SearchRequestExtract.from_json(json)
# print the JSON string representation of the object
print(SearchRequestExtract.to_json())

# convert the object into a dict
search_request_extract_dict = search_request_extract_instance.to_dict()
# create an instance of SearchRequestExtract from a dict
search_request_extract_from_dict = SearchRequestExtract.from_dict(search_request_extract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


