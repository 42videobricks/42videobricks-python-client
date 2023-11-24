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

from Api42Vb.models.playlist import Playlist

class TestPlaylist(unittest.TestCase):
    """Playlist unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Playlist:
        """Test Playlist
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Playlist`
        """
        model = Playlist()
        if include_optional:
            return Playlist(
                id = 'STNQM2FIN1Bpa3I3bC9IRw==',
                name = 'My playlist name',
                description = 'My video description',
                children = [
                    null
                    ],
                ctime = 1677020400,
                mtime = 1679526000
            )
        else:
            return Playlist(
                id = 'STNQM2FIN1Bpa3I3bC9IRw==',
        )
        """

    def testPlaylist(self):
        """Test Playlist"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
