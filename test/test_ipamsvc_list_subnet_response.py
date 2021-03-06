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
from bloxoneipam.models.ipamsvc_list_subnet_response import IpamsvcListSubnetResponse  # noqa: E501
from bloxoneipam.rest import ApiException


class TestIpamsvcListSubnetResponse(unittest.TestCase):
    """IpamsvcListSubnetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIpamsvcListSubnetResponse(self):
        """Test IpamsvcListSubnetResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = bloxoneipam.models.ipamsvc_list_subnet_response.IpamsvcListSubnetResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
