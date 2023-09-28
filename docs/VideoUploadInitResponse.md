# VideoUploadInitResponse

Video Single Upload Init response object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_url** | **str** | signed url | [optional] 

## Example

```python
from openapi_client.models.video_upload_init_response import VideoUploadInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VideoUploadInitResponse from a JSON string
video_upload_init_response_instance = VideoUploadInitResponse.from_json(json)
# print the JSON string representation of the object
print VideoUploadInitResponse.to_json()

# convert the object into a dict
video_upload_init_response_dict = video_upload_init_response_instance.to_dict()
# create an instance of VideoUploadInitResponse from a dict
video_upload_init_response_form_dict = video_upload_init_response.from_dict(video_upload_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


