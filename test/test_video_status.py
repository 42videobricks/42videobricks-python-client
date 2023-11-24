# coding: utf-8

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from Api42Vb.models.video_status import VideoStatus

class TestVideoStatus(unittest.TestCase):
    """VideoStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoStatus:
        """Test VideoStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoStatus`
        """
        model = VideoStatus()
        if include_optional:
            return VideoStatus(
                status = 'REQUESTED',
                message = ''
            )
        else:
            return VideoStatus(
        )
        """

    def testVideoStatus(self):
        """Test VideoStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
