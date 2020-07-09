# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IpamsvcAsmEnableBlock(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enable': 'bool',
        'enable_notification': 'bool',
        'reenable_date': 'datetime'
    }

    attribute_map = {
        'enable': 'enable',
        'enable_notification': 'enable_notification',
        'reenable_date': 'reenable_date'
    }

    def __init__(self, enable=None, enable_notification=None, reenable_date=None):  # noqa: E501
        """IpamsvcAsmEnableBlock - a model defined in Swagger"""  # noqa: E501

        self._enable = None
        self._enable_notification = None
        self._reenable_date = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if enable_notification is not None:
            self.enable_notification = enable_notification
        if reenable_date is not None:
            self.reenable_date = reenable_date

    @property
    def enable(self):
        """Gets the enable of this IpamsvcAsmEnableBlock.  # noqa: E501


        :return: The enable of this IpamsvcAsmEnableBlock.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this IpamsvcAsmEnableBlock.


        :param enable: The enable of this IpamsvcAsmEnableBlock.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def enable_notification(self):
        """Gets the enable_notification of this IpamsvcAsmEnableBlock.  # noqa: E501


        :return: The enable_notification of this IpamsvcAsmEnableBlock.  # noqa: E501
        :rtype: bool
        """
        return self._enable_notification

    @enable_notification.setter
    def enable_notification(self, enable_notification):
        """Sets the enable_notification of this IpamsvcAsmEnableBlock.


        :param enable_notification: The enable_notification of this IpamsvcAsmEnableBlock.  # noqa: E501
        :type: bool
        """

        self._enable_notification = enable_notification

    @property
    def reenable_date(self):
        """Gets the reenable_date of this IpamsvcAsmEnableBlock.  # noqa: E501


        :return: The reenable_date of this IpamsvcAsmEnableBlock.  # noqa: E501
        :rtype: datetime
        """
        return self._reenable_date

    @reenable_date.setter
    def reenable_date(self, reenable_date):
        """Sets the reenable_date of this IpamsvcAsmEnableBlock.


        :param reenable_date: The reenable_date of this IpamsvcAsmEnableBlock.  # noqa: E501
        :type: datetime
        """

        self._reenable_date = reenable_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IpamsvcAsmEnableBlock, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IpamsvcAsmEnableBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other