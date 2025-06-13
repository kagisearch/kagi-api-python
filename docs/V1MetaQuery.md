# V1MetaQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**fields** | [**List[V1MetaQueryFieldsInner]**](V1MetaQueryFieldsInner.md) |  | [optional] 
**workflow** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.v1_meta_query import V1MetaQuery

# TODO update the JSON string below
json = "{}"
# create an instance of V1MetaQuery from a JSON string
v1_meta_query_instance = V1MetaQuery.from_json(json)
# print the JSON string representation of the object
print(V1MetaQuery.to_json())

# convert the object into a dict
v1_meta_query_dict = v1_meta_query_instance.to_dict()
# create an instance of V1MetaQuery from a dict
v1_meta_query_from_dict = V1MetaQuery.from_dict(v1_meta_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


