# 42videobricks-python-client.VideosApi

All URIs are relative to *https://api-sbx.42videobricks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attachment_by_video_id**](VideosApi.md#add_attachment_by_video_id) | **POST** /videos/{videoId}/attachments/{attachmentType}/{locale} | Upload an attachement
[**add_thumbnail_by_video_id**](VideosApi.md#add_thumbnail_by_video_id) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail
[**add_video**](VideosApi.md#add_video) | **POST** /videos | Add a new video
[**delete_attachment_by_video_id**](VideosApi.md#delete_attachment_by_video_id) | **DELETE** /videos/{videoId}/attachments/{attachmentType}/{locale} | Delete an attachment
[**delete_thumbnail_by_video_id**](VideosApi.md#delete_thumbnail_by_video_id) | **DELETE** /videos/{videoId}/thumbnail | Delete a thumbnail
[**delete_video_by_id**](VideosApi.md#delete_video_by_id) | **DELETE** /videos/{videoId} | Delete a video
[**finalize_multipart_upload_video_by_id**](VideosApi.md#finalize_multipart_upload_video_by_id) | **POST** /videos/{videoId}/multipart-upload/finalize | Multipart upload finalization
[**finalize_upload_video_by_id**](VideosApi.md#finalize_upload_video_by_id) | **PUT** /videos/{videoId}/upload/finalize | Single file upload finalization
[**get_attachment_by_video_id**](VideosApi.md#get_attachment_by_video_id) | **GET** /videos/{videoId}/attachments/{attachmentType}/{locale} | Get the attachment
[**get_attachment_file_by_video_id**](VideosApi.md#get_attachment_file_by_video_id) | **GET** /videos/{videoId}/attachments/{attachmentType}/{locale}/file | Get attachement file
[**get_attachments_by_video_id**](VideosApi.md#get_attachments_by_video_id) | **GET** /videos/{videoId}/attachments | List of attachments
[**get_video_by_id**](VideosApi.md#get_video_by_id) | **GET** /videos/{videoId} | Retun a single video
[**get_videos**](VideosApi.md#get_videos) | **GET** /videos | List videos
[**init_multipart_upload_video_by_id**](VideosApi.md#init_multipart_upload_video_by_id) | **POST** /videos/{videoId}/multipart-upload/init | Multipart upload intialization
[**init_upload_video_by_id**](VideosApi.md#init_upload_video_by_id) | **GET** /videos/{videoId}/upload/init | Single file upload intialization
[**update_video_by_id**](VideosApi.md#update_video_by_id) | **PUT** /videos/{videoId} | Update an existing video


# **add_attachment_by_video_id**
> add_attachment_by_video_id(video_id, attachment_type, locale, file=file)

Upload an attachement

Upload an attachement file and attached it to a video Currently: - attachement file type is limited to \"subtitle\" and \"cpation\" (close caption) - supported file types: SRT (text/plain), SCC (text/plain), TTML (application/ttml), VTT (text/vtt)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    attachment_type = '{{attachmentType}}' # str | Type of attachment
    locale = '{{locale}}' # str | Le locale value of the attachment
    file = None # bytearray | The file to upload (optional)

    try:
        # Upload an attachement
        api_instance.add_attachment_by_video_id(video_id, attachment_type, locale, file=file)
    except Exception as e:
        print("Exception when calling VideosApi->add_attachment_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **attachment_type** | **str**| Type of attachment | 
 **locale** | **str**| Le locale value of the attachment | 
 **file** | **bytearray**| The file to upload | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | File Accepted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_thumbnail_by_video_id**
> add_thumbnail_by_video_id(video_id, file=file)

Upload a thumbnail

Upload an image file and set it as Thumbnail to the video

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    file = None # bytearray | The file to upload (optional)

    try:
        # Upload a thumbnail
        api_instance.add_thumbnail_by_video_id(video_id, file=file)
    except Exception as e:
        print("Exception when calling VideosApi->add_thumbnail_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **file** | **bytearray**| The file to upload | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image file accepted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video**
> Video add_video(video_properties)

Add a new video

You can create a video object by using this endpoint.  Once the video is created you can then upload the video.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video import Video
from 42videobricks-python-client.models.video_properties import VideoProperties
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_properties = 42videobricks-python-client.VideoProperties() # VideoProperties | 

    try:
        # Add a new video
        api_response = api_instance.add_video(video_properties)
        print("The response of VideosApi->add_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->add_video: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_properties** | [**VideoProperties**](VideoProperties.md)|  | 

### Return type

[**Video**](Video.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Video Created |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment_by_video_id**
> delete_attachment_by_video_id(video_id, attachment_type, locale)

Delete an attachment

Delete an attachment (and the attached file)

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    attachment_type = '{{attachmentType}}' # str | Type of attachment
    locale = '{{locale}}' # str | Le locale value of the attachment

    try:
        # Delete an attachment
        api_instance.delete_attachment_by_video_id(video_id, attachment_type, locale)
    except Exception as e:
        print("Exception when calling VideosApi->delete_attachment_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **attachment_type** | **str**| Type of attachment | 
 **locale** | **str**| Le locale value of the attachment | 

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
**204** | empty content |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_thumbnail_by_video_id**
> delete_thumbnail_by_video_id(video_id)

Delete a thumbnail

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video

    try:
        # Delete a thumbnail
        api_instance.delete_thumbnail_by_video_id(video_id)
    except Exception as e:
        print("Exception when calling VideosApi->delete_thumbnail_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 

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
**204** | Thumbnail deleted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_by_id**
> delete_video_by_id(video_id)

Delete a video

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video

    try:
        # Delete a video
        api_instance.delete_video_by_id(video_id)
    except Exception as e:
        print("Exception when calling VideosApi->delete_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 

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
**204** | Video Deleted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_multipart_upload_video_by_id**
> finalize_multipart_upload_video_by_id(video_id, video_multipart_upload_finalize=video_multipart_upload_finalize)

Multipart upload finalization

Once video parts are uploaded, finalize the upload by requesting to transcode the file.  New video file is replacing previous video file.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video_multipart_upload_finalize import VideoMultipartUploadFinalize
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    video_multipart_upload_finalize = 42videobricks-python-client.VideoMultipartUploadFinalize() # VideoMultipartUploadFinalize |  (optional)

    try:
        # Multipart upload finalization
        api_instance.finalize_multipart_upload_video_by_id(video_id, video_multipart_upload_finalize=video_multipart_upload_finalize)
    except Exception as e:
        print("Exception when calling VideosApi->finalize_multipart_upload_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **video_multipart_upload_finalize** | [**VideoMultipartUploadFinalize**](VideoMultipartUploadFinalize.md)|  | [optional] 

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
**202** | Upload Accepted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_upload_video_by_id**
> finalize_upload_video_by_id(video_id)

Single file upload finalization

Once video file is uploaded, finalize the upload by requesting to transcode the file. Finalize apply to the last signedurl provided by the upload initialization.  New video file is replacing previous video file.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video

    try:
        # Single file upload finalization
        api_instance.finalize_upload_video_by_id(video_id)
    except Exception as e:
        print("Exception when calling VideosApi->finalize_upload_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 

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
**202** | Upload Accepted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_by_video_id**
> get_attachment_by_video_id(video_id, attachment_type, locale)

Get the attachment

Get a video attachement object

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    attachment_type = '{{attachmentType}}' # str | Type of attachment
    locale = '{{locale}}' # str | Le locale value of the attachment

    try:
        # Get the attachment
        api_instance.get_attachment_by_video_id(video_id, attachment_type, locale)
    except Exception as e:
        print("Exception when calling VideosApi->get_attachment_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **attachment_type** | **str**| Type of attachment | 
 **locale** | **str**| Le locale value of the attachment | 

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
**200** | video attachement object |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_file_by_video_id**
> get_attachment_file_by_video_id(video_id, attachment_type, locale)

Get attachement file

Get the attachement file Currently only text/plain files are handled.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    attachment_type = '{{attachmentType}}' # str | Type of attachment
    locale = '{{locale}}' # str | Le locale value of the attachment

    try:
        # Get attachement file
        api_instance.get_attachment_file_by_video_id(video_id, attachment_type, locale)
    except Exception as e:
        print("Exception when calling VideosApi->get_attachment_file_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **attachment_type** | **str**| Type of attachment | 
 **locale** | **str**| Le locale value of the attachment | 

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
**200** | Attachement file |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_by_video_id**
> VideoAttachmentList get_attachments_by_video_id(video_id, attachment_type=attachment_type, locale=locale, limit=limit, offset=offset)

List of attachments

Return a list of attachments to a videos

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video_attachment_list import VideoAttachmentList
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    attachment_type = 'attachment_type_example' # str | The type of attachments (optional)
    locale = 'locale_example' # str | The locale (optional)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)

    try:
        # List of attachments
        api_response = api_instance.get_attachments_by_video_id(video_id, attachment_type=attachment_type, locale=locale, limit=limit, offset=offset)
        print("The response of VideosApi->get_attachments_by_video_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_attachments_by_video_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **attachment_type** | **str**| The type of attachments | [optional] 
 **locale** | **str**| The locale | [optional] 
 **limit** | **int**| Number of elements to return (default&#x3D;10) | [optional] 
 **offset** | **int**| offset for pagination | [optional] 

### Return type

[**VideoAttachmentList**](VideoAttachmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of attachments |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_by_id**
> Video get_video_by_id(video_id, token=token)

Retun a single video

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video import Video
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    token = true # bool | add a token to assets to alloaw access to private video (optional)

    try:
        # Retun a single video
        api_response = api_instance.get_video_by_id(video_id, token=token)
        print("The response of VideosApi->get_video_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **token** | **bool**| add a token to assets to alloaw access to private video | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested Video |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos**
> VideoList get_videos(limit=limit, offset=offset, search=search, sort=sort)

List videos

Return the list of videos.  Optionnal: Title is used to filter video: only video containing  this string ware returned.  Return an empty list it there is no video to return.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video_list import VideoList
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)
    search = '{{search}}' # str | Keywords search in all indexed fields (optional)
    sort = 'title:desc,ctime:asc' # str | Sorting results (optional)

    try:
        # List videos
        api_response = api_instance.get_videos(limit=limit, offset=offset, search=search, sort=sort)
        print("The response of VideosApi->get_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_videos: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of elements to return (default&#x3D;10) | [optional] 
 **offset** | **int**| offset for pagination | [optional] 
 **search** | **str**| Keywords search in all indexed fields | [optional] 
 **sort** | **str**| Sorting results | [optional] 

### Return type

[**VideoList**](VideoList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Videos |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_multipart_upload_video_by_id**
> VideoMultipartUploadInitResponse init_multipart_upload_video_by_id(video_id, video_multipart_upload_init=video_multipart_upload_init)

Multipart upload intialization

Get signed urls to upload a big file split in multiparts Once the video is uploaded, do not forget to call the multipart upload finalize  New video file is replacing previous video file.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video_multipart_upload_init import VideoMultipartUploadInit
from 42videobricks-python-client.models.video_multipart_upload_init_response import VideoMultipartUploadInitResponse
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    video_multipart_upload_init = 42videobricks-python-client.VideoMultipartUploadInit() # VideoMultipartUploadInit |  (optional)

    try:
        # Multipart upload intialization
        api_response = api_instance.init_multipart_upload_video_by_id(video_id, video_multipart_upload_init=video_multipart_upload_init)
        print("The response of VideosApi->init_multipart_upload_video_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->init_multipart_upload_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **video_multipart_upload_init** | [**VideoMultipartUploadInit**](VideoMultipartUploadInit.md)|  | [optional] 

### Return type

[**VideoMultipartUploadInitResponse**](VideoMultipartUploadInitResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of signed urls to post parts of the video to upload |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_upload_video_by_id**
> VideoUploadInitResponse init_upload_video_by_id(video_id)

Single file upload intialization

Get a single signed url to upload a file Once the video is uploaded, do not forget to call the single upload finalize  File formats currently supported: avi, mov, mp4, mpeg, mpg, mxf, ts. New video file is replacing previous video file.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video_upload_init_response import VideoUploadInitResponse
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video

    try:
        # Single file upload intialization
        api_response = api_instance.init_upload_video_by_id(video_id)
        print("The response of VideosApi->init_upload_video_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->init_upload_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 

### Return type

[**VideoUploadInitResponse**](VideoUploadInitResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed url to post the video file to upload |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_by_id**
> update_video_by_id(video_id, video_properties)

Update an existing video

Update video properties  Only properties provided are updated.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import 42videobricks-python-client
from 42videobricks-python-client.models.video_properties import VideoProperties
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
    api_instance = 42videobricks-python-client.VideosApi(api_client)
    video_id = '{{videoId}}' # str | Id of the video
    video_properties = 42videobricks-python-client.VideoProperties() # VideoProperties | 

    try:
        # Update an existing video
        api_instance.update_video_by_id(video_id, video_properties)
    except Exception as e:
        print("Exception when calling VideosApi->update_video_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of the video | 
 **video_properties** | [**VideoProperties**](VideoProperties.md)|  | 

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

