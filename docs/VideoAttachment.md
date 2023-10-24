# VideoAttachment

Video Attachment Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **str** | id of the video | 
**attachment_type** | **str** | Attachment type | [optional] [default to 'caption']
**name** | **str** | the name of file | [optional] 
**url** | **str** | the path of the content | [optional] 
**locale** | **str** | the local of attachment | [optional] 

## Example

```python
from Api42Vb.models.video_attachment import VideoAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAttachment from a JSON string
video_attachment_instance = VideoAttachment.from_json(json)
# print the JSON string representation of the object
print VideoAttachment.to_json()

# convert the object into a dict
video_attachment_dict = video_attachment_instance.to_dict()
# create an instance of VideoAttachment from a dict
video_attachment_form_dict = video_attachment.from_dict(video_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


