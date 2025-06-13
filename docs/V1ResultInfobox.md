# V1ResultInfobox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | 
**time** | **str** |  | [optional] 
**image** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**props** | [**V1ResultInfoboxProps**](V1ResultInfoboxProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_infobox import V1ResultInfobox

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultInfobox from a JSON string
v1_result_infobox_instance = V1ResultInfobox.from_json(json)
# print the JSON string representation of the object
print(V1ResultInfobox.to_json())

# convert the object into a dict
v1_result_infobox_dict = v1_result_infobox_instance.to_dict()
# create an instance of V1ResultInfobox from a dict
v1_result_infobox_from_dict = V1ResultInfobox.from_dict(v1_result_infobox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


