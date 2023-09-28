# coding: utf-8

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.video_multipart_upload_init import VideoMultipartUploadInit  # noqa: E501

class TestVideoMultipartUploadInit(unittest.TestCase):
    """VideoMultipartUploadInit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoMultipartUploadInit:
        """Test VideoMultipartUploadInit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoMultipartUploadInit`
        """
        model = VideoMultipartUploadInit()  # noqa: E501
        if include_optional:
            return VideoMultipartUploadInit(
                name = 'myvideo.mov',
                size = 1000000
            )
        else:
            return VideoMultipartUploadInit(
                name = 'myvideo.mov',
                size = 1000000,
        )
        """

    def testVideoMultipartUploadInit(self):
        """Test VideoMultipartUploadInit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
