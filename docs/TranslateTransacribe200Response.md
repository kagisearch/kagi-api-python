# TranslateTransacribe200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transcription** | **str** | The transcribed text, with appropriate punctuation and formatting | [optional] 
**detected_language** | **str** | The detected language code (when using automatic detection) | [optional] 

## Example

```python
from openapi_client.models.translate_transacribe200_response import TranslateTransacribe200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTransacribe200Response from a JSON string
translate_transacribe200_response_instance = TranslateTransacribe200Response.from_json(json)
# print the JSON string representation of the object
print(TranslateTransacribe200Response.to_json())

# convert the object into a dict
translate_transacribe200_response_dict = translate_transacribe200_response_instance.to_dict()
# create an instance of TranslateTransacribe200Response from a dict
translate_transacribe200_response_from_dict = TranslateTransacribe200Response.from_dict(translate_transacribe200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


