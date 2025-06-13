# FastGPT200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | [optional] 
**tokens** | **int** |  | [optional] 
**references** | [**List[SearchObject]**](SearchObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.fast_gpt200_response_data import FastGPT200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FastGPT200ResponseData from a JSON string
fast_gpt200_response_data_instance = FastGPT200ResponseData.from_json(json)
# print the JSON string representation of the object
print(FastGPT200ResponseData.to_json())

# convert the object into a dict
fast_gpt200_response_data_dict = fast_gpt200_response_data_instance.to_dict()
# create an instance of FastGPT200ResponseData from a dict
fast_gpt200_response_data_from_dict = FastGPT200ResponseData.from_dict(fast_gpt200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


