# PlaylistList

Playlist Object list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[Playlist]**](Playlist.md) |  | [optional] 

## Example

```python
from Api42Vb.models.playlist_list import PlaylistList

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistList from a JSON string
playlist_list_instance = PlaylistList.from_json(json)
# print the JSON string representation of the object
print PlaylistList.to_json()

# convert the object into a dict
playlist_list_dict = playlist_list_instance.to_dict()
# create an instance of PlaylistList from a dict
playlist_list_form_dict = playlist_list.from_dict(playlist_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


