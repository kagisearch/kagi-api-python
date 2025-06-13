# ExampleError

I need an example error to appease the linter. Please accept my offering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**error** | [**ExampleErrorError**](ExampleErrorError.md) |  | 

## Example

```python
from openapi_client.models.example_error import ExampleError

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleError from a JSON string
example_error_instance = ExampleError.from_json(json)
# print the JSON string representation of the object
print(ExampleError.to_json())

# convert the object into a dict
example_error_dict = example_error_instance.to_dict()
# create an instance of ExampleError from a dict
example_error_from_dict = ExampleError.from_dict(example_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


