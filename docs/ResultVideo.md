# ResultVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**image** | [**ResultSearchImage**](ResultSearchImage.md) |  | [optional] 
**props** | [**ResultVideoProps**](ResultVideoProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.result_video import ResultVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ResultVideo from a JSON string
result_video_instance = ResultVideo.from_json(json)
# print the JSON string representation of the object
print(ResultVideo.to_json())

# convert the object into a dict
result_video_dict = result_video_instance.to_dict()
# create an instance of ResultVideo from a dict
result_video_from_dict = ResultVideo.from_dict(result_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


