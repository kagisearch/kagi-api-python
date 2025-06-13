# FastGPT200Response

A response with a description and results references used

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**FastGPT200ResponseData**](FastGPT200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.fast_gpt200_response import FastGPT200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FastGPT200Response from a JSON string
fast_gpt200_response_instance = FastGPT200Response.from_json(json)
# print the JSON string representation of the object
print(FastGPT200Response.to_json())

# convert the object into a dict
fast_gpt200_response_dict = fast_gpt200_response_instance.to_dict()
# create an instance of FastGPT200Response from a dict
fast_gpt200_response_from_dict = FastGPT200Response.from_dict(fast_gpt200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


