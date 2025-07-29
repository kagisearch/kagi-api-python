# SearchObjectImage

An image that is linked to the search result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the image | 
**height** | **int** | hight of the image | [optional] 
**width** | **int** | width of the image | [optional] 

## Example

```python
from openapi_client.models.search_object_image import SearchObjectImage

# TODO update the JSON string below
json = "{}"
# create an instance of SearchObjectImage from a JSON string
search_object_image_instance = SearchObjectImage.from_json(json)
# print the JSON string representation of the object
print(SearchObjectImage.to_json())

# convert the object into a dict
search_object_image_dict = search_object_image_instance.to_dict()
# create an instance of SearchObjectImage from a dict
search_object_image_from_dict = SearchObjectImage.from_dict(search_object_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


