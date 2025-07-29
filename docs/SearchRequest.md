# SearchRequest

Used to upload the search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query to perform. | 
**workflow** | **str** | Can be used to filter result output to a single category. | [optional] [default to 'search']
**lens_id** | **str** | A lens ID, as shown on https://kagi.com/settings/lenses when a lens is set to be shareable. Can be just the ID portion of the URL (&#x60;https://kagi.com/lenses/ID&#x60;), or the full URL. | [optional] 
**lens** | [**SearchRequestLens**](SearchRequestLens.md) |  | [optional] 
**timeout** | **float** | Number of seconds to allow for collecting search results. Lower values will return results more quickly, but may be lower quality or inconsistent between calls. If omitted, will use the latest recommended value by Kagi. | [optional] 

## Example

```python
from openapi_client.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


