# TranslateProofReadGet200ResponseChangesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | Original text segment with the error | [optional] 
**correction** | **str** | Corrected text segment | [optional] 
**explanation** | **str** | Brief explanation of why this change was necessary | [optional] 
**types** | **List[str]** | Array of correction types/reasons that explain why the change was necessary (e.g., grammar, spelling, punctuation, word_choice, style, typography, formatting, clarity, etc.) | [optional] 
**severity** | **str** | Importance of this correction | [optional] 

## Example

```python
from openapi_client.models.translate_proof_read_get200_response_changes_inner import TranslateProofReadGet200ResponseChangesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateProofReadGet200ResponseChangesInner from a JSON string
translate_proof_read_get200_response_changes_inner_instance = TranslateProofReadGet200ResponseChangesInner.from_json(json)
# print the JSON string representation of the object
print(TranslateProofReadGet200ResponseChangesInner.to_json())

# convert the object into a dict
translate_proof_read_get200_response_changes_inner_dict = translate_proof_read_get200_response_changes_inner_instance.to_dict()
# create an instance of TranslateProofReadGet200ResponseChangesInner from a dict
translate_proof_read_get200_response_changes_inner_from_dict = TranslateProofReadGet200ResponseChangesInner.from_dict(translate_proof_read_get200_response_changes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


