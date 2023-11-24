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

from Api42Vb.models.playlist_properties import PlaylistProperties

class TestPlaylistProperties(unittest.TestCase):
    """PlaylistProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaylistProperties:
        """Test PlaylistProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaylistProperties`
        """
        model = PlaylistProperties()
        if include_optional:
            return PlaylistProperties(
                name = 'My playlist name',
                description = 'My playlist description',
                children = ["{{videoId}}"]
            )
        else:
            return PlaylistProperties(
        )
        """

    def testPlaylistProperties(self):
        """Test PlaylistProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
