# ResultAdjacentQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | 
**time** | **str** |  | [optional] 
**image** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 
**props** | [**ResultAdjacentQuestionProps**](ResultAdjacentQuestionProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.result_adjacent_question import ResultAdjacentQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of ResultAdjacentQuestion from a JSON string
result_adjacent_question_instance = ResultAdjacentQuestion.from_json(json)
# print the JSON string representation of the object
print(ResultAdjacentQuestion.to_json())

# convert the object into a dict
result_adjacent_question_dict = result_adjacent_question_instance.to_dict()
# create an instance of ResultAdjacentQuestion from a dict
result_adjacent_question_from_dict = ResultAdjacentQuestion.from_dict(result_adjacent_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


