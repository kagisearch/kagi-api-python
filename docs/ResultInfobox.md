# ResultInfobox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | 
**time** | **str** |  | [optional] 
**image** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 
**props** | [**ResultInfoboxProps**](ResultInfoboxProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.result_infobox import ResultInfobox

# TODO update the JSON string below
json = "{}"
# create an instance of ResultInfobox from a JSON string
result_infobox_instance = ResultInfobox.from_json(json)
# print the JSON string representation of the object
print(ResultInfobox.to_json())

# convert the object into a dict
result_infobox_dict = result_infobox_instance.to_dict()
# create an instance of ResultInfobox from a dict
result_infobox_from_dict = ResultInfobox.from_dict(result_infobox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


