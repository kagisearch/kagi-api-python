# V1MetaQueryFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**negate** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.v1_meta_query_fields_inner import V1MetaQueryFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1MetaQueryFieldsInner from a JSON string
v1_meta_query_fields_inner_instance = V1MetaQueryFieldsInner.from_json(json)
# print the JSON string representation of the object
print(V1MetaQueryFieldsInner.to_json())

# convert the object into a dict
v1_meta_query_fields_inner_dict = v1_meta_query_fields_inner_instance.to_dict()
# create an instance of V1MetaQueryFieldsInner from a dict
v1_meta_query_fields_inner_from_dict = V1MetaQueryFieldsInner.from_dict(v1_meta_query_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


