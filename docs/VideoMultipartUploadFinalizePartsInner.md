# VideoMultipartUploadFinalizePartsInner

part signed url object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **int** | part number | [optional] 
**e_tag** | **str** | part Etag | [optional] 

## Example

```python
from 42videobricks-python-client.models.video_multipart_upload_finalize_parts_inner import VideoMultipartUploadFinalizePartsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMultipartUploadFinalizePartsInner from a JSON string
video_multipart_upload_finalize_parts_inner_instance = VideoMultipartUploadFinalizePartsInner.from_json(json)
# print the JSON string representation of the object
print VideoMultipartUploadFinalizePartsInner.to_json()

# convert the object into a dict
video_multipart_upload_finalize_parts_inner_dict = video_multipart_upload_finalize_parts_inner_instance.to_dict()
# create an instance of VideoMultipartUploadFinalizePartsInner from a dict
video_multipart_upload_finalize_parts_inner_form_dict = video_multipart_upload_finalize_parts_inner.from_dict(video_multipart_upload_finalize_parts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


