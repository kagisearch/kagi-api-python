# openapi_client.TranslateApi

All URIs are relative to *https://kagi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate**](TranslateApi.md#translate) | **POST** /api/translate | Text Translation
[**translate_alternatives**](TranslateApi.md#translate_alternatives) | **POST** /alternative-translations | Alternative Translations
[**translate_detect**](TranslateApi.md#translate_detect) | **POST** /api/detect | Language Detection
[**translate_dictionary**](TranslateApi.md#translate_dictionary) | **POST** /api/dictionary | Dictionary
[**translate_list_languages**](TranslateApi.md#translate_list_languages) | **GET** /api/list-languages | List Supported Languages
[**translate_romanize**](TranslateApi.md#translate_romanize) | **GET** /api/romanize | Text Romanization
[**translate_word_insights**](TranslateApi.md#translate_word_insights) | **POST** /api/word-insights | Word Insights


# **translate**
> Translate200Response translate(translate_request)

Text Translation

Translates text between languages with customizable options for gender, formality, and style. Supports both single text translation and efficient batch translation of multiple text snippets with context awareness.

### Example

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate200_response import Translate200Response
from openapi_client.models.translate_request import TranslateRequest
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

# Configure Bearer authorization: kagi-translate
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TranslateApi(api_client)
    translate_request = {"text":"Hello world","source_lang":"en","target_lang":"es"} # TranslateRequest | 

    try:
        # Text Translation
        api_response = api_instance.translate(translate_request)
        print("The response of TranslateApi->translate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_request** | [**TranslateRequest**](TranslateRequest.md)|  | 

### Return type

[**Translate200Response**](Translate200Response.md)

### Authorization

[kagi-translate](../README.md#kagi-translate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful translation |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_alternatives**
> TranslateAlternatives200Response translate_alternatives(original_text, existing_translation, target_lang, source_lang=source_lang, target_explanation_language=target_explanation_language, translation_options=translation_options, partial_translation=partial_translation)

Alternative Translations

Provides alternative translation options for a given text with explanations. Supports two modes: standard mode (alternatives for a full translation) and partial mode (alternative ways to phrase a specific part of a translation).

### Example

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate_alternatives200_response import TranslateAlternatives200Response
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

# Configure Bearer authorization: kagi-translate
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

[kagi-translate](../README.md#kagi-translate)

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
> TranslateDetect200Response translate_detect(translate_detect_request)

Language Detection

Detects the language of the provided text.

### Example

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate_detect200_response import TranslateDetect200Response
from openapi_client.models.translate_detect_request import TranslateDetectRequest
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

# Configure Bearer authorization: kagi-translate
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

[**TranslateDetect200Response**](TranslateDetect200Response.md)

### Authorization

[kagi-translate](../README.md#kagi-translate)

### HTTP request headers

 - **Content-Type**: application/json
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

**Translation behavior:**
- Fields translated to `definition_language`: definition, notes, etymology, part_of_speech, usage_level, dialect
- Fields that remain in `word_language`: word, synonyms, pronunciation, plural, related_words, examples (with translations in parentheses when languages differ)
- Fields always in English (strict enums): gender ("masculine", "feminine", "neuter", "common"), temporal_trend ("increasing", "stable", "decreasing")


### Example

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate_dictionary200_response import TranslateDictionary200Response
from openapi_client.models.translate_dictionary_request import TranslateDictionaryRequest
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

# Configure Bearer authorization: kagi-translate
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

[kagi-translate](../README.md#kagi-translate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful dictionary lookup |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_list_languages**
> List[TranslateListLanguages200ResponseInner] translate_list_languages(type=type, locale=locale)

List Supported Languages

Returns a list of languages supported by the translation API.

The response includes language codes, names, and whether each language supports formality settings.


### Example

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate_list_languages200_response_inner import TranslateListLanguages200ResponseInner
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

# Configure Bearer authorization: kagi-translate
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

[kagi-translate](../README.md#kagi-translate)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of supported languages |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_romanize**
> TranslateRomanize200Response translate_romanize(text, language)

Text Romanization

Converts non-Latin script text to Latin script (romanization/transliteration). Uses standardized romanization styles for each language: Hepburn for Japanese, Pinyin for Chinese, ALA-LC for Arabic, etc.

### Example

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate_romanize200_response import TranslateRomanize200Response
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

# Configure Bearer authorization: kagi-translate
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

[kagi-translate](../README.md#kagi-translate)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful romanization |  -  |
**400** | Bad request |  -  |

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

* Bearer Authentication (kagi-translate):

```python
import openapi_client
from openapi_client.models.translate_word_insights200_response import TranslateWordInsights200Response
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

# Configure Bearer authorization: kagi-translate
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

[kagi-translate](../README.md#kagi-translate)

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

