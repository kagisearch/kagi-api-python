# SuperSearchRequest

Used to upload the search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**workflow** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.super_search_request import SuperSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuperSearchRequest from a JSON string
super_search_request_instance = SuperSearchRequest.from_json(json)
# print the JSON string representation of the object
print(SuperSearchRequest.to_json())

# convert the object into a dict
super_search_request_dict = super_search_request_instance.to_dict()
# create an instance of SuperSearchRequest from a dict
super_search_request_from_dict = SuperSearchRequest.from_dict(super_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


