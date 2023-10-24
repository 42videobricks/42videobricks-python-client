# Webhook

Webhook Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Url of the application wich is receiving Notifications | 
**token** | **str** | Optionnal Secret token to validate notifications. Sent with the request in the X-Vpass-Token HTTP header. | [optional] 
**event_type** | **List[str]** | List of event to be notified:   * VIDEO_STATUS: Get Video object status modification notifications   Status values: REQUESTED, CREATED, TRANSCODING, AVAILABLE, DELETED   * VIDEO_TRANSCODING_PROGRESS: Get transcoding progression notifications | 
**id** | **str** | id of the webhook | 
**ctime** | **int** | Creation date (timestamp) | [optional] 
**mtime** | **int** | Modification date (timestamp) | [optional] 

## Example

```python
from Api42Vb.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print Webhook.to_json()

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_form_dict = webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


