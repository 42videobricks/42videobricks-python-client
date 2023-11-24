# PlaylistProperties

Video Properties Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the playlist | [optional] 
**description** | **str** | description of the playlist | [optional] 
**children** | **List[str]** | ordered list of video Id in the playlist | [optional] 

## Example

```python
from Api42Vb.models.playlist_properties import PlaylistProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistProperties from a JSON string
playlist_properties_instance = PlaylistProperties.from_json(json)
# print the JSON string representation of the object
print PlaylistProperties.to_json()

# convert the object into a dict
playlist_properties_dict = playlist_properties_instance.to_dict()
# create an instance of PlaylistProperties from a dict
playlist_properties_form_dict = playlist_properties.from_dict(playlist_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


