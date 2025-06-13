# openapi_client.SummarizerApi

All URIs are relative to *https://kagi.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**summarize_text**](SummarizerApi.md#summarize_text) | **POST** /summarize | Upload text to summarize.
[**summarize_url**](SummarizerApi.md#summarize_url) | **GET** /summarize | Get a summary for a URL


# **summarize_text**
> Summary summarize_text(upload_text, engine=engine, summary_type=summary_type, target_language=target_language, cache=cache)

Upload text to summarize.

### Example

* Api Key Authentication (kagi):

```python
import openapi_client
from openapi_client.models.summary import Summary
from openapi_client.models.upload_text import UploadText
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
    api_instance = openapi_client.SummarizerApi(api_client)
    upload_text = openapi_client.UploadText() # UploadText | Text to summarize
    engine = cecil # str | Different summarization engines are provided that will give you choices over the \"flavor\" of the summarization text. (optional) (default to cecil)
    summary_type = summary # str | Different summary types are provided that control the structure of the summary output. (optional) (default to summary)
    target_language = 'target_language_example' # str | The summarizer can translate the output into a desired language, using the table of supported language codes below.  If no language is specified, the document's original language is allowed to influence the summarizer's output. Specifying a language will add an explicit translation step, to translate the summary to the desired language.  For example, if a document is mostly written in Spanish, the summary output may itself be in Spanish or contain Spanish passages. Specifying \"EN\" will ensure all passages are translated as English.  (optional)
    cache = True # bool | Whether to allow cached requests & responses. (optional) (default to True)

    try:
        # Upload text to summarize.
        api_response = api_instance.summarize_text(upload_text, engine=engine, summary_type=summary_type, target_language=target_language, cache=cache)
        print("The response of SummarizerApi->summarize_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizerApi->summarize_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_text** | [**UploadText**](UploadText.md)| Text to summarize | 
 **engine** | **str**| Different summarization engines are provided that will give you choices over the \&quot;flavor\&quot; of the summarization text. | [optional] [default to cecil]
 **summary_type** | **str**| Different summary types are provided that control the structure of the summary output. | [optional] [default to summary]
 **target_language** | **str**| The summarizer can translate the output into a desired language, using the table of supported language codes below.  If no language is specified, the document&#39;s original language is allowed to influence the summarizer&#39;s output. Specifying a language will add an explicit translation step, to translate the summary to the desired language.  For example, if a document is mostly written in Spanish, the summary output may itself be in Spanish or contain Spanish passages. Specifying \&quot;EN\&quot; will ensure all passages are translated as English.  | [optional] 
 **cache** | **bool**| Whether to allow cached requests &amp; responses. | [optional] [default to True]

### Return type

[**Summary**](Summary.md)

### Authorization

[kagi](../README.md#kagi)

### HTTP request headers

 - **Content-Type**: application/json, x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarize_url**
> Summary summarize_url(url, engine=engine, summary_type=summary_type, target_language=target_language, cache=cache)

Get a summary for a URL

### Example

* Api Key Authentication (kagi):

```python
import openapi_client
from openapi_client.models.summary import Summary
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
    api_instance = openapi_client.SummarizerApi(api_client)
    url = 'url_example' # str | A URL to a document to summarize.
    engine = cecil # str | Different summarization engines are provided that will give you choices over the \"flavor\" of the summarization text. (optional) (default to cecil)
    summary_type = summary # str | Different summary types are provided that control the structure of the summary output. (optional) (default to summary)
    target_language = 'target_language_example' # str | The summarizer can translate the output into a desired language, using the table of supported language codes below.  If no language is specified, the document's original language is allowed to influence the summarizer's output. Specifying a language will add an explicit translation step, to translate the summary to the desired language.  For example, if a document is mostly written in Spanish, the summary output may itself be in Spanish or contain Spanish passages. Specifying \"EN\" will ensure all passages are translated as English.  (optional)
    cache = True # bool | Whether to allow cached requests & responses. (optional) (default to True)

    try:
        # Get a summary for a URL
        api_response = api_instance.summarize_url(url, engine=engine, summary_type=summary_type, target_language=target_language, cache=cache)
        print("The response of SummarizerApi->summarize_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizerApi->summarize_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| A URL to a document to summarize. | 
 **engine** | **str**| Different summarization engines are provided that will give you choices over the \&quot;flavor\&quot; of the summarization text. | [optional] [default to cecil]
 **summary_type** | **str**| Different summary types are provided that control the structure of the summary output. | [optional] [default to summary]
 **target_language** | **str**| The summarizer can translate the output into a desired language, using the table of supported language codes below.  If no language is specified, the document&#39;s original language is allowed to influence the summarizer&#39;s output. Specifying a language will add an explicit translation step, to translate the summary to the desired language.  For example, if a document is mostly written in Spanish, the summary output may itself be in Spanish or contain Spanish passages. Specifying \&quot;EN\&quot; will ensure all passages are translated as English.  | [optional] 
 **cache** | **bool**| Whether to allow cached requests &amp; responses. | [optional] [default to True]

### Return type

[**Summary**](Summary.md)

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

