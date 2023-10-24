# DataVideoUsage

Video Usage KPIs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month_id** | **str** | month of the kpis | 
**transcoding** | **float** | total of transcoding second since the begining of the month | 
**hosting** | **float** | total of hosting second since the begining of the month | 
**delivery** | **float** | total of delivery (stream) second since the begining of the month | [optional] 
**drm** | **float** | total of delivery (stream) second since the begining of the month | [optional] 

## Example

```python
from Api42Vb.models.data_video_usage import DataVideoUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DataVideoUsage from a JSON string
data_video_usage_instance = DataVideoUsage.from_json(json)
# print the JSON string representation of the object
print DataVideoUsage.to_json()

# convert the object into a dict
data_video_usage_dict = data_video_usage_instance.to_dict()
# create an instance of DataVideoUsage from a dict
data_video_usage_form_dict = data_video_usage.from_dict(data_video_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


