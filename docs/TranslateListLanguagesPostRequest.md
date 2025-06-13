# TranslateListLanguagesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of languages to return (&#39;source&#39; or &#39;target&#39;) | [optional] 
**locale** | **str** | Locale code to use for language names (e.g., &#39;en&#39;, &#39;de&#39;, &#39;fr&#39;) | [optional] 

## Example

```python
from openapi_client.models.translate_list_languages_post_request import TranslateListLanguagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateListLanguagesPostRequest from a JSON string
translate_list_languages_post_request_instance = TranslateListLanguagesPostRequest.from_json(json)
# print the JSON string representation of the object
print(TranslateListLanguagesPostRequest.to_json())

# convert the object into a dict
translate_list_languages_post_request_dict = translate_list_languages_post_request_instance.to_dict()
# create an instance of TranslateListLanguagesPostRequest from a dict
translate_list_languages_post_request_from_dict = TranslateListLanguagesPostRequest.from_dict(translate_list_languages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


