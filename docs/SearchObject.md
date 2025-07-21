# SearchObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t** | **int** | This is always set to 0. It is used as a flag to identify if the result was a rearch result or a related searches object. | [optional] 
**rank** | **int** | Order of resarch results, the highest rank is 1 and should identify results that match the search request better. | [optional] 
**url** | **str** | URL of the resource identified in the search result. | 
**title** | **str** | Title of the search result. This can be taken from the title of the html document, or the title of a media resource. | 
**snippet** | **str** | a short desciption, or summary, of the content. | [optional] 
**published** | **str** | the date the rearch result was created | [optional] 
**thumbnail** | [**SearchObjectThumbnail**](SearchObjectThumbnail.md) |  | [optional] 
**image** | [**SearchObjectImage**](SearchObjectImage.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_object import SearchObject

# TODO update the JSON string below
json = "{}"
# create an instance of SearchObject from a JSON string
search_object_instance = SearchObject.from_json(json)
# print the JSON string representation of the object
print(SearchObject.to_json())

# convert the object into a dict
search_object_dict = search_object_instance.to_dict()
# create an instance of SearchObject from a dict
search_object_from_dict = SearchObject.from_dict(search_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


