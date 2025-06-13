# TranslateProofReadGet200ResponseRepetitionDetection

Analysis of repeated words and phrases

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeated_words** | [**List[TranslateProofReadGet200ResponseRepetitionDetectionRepeatedWordsInner]**](TranslateProofReadGet200ResponseRepetitionDetectionRepeatedWordsInner.md) | Words that appear frequently in the text | [optional] 
**repeated_phrases** | [**List[TranslateProofReadGet200ResponseRepetitionDetectionRepeatedPhrasesInner]**](TranslateProofReadGet200ResponseRepetitionDetectionRepeatedPhrasesInner.md) | Phrases that appear frequently in the text | [optional] 
**summary** | **str** | Overall assessment of word/phrase repetition and its impact | [optional] 

## Example

```python
from openapi_client.models.translate_proof_read_get200_response_repetition_detection import TranslateProofReadGet200ResponseRepetitionDetection

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateProofReadGet200ResponseRepetitionDetection from a JSON string
translate_proof_read_get200_response_repetition_detection_instance = TranslateProofReadGet200ResponseRepetitionDetection.from_json(json)
# print the JSON string representation of the object
print(TranslateProofReadGet200ResponseRepetitionDetection.to_json())

# convert the object into a dict
translate_proof_read_get200_response_repetition_detection_dict = translate_proof_read_get200_response_repetition_detection_instance.to_dict()
# create an instance of TranslateProofReadGet200ResponseRepetitionDetection from a dict
translate_proof_read_get200_response_repetition_detection_from_dict = TranslateProofReadGet200ResponseRepetitionDetection.from_dict(translate_proof_read_get200_response_repetition_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


