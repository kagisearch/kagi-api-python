# TranslateDictionary200ResponseDefinition

Structured definition of the word

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word being defined | [optional] 
**part_of_speech** | **List[str]** | All parts of speech that apply to the word across all meanings | [optional] 
**usage_level** | **List[str]** | Register or context where the word is typically used (formal, informal, slang, technical, etc.) | [optional] 
**primary_meaning** | [**TranslateDictionary200ResponseDefinitionPrimaryMeaning**](TranslateDictionary200ResponseDefinitionPrimaryMeaning.md) |  | [optional] 
**secondary_meanings** | [**List[TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner]**](TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner.md) | Secondary or less common meanings | [optional] 
**examples** | **List[str]** | Example sentences showing usage | [optional] 
**pronunciation** | **str** | Phonetic pronunciation (if available) | [optional] 
**etymology** | **str** | Information about word origin (if available) | [optional] 

## Example

```python
from openapi_client.models.translate_dictionary200_response_definition import TranslateDictionary200ResponseDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDictionary200ResponseDefinition from a JSON string
translate_dictionary200_response_definition_instance = TranslateDictionary200ResponseDefinition.from_json(json)
# print the JSON string representation of the object
print(TranslateDictionary200ResponseDefinition.to_json())

# convert the object into a dict
translate_dictionary200_response_definition_dict = translate_dictionary200_response_definition_instance.to_dict()
# create an instance of TranslateDictionary200ResponseDefinition from a dict
translate_dictionary200_response_definition_from_dict = TranslateDictionary200ResponseDefinition.from_dict(translate_dictionary200_response_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


