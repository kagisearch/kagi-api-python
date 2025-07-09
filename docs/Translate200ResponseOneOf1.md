# Translate200ResponseOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snippets** | **List[str]** | Array of translated text snippets (for batch translation). The order matches the input array and preserves context between snippets. | [optional] 

## Example

```python
from openapi_client.models.translate200_response_one_of1 import Translate200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of Translate200ResponseOneOf1 from a JSON string
translate200_response_one_of1_instance = Translate200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(Translate200ResponseOneOf1.to_json())

# convert the object into a dict
translate200_response_one_of1_dict = translate200_response_one_of1_instance.to_dict()
# create an instance of Translate200ResponseOneOf1 from a dict
translate200_response_one_of1_from_dict = Translate200ResponseOneOf1.from_dict(translate200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


