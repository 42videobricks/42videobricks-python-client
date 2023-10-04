# 42videobricks-python-client.TagsApi

All URIs are relative to *https://api-sbx.42videobricks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | List Video Tags


# **get_tags**
> TagList get_tags(limit=limit, offset=offset, partial=partial)

List Video Tags

Return the list of tags created and set to videos

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.tag_list import TagList
from 42videobricks-python-client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sbx.42videobricks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = 42videobricks-python-client.Configuration(
    host = "https://api-sbx.42videobricks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with 42videobricks-python-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = 42videobricks-python-client.TagsApi(api_client)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)
    partial = '{{partial}}' # str | \\'partial\\' string to filter list (optional)

    try:
        # List Video Tags
        api_response = api_instance.get_tags(limit=limit, offset=offset, partial=partial)
        print("The response of TagsApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of elements to return (default&#x3D;10) | [optional] 
 **offset** | **int**| offset for pagination | [optional] 
 **partial** | **str**| \\&#39;partial\\&#39; string to filter list | [optional] 

### Return type

[**TagList**](TagList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of video tags |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

