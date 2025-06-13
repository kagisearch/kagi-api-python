# TranslateDictionary200ResponseDefinitionPrimaryMeaning

The primary or most common meaning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | **str** | The text of the primary definition | [optional] 
**part_of_speech** | **List[str]** | The part(s) of speech that apply to this specific meaning | [optional] 

## Example

```python
from openapi_client.models.translate_dictionary200_response_definition_primary_meaning import TranslateDictionary200ResponseDefinitionPrimaryMeaning

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDictionary200ResponseDefinitionPrimaryMeaning from a JSON string
translate_dictionary200_response_definition_primary_meaning_instance = TranslateDictionary200ResponseDefinitionPrimaryMeaning.from_json(json)
# print the JSON string representation of the object
print(TranslateDictionary200ResponseDefinitionPrimaryMeaning.to_json())

# convert the object into a dict
translate_dictionary200_response_definition_primary_meaning_dict = translate_dictionary200_response_definition_primary_meaning_instance.to_dict()
# create an instance of TranslateDictionary200ResponseDefinitionPrimaryMeaning from a dict
translate_dictionary200_response_definition_primary_meaning_from_dict = TranslateDictionary200ResponseDefinitionPrimaryMeaning.from_dict(translate_dictionary200_response_definition_primary_meaning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


