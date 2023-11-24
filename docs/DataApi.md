# Api42Vb.DataApi

All URIs are relative to *https://api-sbx.42videobricks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_video_usage**](DataApi.md#get_data_video_usage) | **GET** /data/videos/usage | List Video Usage KPIs


# **get_data_video_usage**
> DataVideoUsageList get_data_video_usage(limit=limit, offset=offset, interval=interval, start_date=start_date, end_date=end_date)

List Video Usage KPIs

Return the usage of the platform ressources.  By default, it returns monthly usage but unit (dayly|week|month) can be defined. For current period, usage is calculated until current time. Start and end dates can be also optionaly defined to filter results.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.data_video_usage_list import DataVideoUsageList
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
    api_instance = Api42Vb.DataApi(api_client)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)
    interval = '{{interval}}' # str | Period unit (day|week|month) (optional)
    start_date = '{{starDate}}' # str | Start date for the period (optional)
    end_date = '{{endDate}}' # str | End date for the period (optional)

    try:
        # List Video Usage KPIs
        api_response = api_instance.get_data_video_usage(limit=limit, offset=offset, interval=interval, start_date=start_date, end_date=end_date)
        print("The response of DataApi->get_data_video_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->get_data_video_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of elements to return (default&#x3D;10) | [optional] 
 **offset** | **int**| offset for pagination | [optional] 
 **interval** | **str**| Period unit (day|week|month) | [optional] 
 **start_date** | **str**| Start date for the period | [optional] 
 **end_date** | **str**| End date for the period | [optional] 

### Return type

[**DataVideoUsageList**](DataVideoUsageList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monthly usage KPIs |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

