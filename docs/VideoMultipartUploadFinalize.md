# VideoMultipartUploadFinalize

Video Multipart upload finalization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | file id | 
**file_key** | **str** | file key | 
**parts** | [**List[VideoMultipartUploadFinalizePartsInner]**](VideoMultipartUploadFinalizePartsInner.md) |  | 

## Example

```python
from openapi_client.models.video_multipart_upload_finalize import VideoMultipartUploadFinalize

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMultipartUploadFinalize from a JSON string
video_multipart_upload_finalize_instance = VideoMultipartUploadFinalize.from_json(json)
# print the JSON string representation of the object
print VideoMultipartUploadFinalize.to_json()

# convert the object into a dict
video_multipart_upload_finalize_dict = video_multipart_upload_finalize_instance.to_dict()
# create an instance of VideoMultipartUploadFinalize from a dict
video_multipart_upload_finalize_form_dict = video_multipart_upload_finalize.from_dict(video_multipart_upload_finalize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


