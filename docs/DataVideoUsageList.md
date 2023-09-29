# DataVideoUsageList

Data Video Usage Object list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[DataVideoUsage]**](DataVideoUsage.md) |  | [optional] 

## Example

```python
from 42videobricks-python-client.models.data_video_usage_list import DataVideoUsageList

# TODO update the JSON string below
json = "{}"
# create an instance of DataVideoUsageList from a JSON string
data_video_usage_list_instance = DataVideoUsageList.from_json(json)
# print the JSON string representation of the object
print DataVideoUsageList.to_json()

# convert the object into a dict
data_video_usage_list_dict = data_video_usage_list_instance.to_dict()
# create an instance of DataVideoUsageList from a dict
data_video_usage_list_form_dict = data_video_usage_list.from_dict(data_video_usage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


