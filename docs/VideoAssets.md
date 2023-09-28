# VideoAssets

Video Assets Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbnail** | **str** | Url of the video thumbnail (cann be empty ?) | [optional] 
**player** | **str** | Url to the video player code | [optional] 
**stream** | **str** | Url to the video player stream | [optional] 
**iframe** | **str** | html code to integrate the player in an iframe | [optional] 

## Example

```python
from openapi_client.models.video_assets import VideoAssets

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAssets from a JSON string
video_assets_instance = VideoAssets.from_json(json)
# print the JSON string representation of the object
print VideoAssets.to_json()

# convert the object into a dict
video_assets_dict = video_assets_instance.to_dict()
# create an instance of VideoAssets from a dict
video_assets_form_dict = video_assets.from_dict(video_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


