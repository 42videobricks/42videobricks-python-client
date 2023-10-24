# TagList

Tag string list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | **List[str]** |  | [optional] 

## Example

```python
from Api42Vb.models.tag_list import TagList

# TODO update the JSON string below
json = "{}"
# create an instance of TagList from a JSON string
tag_list_instance = TagList.from_json(json)
# print the JSON string representation of the object
print TagList.to_json()

# convert the object into a dict
tag_list_dict = tag_list_instance.to_dict()
# create an instance of TagList from a dict
tag_list_form_dict = tag_list.from_dict(tag_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


