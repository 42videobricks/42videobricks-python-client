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

from 42videobricks-python-client.models.tag_list import TagList  # noqa: E501

class TestTagList(unittest.TestCase):
    """TagList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagList:
        """Test TagList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagList`
        """
        model = TagList()  # noqa: E501
        if include_optional:
            return TagList(
                offset = 30,
                limit = 1,
                total = 355,
                data = ["alien","cowboy"]
            )
        else:
            return TagList(
                offset = 30,
                limit = 1,
                total = 355,
        )
        """

    def testTagList(self):
        """Test TagList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()