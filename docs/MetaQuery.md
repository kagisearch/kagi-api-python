# MetaQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**fields** | [**List[MetaQueryFieldsInner]**](MetaQueryFieldsInner.md) |  | [optional] 
**workflow** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.meta_query import MetaQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetaQuery from a JSON string
meta_query_instance = MetaQuery.from_json(json)
# print the JSON string representation of the object
print(MetaQuery.to_json())

# convert the object into a dict
meta_query_dict = meta_query_instance.to_dict()
# create an instance of MetaQuery from a dict
meta_query_from_dict = MetaQuery.from_dict(meta_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


