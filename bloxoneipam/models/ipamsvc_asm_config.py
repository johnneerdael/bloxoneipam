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


class IpamsvcASMConfig(object):
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
        'asm_threshold': 'int',
        'enable': 'bool',
        'enable_notification': 'bool',
        'forecast_period': 'int',
        'growth_factor': 'int',
        'growth_type': 'str',
        'history': 'int',
        'min_total': 'int',
        'min_unused': 'int',
        'reenable_date': 'datetime'
    }

    attribute_map = {
        'asm_threshold': 'asm_threshold',
        'enable': 'enable',
        'enable_notification': 'enable_notification',
        'forecast_period': 'forecast_period',
        'growth_factor': 'growth_factor',
        'growth_type': 'growth_type',
        'history': 'history',
        'min_total': 'min_total',
        'min_unused': 'min_unused',
        'reenable_date': 'reenable_date'
    }

    def __init__(self, asm_threshold=None, enable=None, enable_notification=None, forecast_period=None, growth_factor=None, growth_type=None, history=None, min_total=None, min_unused=None, reenable_date=None):  # noqa: E501
        """IpamsvcASMConfig - a model defined in Swagger"""  # noqa: E501

        self._asm_threshold = None
        self._enable = None
        self._enable_notification = None
        self._forecast_period = None
        self._growth_factor = None
        self._growth_type = None
        self._history = None
        self._min_total = None
        self._min_unused = None
        self._reenable_date = None
        self.discriminator = None

        if asm_threshold is not None:
            self.asm_threshold = asm_threshold
        if enable is not None:
            self.enable = enable
        if enable_notification is not None:
            self.enable_notification = enable_notification
        if forecast_period is not None:
            self.forecast_period = forecast_period
        if growth_factor is not None:
            self.growth_factor = growth_factor
        if growth_type is not None:
            self.growth_type = growth_type
        if history is not None:
            self.history = history
        if min_total is not None:
            self.min_total = min_total
        if min_unused is not None:
            self.min_unused = min_unused
        if reenable_date is not None:
            self.reenable_date = reenable_date

    @property
    def asm_threshold(self):
        """Gets the asm_threshold of this IpamsvcASMConfig.  # noqa: E501


        :return: The asm_threshold of this IpamsvcASMConfig.  # noqa: E501
        :rtype: int
        """
        return self._asm_threshold

    @asm_threshold.setter
    def asm_threshold(self, asm_threshold):
        """Sets the asm_threshold of this IpamsvcASMConfig.


        :param asm_threshold: The asm_threshold of this IpamsvcASMConfig.  # noqa: E501
        :type: int
        """

        self._asm_threshold = asm_threshold

    @property
    def enable(self):
        """Gets the enable of this IpamsvcASMConfig.  # noqa: E501


        :return: The enable of this IpamsvcASMConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this IpamsvcASMConfig.


        :param enable: The enable of this IpamsvcASMConfig.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def enable_notification(self):
        """Gets the enable_notification of this IpamsvcASMConfig.  # noqa: E501


        :return: The enable_notification of this IpamsvcASMConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enable_notification

    @enable_notification.setter
    def enable_notification(self, enable_notification):
        """Sets the enable_notification of this IpamsvcASMConfig.


        :param enable_notification: The enable_notification of this IpamsvcASMConfig.  # noqa: E501
        :type: bool
        """

        self._enable_notification = enable_notification

    @property
    def forecast_period(self):
        """Gets the forecast_period of this IpamsvcASMConfig.  # noqa: E501


        :return: The forecast_period of this IpamsvcASMConfig.  # noqa: E501
        :rtype: int
        """
        return self._forecast_period

    @forecast_period.setter
    def forecast_period(self, forecast_period):
        """Sets the forecast_period of this IpamsvcASMConfig.


        :param forecast_period: The forecast_period of this IpamsvcASMConfig.  # noqa: E501
        :type: int
        """

        self._forecast_period = forecast_period

    @property
    def growth_factor(self):
        """Gets the growth_factor of this IpamsvcASMConfig.  # noqa: E501

        Either the number or percentage of addresses to grow by.  # noqa: E501

        :return: The growth_factor of this IpamsvcASMConfig.  # noqa: E501
        :rtype: int
        """
        return self._growth_factor

    @growth_factor.setter
    def growth_factor(self, growth_factor):
        """Sets the growth_factor of this IpamsvcASMConfig.

        Either the number or percentage of addresses to grow by.  # noqa: E501

        :param growth_factor: The growth_factor of this IpamsvcASMConfig.  # noqa: E501
        :type: int
        """

        self._growth_factor = growth_factor

    @property
    def growth_type(self):
        """Gets the growth_type of this IpamsvcASMConfig.  # noqa: E501


        :return: The growth_type of this IpamsvcASMConfig.  # noqa: E501
        :rtype: str
        """
        return self._growth_type

    @growth_type.setter
    def growth_type(self, growth_type):
        """Sets the growth_type of this IpamsvcASMConfig.


        :param growth_type: The growth_type of this IpamsvcASMConfig.  # noqa: E501
        :type: str
        """

        self._growth_type = growth_type

    @property
    def history(self):
        """Gets the history of this IpamsvcASMConfig.  # noqa: E501

        The minimum amount of history needed before ASM can run on this subnet.  # noqa: E501

        :return: The history of this IpamsvcASMConfig.  # noqa: E501
        :rtype: int
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this IpamsvcASMConfig.

        The minimum amount of history needed before ASM can run on this subnet.  # noqa: E501

        :param history: The history of this IpamsvcASMConfig.  # noqa: E501
        :type: int
        """

        self._history = history

    @property
    def min_total(self):
        """Gets the min_total of this IpamsvcASMConfig.  # noqa: E501

        Minimum size of range needed for ASM to run on this subnet.  # noqa: E501

        :return: The min_total of this IpamsvcASMConfig.  # noqa: E501
        :rtype: int
        """
        return self._min_total

    @min_total.setter
    def min_total(self, min_total):
        """Sets the min_total of this IpamsvcASMConfig.

        Minimum size of range needed for ASM to run on this subnet.  # noqa: E501

        :param min_total: The min_total of this IpamsvcASMConfig.  # noqa: E501
        :type: int
        """

        self._min_total = min_total

    @property
    def min_unused(self):
        """Gets the min_unused of this IpamsvcASMConfig.  # noqa: E501

        The minimum number of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change. This value is a percentage.  # noqa: E501

        :return: The min_unused of this IpamsvcASMConfig.  # noqa: E501
        :rtype: int
        """
        return self._min_unused

    @min_unused.setter
    def min_unused(self, min_unused):
        """Sets the min_unused of this IpamsvcASMConfig.

        The minimum number of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change. This value is a percentage.  # noqa: E501

        :param min_unused: The min_unused of this IpamsvcASMConfig.  # noqa: E501
        :type: int
        """

        self._min_unused = min_unused

    @property
    def reenable_date(self):
        """Gets the reenable_date of this IpamsvcASMConfig.  # noqa: E501


        :return: The reenable_date of this IpamsvcASMConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._reenable_date

    @reenable_date.setter
    def reenable_date(self, reenable_date):
        """Sets the reenable_date of this IpamsvcASMConfig.


        :param reenable_date: The reenable_date of this IpamsvcASMConfig.  # noqa: E501
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
        if issubclass(IpamsvcASMConfig, dict):
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
        if not isinstance(other, IpamsvcASMConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
