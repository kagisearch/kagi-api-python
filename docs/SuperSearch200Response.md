# SuperSearch200Response

A response with a description and results references used

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**SuperSearch200ResponseData**](SuperSearch200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.super_search200_response import SuperSearch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SuperSearch200Response from a JSON string
super_search200_response_instance = SuperSearch200Response.from_json(json)
# print the JSON string representation of the object
print(SuperSearch200Response.to_json())

# convert the object into a dict
super_search200_response_dict = super_search200_response_instance.to_dict()
# create an instance of SuperSearch200Response from a dict
super_search200_response_from_dict = SuperSearch200Response.from_dict(super_search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


