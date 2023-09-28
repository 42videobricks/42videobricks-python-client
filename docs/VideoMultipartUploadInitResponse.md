# VideoMultipartUploadInitResponse

Video Mutlipart Upload Init response object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_size** | **int** | part chunk size | [optional] 
**file_id** | **str** | file id | [optional] 
**file_key** | **str** | file key | [optional] 
**parts** | [**List[VideoMultipartUploadInitResponsePartsInner]**](VideoMultipartUploadInitResponsePartsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.video_multipart_upload_init_response import VideoMultipartUploadInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMultipartUploadInitResponse from a JSON string
video_multipart_upload_init_response_instance = VideoMultipartUploadInitResponse.from_json(json)
# print the JSON string representation of the object
print VideoMultipartUploadInitResponse.to_json()

# convert the object into a dict
video_multipart_upload_init_response_dict = video_multipart_upload_init_response_instance.to_dict()
# create an instance of VideoMultipartUploadInitResponse from a dict
video_multipart_upload_init_response_form_dict = video_multipart_upload_init_response.from_dict(video_multipart_upload_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


