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

from 42videobricks-python-client.models.webhook import Webhook  # noqa: E501

class TestWebhook(unittest.TestCase):
    """Webhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Webhook:
        """Test Webhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Webhook`
        """
        model = Webhook()  # noqa: E501
        if include_optional:
            return Webhook(
                url = 'https://myapplication.com/notification',
                token = '9981f9f4-657a-4ebf-be7c-19bedd4775',
                event_type = ["VIDEO_STATUS","VIDEO_TRANSCODING_PROGRESS"],
                id = '01GVZHMKS5B8SKEHSHRD0QHKYF',
                ctime = 1677020400,
                mtime = 1679526000
            )
        else:
            return Webhook(
                url = 'https://myapplication.com/notification',
                event_type = ["VIDEO_STATUS","VIDEO_TRANSCODING_PROGRESS"],
                id = '01GVZHMKS5B8SKEHSHRD0QHKYF',
        )
        """

    def testWebhook(self):
        """Test Webhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
