# ResultSearchProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_image** | [**ResultSearchPropsThumbnailImage**](ResultSearchPropsThumbnailImage.md) |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 
**paywalled** | **bool** |  | [optional] 
**sort_normalize_url** | **str** |  | [optional] 
**sort_group_id** | **str** |  | [optional] 
**source_history** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.result_search_props import ResultSearchProps

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSearchProps from a JSON string
result_search_props_instance = ResultSearchProps.from_json(json)
# print the JSON string representation of the object
print(ResultSearchProps.to_json())

# convert the object into a dict
result_search_props_dict = result_search_props_instance.to_dict()
# create an instance of ResultSearchProps from a dict
result_search_props_from_dict = ResultSearchProps.from_dict(result_search_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


