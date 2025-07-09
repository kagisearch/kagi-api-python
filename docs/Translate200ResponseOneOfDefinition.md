# Translate200ResponseOneOfDefinition

Dictionary definition of the translated term (if available)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word being defined | [optional] 
**phonetic** | **str** | Phonetic pronunciation | [optional] 
**definitions** | [**List[Translate200ResponseOneOfDefinitionDefinitionsInner]**](Translate200ResponseOneOfDefinitionDefinitionsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.translate200_response_one_of_definition import Translate200ResponseOneOfDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of Translate200ResponseOneOfDefinition from a JSON string
translate200_response_one_of_definition_instance = Translate200ResponseOneOfDefinition.from_json(json)
# print the JSON string representation of the object
print(Translate200ResponseOneOfDefinition.to_json())

# convert the object into a dict
translate200_response_one_of_definition_dict = translate200_response_one_of_definition_instance.to_dict()
# create an instance of Translate200ResponseOneOfDefinition from a dict
translate200_response_one_of_definition_from_dict = Translate200ResponseOneOfDefinition.from_dict(translate200_response_one_of_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


