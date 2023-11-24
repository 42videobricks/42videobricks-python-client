# Playlist

Playlist Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the playlist (null when adding a new video) | 
**name** | **str** | name of the playlist | [optional] 
**description** | **str** | description of the playlist | [optional] 
**children** | [**List[Video]**](Video.md) | ordered list of video in the playlist | [optional] 
**ctime** | **int** | Creation date (timestamp) | [optional] 
**mtime** | **int** | Modification date (timestamp) | [optional] 

## Example

```python
from Api42Vb.models.playlist import Playlist

# TODO update the JSON string below
json = "{}"
# create an instance of Playlist from a JSON string
playlist_instance = Playlist.from_json(json)
# print the JSON string representation of the object
print Playlist.to_json()

# convert the object into a dict
playlist_dict = playlist_instance.to_dict()
# create an instance of Playlist from a dict
playlist_form_dict = playlist.from_dict(playlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


