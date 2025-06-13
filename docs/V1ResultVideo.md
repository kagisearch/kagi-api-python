# V1ResultVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**title** | **str** |  | 
**snippet** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**image** | [**V1ResultSearchImage**](V1ResultSearchImage.md) |  | [optional] 
**props** | [**V1ResultVideoProps**](V1ResultVideoProps.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_result_video import V1ResultVideo

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResultVideo from a JSON string
v1_result_video_instance = V1ResultVideo.from_json(json)
# print the JSON string representation of the object
print(V1ResultVideo.to_json())

# convert the object into a dict
v1_result_video_dict = v1_result_video_instance.to_dict()
# create an instance of V1ResultVideo from a dict
v1_result_video_from_dict = V1ResultVideo.from_dict(v1_result_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


