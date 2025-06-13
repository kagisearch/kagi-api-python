# V1ResultSearchProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail_image** | [**V1ResultSearchPropsThumbnailImage**](V1ResultSearchPropsThumbnailImage.md) |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 
**paywalled** | **bool** |  | [optional] 
**sort_normalize_url** | **str** |  | [optional] 
**sort_group_id** | **str** |  | [optional] 
**source_history** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_search_props import V1ResultSearchProps

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultSearchProps from a JSON string
v1_result_search_props_instance = V1ResultSearchProps.from_json(json)
# print the JSON string representation of the object
print(V1ResultSearchProps.to_json())

# convert the object into a dict
v1_result_search_props_dict = v1_result_search_props_instance.to_dict()
# create an instance of V1ResultSearchProps from a dict
v1_result_search_props_from_dict = V1ResultSearchProps.from_dict(v1_result_search_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


