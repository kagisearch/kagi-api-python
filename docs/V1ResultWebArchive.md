# V1ResultWebArchive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | 
**time** | **str** |  | [optional] 
**image** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**props** | [**V1ResultWebArchiveProps**](V1ResultWebArchiveProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_web_archive import V1ResultWebArchive

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultWebArchive from a JSON string
v1_result_web_archive_instance = V1ResultWebArchive.from_json(json)
# print the JSON string representation of the object
print(V1ResultWebArchive.to_json())

# convert the object into a dict
v1_result_web_archive_dict = v1_result_web_archive_instance.to_dict()
# create an instance of V1ResultWebArchive from a dict
v1_result_web_archive_from_dict = V1ResultWebArchive.from_dict(v1_result_web_archive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


