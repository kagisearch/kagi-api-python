# TranslateProofReadGet200ResponseVoiceConsistency

Analysis of active vs. passive voice usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_voice_percentage** | **float** | Approximate percentage of sentences using active voice | [optional] 
**passive_voice_percentage** | **float** | Approximate percentage of sentences using passive voice | [optional] 
**is_consistent** | **bool** | Whether the voice usage is consistent throughout | [optional] 
**suggestion** | **str** | Optional suggestion about voice usage | [optional] 
**passive_instances** | [**List[TranslateProofReadGet200ResponseVoiceConsistencyPassiveInstancesInner]**](TranslateProofReadGet200ResponseVoiceConsistencyPassiveInstancesInner.md) |  | [optional] 
**summary** | **str** | Overall assessment of voice usage and its effectiveness | [optional] 

## Example

```python
from openapi_client.models.translate_proof_read_get200_response_voice_consistency import TranslateProofReadGet200ResponseVoiceConsistency

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateProofReadGet200ResponseVoiceConsistency from a JSON string
translate_proof_read_get200_response_voice_consistency_instance = TranslateProofReadGet200ResponseVoiceConsistency.from_json(json)
# print the JSON string representation of the object
print(TranslateProofReadGet200ResponseVoiceConsistency.to_json())

# convert the object into a dict
translate_proof_read_get200_response_voice_consistency_dict = translate_proof_read_get200_response_voice_consistency_instance.to_dict()
# create an instance of TranslateProofReadGet200ResponseVoiceConsistency from a dict
translate_proof_read_get200_response_voice_consistency_from_dict = TranslateProofReadGet200ResponseVoiceConsistency.from_dict(translate_proof_read_get200_response_voice_consistency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


