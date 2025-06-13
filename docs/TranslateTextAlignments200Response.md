# TranslateTextAlignments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignments** | [**List[TranslateTextAlignments200ResponseAlignmentsInner]**](TranslateTextAlignments200ResponseAlignmentsInner.md) | Array of alignment entries between source and target text segments | [optional] 

## Example

```python
from openapi_client.models.translate_text_alignments200_response import TranslateTextAlignments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTextAlignments200Response from a JSON string
translate_text_alignments200_response_instance = TranslateTextAlignments200Response.from_json(json)
# print the JSON string representation of the object
print(TranslateTextAlignments200Response.to_json())

# convert the object into a dict
translate_text_alignments200_response_dict = translate_text_alignments200_response_instance.to_dict()
# create an instance of TranslateTextAlignments200Response from a dict
translate_text_alignments200_response_from_dict = TranslateTextAlignments200Response.from_dict(translate_text_alignments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


