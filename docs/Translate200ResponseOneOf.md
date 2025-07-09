# Translate200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translation** | **str** | Translated text | [optional] 
**detected_language** | [**Translate200ResponseOneOfDetectedLanguage**](Translate200ResponseOneOfDetectedLanguage.md) |  | [optional] 
**definition** | [**Translate200ResponseOneOfDefinition**](Translate200ResponseOneOfDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.translate200_response_one_of import Translate200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of Translate200ResponseOneOf from a JSON string
translate200_response_one_of_instance = Translate200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(Translate200ResponseOneOf.to_json())

# convert the object into a dict
translate200_response_one_of_dict = translate200_response_one_of_instance.to_dict()
# create an instance of Translate200ResponseOneOf from a dict
translate200_response_one_of_from_dict = Translate200ResponseOneOf.from_dict(translate200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


