# openapi_client.TranslateApi

All URIs are relative to *https://kagi.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate_alternatives**](TranslateApi.md#translate_alternatives) | **POST** /alternative-translations | Alternative Translations
[**translate_detect**](TranslateApi.md#translate_detect) | **POST** /api/detect | Language Detection
[**translate_detect_get**](TranslateApi.md#translate_detect_get) | **GET** /api/detect | Language Detection API
[**translate_dictionary**](TranslateApi.md#translate_dictionary) | **POST** /api/dictionary | Dictionary
[**translate_file**](TranslateApi.md#translate_file) | **POST** /api/translate-file | File Translation
[**translate_list_languages**](TranslateApi.md#translate_list_languages) | **GET** /api/list-languages | List Supported Languages
[**translate_list_languages_post**](TranslateApi.md#translate_list_languages_post) | **POST** /api/list-languages | List Supported Languages API (POST method)
[**translate_proof_read**](TranslateApi.md#translate_proof_read) | **POST** /api/proofread | Text Proofreading
[**translate_proof_read_get**](TranslateApi.md#translate_proof_read_get) | **GET** /api/proofread | Text Proofreading API
[**translate_romanize**](TranslateApi.md#translate_romanize) | **GET** /api/romanize | Text Romanization
[**translate_speech**](TranslateApi.md#translate_speech) | **GET** /api/speech | Text-to-Speech
[**translate_text_alignments**](TranslateApi.md#translate_text_alignments) | **POST** /api/text-alignments | Text Alignments
[**translate_transacribe**](TranslateApi.md#translate_transacribe) | **POST** /api/transcribe | Audio Transcription
[**translate_word_insights**](TranslateApi.md#translate_word_insights) | **POST** /api/word-insights | Word Insights


# **translate_alternatives**
> TranslateAlternatives200Response translate_alternatives(original_text, existing_translation, target_lang, source_lang=source_lang, target_explanation_language=target_explanation_language, translation_options=translation_options, partial_translation=partial_translation)

Alternative Translations

Provides alternative translation options for a given text with explanations. Supports two modes: standard mode (alternatives for a full translation) and partial mode (alternative ways to phrase a specific part of a translation).

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_alternatives200_response import TranslateAlternatives200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    original_text = 'original_text_example' # str | Original text to translate. In partial mode, this serves as context for the phrase (may be ignored if not relevant).
    existing_translation = 'existing_translation_example' # str | In standard mode: existing full translation of the original text. In partial mode: the specific phrase you want alternative ways to express.
    target_lang = 'target_lang_example' # str | Target language code (ISO-639) for the translations
    source_lang = 'source_lang_example' # str | Source language code (ISO-639) of the original text. Helps provide more accurate alternatives by understanding language-specific nuances. (optional)
    target_explanation_language = 'en' # str | Language code (ISO-639) for the explanations (optional) (default to 'en')
    translation_options = 'translation_options_example' # str | JSON string with translation customization options: - `formality`: Controls formality level [\\\"default\\\", \\\"more\\\", \\\"less\\\"] - `speaker_gender`: Gender of the speaker [\\\"unknown\\\", \\\"feminine\\\", \\\"masculine\\\", \\\"neutral\\\"] - `addressee_gender`: Gender of the person being addressed [\\\"unknown\\\", \\\"feminine\\\", \\\"masculine\\\", \\\"neutral\\\"] - `style`: Translation style [\\\"natural\\\", \\\"literal\\\"] - `context`: Additional context to inform translation (string)  (optional)
    partial_translation = 'false' # str | Mode switch: 'false' for standard mode (full translation alternatives), 'true' for partial mode (alternative ways to phrase a specific part) (optional) (default to 'false')

    try:
        # Alternative Translations
        api_response = api_instance.translate_alternatives(original_text, existing_translation, target_lang, source_lang=source_lang, target_explanation_language=target_explanation_language, translation_options=translation_options, partial_translation=partial_translation)
        print("The response of TranslateApi->translate_alternatives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_alternatives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_text** | **str**| Original text to translate. In partial mode, this serves as context for the phrase (may be ignored if not relevant). | 
 **existing_translation** | **str**| In standard mode: existing full translation of the original text. In partial mode: the specific phrase you want alternative ways to express. | 
 **target_lang** | **str**| Target language code (ISO-639) for the translations | 
 **source_lang** | **str**| Source language code (ISO-639) of the original text. Helps provide more accurate alternatives by understanding language-specific nuances. | [optional] 
 **target_explanation_language** | **str**| Language code (ISO-639) for the explanations | [optional] [default to &#39;en&#39;]
 **translation_options** | **str**| JSON string with translation customization options: - &#x60;formality&#x60;: Controls formality level [\\\&quot;default\\\&quot;, \\\&quot;more\\\&quot;, \\\&quot;less\\\&quot;] - &#x60;speaker_gender&#x60;: Gender of the speaker [\\\&quot;unknown\\\&quot;, \\\&quot;feminine\\\&quot;, \\\&quot;masculine\\\&quot;, \\\&quot;neutral\\\&quot;] - &#x60;addressee_gender&#x60;: Gender of the person being addressed [\\\&quot;unknown\\\&quot;, \\\&quot;feminine\\\&quot;, \\\&quot;masculine\\\&quot;, \\\&quot;neutral\\\&quot;] - &#x60;style&#x60;: Translation style [\\\&quot;natural\\\&quot;, \\\&quot;literal\\\&quot;] - &#x60;context&#x60;: Additional context to inform translation (string)  | [optional] 
 **partial_translation** | **str**| Mode switch: &#39;false&#39; for standard mode (full translation alternatives), &#39;true&#39; for partial mode (alternative ways to phrase a specific part) | [optional] [default to &#39;false&#39;]

### Return type

[**TranslateAlternatives200Response**](TranslateAlternatives200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alternative translations with explanations |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_detect**
> TranslateDetectGet200Response translate_detect(translate_detect_request)

Language Detection

Detects the language of the provided text.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_detect_get200_response import TranslateDetectGet200Response
from openapi_client.models.translate_detect_request import TranslateDetectRequest
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    translate_detect_request = {"text":"Hello world"} # TranslateDetectRequest | 

    try:
        # Language Detection
        api_response = api_instance.translate_detect(translate_detect_request)
        print("The response of TranslateApi->translate_detect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_detect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_detect_request** | [**TranslateDetectRequest**](TranslateDetectRequest.md)|  | 

### Return type

[**TranslateDetectGet200Response**](TranslateDetectGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful language detection |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_detect_get**
> TranslateDetectGet200Response translate_detect_get(text)

Language Detection API

Detects the language of the provided text.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_detect_get200_response import TranslateDetectGet200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    text = 'Hello world' # str | Text to detect language from

    try:
        # Language Detection API
        api_response = api_instance.translate_detect_get(text)
        print("The response of TranslateApi->translate_detect_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_detect_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to detect language from | 

### Return type

[**TranslateDetectGet200Response**](TranslateDetectGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful language detection |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_dictionary**
> TranslateDictionary200Response translate_dictionary(translate_dictionary_request)

Dictionary

Provides dictionary definitions for words in different languages.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_dictionary200_response import TranslateDictionary200Response
from openapi_client.models.translate_dictionary_request import TranslateDictionaryRequest
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    translate_dictionary_request = {"word":"hello","word_language":"en","definition_language":"en"} # TranslateDictionaryRequest | 

    try:
        # Dictionary
        api_response = api_instance.translate_dictionary(translate_dictionary_request)
        print("The response of TranslateApi->translate_dictionary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_dictionary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_dictionary_request** | [**TranslateDictionaryRequest**](TranslateDictionaryRequest.md)|  | 

### Return type

[**TranslateDictionary200Response**](TranslateDictionary200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful dictionary lookup |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_file**
> bytearray translate_file(file, var_from=var_from, to=to, is_multi_language=is_multi_language, additional_languages=additional_languages)

File Translation

Translates documents between languages while preserving their formatting.

**Note: This endpoint will be deprecated in the future and its functionality will be moved to the main /api/translate endpoint.**


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    file = None # bytearray | The file to translate. Supported formats include: - Microsoft Word (.doc, .docx) - Text (.txt) - CSV spreadsheets (.csv) - Markdown (.md) 
    var_from = 'auto' # str | Source language code (ISO-639) or \\\"auto\\\" for automatic detection (optional) (default to 'auto')
    to = 'en' # str | Target language code (ISO-639) (optional) (default to 'en')
    is_multi_language = True # bool | If true, creates a file with multiple languages side by side (optional)
    additional_languages = ['additional_languages_example'] # List[str] | Additional target languages for multi-language translation (optional)

    try:
        # File Translation
        api_response = api_instance.translate_file(file, var_from=var_from, to=to, is_multi_language=is_multi_language, additional_languages=additional_languages)
        print("The response of TranslateApi->translate_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The file to translate. Supported formats include: - Microsoft Word (.doc, .docx) - Text (.txt) - CSV spreadsheets (.csv) - Markdown (.md)  | 
 **var_from** | **str**| Source language code (ISO-639) or \\\&quot;auto\\\&quot; for automatic detection | [optional] [default to &#39;auto&#39;]
 **to** | **str**| Target language code (ISO-639) | [optional] [default to &#39;en&#39;]
 **is_multi_language** | **bool**| If true, creates a file with multiple languages side by side | [optional] 
 **additional_languages** | [**List[str]**](str.md)| Additional target languages for multi-language translation | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful translation |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_list_languages**
> List[TranslateListLanguages200ResponseInner] translate_list_languages(type=type, locale=locale)

List Supported Languages

Returns a list of languages supported by the translation API.

The response includes language codes, names, and whether each language supports formality settings.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_list_languages200_response_inner import TranslateListLanguages200ResponseInner
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    type = 'type_example' # str | Type of languages to return ('source' or 'target') (optional)
    locale = 'locale_example' # str | Locale code to use for language names (e.g., 'en', 'de', 'fr') (optional)

    try:
        # List Supported Languages
        api_response = api_instance.translate_list_languages(type=type, locale=locale)
        print("The response of TranslateApi->translate_list_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_list_languages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of languages to return (&#39;source&#39; or &#39;target&#39;) | [optional] 
 **locale** | **str**| Locale code to use for language names (e.g., &#39;en&#39;, &#39;de&#39;, &#39;fr&#39;) | [optional] 

### Return type

[**List[TranslateListLanguages200ResponseInner]**](TranslateListLanguages200ResponseInner.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of supported languages |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_list_languages_post**
> List[Language] translate_list_languages_post(translate_list_languages_post_request=translate_list_languages_post_request)

List Supported Languages API (POST method)

Returns a list of languages supported by the translation API using POST method.

The response includes language codes, names, and whether each language supports formality settings.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.language import Language
from openapi_client.models.translate_list_languages_post_request import TranslateListLanguagesPostRequest
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    translate_list_languages_post_request = {"type":"target"} # TranslateListLanguagesPostRequest |  (optional)

    try:
        # List Supported Languages API (POST method)
        api_response = api_instance.translate_list_languages_post(translate_list_languages_post_request=translate_list_languages_post_request)
        print("The response of TranslateApi->translate_list_languages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_list_languages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_list_languages_post_request** | [**TranslateListLanguagesPostRequest**](TranslateListLanguagesPostRequest.md)|  | [optional] 

### Return type

[**List[Language]**](Language.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of supported languages |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_proof_read**
> TranslateProofReadGet200Response translate_proof_read(translate_proof_read_request)

Text Proofreading

Proofreads text to correct grammar, spelling, punctuation, and style issues. Returns the corrected text along with detailed explanations of each change, tone analysis, voice consistency, and repetition detection.

**ALPHA STATUS**: This endpoint is in alpha state and may change more frequently than other endpoints. The response format, parameters, or behavior might be modified in future releases.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_proof_read_get200_response import TranslateProofReadGet200Response
from openapi_client.models.translate_proof_read_request import TranslateProofReadRequest
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    translate_proof_read_request = openapi_client.TranslateProofReadRequest() # TranslateProofReadRequest | 

    try:
        # Text Proofreading
        api_response = api_instance.translate_proof_read(translate_proof_read_request)
        print("The response of TranslateApi->translate_proof_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_proof_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_proof_read_request** | [**TranslateProofReadRequest**](TranslateProofReadRequest.md)|  | 

### Return type

[**TranslateProofReadGet200Response**](TranslateProofReadGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful proofreading |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_proof_read_get**
> TranslateProofReadGet200Response translate_proof_read_get(text, source_lang=source_lang, explanation_language=explanation_language, stream=stream)

Text Proofreading API

Proofreads text to correct grammar, spelling, punctuation, and style issues. Returns the corrected text along with detailed explanations of each change, tone analysis, voice consistency, and repetition detection.

**ALPHA STATUS**: This endpoint is in alpha state and may change more frequently than other endpoints. The response format, parameters, or behavior might be modified in future releases.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_proof_read_get200_response import TranslateProofReadGet200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    text = 'text_example' # str | Text content to proofread
    source_lang = 'source_lang_example' # str | Source language code (ISO-639) or \"auto\" for automatic detection (optional)
    explanation_language = 'explanation_language_example' # str | Language code (ISO-639) for explanations and analysis. If not provided, explanations will be in the same language as the source text. (optional)
    stream = True # bool | Whether to stream the response as Server-Sent Events (optional)

    try:
        # Text Proofreading API
        api_response = api_instance.translate_proof_read_get(text, source_lang=source_lang, explanation_language=explanation_language, stream=stream)
        print("The response of TranslateApi->translate_proof_read_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_proof_read_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text content to proofread | 
 **source_lang** | **str**| Source language code (ISO-639) or \&quot;auto\&quot; for automatic detection | [optional] 
 **explanation_language** | **str**| Language code (ISO-639) for explanations and analysis. If not provided, explanations will be in the same language as the source text. | [optional] 
 **stream** | **bool**| Whether to stream the response as Server-Sent Events | [optional] 

### Return type

[**TranslateProofReadGet200Response**](TranslateProofReadGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful proofreading |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_romanize**
> TranslateRomanize200Response translate_romanize(text, language)

Text Romanization

Converts non-Latin script text to Latin script (romanization/transliteration). Uses standardized romanization styles for each language: Hepburn for Japanese, Pinyin for Chinese, ALA-LC for Arabic, etc.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_romanize200_response import TranslateRomanize200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    text = 'こんにちは' # str | Text to romanize
    language = 'ja' # str | Language code (ISO-639) of the source text

    try:
        # Text Romanization
        api_response = api_instance.translate_romanize(text, language)
        print("The response of TranslateApi->translate_romanize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_romanize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to romanize | 
 **language** | **str**| Language code (ISO-639) of the source text | 

### Return type

[**TranslateRomanize200Response**](TranslateRomanize200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful romanization |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_speech**
> bytearray translate_speech(text, language=language, voice=voice, raw=raw)

Text-to-Speech

Converts text to natural-sounding speech audio.

Supports multiple languages and voices, with audio delivered in WAV format at 24kHz sample rate.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    text = 'Hello, how are you today?' # str | Text to convert to speech
    language = 'en' # str | Language code (ISO-639) for speech synthesis. The API supports a wide range of languages and automatically applies appropriate voice prompts for each language. (optional)
    voice = coral # str | Voice to use for speech synthesis (optional) (default to coral)
    raw = False # bool | If true, returns the raw audio stream without WAV header processing (optional) (default to False)

    try:
        # Text-to-Speech
        api_response = api_instance.translate_speech(text, language=language, voice=voice, raw=raw)
        print("The response of TranslateApi->translate_speech:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_speech: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Text to convert to speech | 
 **language** | **str**| Language code (ISO-639) for speech synthesis. The API supports a wide range of languages and automatically applies appropriate voice prompts for each language. | [optional] 
 **voice** | **str**| Voice to use for speech synthesis | [optional] [default to coral]
 **raw** | **bool**| If true, returns the raw audio stream without WAV header processing | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/x-wav, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audio stream of synthesized speech |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_text_alignments**
> TranslateTextAlignments200Response translate_text_alignments(source_text, target_text)

Text Alignments

Returns word and phrase alignment data between source and target texts, breaking down the texts into corresponding segments.

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_text_alignments200_response import TranslateTextAlignments200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    source_text = 'source_text_example' # str | Source text to align
    target_text = 'target_text_example' # str | Target text to align with the source

    try:
        # Text Alignments
        api_response = api_instance.translate_text_alignments(source_text, target_text)
        print("The response of TranslateApi->translate_text_alignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_text_alignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_text** | **str**| Source text to align | 
 **target_text** | **str**| Target text to align with the source | 

### Return type

[**TranslateTextAlignments200Response**](TranslateTextAlignments200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Word and phrase alignment data |  -  |
**400** | Bad request |  -  |
**402** | Payment Required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_transacribe**
> TranslateTransacribe200Response translate_transacribe(body, language=language)

Audio Transcription

Converts audio speech into accurate text transcriptions. This API accepts various audio formats and
can automatically detect the spoken language or use a specified language parameter for improved accuracy.

The service processes the audio through a high-quality speech recognition model optimized for clarity and accuracy.
Audio is temporarily stored for processing, then immediately deleted after transcription is complete.


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_transacribe200_response import TranslateTransacribe200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    body = None # bytearray | 
    language = 'en' # str | Language code (ISO-639) of the audio content. Use \"auto\" for automatic language detection. Specifying the correct language can improve transcription accuracy.  (optional)

    try:
        # Audio Transcription
        api_response = api_instance.translate_transacribe(body, language=language)
        print("The response of TranslateApi->translate_transacribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_transacribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 
 **language** | **str**| Language code (ISO-639) of the audio content. Use \&quot;auto\&quot; for automatic language detection. Specifying the correct language can improve transcription accuracy.  | [optional] 

### Return type

[**TranslateTransacribe200Response**](TranslateTransacribe200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: audio/*
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful transcription |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_word_insights**
> TranslateWordInsights200Response translate_word_insights(original_text, translated_text, target_explanation_language=target_explanation_language, translation_options=translation_options)

Word Insights

Provides detailed linguistic insights and alternatives for translated text. The API identifies 3-5 key
words or phrases in the translated text that have meaningful alternative expressions, and returns:

1. A marked version of the translation with insight markers
2. Alternative expressions for each identified word/phrase
3. Brief explanations for each alternative in the target explanation language
4. Type labels categorizing each insight (e.g., "Lexical choice", "Cultural reference")


### Example

* Bearer Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.translate_word_insights200_response import TranslateWordInsights200Response
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

# Configure Bearer authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    original_text = 'original_text_example' # str | Source text that was translated
    translated_text = 'translated_text_example' # str | Translated text to analyze for linguistic insights
    target_explanation_language = 'en' # str | Language code (ISO-639) for the explanations and type labels (optional) (default to 'en')
    translation_options = 'translation_options_example' # str | Optional JSON string with translation options that provide context for the insights. Can include formality, gender preferences, and style.  (optional)

    try:
        # Word Insights
        api_response = api_instance.translate_word_insights(original_text, translated_text, target_explanation_language=target_explanation_language, translation_options=translation_options)
        print("The response of TranslateApi->translate_word_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_word_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_text** | **str**| Source text that was translated | 
 **translated_text** | **str**| Translated text to analyze for linguistic insights | 
 **target_explanation_language** | **str**| Language code (ISO-639) for the explanations and type labels | [optional] [default to &#39;en&#39;]
 **translation_options** | **str**| Optional JSON string with translation options that provide context for the insights. Can include formality, gender preferences, and style.  | [optional] 

### Return type

[**TranslateWordInsights200Response**](TranslateWordInsights200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed linguistic insights for the translated text |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

