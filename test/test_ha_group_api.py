# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bloxoneipam
from bloxoneipam.api.ha_group_api import HaGroupApi  # noqa: E501
from bloxoneipam.rest import ApiException


class TestHaGroupApi(unittest.TestCase):
    """HaGroupApi unit test stubs"""

    def setUp(self):
        self.api = bloxoneipam.api.ha_group_api.HaGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ha_group_create(self):
        """Test case for ha_group_create

        Create the HA Group object.  # noqa: E501
        """
        pass

    def test_ha_group_delete(self):
        """Test case for ha_group_delete

        Delete the HA Group object.  # noqa: E501
        """
        pass

    def test_ha_group_list(self):
        """Test case for ha_group_list

        List HA Group objects.  # noqa: E501
        """
        pass

    def test_ha_group_read(self):
        """Test case for ha_group_read

        Read the HA Group object.  # noqa: E501
        """
        pass

    def test_ha_group_update(self):
        """Test case for ha_group_update

        Update the HA Group object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
