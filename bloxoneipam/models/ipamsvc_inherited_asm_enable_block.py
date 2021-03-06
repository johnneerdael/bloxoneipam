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


class IpamsvcInheritedAsmEnableBlock(object):
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
        'action': 'str',
        'display_name': 'str',
        'source': 'str',
        'value': 'IpamsvcAsmEnableBlock'
    }

    attribute_map = {
        'action': 'action',
        'display_name': 'display_name',
        'source': 'source',
        'value': 'value'
    }

    def __init__(self, action=None, display_name=None, source=None, value=None):  # noqa: E501
        """IpamsvcInheritedAsmEnableBlock - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._display_name = None
        self._source = None
        self._value = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if display_name is not None:
            self.display_name = display_name
        if source is not None:
            self.source = source
        if value is not None:
            self.value = value

    @property
    def action(self):
        """Gets the action of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501

        Defaults to 'inherit'.  # noqa: E501

        :return: The action of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IpamsvcInheritedAsmEnableBlock.

        Defaults to 'inherit'.  # noqa: E501

        :param action: The action of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def display_name(self):
        """Gets the display_name of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501

        Read-only. Human-readable display name for the object referred to by source.  # noqa: E501

        :return: The display_name of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IpamsvcInheritedAsmEnableBlock.

        Read-only. Human-readable display name for the object referred to by source.  # noqa: E501

        :param display_name: The display_name of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def source(self):
        """Gets the source of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The source of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IpamsvcInheritedAsmEnableBlock.

        The resource identifier.  # noqa: E501

        :param source: The source of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def value(self):
        """Gets the value of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501

        Read-only. Inherited value.  # noqa: E501

        :return: The value of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :rtype: IpamsvcAsmEnableBlock
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IpamsvcInheritedAsmEnableBlock.

        Read-only. Inherited value.  # noqa: E501

        :param value: The value of this IpamsvcInheritedAsmEnableBlock.  # noqa: E501
        :type: IpamsvcAsmEnableBlock
        """

        self._value = value

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
        if issubclass(IpamsvcInheritedAsmEnableBlock, dict):
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
        if not isinstance(other, IpamsvcInheritedAsmEnableBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
