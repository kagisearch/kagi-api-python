# openapi_client.SearchApi

All URIs are relative to *https://kagi.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Perform a search.
[**super_search**](SearchApi.md#super_search) | **GET** /v1/search | Perform a super charged search.


# **search**
> Search200Response search(q, limit=limit)

Perform a search.

### Example

* Api Key Authentication (kagi):

```python
import openapi_client
from openapi_client.models.search200_response import Search200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kagi.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://kagi.com/api/v0"
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
    api_instance = openapi_client.SearchApi(api_client)
    q = 'q_example' # str | A query used to perform the search.
    limit = 56 # int | Limit number of search results. (optional)

    try:
        # Perform a search.
        api_response = api_instance.search(q, limit=limit)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A query used to perform the search. | 
 **limit** | **int**| Limit number of search results. | [optional] 

### Return type

[**Search200Response**](Search200Response.md)

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

# **super_search**
> SuperSearch200Response super_search(super_search_request)

Perform a super charged search.

### Example

* Api Key Authentication (kagi):

```python
import openapi_client
from openapi_client.models.super_search200_response import SuperSearch200Response
from openapi_client.models.super_search_request import SuperSearchRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://kagi.com/api/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://kagi.com/api/v0"
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
    api_instance = openapi_client.SearchApi(api_client)
    super_search_request = openapi_client.SuperSearchRequest() # SuperSearchRequest | Contains the search query to run

    try:
        # Perform a super charged search.
        api_response = api_instance.super_search(super_search_request)
        print("The response of SearchApi->super_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->super_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **super_search_request** | [**SuperSearchRequest**](SuperSearchRequest.md)| Contains the search query to run | 

### Return type

[**SuperSearch200Response**](SuperSearch200Response.md)

### Authorization

[kagi](../README.md#kagi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

