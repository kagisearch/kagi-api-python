# TranslateDetectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text to detect language from | 

## Example

```python
from openapi_client.models.translate_detect_request import TranslateDetectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDetectRequest from a JSON string
translate_detect_request_instance = TranslateDetectRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateDetectRequest.to_json())

# convert the object into a dict
translate_detect_request_dict = translate_detect_request_instance.to_dict()
# create an instance of TranslateDetectRequest from a dict
translate_detect_request_from_dict = TranslateDetectRequest.from_dict(translate_detect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


