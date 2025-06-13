# MetaQueryFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**negate** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.meta_query_fields_inner import MetaQueryFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MetaQueryFieldsInner from a JSON string
meta_query_fields_inner_instance = MetaQueryFieldsInner.from_json(json)
# print the JSON string representation of the object
print(MetaQueryFieldsInner.to_json())

# convert the object into a dict
meta_query_fields_inner_dict = meta_query_fields_inner_instance.to_dict()
# create an instance of MetaQueryFieldsInner from a dict
meta_query_fields_inner_from_dict = MetaQueryFieldsInner.from_dict(meta_query_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


