# Search200ResponseData

Holds all the search results for the query specified. As results have different types and sources, they are spearated into different fields within this object. For example image results are stored under `data.image` while news results are stored under `data.news`. All results will have the same main structure, but additional data might be stored under the `data.{name}[].props` path. Please look at each different type of result for more information about this.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for html pages or wedbsites. | [optional] 
**image** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for images. | [optional] 
**video** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for videos. | [optional] 
**podcast** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for podcasts. | [optional] 
**podcast_creator** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for creators of podcasta. | [optional] 
**news** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for news articles. | [optional] 
**adjacent_question** | [**List[SearchResult]**](SearchResult.md) | Contains results that are obtained by searching for slightly different queries. These questions are stored under the &#x60;props.question&#x60; path. | [optional] 
**direct_answer** | [**List[SearchResult]**](SearchResult.md) | If the search query was a math equation, or unit conversions, things that can be answered quickly, the result will be in here. | [optional] 
**interesting_news** | [**List[SearchResult]**](SearchResult.md) | Contains news results from publishers collected and stored in Kagis&#39; news index. | [optional] 
**interesting_finds** | [**List[SearchResult]**](SearchResult.md) | Contains small web results from publishers collected and stored in Kagis&#39; small web index. | [optional] 
**infobox** | [**List[SearchResult]**](SearchResult.md) | Contains detailed summary and tabulated information about a person, place, or thing. | [optional] 
**code** | [**List[SearchResult]**](SearchResult.md) | Contains all search results that link to code resources or repositories. | [optional] 
**package_tracking** | [**List[SearchResult]**](SearchResult.md) | If the search query was a package tracking number, the correct package tracking website should be present in this collection. | [optional] 
**public_records** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for public records, such as government documents, or public court records. | [optional] 
**weather** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for the current weather. | [optional] 
**related_search** | [**List[SearchResult]**](SearchResult.md) | Contains a list of searches that are related to the current search, and may help narrow down the results. | [optional] 
**listicle** | [**List[SearchResult]**](SearchResult.md) | Contains all search results that are lists of things. Results with titles like \&quot;5 things you didn&#39;t know about...\&quot;, or \&quot;10 of the best headphones\&quot;. | [optional] 
**web_archive** | [**List[SearchResult]**](SearchResult.md) | Contains all search results for archived websites that may not be available anymore | [optional] 

## Example

```python
from openapi_client.models.search200_response_data import Search200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of Search200ResponseData from a JSON string
search200_response_data_instance = Search200ResponseData.from_json(json)
# print the JSON string representation of the object
print(Search200ResponseData.to_json())

# convert the object into a dict
search200_response_data_dict = search200_response_data_instance.to_dict()
# create an instance of Search200ResponseData from a dict
search200_response_data_from_dict = Search200ResponseData.from_dict(search200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


