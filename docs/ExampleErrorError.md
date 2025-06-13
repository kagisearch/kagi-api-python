# ExampleErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | 
**msg** | **str** |  | 
**ref** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.example_error_error import ExampleErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleErrorError from a JSON string
example_error_error_instance = ExampleErrorError.from_json(json)
# print the JSON string representation of the object
print(ExampleErrorError.to_json())

# convert the object into a dict
example_error_error_dict = example_error_error_instance.to_dict()
# create an instance of ExampleErrorError from a dict
example_error_error_from_dict = ExampleErrorError.from_dict(example_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


