# TranslateDictionary200ResponseDefinition

Structured definition of the word

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word being defined (remains in word_language) | [optional] 
**primary_meaning** | [**TranslateDictionary200ResponseDefinitionPrimaryMeaning**](TranslateDictionary200ResponseDefinitionPrimaryMeaning.md) |  | [optional] 
**secondary_meanings** | [**List[TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner]**](TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner.md) | Secondary or less common meanings | [optional] 
**examples** | **List[str]** | Example sentences showing usage (remains in word_language, but includes translations in parentheses when word_language differs from definition_language) | [optional] 
**pronunciation** | **str** | Phonetic pronunciation of the word in its original language (if available) | [optional] 
**etymology** | **str** | Information about word origin (translated to definition_language if available) | [optional] 
**notes** | **str** | Brief usage notes, cultural context, or helpful tips for language learners (translated to definition_language) | [optional] 
**temporal_trend** | **str** | Optional usage trend indicator. Always in English as an enum value. Only provided when trend data is clear and meaningful. | [optional] 
**gender** | **str** | Grammatical gender for nouns in languages that have gender. Always in English as an enum value. Only included for nouns in gendered languages. | [optional] 
**plural** | **str** | Plural form of the word (remains in word_language). Only included for irregular or non-standard plurals. | [optional] 
**conjugation_notes** | **str** | Brief notes about verb conjugation irregularities (remains in word_language). Only included for verbs with notable irregularities. | [optional] 
**related_words** | **List[str]** | Related words from the same root or word family (remains in word_language) | [optional] 

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


