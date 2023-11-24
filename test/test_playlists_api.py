# coding: utf-8

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from Api42Vb.api.playlists_api import PlaylistsApi


class TestPlaylistsApi(unittest.TestCase):
    """PlaylistsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlaylistsApi()

    def tearDown(self) -> None:
        pass

    def test_add_playlist(self) -> None:
        """Test case for add_playlist

        Add a new playlist
        """
        pass

    def test_delete_playlist_by_id(self) -> None:
        """Test case for delete_playlist_by_id

        Delete a playlist
        """
        pass

    def test_get_playlist_by_id(self) -> None:
        """Test case for get_playlist_by_id

        Retun a single playlist
        """
        pass

    def test_get_playlists(self) -> None:
        """Test case for get_playlists

        List playlists
        """
        pass

    def test_update_playlist_by_id(self) -> None:
        """Test case for update_playlist_by_id

        Update an existing playlist
        """
        pass


if __name__ == '__main__':
    unittest.main()
