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

from openapi_client.models.video_multipart_upload_init_response import VideoMultipartUploadInitResponse  # noqa: E501

class TestVideoMultipartUploadInitResponse(unittest.TestCase):
    """VideoMultipartUploadInitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VideoMultipartUploadInitResponse:
        """Test VideoMultipartUploadInitResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VideoMultipartUploadInitResponse`
        """
        model = VideoMultipartUploadInitResponse()  # noqa: E501
        if include_optional:
            return VideoMultipartUploadInitResponse(
                chunk_size = 1000000,
                file_id = '5Fu8SetDoWjk3wwReTuWzLat6KubZECxfek863H9nsYreaEaKUmQ4G5iyEAETMK9X_DYJ8QBsgnEoM5bM8B.HQBe9eBtpSxLuXM.THMzKy1JBd0b5XGZ7OT6z.RfZAafc4B4PJ.KyQFarsAY4X7j_Eq2bz6ydqfQHdPyE73vl0Q-',
                file_key = 'ABkWl5kVPykAMSyu/myvideo.mov',
                parts = [
                    openapi_client.models.video_multipart_upload_init_response_parts_inner.VideoMultipartUploadInitResponse_parts_inner(
                        signed_url = 'https://alchimie-vpaas-client-uploads.s3.amazonaws.com/ABkWl5kVPykAMSyu/toto?uploadId=5Fu8SetDoWjk3wwReTuWzLat6KubZECxfek863H9nsYreaEaKUmQ4G5iyEAETMK9X_DYJ8QBsgnEoM5bM8B.HQBe9eBtpSxLuXM.THMzKy1JBd0b5XGZ7OT6z.RfZAafc4B4PJ.KyQFarsAY4X7j_Eq2bz6ydqfQHdPyE73vl0Q-&partNumber=1&AWSAccessKeyId=XXXXXXXXXXX&Signature=8mCPTseHxpgP73GT0p7ADyWcwmM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEG4aCWV1LXdlc3QtMSJGMEQCIEiVvECtKd5v3fq5irCP7lL7OYF5TJgRopk4CzLooWGQAiBkTzXTxwjLQBEqjG%2FoNmVEOvVRZE0N059PR4OLhe9FoSrEAwin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDQ4OTE0MzIzNDE5OSIMlmuGOIiRddNi%2FwP5KpgDxldMYVS3L%2BAG%2Bl0glvUlqzSwaWuhSJQeYFvDHSF7mMcy%2B8wXzg7GH8B6DkAjQtDITWpdmIBTbpKK7WcDCLfxOobixWz9CkKyBsHuKvbxC0WdoKRpg6UgTA7ZrB9flETvHGgqaYbE%2FJxIzCPy3x79E2y1egpLOwHMGwxg4TBC7OrqIuJjR9v7x%2FYoUTU54%2F7x1VZYHUfhv5rxiE9Pmy91klwYYY2Ht8OIUnDDtWWZoSAvyVXxtSXGsu0yI9HfP9rMtK6DbNX3sNlws97rPQkuBh97gFfr%2Fh39SVKTwGEbz4vqD9DFVPMzJj0%2BBfbWUzMrUzWU1%2FUXskxR4SCTEWuCEiv%2FvAQWAYbCW4ItXnnePh3gTQPXAikwkqSgYOGfWsSpYYkzegvkAuzA03ej9H4Ud6lV0y8Rh8ujB%2F8uwlMsG1DFJnoDMfkNv5WK5zws6rzVJ90PA5j%2BwI7bGA5ejO1cPjC1dp1H5UmYFDDzE2ZxPmd%2BJkTrVnpon4jMkwBkIWZoSQ7gRFfuraiiTJ8jWpTW4MemXHe5kDRaMP%2Bg3aMGOp8BVkQUKhbtZKskDCy1cis%2BXH30kmpjThcQdXcgS6aV5PUQsLx2wn%2BNl66m2zZGZMfh5PCMB0AYs3eXFVgJVGd5sCsP4u20JHKBBfQYAPidGpAIDL2NWrR71pr4vFR0vB32TB4wWzCjM%2BmVgub6Je17mMi19KZCLAtrhyKpxi1ajjG8TGxaNxERrG0LWasiddcuMiEe7QbXjxQvnhg7Jg6d&Expires=1685541291', 
                        part_number = 1, )
                    ]
            )
        else:
            return VideoMultipartUploadInitResponse(
        )
        """

    def testVideoMultipartUploadInitResponse(self):
        """Test VideoMultipartUploadInitResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
