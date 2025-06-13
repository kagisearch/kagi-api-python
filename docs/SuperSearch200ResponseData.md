# SuperSearch200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**List[ResultSearch]**](ResultSearch.md) |  | [optional] 
**video** | [**List[ResultVideo]**](ResultVideo.md) |  | [optional] 
**adjacent_question** | [**List[ResultAdjacentQuestion]**](ResultAdjacentQuestion.md) |  | [optional] 
**infobox** | [**List[ResultInfobox]**](ResultInfobox.md) |  | [optional] 
**web_archive** | [**List[ResultWebArchive]**](ResultWebArchive.md) |  | [optional] 

## Example

```python
from openapi_client.models.super_search200_response_data import SuperSearch200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SuperSearch200ResponseData from a JSON string
super_search200_response_data_instance = SuperSearch200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SuperSearch200ResponseData.to_json())

# convert the object into a dict
super_search200_response_data_dict = super_search200_response_data_instance.to_dict()
# create an instance of SuperSearch200ResponseData from a dict
super_search200_response_data_from_dict = SuperSearch200ResponseData.from_dict(super_search200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


