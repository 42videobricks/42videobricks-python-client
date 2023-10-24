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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr

class VideoProperties(BaseModel):
    """
    Video Properties Object  # noqa: E501
    """
    title: Optional[constr(strict=True, max_length=256)] = Field(None, description="title of the video")
    description: Optional[constr(strict=True, max_length=2048)] = Field(None, description="description of the video")
    public: Optional[StrictBool] = Field(None, description="Define if the video is public (it can be accessible by anybody with the video url). Default = tue")
    tags: Optional[conlist(StrictStr)] = Field(None, description="tags list linked to video")
    __properties = ["title", "description", "public", "tags"]

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
    def from_json(cls, json_str: str) -> VideoProperties:
        """Create an instance of VideoProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoProperties:
        """Create an instance of VideoProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoProperties.parse_obj(obj)

        _obj = VideoProperties.parse_obj({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "public": obj.get("public"),
            "tags": obj.get("tags")
        })
        return _obj

