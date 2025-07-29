# SearchObjectThumbnail

A small image that can be displayed along side the serach result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the thumbnail | 
**height** | **int** | hight of the thumbnail | [optional] 
**width** | **int** | width of the thumbnail | [optional] 

## Example

```python
from openapi_client.models.search_object_thumbnail import SearchObjectThumbnail

# TODO update the JSON string below
json = "{}"
# create an instance of SearchObjectThumbnail from a JSON string
search_object_thumbnail_instance = SearchObjectThumbnail.from_json(json)
# print the JSON string representation of the object
print(SearchObjectThumbnail.to_json())

# convert the object into a dict
search_object_thumbnail_dict = search_object_thumbnail_instance.to_dict()
# create an instance of SearchObjectThumbnail from a dict
search_object_thumbnail_from_dict = SearchObjectThumbnail.from_dict(search_object_thumbnail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


