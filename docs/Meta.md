# Meta

This object is subject to change as it is provided for debugging purposes. Fields may be added or removed as required. Don't build any hard dependancies on any of this data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace** | **str** | Trace ID that can be used to debug individual API requests. Provide this, if needed, when contacting Kagi support. | [optional] 
**id** | **str** |  | [optional] 
**node** | **str** | The hostname of the node that fulfilled the request. | [optional] 
**ms** | **int** | how long the request took to fulfill, excluding round trip to the client. | [optional] 

## Example

```python
from openapi_client.models.meta import Meta

# TODO update the JSON string below
json = "{}"
# create an instance of Meta from a JSON string
meta_instance = Meta.from_json(json)
# print the JSON string representation of the object
print(Meta.to_json())

# convert the object into a dict
meta_dict = meta_instance.to_dict()
# create an instance of Meta from a dict
meta_from_dict = Meta.from_dict(meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


