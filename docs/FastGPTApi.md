# openapi_client.FastGPTApi

All URIs are relative to *https://kagi.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fast_gpt**](FastGPTApi.md#fast_gpt) | **POST** /fastgpt | Answer a query.


# **fast_gpt**
> FastGPT200Response fast_gpt(fast_gpt_request)

Answer a query.

FastGPT is a Kagi service using powerful LLMs to answer user queries running a full search engine underneath. Think ChatGPT, but on steroids and faster! You can try the web app here.

### Example

* Api Key Authentication (kagi):

```python
import openapi_client
from openapi_client.models.fast_gpt200_response import FastGPT200Response
from openapi_client.models.fast_gpt_request import FastGPTRequest
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
    api_instance = openapi_client.FastGPTApi(api_client)
    fast_gpt_request = openapi_client.FastGPTRequest() # FastGPTRequest | Contains the query to process.

    try:
        # Answer a query.
        api_response = api_instance.fast_gpt(fast_gpt_request)
        print("The response of FastGPTApi->fast_gpt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FastGPTApi->fast_gpt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fast_gpt_request** | [**FastGPTRequest**](FastGPTRequest.md)| Contains the query to process. | 

### Return type

[**FastGPT200Response**](FastGPT200Response.md)

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

