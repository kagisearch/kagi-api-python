# EnrichSearch200Response

An array of search objects that can enrich a search query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[SearchObject]**](SearchObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.enrich_search200_response import EnrichSearch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichSearch200Response from a JSON string
enrich_search200_response_instance = EnrichSearch200Response.from_json(json)
# print the JSON string representation of the object
print(EnrichSearch200Response.to_json())

# convert the object into a dict
enrich_search200_response_dict = enrich_search200_response_instance.to_dict()
# create an instance of EnrichSearch200Response from a dict
enrich_search200_response_from_dict = EnrichSearch200Response.from_dict(enrich_search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


