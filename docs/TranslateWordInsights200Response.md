# TranslateWordInsights200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marked_translation** | **str** | The translated text with markers (&lt;&lt;INSIGHT_N&gt;&gt;) indicating insight locations | [optional] 
**insights** | [**List[TranslateWordInsights200ResponseInsightsInner]**](TranslateWordInsights200ResponseInsightsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.translate_word_insights200_response import TranslateWordInsights200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateWordInsights200Response from a JSON string
translate_word_insights200_response_instance = TranslateWordInsights200Response.from_json(json)
# print the JSON string representation of the object
print(TranslateWordInsights200Response.to_json())

# convert the object into a dict
translate_word_insights200_response_dict = translate_word_insights200_response_instance.to_dict()
# create an instance of TranslateWordInsights200Response from a dict
translate_word_insights200_response_from_dict = TranslateWordInsights200Response.from_dict(translate_word_insights200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


