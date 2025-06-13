# V1ResultAdjacentQuestionProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_adjacent_question_props import V1ResultAdjacentQuestionProps

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultAdjacentQuestionProps from a JSON string
v1_result_adjacent_question_props_instance = V1ResultAdjacentQuestionProps.from_json(json)
# print the JSON string representation of the object
print(V1ResultAdjacentQuestionProps.to_json())

# convert the object into a dict
v1_result_adjacent_question_props_dict = v1_result_adjacent_question_props_instance.to_dict()
# create an instance of V1ResultAdjacentQuestionProps from a dict
v1_result_adjacent_question_props_from_dict = V1ResultAdjacentQuestionProps.from_dict(v1_result_adjacent_question_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


