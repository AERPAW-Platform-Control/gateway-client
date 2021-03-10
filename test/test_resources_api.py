# coding: utf-8

"""
    Aerpaw Gateway

    This is Aerpaw gateway service to interact with Emulab  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ericafu@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import aerpawgw_client
from aerpawgw_client.api.resources_api import ResourcesApi  # noqa: E501
from aerpawgw_client.rest import ApiException


class TestResourcesApi(unittest.TestCase):
    """ResourcesApi unit test stubs"""

    def setUp(self):
        self.api = ResourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_resources(self):
        """Test case for list_resources

        list resources  # noqa: E501
        """
        pass

    def test_parse_resources(self):
        """Test case for parse_resources

        Parse resources  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
