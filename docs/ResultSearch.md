# ResultSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**image** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 
**props** | [**ResultSearchProps**](ResultSearchProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.result_search import ResultSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSearch from a JSON string
result_search_instance = ResultSearch.from_json(json)
# print the JSON string representation of the object
print(ResultSearch.to_json())

# convert the object into a dict
result_search_dict = result_search_instance.to_dict()
# create an instance of ResultSearch from a dict
result_search_from_dict = ResultSearch.from_dict(result_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


