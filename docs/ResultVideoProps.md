# ResultVideoProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hires_thumbnail_url** | **str** |  | [optional] 
**sort_normalize_url** | **str** |  | [optional] 
**sort_group_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 
**source_history** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.result_video_props import ResultVideoProps

# TODO update the JSON string below
json = "{}"
# create an instance of ResultVideoProps from a JSON string
result_video_props_instance = ResultVideoProps.from_json(json)
# print the JSON string representation of the object
print(ResultVideoProps.to_json())

# convert the object into a dict
result_video_props_dict = result_video_props_instance.to_dict()
# create an instance of ResultVideoProps from a dict
result_video_props_from_dict = ResultVideoProps.from_dict(result_video_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


