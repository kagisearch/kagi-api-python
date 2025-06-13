# TranslateProofReadGet200ResponseToneAnalysis

Analysis of the text's tone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_tone** | **str** | The primary tone of the text (formal, informal, neutral, friendly, academic, professional, casual, etc.) | [optional] 
**description** | **str** | Brief description of the tone of the text | [optional] 
**suggestions** | **str** | Optional suggestions for tone adjustment if needed | [optional] 

## Example

```python
from openapi_client.models.translate_proof_read_get200_response_tone_analysis import TranslateProofReadGet200ResponseToneAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateProofReadGet200ResponseToneAnalysis from a JSON string
translate_proof_read_get200_response_tone_analysis_instance = TranslateProofReadGet200ResponseToneAnalysis.from_json(json)
# print the JSON string representation of the object
print(TranslateProofReadGet200ResponseToneAnalysis.to_json())

# convert the object into a dict
translate_proof_read_get200_response_tone_analysis_dict = translate_proof_read_get200_response_tone_analysis_instance.to_dict()
# create an instance of TranslateProofReadGet200ResponseToneAnalysis from a dict
translate_proof_read_get200_response_tone_analysis_from_dict = TranslateProofReadGet200ResponseToneAnalysis.from_dict(translate_proof_read_get200_response_tone_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


