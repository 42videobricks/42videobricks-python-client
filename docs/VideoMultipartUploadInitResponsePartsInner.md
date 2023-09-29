# VideoMultipartUploadInitResponsePartsInner

part signed url object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_url** | **str** | part signed url | [optional] 
**part_number** | **int** | part number | [optional] 

## Example

```python
from 42videobricks-python-client.models.video_multipart_upload_init_response_parts_inner import VideoMultipartUploadInitResponsePartsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VideoMultipartUploadInitResponsePartsInner from a JSON string
video_multipart_upload_init_response_parts_inner_instance = VideoMultipartUploadInitResponsePartsInner.from_json(json)
# print the JSON string representation of the object
print VideoMultipartUploadInitResponsePartsInner.to_json()

# convert the object into a dict
video_multipart_upload_init_response_parts_inner_dict = video_multipart_upload_init_response_parts_inner_instance.to_dict()
# create an instance of VideoMultipartUploadInitResponsePartsInner from a dict
video_multipart_upload_init_response_parts_inner_form_dict = video_multipart_upload_init_response_parts_inner.from_dict(video_multipart_upload_init_response_parts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


