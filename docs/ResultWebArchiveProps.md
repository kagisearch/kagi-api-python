# ResultWebArchiveProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_archive_domain** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.result_web_archive_props import ResultWebArchiveProps

# TODO update the JSON string below
json = "{}"
# create an instance of ResultWebArchiveProps from a JSON string
result_web_archive_props_instance = ResultWebArchiveProps.from_json(json)
# print the JSON string representation of the object
print(ResultWebArchiveProps.to_json())

# convert the object into a dict
result_web_archive_props_dict = result_web_archive_props_instance.to_dict()
# create an instance of ResultWebArchiveProps from a dict
result_web_archive_props_from_dict = ResultWebArchiveProps.from_dict(result_web_archive_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


