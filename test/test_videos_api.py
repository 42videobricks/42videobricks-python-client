# coding: utf-8

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.videos_api import VideosApi  # noqa: E501


class TestVideosApi(unittest.TestCase):
    """VideosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VideosApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_attachment_by_video_id(self) -> None:
        """Test case for add_attachment_by_video_id

        Upload an attachement  # noqa: E501
        """
        pass

    def test_add_thumbnail_by_video_id(self) -> None:
        """Test case for add_thumbnail_by_video_id

        Upload a thumbnail  # noqa: E501
        """
        pass

    def test_add_video(self) -> None:
        """Test case for add_video

        Add a new video  # noqa: E501
        """
        pass

    def test_delete_attachment_by_video_id(self) -> None:
        """Test case for delete_attachment_by_video_id

        Delete an attachment  # noqa: E501
        """
        pass

    def test_delete_thumbnail_by_video_id(self) -> None:
        """Test case for delete_thumbnail_by_video_id

        Delete a thumbnail  # noqa: E501
        """
        pass

    def test_delete_video_by_id(self) -> None:
        """Test case for delete_video_by_id

        Delete a video  # noqa: E501
        """
        pass

    def test_finalize_multipart_upload_video_by_id(self) -> None:
        """Test case for finalize_multipart_upload_video_by_id

        Multipart upload finalization  # noqa: E501
        """
        pass

    def test_finalize_upload_video_by_id(self) -> None:
        """Test case for finalize_upload_video_by_id

        Single file upload finalization  # noqa: E501
        """
        pass

    def test_get_attachment_by_video_id(self) -> None:
        """Test case for get_attachment_by_video_id

        Get the attachment  # noqa: E501
        """
        pass

    def test_get_attachment_file_by_video_id(self) -> None:
        """Test case for get_attachment_file_by_video_id

        Get attachement file  # noqa: E501
        """
        pass

    def test_get_attachments_by_video_id(self) -> None:
        """Test case for get_attachments_by_video_id

        List of attachments  # noqa: E501
        """
        pass

    def test_get_video_by_id(self) -> None:
        """Test case for get_video_by_id

        Retun a single video  # noqa: E501
        """
        pass

    def test_get_videos(self) -> None:
        """Test case for get_videos

        List videos  # noqa: E501
        """
        pass

    def test_init_multipart_upload_video_by_id(self) -> None:
        """Test case for init_multipart_upload_video_by_id

        Multipart upload intialization  # noqa: E501
        """
        pass

    def test_init_upload_video_by_id(self) -> None:
        """Test case for init_upload_video_by_id

        Single file upload intialization  # noqa: E501
        """
        pass

    def test_update_video_by_id(self) -> None:
        """Test case for update_video_by_id

        Update an existing video  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()