# TranslateProofReadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text content to proofread | 
**source_lang** | **str** | Source language code (ISO-639) or \&quot;auto\&quot; for automatic detection | [optional] [default to 'auto']
**explanation_language** | **str** | Language code (ISO-639) for explanations and analysis. If not provided, explanations will be in the same language as the source text. | [optional] 
**stream** | **bool** | Whether to stream the response as Server-Sent Events | [optional] [default to False]

## Example

```python
from openapi_client.models.translate_proof_read_request import TranslateProofReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateProofReadRequest from a JSON string
translate_proof_read_request_instance = TranslateProofReadRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateProofReadRequest.to_json())

# convert the object into a dict
translate_proof_read_request_dict = translate_proof_read_request_instance.to_dict()
# create an instance of TranslateProofReadRequest from a dict
translate_proof_read_request_from_dict = TranslateProofReadRequest.from_dict(translate_proof_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


