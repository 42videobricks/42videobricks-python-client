# VideoProperties

Video Properties Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the video | [optional] 
**description** | **str** | description of the video | [optional] 
**public** | **bool** | Define if the video is public (it can be accessible by anybody with the video url). Default &#x3D; tue | [optional] 
**tags** | **List[str]** | tags list linked to video | [optional] 

## Example

```python
from openapi_client.models.video_properties import VideoProperties

# TODO update the JSON string below
json = "{}"
# create an instance of VideoProperties from a JSON string
video_properties_instance = VideoProperties.from_json(json)
# print the JSON string representation of the object
print VideoProperties.to_json()

# convert the object into a dict
video_properties_dict = video_properties_instance.to_dict()
# create an instance of VideoProperties from a dict
video_properties_form_dict = video_properties.from_dict(video_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


