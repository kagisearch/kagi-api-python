# SearchObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**thumbnail** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 
**image** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 

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


