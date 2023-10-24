# VideoAttachmentList

Video Attachment Object list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[VideoAttachment]**](VideoAttachment.md) |  | [optional] 

## Example

```python
from Api42Vb.models.video_attachment_list import VideoAttachmentList

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAttachmentList from a JSON string
video_attachment_list_instance = VideoAttachmentList.from_json(json)
# print the JSON string representation of the object
print VideoAttachmentList.to_json()

# convert the object into a dict
video_attachment_list_dict = video_attachment_list_instance.to_dict()
# create an instance of VideoAttachmentList from a dict
video_attachment_list_form_dict = video_attachment_list.from_dict(video_attachment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


