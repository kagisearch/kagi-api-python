# FastGPTRequest

Used to upload the query to FastGPT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**cache** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.fast_gpt_request import FastGPTRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FastGPTRequest from a JSON string
fast_gpt_request_instance = FastGPTRequest.from_json(json)
# print the JSON string representation of the object
print(FastGPTRequest.to_json())

# convert the object into a dict
fast_gpt_request_dict = fast_gpt_request_instance.to_dict()
# create an instance of FastGPTRequest from a dict
fast_gpt_request_from_dict = FastGPTRequest.from_dict(fast_gpt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


