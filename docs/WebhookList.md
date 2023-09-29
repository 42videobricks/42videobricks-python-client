# WebhookList

Webhook Object List

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**total** | **int** |  | 
**data** | [**List[Webhook]**](Webhook.md) |  | [optional] 

## Example

```python
from 42videobricks-python-client.models.webhook_list import WebhookList

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookList from a JSON string
webhook_list_instance = WebhookList.from_json(json)
# print the JSON string representation of the object
print WebhookList.to_json()

# convert the object into a dict
webhook_list_dict = webhook_list_instance.to_dict()
# create an instance of WebhookList from a dict
webhook_list_form_dict = webhook_list.from_dict(webhook_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


