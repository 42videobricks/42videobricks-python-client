# Api42Vb.PlaylistsApi

All URIs are relative to *https://api-sbx.42videobricks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_playlist**](PlaylistsApi.md#add_playlist) | **POST** /playlists | Add a new playlist
[**delete_playlist_by_id**](PlaylistsApi.md#delete_playlist_by_id) | **DELETE** /playlists/{playlistId} | Delete a playlist
[**get_playlist_by_id**](PlaylistsApi.md#get_playlist_by_id) | **GET** /playlists/{playlistId} | Retun a single playlist
[**get_playlists**](PlaylistsApi.md#get_playlists) | **GET** /playlists | List playlists
[**update_playlist_by_id**](PlaylistsApi.md#update_playlist_by_id) | **PUT** /playlists/{playlistId} | Update an existing playlist


# **add_playlist**
> Playlist add_playlist(playlist_properties)

Add a new playlist

Create a new playlist.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.playlist import Playlist
from Api42Vb.models.playlist_properties import PlaylistProperties
from Api42Vb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sbx.42videobricks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Api42Vb.Configuration(
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
with Api42Vb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Api42Vb.PlaylistsApi(api_client)
    playlist_properties = Api42Vb.PlaylistProperties() # PlaylistProperties | 

    try:
        # Add a new playlist
        api_response = api_instance.add_playlist(playlist_properties)
        print("The response of PlaylistsApi->add_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->add_playlist: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_properties** | [**PlaylistProperties**](PlaylistProperties.md)|  | 

### Return type

[**Playlist**](Playlist.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Playlist Created |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_playlist_by_id**
> delete_playlist_by_id(playlist_id)

Delete a playlist

Delete a playlist.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sbx.42videobricks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Api42Vb.Configuration(
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
with Api42Vb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Api42Vb.PlaylistsApi(api_client)
    playlist_id = '{{playlistId}}' # str | Id of the playlist

    try:
        # Delete a playlist
        api_instance.delete_playlist_by_id(playlist_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->delete_playlist_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| Id of the playlist | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Playlist Deleted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_by_id**
> Playlist get_playlist_by_id(playlist_id)

Retun a single playlist

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.playlist import Playlist
from Api42Vb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sbx.42videobricks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Api42Vb.Configuration(
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
with Api42Vb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Api42Vb.PlaylistsApi(api_client)
    playlist_id = '{{playlistId}}' # str | Id of the playlist

    try:
        # Retun a single playlist
        api_response = api_instance.get_playlist_by_id(playlist_id)
        print("The response of PlaylistsApi->get_playlist_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| Id of the playlist | 

### Return type

[**Playlist**](Playlist.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested playlist |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlists**
> PlaylistList get_playlists(limit=limit, offset=offset, search=search, sort=sort)

List playlists

Return the list of playlist.  Return an empty list it there is no playlist to return.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.playlist_list import PlaylistList
from Api42Vb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sbx.42videobricks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Api42Vb.Configuration(
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
with Api42Vb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Api42Vb.PlaylistsApi(api_client)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)
    search = '{{search}}' # str | Keywords search in all indexed fields (optional)
    sort = 'ctime:asc' # str | Sorting results (optional)

    try:
        # List playlists
        api_response = api_instance.get_playlists(limit=limit, offset=offset, search=search, sort=sort)
        print("The response of PlaylistsApi->get_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlists: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of elements to return (default&#x3D;10) | [optional] 
 **offset** | **int**| offset for pagination | [optional] 
 **search** | **str**| Keywords search in all indexed fields | [optional] 
 **sort** | **str**| Sorting results | [optional] 

### Return type

[**PlaylistList**](PlaylistList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of playlists |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_playlist_by_id**
> update_playlist_by_id(playlist_id, playlist_properties)

Update an existing playlist

Update a existing playlist.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.playlist_properties import PlaylistProperties
from Api42Vb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sbx.42videobricks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = Api42Vb.Configuration(
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
with Api42Vb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Api42Vb.PlaylistsApi(api_client)
    playlist_id = '{{playlistId}}' # str | Id of the playlist
    playlist_properties = Api42Vb.PlaylistProperties() # PlaylistProperties | 

    try:
        # Update an existing playlist
        api_instance.update_playlist_by_id(playlist_id, playlist_properties)
    except Exception as e:
        print("Exception when calling PlaylistsApi->update_playlist_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| Id of the playlist | 
 **playlist_properties** | [**PlaylistProperties**](PlaylistProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Video update accepted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

