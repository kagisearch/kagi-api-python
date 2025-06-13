# V1ResultWebArchiveProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_archive_domain** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_web_archive_props import V1ResultWebArchiveProps

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultWebArchiveProps from a JSON string
v1_result_web_archive_props_instance = V1ResultWebArchiveProps.from_json(json)
# print the JSON string representation of the object
print(V1ResultWebArchiveProps.to_json())

# convert the object into a dict
v1_result_web_archive_props_dict = v1_result_web_archive_props_instance.to_dict()
# create an instance of V1ResultWebArchiveProps from a dict
v1_result_web_archive_props_from_dict = V1ResultWebArchiveProps.from_dict(v1_result_web_archive_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


