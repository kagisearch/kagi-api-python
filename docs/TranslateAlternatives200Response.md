# TranslateAlternatives200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_description** | **str** | A short description of the style, formality, or key characteristics of the text | [optional] 
**elements** | [**List[TranslateAlternatives200ResponseElementsInner]**](TranslateAlternatives200ResponseElementsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.translate_alternatives200_response import TranslateAlternatives200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateAlternatives200Response from a JSON string
translate_alternatives200_response_instance = TranslateAlternatives200Response.from_json(json)
# print the JSON string representation of the object
print(TranslateAlternatives200Response.to_json())

# convert the object into a dict
translate_alternatives200_response_dict = translate_alternatives200_response_instance.to_dict()
# create an instance of TranslateAlternatives200Response from a dict
translate_alternatives200_response_from_dict = TranslateAlternatives200Response.from_dict(translate_alternatives200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


