# ErrorEnvelope

API error response envelope containing metadata and an array of error details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**data** | **List[object]** | Empty data array when error occurs | [optional] 
**error** | [**List[ErrorDetail]**](ErrorDetail.md) | Array of error detail objects describing what went wrong | 

## Example

```python
from openapi_client.models.error_envelope import ErrorEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorEnvelope from a JSON string
error_envelope_instance = ErrorEnvelope.from_json(json)
# print the JSON string representation of the object
print(ErrorEnvelope.to_json())

# convert the object into a dict
error_envelope_dict = error_envelope_instance.to_dict()
# create an instance of ErrorEnvelope from a dict
error_envelope_from_dict = ErrorEnvelope.from_dict(error_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


