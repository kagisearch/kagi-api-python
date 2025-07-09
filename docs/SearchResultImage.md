# SearchResultImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**height** | **int** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.search_result_image import SearchResultImage

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultImage from a JSON string
search_result_image_instance = SearchResultImage.from_json(json)
# print the JSON string representation of the object
print(SearchResultImage.to_json())

# convert the object into a dict
search_result_image_dict = search_result_image_instance.to_dict()
# create an instance of SearchResultImage from a dict
search_result_image_from_dict = SearchResultImage.from_dict(search_result_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


