# Video

Video Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the video | [optional] 
**description** | **str** | description of the video | [optional] 
**public** | **bool** | Define if the video is public (it can be accessible by anybody with the video url). Default &#x3D; tue | [optional] 
**tags** | **List[str]** | tags list linked to video | [optional] 
**id** | **str** | id of the video (null when adding a new video) | 
**status** | **str** | Status of the video : * &#39;REQUESTED&#39;: video as been submited, waiting for its creation * &#39;CREATED&#39;: video has been created and file can be uploaded          * &#39;TRANSCODING&#39;: video is unvailable because still in the creation  &amp; in encoding process * &#39;TRANSCODING_ERROR&#39;: video is unvailable because the encoding failed  * &#39;AVAILABLE&#39;: video is ready to be stream | [optional] 
**duration** | **int** | video duration in second | [optional] 
**ctime** | **int** | Creation date (timestamp) | [optional] 
**mtime** | **int** | Modification date (timestamp) | [optional] 
**assets** | [**VideoAssets**](VideoAssets.md) |  | [optional] 
**metas** | **Dict[str, object]** | metas data  free-form object: refere to the documentation | [optional] 

## Example

```python
from Api42Vb.models.video import Video

# TODO update the JSON string below
json = "{}"
# create an instance of Video from a JSON string
video_instance = Video.from_json(json)
# print the JSON string representation of the object
print Video.to_json()

# convert the object into a dict
video_dict = video_instance.to_dict()
# create an instance of Video from a dict
video_form_dict = video.from_dict(video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


