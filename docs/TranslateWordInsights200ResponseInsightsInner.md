# TranslateWordInsights200ResponseInsightsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier matching the marker in marked_translation | [optional] 
**original_text** | **str** | The original word or phrase from the translated text | [optional] 
**variations** | [**List[TranslateWordInsights200ResponseInsightsInnerVariationsInner]**](TranslateWordInsights200ResponseInsightsInnerVariationsInner.md) | Alternative expressions with explanations | [optional] 
**type** | **str** | Category of the insight in the explanation language | [optional] 

## Example

```python
from openapi_client.models.translate_word_insights200_response_insights_inner import TranslateWordInsights200ResponseInsightsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateWordInsights200ResponseInsightsInner from a JSON string
translate_word_insights200_response_insights_inner_instance = TranslateWordInsights200ResponseInsightsInner.from_json(json)
# print the JSON string representation of the object
print(TranslateWordInsights200ResponseInsightsInner.to_json())

# convert the object into a dict
translate_word_insights200_response_insights_inner_dict = translate_word_insights200_response_insights_inner_instance.to_dict()
# create an instance of TranslateWordInsights200ResponseInsightsInner from a dict
translate_word_insights200_response_insights_inner_from_dict = TranslateWordInsights200ResponseInsightsInner.from_dict(translate_word_insights200_response_insights_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


