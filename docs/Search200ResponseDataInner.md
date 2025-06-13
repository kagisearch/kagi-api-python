# Search200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t** | **int** |  | 
**rank** | **int** |  | [optional] 
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**thumbnail** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**image** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**list** | **List[str]** |  | 

## Example

```python
from openapi_client.models.search200_response_data_inner import Search200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of Search200ResponseDataInner from a JSON string
search200_response_data_inner_instance = Search200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(Search200ResponseDataInner.to_json())

# convert the object into a dict
search200_response_data_inner_dict = search200_response_data_inner_instance.to_dict()
# create an instance of Search200ResponseDataInner from a dict
search200_response_data_inner_from_dict = Search200ResponseDataInner.from_dict(search200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


