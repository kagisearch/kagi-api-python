# UploadText

Used to upload text to be summarized

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from openapi_client.models.upload_text import UploadText

# TODO update the JSON string below
json = "{}"
# create an instance of UploadText from a JSON string
upload_text_instance = UploadText.from_json(json)
# print the JSON string representation of the object
print(UploadText.to_json())

# convert the object into a dict
upload_text_dict = upload_text_instance.to_dict()
# create an instance of UploadText from a dict
upload_text_from_dict = UploadText.from_dict(upload_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


