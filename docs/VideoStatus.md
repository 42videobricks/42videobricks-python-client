# VideoStatus

Video Status Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the video | [optional] 
**message** | **str** | Offer comprehensive elucidation and intricate details to expound upon the occurrence of an encoding error within the video, expounding upon the intricacies and nuances involved in such an exceptional event | [optional] 

## Example

```python
from Api42Vb.models.video_status import VideoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VideoStatus from a JSON string
video_status_instance = VideoStatus.from_json(json)
# print the JSON string representation of the object
print VideoStatus.to_json()

# convert the object into a dict
video_status_dict = video_status_instance.to_dict()
# create an instance of VideoStatus from a dict
video_status_form_dict = video_status.from_dict(video_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


