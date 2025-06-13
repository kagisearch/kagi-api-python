# openapi_client.EnrichmentApi

All URIs are relative to *https://kagi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrich_search**](EnrichmentApi.md#enrich_search) | **GET** /enrich/{type} | Get enriched search results


# **enrich_search**
> EnrichSearch200Response enrich_search(q, type)

Get enriched search results

### Example

* Api Key Authentication (kagi):

```python
import openapi_client
from openapi_client.models.enrich_search200_response import EnrichSearch200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kagi.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://kagi.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: kagi
configuration.api_key['kagi'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['kagi'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EnrichmentApi(api_client)
    q = 'steve jobs' # str | Query to enrich
    type = web # str | Enrich with 'web' results or 'news' results (default to web)

    try:
        # Get enriched search results
        api_response = api_instance.enrich_search(q, type)
        print("The response of EnrichmentApi->enrich_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrichmentApi->enrich_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query to enrich | 
 **type** | **str**| Enrich with &#39;web&#39; results or &#39;news&#39; results | [default to web]

### Return type

[**EnrichSearch200Response**](EnrichSearch200Response.md)

### Authorization

[kagi](../README.md#kagi)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

