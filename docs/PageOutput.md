# PageOutput

Extracted content for a single page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the extracted page | 
**markdown** | **str** | Extracted markdown content of the page | [optional] 

## Example

```python
from openapi_client.models.page_output import PageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PageOutput from a JSON string
page_output_instance = PageOutput.from_json(json)
# print the JSON string representation of the object
print(PageOutput.to_json())

# convert the object into a dict
page_output_dict = page_output_instance.to_dict()
# create an instance of PageOutput from a dict
page_output_from_dict = PageOutput.from_dict(page_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


