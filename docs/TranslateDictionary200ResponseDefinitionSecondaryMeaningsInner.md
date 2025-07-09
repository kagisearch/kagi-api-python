# TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | **str** | The text of a secondary definition | [optional] 
**part_of_speech** | **List[str]** | The part(s) of speech that apply to this specific meaning | [optional] 
**usage_level** | **List[str]** | Register or context where this specific meaning is used (formal, informal, slang, technical, etc.) | [optional] 
**dialect** | **List[str]** | Specific dialects where this meaning is used | [optional] 
**synonyms** | **List[str]** | List of synonyms for this meaning, ordered from strongest/closest to least similar | [optional] 

## Example

```python
from openapi_client.models.translate_dictionary200_response_definition_secondary_meanings_inner import TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner from a JSON string
translate_dictionary200_response_definition_secondary_meanings_inner_instance = TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner.from_json(json)
# print the JSON string representation of the object
print(TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner.to_json())

# convert the object into a dict
translate_dictionary200_response_definition_secondary_meanings_inner_dict = translate_dictionary200_response_definition_secondary_meanings_inner_instance.to_dict()
# create an instance of TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner from a dict
translate_dictionary200_response_definition_secondary_meanings_inner_from_dict = TranslateDictionary200ResponseDefinitionSecondaryMeaningsInner.from_dict(translate_dictionary200_response_definition_secondary_meanings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


