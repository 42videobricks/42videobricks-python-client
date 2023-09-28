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

from openapi_client.models.video import Video  # noqa: E501

class TestVideo(unittest.TestCase):
    """Video unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Video:
        """Test Video
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Video`
        """
        model = Video()  # noqa: E501
        if include_optional:
            return Video(
                title = 'My video title',
                description = 'My video description',
                public = True,
                tags = ["MyTag"],
                id = 'STNQM2FIN1Bpa3I3bC9IRw==',
                status = 'AVAILABLE',
                duration = 3600,
                ctime = 1677020400,
                mtime = 1679526000,
                assets = openapi_client.models.video_assets.VideoAssets(
                    thumbnail = 'https://media-delivery-cdn.alchimie-services.net/image/v1/mediadb-product-filetype-dev/1002541/COVER.jpg', 
                    player = 'https://stream.video-bricks.com/STNQM2FIN1Bpa3I3bC9IRw==/player', 
                    stream = 'https://stream.video-bricks.com/STNQM2FIN1Bpa3I3bC9IRw==', 
                    iframe = '<iframe src="https://player.video-bricks.com/STNQM2FIN1Bpa3I3bC9IRw==/player" gesture="media" allow="encrypted-media" allowfullscreen="allowfullscreen" width="100%"></iframe>', ),
                metas = { }
            )
        else:
            return Video(
                id = 'STNQM2FIN1Bpa3I3bC9IRw==',
        )
        """

    def testVideo(self):
        """Test Video"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
