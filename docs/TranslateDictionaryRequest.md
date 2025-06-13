# TranslateDictionaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word to look up | 
**word_language** | **str** | Language code (ISO-639) of the word, or \&quot;auto\&quot; for automatic detection | [optional] [default to 'en']
**definition_language** | **str** | Language code (ISO-639) for the definition output | [optional] [default to 'en']

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


