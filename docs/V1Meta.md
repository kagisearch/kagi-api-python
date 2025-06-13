# V1Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace** | **str** |  | 
**node** | **str** |  | 
**ms** | **int** |  | 
**query** | [**V1MetaQuery**](V1MetaQuery.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_meta import V1Meta

# TODO update the JSON string below
json = "{}"
# create an instance of V1Meta from a JSON string
v1_meta_instance = V1Meta.from_json(json)
# print the JSON string representation of the object
print(V1Meta.to_json())

# convert the object into a dict
v1_meta_dict = v1_meta_instance.to_dict()
# create an instance of V1Meta from a dict
v1_meta_from_dict = V1Meta.from_dict(v1_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


