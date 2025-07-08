# Search200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**image** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**video** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**podcast** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**podcast_creator** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**news** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**adjacent_question** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**direct_answer** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**interesting_news** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**interesting_finds** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**infobox** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**code** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**package_tracking** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**public_records** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**weather** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**related_search** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**listicle** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**web_archive** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.search200_response_data import Search200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of Search200ResponseData from a JSON string
search200_response_data_instance = Search200ResponseData.from_json(json)
# print the JSON string representation of the object
print(Search200ResponseData.to_json())

# convert the object into a dict
search200_response_data_dict = search200_response_data_instance.to_dict()
# create an instance of Search200ResponseData from a dict
search200_response_data_from_dict = Search200ResponseData.from_dict(search200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


