# coding: utf-8

# flake8: noqa

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.2"

# import apis into sdk package
from Api42Vb.api.data_api import DataApi
from Api42Vb.api.tags_api import TagsApi
from Api42Vb.api.videos_api import VideosApi
from Api42Vb.api.webhooks_api import WebhooksApi

# import ApiClient
from Api42Vb.api_response import ApiResponse
from Api42Vb.api_client import ApiClient
from Api42Vb.configuration import Configuration
from Api42Vb.exceptions import OpenApiException
from Api42Vb.exceptions import ApiTypeError
from Api42Vb.exceptions import ApiValueError
from Api42Vb.exceptions import ApiKeyError
from Api42Vb.exceptions import ApiAttributeError
from Api42Vb.exceptions import ApiException

# import models into sdk package
from Api42Vb.models.data_video_usage import DataVideoUsage
from Api42Vb.models.data_video_usage_list import DataVideoUsageList
from Api42Vb.models.error import Error
from Api42Vb.models.pagination import Pagination
from Api42Vb.models.tag_list import TagList
from Api42Vb.models.video import Video
from Api42Vb.models.video_assets import VideoAssets
from Api42Vb.models.video_attachment import VideoAttachment
from Api42Vb.models.video_attachment_list import VideoAttachmentList
from Api42Vb.models.video_list import VideoList
from Api42Vb.models.video_multipart_upload_finalize import VideoMultipartUploadFinalize
from Api42Vb.models.video_multipart_upload_finalize_parts_inner import VideoMultipartUploadFinalizePartsInner
from Api42Vb.models.video_multipart_upload_init import VideoMultipartUploadInit
from Api42Vb.models.video_multipart_upload_init_response import VideoMultipartUploadInitResponse
from Api42Vb.models.video_multipart_upload_init_response_parts_inner import VideoMultipartUploadInitResponsePartsInner
from Api42Vb.models.video_properties import VideoProperties
from Api42Vb.models.video_upload_init_response import VideoUploadInitResponse
from Api42Vb.models.webhook import Webhook
from Api42Vb.models.webhook_list import WebhookList
from Api42Vb.models.webhook_properties import WebhookProperties
