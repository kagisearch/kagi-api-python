# V1ResultAdjacentQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | 
**time** | **str** |  | [optional] 
**image** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**props** | [**V1ResultAdjacentQuestionProps**](V1ResultAdjacentQuestionProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_adjacent_question import V1ResultAdjacentQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultAdjacentQuestion from a JSON string
v1_result_adjacent_question_instance = V1ResultAdjacentQuestion.from_json(json)
# print the JSON string representation of the object
print(V1ResultAdjacentQuestion.to_json())

# convert the object into a dict
v1_result_adjacent_question_dict = v1_result_adjacent_question_instance.to_dict()
# create an instance of V1ResultAdjacentQuestion from a dict
v1_result_adjacent_question_from_dict = V1ResultAdjacentQuestion.from_dict(v1_result_adjacent_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


