# ExtractRequest

Request body for content extraction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[PageInput]**](PageInput.md) | Array of pages to extract content from. Must contain 1-10 URLs. Each URL must be a valid HTTPS URL.  | 
**timeout** | **float** | Optional timeout in seconds for the extraction operation | [optional] 
**format** | **str** | Response format | [optional] [default to 'json']

## Example

```python
from openapi_client.models.extract_request import ExtractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractRequest from a JSON string
extract_request_instance = ExtractRequest.from_json(json)
# print the JSON string representation of the object
print(ExtractRequest.to_json())

# convert the object into a dict
extract_request_dict = extract_request_instance.to_dict()
# create an instance of ExtractRequest from a dict
extract_request_from_dict = ExtractRequest.from_dict(extract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


