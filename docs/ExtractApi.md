# openapi_client.ExtractApi

All URIs are relative to *https://kagi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_content**](ExtractApi.md#extract_content) | **POST** /extract | Extract page content as markdown from URLs


# **extract_content**
> ExtractResponse extract_content(extract_request)

Extract page content as markdown from URLs

Extracts markdown content from up to 10 HTTP(s) URLs. Each URL is processed
and the extracted content is returned in the response.


### Example

* Bearer Authentication (kagi):

```python
import openapi_client
from openapi_client.models.extract_request import ExtractRequest
from openapi_client.models.extract_response import ExtractResponse
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

# Configure Bearer authorization: kagi
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExtractApi(api_client)
    extract_request = {"pages":[{"url":"https://example.com/article1"},{"url":"https://example.com/article2"}],"timeout":30,"format":"json"} # ExtractRequest | 

    try:
        # Extract page content as markdown from URLs
        api_response = api_instance.extract_content(extract_request)
        print("The response of ExtractApi->extract_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractApi->extract_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_request** | [**ExtractRequest**](ExtractRequest.md)|  | 

### Return type

[**ExtractResponse**](ExtractResponse.md)

### Authorization

[kagi](../README.md#kagi)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/markdown

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful extraction |  -  |
**400** | Invalid request parameters |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Forbidden - IP address not authorized |  -  |
**429** | Rate limited or usage limit exhausted |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

