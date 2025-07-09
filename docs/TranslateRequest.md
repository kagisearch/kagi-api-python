# TranslateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | [**TranslateRequestText**](TranslateRequestText.md) |  | 
**source_lang** | **str** | Source language code (ISO-639) or \&quot;auto\&quot; for automatic detection | [optional] [default to 'auto']
**target_lang** | **str** | Target language code (ISO-639) | [optional] [default to 'en']
**var_from** | **str** | Legacy parameter for source language (use source_lang instead) | [optional] 
**to** | **str** | Legacy parameter for target language (use target_lang instead) | [optional] 
**context** | **str** | Additional context to improve translation accuracy | [optional] 
**preserve_formatting** | **bool** | Whether to preserve original text formatting | [optional] [default to False]
**formality** | **str** | Level of formality in translation. All formality levels are supported for all language pairs. &#39;prefer_more&#39; is same as &#39;more&#39;, and &#39;prefer_less&#39; is same as &#39;less&#39; (included for backwards compatibility). | [optional] [default to 'default']
**speaker_gender** | **str** | Gender of the speaker for languages with gender-specific expressions | [optional] [default to 'unknown']
**addressee_gender** | **str** | Gender of the addressee for languages with gender-specific expressions | [optional] [default to 'unknown']
**translation_style** | **str** | Style of translation (natural for fluency, literal for exactness) | [optional] [default to 'natural']
**predicted_language** | **str** | Pre-detected source language (if available) | [optional] 
**prediction** | **str** | Pre-generated translation (if available) | [optional] 
**stream** | **bool** | Whether to stream the response as Server-Sent Events | [optional] [default to False]
**dictionary_language** | **str** | Language code for dictionary definitions (if not provided, the source language will be used) | [optional] 

## Example

```python
from openapi_client.models.translate_request import TranslateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateRequest from a JSON string
translate_request_instance = TranslateRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateRequest.to_json())

# convert the object into a dict
translate_request_dict = translate_request_instance.to_dict()
# create an instance of TranslateRequest from a dict
translate_request_from_dict = TranslateRequest.from_dict(translate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


