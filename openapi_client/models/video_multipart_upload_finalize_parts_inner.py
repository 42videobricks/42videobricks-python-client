# coding: utf-8

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class VideoMultipartUploadFinalizePartsInner(BaseModel):
    """
    part signed url object  # noqa: E501
    """
    part_number: Optional[StrictInt] = Field(None, alias="PartNumber", description="part number")
    e_tag: Optional[StrictStr] = Field(None, alias="ETag", description="part Etag")
    __properties = ["PartNumber", "ETag"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VideoMultipartUploadFinalizePartsInner:
        """Create an instance of VideoMultipartUploadFinalizePartsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoMultipartUploadFinalizePartsInner:
        """Create an instance of VideoMultipartUploadFinalizePartsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoMultipartUploadFinalizePartsInner.parse_obj(obj)

        _obj = VideoMultipartUploadFinalizePartsInner.parse_obj({
            "part_number": obj.get("PartNumber"),
            "e_tag": obj.get("ETag")
        })
        return _obj


