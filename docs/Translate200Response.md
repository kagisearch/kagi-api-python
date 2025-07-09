# Translate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translation** | **str** | Translated text | [optional] 
**detected_language** | [**Translate200ResponseOneOfDetectedLanguage**](Translate200ResponseOneOfDetectedLanguage.md) |  | [optional] 
**definition** | [**Translate200ResponseOneOfDefinition**](Translate200ResponseOneOfDefinition.md) |  | [optional] 
**snippets** | **List[str]** | Array of translated text snippets (for batch translation). The order matches the input array and preserves context between snippets. | [optional] 

## Example

```python
from openapi_client.models.translate200_response import Translate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Translate200Response from a JSON string
translate200_response_instance = Translate200Response.from_json(json)
# print the JSON string representation of the object
print(Translate200Response.to_json())

# convert the object into a dict
translate200_response_dict = translate200_response_instance.to_dict()
# create an instance of Translate200Response from a dict
translate200_response_from_dict = Translate200Response.from_dict(translate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


