# TranslateDictionaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word to look up | 
**word_language** | **str** | Language code (ISO-639) of the word, or \&quot;auto\&quot; for automatic detection | [optional] [default to 'en']
**definition_language** | **str** | Language code (ISO-639) for the definition output | [optional] [default to 'en']
**stream** | **bool** | Whether to return a streaming response with fields sent as they become available | [optional] [default to False]
**nsfw** | **bool** | Whether to allow NSFW/inappropriate content. If false, returns empty definition for inappropriate words | [optional] [default to True]
**model** | **str** | Optional model identifier. Can be either a model name (e.g., \&quot;gpt-4o\&quot;, \&quot;claude-35-sonnet\&quot;, \&quot;gemini-flash-2.0\&quot;) or a model constant (e.g., \&quot;ANTHROPIC_CLAUDE_35_SONNET\&quot;, \&quot;OPENAI_GPT4O\&quot;). See model-selection.ts for full list. | [optional] 

## Example

```python
from openapi_client.models.translate_dictionary_request import TranslateDictionaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDictionaryRequest from a JSON string
translate_dictionary_request_instance = TranslateDictionaryRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateDictionaryRequest.to_json())

# convert the object into a dict
translate_dictionary_request_dict = translate_dictionary_request_instance.to_dict()
# create an instance of TranslateDictionaryRequest from a dict
translate_dictionary_request_from_dict = TranslateDictionaryRequest.from_dict(translate_dictionary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


