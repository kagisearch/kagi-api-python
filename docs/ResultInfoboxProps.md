# ResultInfoboxProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infobox** | [**List[ResultInfoboxPropsInfoboxInner]**](ResultInfoboxPropsInfoboxInner.md) |  | [optional] 
**wikipedia_subtext** | **str** |  | [optional] 
**wikipedia_page_id** | **int** |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 
**sort_normalize_url** | **str** |  | [optional] 
**sort_group_id** | **str** |  | [optional] 
**source_history** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.result_infobox_props import ResultInfoboxProps

# TODO update the JSON string below
json = "{}"
# create an instance of ResultInfoboxProps from a JSON string
result_infobox_props_instance = ResultInfoboxProps.from_json(json)
# print the JSON string representation of the object
print(ResultInfoboxProps.to_json())

# convert the object into a dict
result_infobox_props_dict = result_infobox_props_instance.to_dict()
# create an instance of ResultInfoboxProps from a dict
result_infobox_props_from_dict = ResultInfoboxProps.from_dict(result_infobox_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


