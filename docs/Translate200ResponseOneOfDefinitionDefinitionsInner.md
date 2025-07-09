# Translate200ResponseOneOfDefinitionDefinitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_of_speech** | **str** | Part of speech | [optional] 
**meanings** | [**List[Translate200ResponseOneOfDefinitionDefinitionsInnerMeaningsInner]**](Translate200ResponseOneOfDefinitionDefinitionsInnerMeaningsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.translate200_response_one_of_definition_definitions_inner import Translate200ResponseOneOfDefinitionDefinitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Translate200ResponseOneOfDefinitionDefinitionsInner from a JSON string
translate200_response_one_of_definition_definitions_inner_instance = Translate200ResponseOneOfDefinitionDefinitionsInner.from_json(json)
# print the JSON string representation of the object
print(Translate200ResponseOneOfDefinitionDefinitionsInner.to_json())

# convert the object into a dict
translate200_response_one_of_definition_definitions_inner_dict = translate200_response_one_of_definition_definitions_inner_instance.to_dict()
# create an instance of Translate200ResponseOneOfDefinitionDefinitionsInner from a dict
translate200_response_one_of_definition_definitions_inner_from_dict = Translate200ResponseOneOfDefinitionDefinitionsInner.from_dict(translate200_response_one_of_definition_definitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


