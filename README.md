# 42videobricks-python-client
42videobricks is a Video Platform As A Service (VPaaS)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import 42videobricks-python-client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import 42videobricks-python-client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = 42videobricks-python-client.DataApi(api_client)
    limit = 56 # int | Number of elements to return (default=10) (optional)
    offset = 56 # int | offset for pagination (optional)

    try:
        # List Video Usage KPIs
        api_response = api_instance.get_data_video_usage(limit=limit, offset=offset)
        print("The response of DataApi->get_data_video_usage:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataApi->get_data_video_usage: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-sbx.42videobricks.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataApi* | [**get_data_video_usage**](docs/DataApi.md#get_data_video_usage) | **GET** /data/videos/usage | List Video Usage KPIs
*VideosApi* | [**add_attachment_by_video_id**](docs/VideosApi.md#add_attachment_by_video_id) | **POST** /videos/{videoId}/attachments/{attachmentType}/{locale} | Upload an attachement
*VideosApi* | [**add_thumbnail_by_video_id**](docs/VideosApi.md#add_thumbnail_by_video_id) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail
*VideosApi* | [**add_video**](docs/VideosApi.md#add_video) | **POST** /videos | Add a new video
*VideosApi* | [**delete_attachment_by_video_id**](docs/VideosApi.md#delete_attachment_by_video_id) | **DELETE** /videos/{videoId}/attachments/{attachmentType}/{locale} | Delete an attachment
*VideosApi* | [**delete_thumbnail_by_video_id**](docs/VideosApi.md#delete_thumbnail_by_video_id) | **DELETE** /videos/{videoId}/thumbnail | Delete a thumbnail
*VideosApi* | [**delete_video_by_id**](docs/VideosApi.md#delete_video_by_id) | **DELETE** /videos/{videoId} | Delete a video
*VideosApi* | [**finalize_multipart_upload_video_by_id**](docs/VideosApi.md#finalize_multipart_upload_video_by_id) | **POST** /videos/{videoId}/multipart-upload/finalize | Multipart upload finalization
*VideosApi* | [**finalize_upload_video_by_id**](docs/VideosApi.md#finalize_upload_video_by_id) | **PUT** /videos/{videoId}/upload/finalize | Single file upload finalization
*VideosApi* | [**get_attachment_by_video_id**](docs/VideosApi.md#get_attachment_by_video_id) | **GET** /videos/{videoId}/attachments/{attachmentType}/{locale} | Get the attachment
*VideosApi* | [**get_attachment_file_by_video_id**](docs/VideosApi.md#get_attachment_file_by_video_id) | **GET** /videos/{videoId}/attachments/{attachmentType}/{locale}/file | Get attachement file
*VideosApi* | [**get_attachments_by_video_id**](docs/VideosApi.md#get_attachments_by_video_id) | **GET** /videos/{videoId}/attachments | List of attachments
*VideosApi* | [**get_video_by_id**](docs/VideosApi.md#get_video_by_id) | **GET** /videos/{videoId} | Retun a single video
*VideosApi* | [**get_videos**](docs/VideosApi.md#get_videos) | **GET** /videos | List videos
*VideosApi* | [**init_multipart_upload_video_by_id**](docs/VideosApi.md#init_multipart_upload_video_by_id) | **POST** /videos/{videoId}/multipart-upload/init | Multipart upload intialization
*VideosApi* | [**init_upload_video_by_id**](docs/VideosApi.md#init_upload_video_by_id) | **GET** /videos/{videoId}/upload/init | Single file upload intialization
*VideosApi* | [**update_video_by_id**](docs/VideosApi.md#update_video_by_id) | **PUT** /videos/{videoId} | Update an existing video
*WebhooksApi* | [**delete_webhook_by_id**](docs/WebhooksApi.md#delete_webhook_by_id) | **DELETE** /webhooks/{webhookId} | Delete a webhook
*WebhooksApi* | [**get_webhook_by_id**](docs/WebhooksApi.md#get_webhook_by_id) | **GET** /webhooks/{webhookId} | Retun a single webhook
*WebhooksApi* | [**update_webhook_by_id**](docs/WebhooksApi.md#update_webhook_by_id) | **PUT** /webhooks/{webhookId} | Update an existing webhook
*WebhooksApi* | [**webhooks_get**](docs/WebhooksApi.md#webhooks_get) | **GET** /webhooks | List webhooks
*WebhooksApi* | [**webhooks_post**](docs/WebhooksApi.md#webhooks_post) | **POST** /webhooks | Add a new webhook


## Documentation For Models

 - [DataVideoUsage](docs/DataVideoUsage.md)
 - [DataVideoUsageList](docs/DataVideoUsageList.md)
 - [Error](docs/Error.md)
 - [Pagination](docs/Pagination.md)
 - [Video](docs/Video.md)
 - [VideoAssets](docs/VideoAssets.md)
 - [VideoAttachment](docs/VideoAttachment.md)
 - [VideoAttachmentList](docs/VideoAttachmentList.md)
 - [VideoList](docs/VideoList.md)
 - [VideoMultipartUploadFinalize](docs/VideoMultipartUploadFinalize.md)
 - [VideoMultipartUploadFinalizePartsInner](docs/VideoMultipartUploadFinalizePartsInner.md)
 - [VideoMultipartUploadInit](docs/VideoMultipartUploadInit.md)
 - [VideoMultipartUploadInitResponse](docs/VideoMultipartUploadInitResponse.md)
 - [VideoMultipartUploadInitResponsePartsInner](docs/VideoMultipartUploadInitResponsePartsInner.md)
 - [VideoProperties](docs/VideoProperties.md)
 - [VideoUploadInitResponse](docs/VideoUploadInitResponse.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookList](docs/WebhookList.md)
 - [WebhookProperties](docs/WebhookProperties.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author



