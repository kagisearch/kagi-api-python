# TranslateDictionary200ResponseLanguage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | ISO code of the language | [optional] 
**label** | **str** | Human-readable language name | [optional] 

## Example

```python
from openapi_client.models.translate_dictionary200_response_language import TranslateDictionary200ResponseLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateDictionary200ResponseLanguage from a JSON string
translate_dictionary200_response_language_instance = TranslateDictionary200ResponseLanguage.from_json(json)
# print the JSON string representation of the object
print(TranslateDictionary200ResponseLanguage.to_json())

# convert the object into a dict
translate_dictionary200_response_language_dict = translate_dictionary200_response_language_instance.to_dict()
# create an instance of TranslateDictionary200ResponseLanguage from a dict
translate_dictionary200_response_language_from_dict = TranslateDictionary200ResponseLanguage.from_dict(translate_dictionary200_response_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


