# VideoList

Video Object list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[Video]**](Video.md) |  | [optional] 

## Example

```python
from Api42Vb.models.video_list import VideoList

# TODO update the JSON string below
json = "{}"
# create an instance of VideoList from a JSON string
video_list_instance = VideoList.from_json(json)
# print the JSON string representation of the object
print VideoList.to_json()

# convert the object into a dict
video_list_dict = video_list_instance.to_dict()
# create an instance of VideoList from a dict
video_list_form_dict = video_list.from_dict(video_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


