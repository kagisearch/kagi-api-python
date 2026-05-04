# PageInput

A single page to extract content from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTPS URL of the page to extract content from. Must use HTTPS scheme with a valid host.  | 

## Example

```python
from openapi_client.models.page_input import PageInput

# TODO update the JSON string below
json = "{}"
# create an instance of PageInput from a JSON string
page_input_instance = PageInput.from_json(json)
# print the JSON string representation of the object
print(PageInput.to_json())

# convert the object into a dict
page_input_dict = page_input_instance.to_dict()
# create an instance of PageInput from a dict
page_input_from_dict = PageInput.from_dict(page_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


