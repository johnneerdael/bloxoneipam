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


class IpamsvcUtilizationThreshold(object):
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
        'enabled': 'bool',
        'high': 'int',
        'low': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'high': 'high',
        'low': 'low'
    }

    def __init__(self, enabled=None, high=None, low=None):  # noqa: E501
        """IpamsvcUtilizationThreshold - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._high = None
        self._low = None
        self.discriminator = None

        self.enabled = enabled
        self.high = high
        self.low = low

    @property
    def enabled(self):
        """Gets the enabled of this IpamsvcUtilizationThreshold.  # noqa: E501

        Indicates utilization threshold is enabled if set to true, false otherwise.  # noqa: E501

        :return: The enabled of this IpamsvcUtilizationThreshold.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IpamsvcUtilizationThreshold.

        Indicates utilization threshold is enabled if set to true, false otherwise.  # noqa: E501

        :param enabled: The enabled of this IpamsvcUtilizationThreshold.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def high(self):
        """Gets the high of this IpamsvcUtilizationThreshold.  # noqa: E501

        High value defined as an integer number constrained to the interval [0, 100] representing respectively 0% and 100% utilization. Thresholds are inclusive in the comparison test.  # noqa: E501

        :return: The high of this IpamsvcUtilizationThreshold.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this IpamsvcUtilizationThreshold.

        High value defined as an integer number constrained to the interval [0, 100] representing respectively 0% and 100% utilization. Thresholds are inclusive in the comparison test.  # noqa: E501

        :param high: The high of this IpamsvcUtilizationThreshold.  # noqa: E501
        :type: int
        """
        if high is None:
            raise ValueError("Invalid value for `high`, must not be `None`")  # noqa: E501

        self._high = high

    @property
    def low(self):
        """Gets the low of this IpamsvcUtilizationThreshold.  # noqa: E501

        Low value defined as an integer number constrained to the interval [0, 100] representing respectively 0% and 100% utilization. Thresholds are inclusive in the comparison test.  # noqa: E501

        :return: The low of this IpamsvcUtilizationThreshold.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this IpamsvcUtilizationThreshold.

        Low value defined as an integer number constrained to the interval [0, 100] representing respectively 0% and 100% utilization. Thresholds are inclusive in the comparison test.  # noqa: E501

        :param low: The low of this IpamsvcUtilizationThreshold.  # noqa: E501
        :type: int
        """
        if low is None:
            raise ValueError("Invalid value for `low`, must not be `None`")  # noqa: E501

        self._low = low

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
        if issubclass(IpamsvcUtilizationThreshold, dict):
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
        if not isinstance(other, IpamsvcUtilizationThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
