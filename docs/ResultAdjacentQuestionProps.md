# ResultAdjacentQuestionProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**language_probability** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.result_adjacent_question_props import ResultAdjacentQuestionProps

# TODO update the JSON string below
json = "{}"
# create an instance of ResultAdjacentQuestionProps from a JSON string
result_adjacent_question_props_instance = ResultAdjacentQuestionProps.from_json(json)
# print the JSON string representation of the object
print(ResultAdjacentQuestionProps.to_json())

# convert the object into a dict
result_adjacent_question_props_dict = result_adjacent_question_props_instance.to_dict()
# create an instance of ResultAdjacentQuestionProps from a dict
result_adjacent_question_props_from_dict = ResultAdjacentQuestionProps.from_dict(result_adjacent_question_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


