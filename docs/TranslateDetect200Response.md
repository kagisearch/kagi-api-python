# TranslateDetect200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | ISO code of detected language | [optional] 
**label** | **str** | Human-readable language name | [optional] 

## Example

```python
from openapi_client.models.translate_detect200_response import TranslateDetect200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDetect200Response from a JSON string
translate_detect200_response_instance = TranslateDetect200Response.from_json(json)
# print the JSON string representation of the object
print(TranslateDetect200Response.to_json())

# convert the object into a dict
translate_detect200_response_dict = translate_detect200_response_instance.to_dict()
# create an instance of TranslateDetect200Response from a dict
translate_detect200_response_from_dict = TranslateDetect200Response.from_dict(translate_detect200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


