# WebhookProperties

Webhook properties object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Url of the application wich is receiving Notifications | 
**token** | **str** | Optionnal Secret token to validate notifications. Sent with the request in the X-Vpass-Token HTTP header. | [optional] 
**event_type** | **List[str]** | List of event to be notified:   * VIDEO_STATUS: Get Video object status modification notifications   Status values: REQUESTED, CREATED, TRANSCODING, TRANSCODING_ERROR, AVAILABLE, DELETED   * VIDEO_TRANSCODING_PROGRESS: Get transcoding progression notifications | 

## Example

```python
from Api42Vb.models.webhook_properties import WebhookProperties

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProperties from a JSON string
webhook_properties_instance = WebhookProperties.from_json(json)
# print the JSON string representation of the object
print WebhookProperties.to_json()

# convert the object into a dict
webhook_properties_dict = webhook_properties_instance.to_dict()
# create an instance of WebhookProperties from a dict
webhook_properties_form_dict = webhook_properties.from_dict(webhook_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


