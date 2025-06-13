# ResultWebArchive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | 
**time** | **str** |  | [optional] 
**image** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 
**props** | [**ResultWebArchiveProps**](ResultWebArchiveProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.result_web_archive import ResultWebArchive

# TODO update the JSON string below
json = "{}"
# create an instance of ResultWebArchive from a JSON string
result_web_archive_instance = ResultWebArchive.from_json(json)
# print the JSON string representation of the object
print(ResultWebArchive.to_json())

# convert the object into a dict
result_web_archive_dict = result_web_archive_instance.to_dict()
# create an instance of ResultWebArchive from a dict
result_web_archive_from_dict = ResultWebArchive.from_dict(result_web_archive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


