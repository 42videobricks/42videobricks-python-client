# VideoMultipartUploadInit

Video Mutlipart Upload Init

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | file name | 
**size** | **int** | file size (in bits) | 

## Example

```python
from Api42Vb.models.video_multipart_upload_init import VideoMultipartUploadInit

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMultipartUploadInit from a JSON string
video_multipart_upload_init_instance = VideoMultipartUploadInit.from_json(json)
# print the JSON string representation of the object
print VideoMultipartUploadInit.to_json()

# convert the object into a dict
video_multipart_upload_init_dict = video_multipart_upload_init_instance.to_dict()
# create an instance of VideoMultipartUploadInit from a dict
video_multipart_upload_init_form_dict = video_multipart_upload_init.from_dict(video_multipart_upload_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


