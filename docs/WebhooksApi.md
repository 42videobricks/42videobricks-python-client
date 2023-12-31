# Api42Vb.WebhooksApi

All URIs are relative to *https://api-sbx.42videobricks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook**](WebhooksApi.md#add_webhook) | **POST** /webhooks | Add a new webhook
[**delete_webhook_by_id**](WebhooksApi.md#delete_webhook_by_id) | **DELETE** /webhooks/{webhookId} | Delete a webhook
[**get_webhook_by_id**](WebhooksApi.md#get_webhook_by_id) | **GET** /webhooks/{webhookId} | Retun a single webhook
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | List webhooks
[**update_webhook_by_id**](WebhooksApi.md#update_webhook_by_id) | **PUT** /webhooks/{webhookId} | Update an existing webhook


# **add_webhook**
> Webhook add_webhook(webhook_properties)

Add a new webhook

Create a new webhook to configure notification.  Only one hook per url

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.webhook import Webhook
from Api42Vb.models.webhook_properties import WebhookProperties
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
    api_instance = Api42Vb.WebhooksApi(api_client)
    webhook_properties = Api42Vb.WebhookProperties() # WebhookProperties | 

    try:
        # Add a new webhook
        api_response = api_instance.add_webhook(webhook_properties)
        print("The response of WebhooksApi->add_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->add_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_properties** | [**WebhookProperties**](WebhookProperties.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhook Created |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_by_id**
> delete_webhook_by_id(webhook_id)

Delete a webhook

Delete a webhook.

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
    api_instance = Api42Vb.WebhooksApi(api_client)
    webhook_id = '{{webhookId}}' # str | Id of the webhook

    try:
        # Delete a webhook
        api_instance.delete_webhook_by_id(webhook_id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Id of the webhook | 

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
**204** | Webhook Deleted |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_by_id**
> Webhook get_webhook_by_id(webhook_id)

Retun a single webhook

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.webhook import Webhook
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
    api_instance = Api42Vb.WebhooksApi(api_client)
    webhook_id = '{{webhookId}}' # str | Id of the webhook

    try:
        # Retun a single webhook
        api_response = api_instance.get_webhook_by_id(webhook_id)
        print("The response of WebhooksApi->get_webhook_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Id of the webhook | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested webhook |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhookList get_webhooks(limit=limit, offset=offset)

List webhooks

Return the list of webhooks.  Return an empty list it there are no webhook to return.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.webhook_list import WebhookList
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
    api_instance = Api42Vb.WebhooksApi(api_client)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)

    try:
        # List webhooks
        api_response = api_instance.get_webhooks(limit=limit, offset=offset)
        print("The response of WebhooksApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of elements to return (default&#x3D;10) | [optional] 
 **offset** | **int**| offset for pagination | [optional] 

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of webhooks |  -  |
**400** | The request is invalid or incomplete |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_by_id**
> Webhook update_webhook_by_id(webhook_id, webhook_properties)

Update an existing webhook

Update a existing webhooks.

### Example

* Api Key Authentication (api_key):
```python
import time
import os
import Api42Vb
from Api42Vb.models.webhook import Webhook
from Api42Vb.models.webhook_properties import WebhookProperties
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
    api_instance = Api42Vb.WebhooksApi(api_client)
    webhook_id = '{{webhookId}}' # str | Id of the webhook
    webhook_properties = Api42Vb.WebhookProperties() # WebhookProperties | 

    try:
        # Update an existing webhook
        api_response = api_instance.update_webhook_by_id(webhook_id, webhook_properties)
        print("The response of WebhooksApi->update_webhook_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Id of the webhook | 
 **webhook_properties** | [**WebhookProperties**](WebhookProperties.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook Updated |  -  |
**400** | The request is invalid or incomplete |  -  |
**404** | The specified resource was not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

