# V1ResultSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**image** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**props** | [**V1ResultSearchProps**](V1ResultSearchProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_search import V1ResultSearch

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultSearch from a JSON string
v1_result_search_instance = V1ResultSearch.from_json(json)
# print the JSON string representation of the object
print(V1ResultSearch.to_json())

# convert the object into a dict
v1_result_search_dict = v1_result_search_instance.to_dict()
# create an instance of V1ResultSearch from a dict
v1_result_search_from_dict = V1ResultSearch.from_dict(v1_result_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


