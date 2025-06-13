# TranslateProofReadGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corrected_text** | **str** | The proofread and corrected text | [optional] 
**detected_language** | [**TranslateProofReadGet200ResponseDetectedLanguage**](TranslateProofReadGet200ResponseDetectedLanguage.md) |  | [optional] 
**changes** | [**List[TranslateProofReadGet200ResponseChangesInner]**](TranslateProofReadGet200ResponseChangesInner.md) |  | [optional] 
**corrections_summary** | **str** | Overall explanation of corrections or acknowledgment of error-free text | [optional] 
**tone_analysis** | [**TranslateProofReadGet200ResponseToneAnalysis**](TranslateProofReadGet200ResponseToneAnalysis.md) |  | [optional] 
**voice_consistency** | [**TranslateProofReadGet200ResponseVoiceConsistency**](TranslateProofReadGet200ResponseVoiceConsistency.md) |  | [optional] 
**repetition_detection** | [**TranslateProofReadGet200ResponseRepetitionDetection**](TranslateProofReadGet200ResponseRepetitionDetection.md) |  | [optional] 
**explanation_language** | **str** | ISO code of the language used for explanations and analysis | [optional] 

## Example

```python
from openapi_client.models.translate_proof_read_get200_response import TranslateProofReadGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateProofReadGet200Response from a JSON string
translate_proof_read_get200_response_instance = TranslateProofReadGet200Response.from_json(json)
# print the JSON string representation of the object
print(TranslateProofReadGet200Response.to_json())

# convert the object into a dict
translate_proof_read_get200_response_dict = translate_proof_read_get200_response_instance.to_dict()
# create an instance of TranslateProofReadGet200Response from a dict
translate_proof_read_get200_response_from_dict = TranslateProofReadGet200Response.from_dict(translate_proof_read_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


