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

from openapi_client.models.data_video_usage_list import DataVideoUsageList  # noqa: E501

class TestDataVideoUsageList(unittest.TestCase):
    """DataVideoUsageList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataVideoUsageList:
        """Test DataVideoUsageList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataVideoUsageList`
        """
        model = DataVideoUsageList()  # noqa: E501
        if include_optional:
            return DataVideoUsageList(
                offset = 30,
                limit = 1,
                total = 355,
                data = [
                    openapi_client.models.data_video_usage.DataVideoUsage(
                        month_id = '2023-02', 
                        transcoding = 15715.23, 
                        hosting = 171523.34, 
                        delivery = 171523.34, 
                        drm = 171523.34, )
                    ]
            )
        else:
            return DataVideoUsageList(
                offset = 30,
                limit = 1,
                total = 355,
        )
        """

    def testDataVideoUsageList(self):
        """Test DataVideoUsageList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
