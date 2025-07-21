# SearchResult

A search result that fulfills the query sent to the kagi API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The location of the result. This is the direct URL to the resource that matches the query | 
**title** | **str** | This is the title of the resource. For HTML resources, it is the title in the header of the document. For Video resources, it is the name of the video that would be displayed on the video site | 
**snippet** | **str** | A short summary of the contents of the resource | [optional] 
**time** | **str** | A date for when the resource was last updated or created. | [optional] 
**image** | [**SearchResultImage**](SearchResultImage.md) |  | [optional] 
**props** | **Dict[str, object]** | Holds arbitrary result metadata | [optional] 

## Example

```python
from openapi_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print(SearchResult.to_json())

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_from_dict = SearchResult.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


