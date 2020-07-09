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


class IpamsvcDDNSZone(object):
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
        'fqdn': 'str',
        'nameservers': 'list[str]',
        'tsig_enabled': 'bool',
        'tsig_key_algo': 'str',
        'tsig_key_data': 'str',
        'tsig_key_name': 'str',
        'view': 'str',
        'view_name': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'fqdn': 'fqdn',
        'nameservers': 'nameservers',
        'tsig_enabled': 'tsig_enabled',
        'tsig_key_algo': 'tsig_key_algo',
        'tsig_key_data': 'tsig_key_data',
        'tsig_key_name': 'tsig_key_name',
        'view': 'view',
        'view_name': 'view_name',
        'zone': 'zone'
    }

    def __init__(self, fqdn=None, nameservers=None, tsig_enabled=None, tsig_key_algo=None, tsig_key_data=None, tsig_key_name=None, view=None, view_name=None, zone=None):  # noqa: E501
        """IpamsvcDDNSZone - a model defined in Swagger"""  # noqa: E501

        self._fqdn = None
        self._nameservers = None
        self._tsig_enabled = None
        self._tsig_key_algo = None
        self._tsig_key_data = None
        self._tsig_key_name = None
        self._view = None
        self._view_name = None
        self._zone = None
        self.discriminator = None

        if fqdn is not None:
            self.fqdn = fqdn
        if nameservers is not None:
            self.nameservers = nameservers
        if tsig_enabled is not None:
            self.tsig_enabled = tsig_enabled
        if tsig_key_algo is not None:
            self.tsig_key_algo = tsig_key_algo
        if tsig_key_data is not None:
            self.tsig_key_data = tsig_key_data
        if tsig_key_name is not None:
            self.tsig_key_name = tsig_key_name
        if view is not None:
            self.view = view
        if view_name is not None:
            self.view_name = view_name
        self.zone = zone

    @property
    def fqdn(self):
        """Gets the fqdn of this IpamsvcDDNSZone.  # noqa: E501

        Optional. Zone FQDN.  If zone is defined the fqdn field must be empty.  # noqa: E501

        :return: The fqdn of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this IpamsvcDDNSZone.

        Optional. Zone FQDN.  If zone is defined the fqdn field must be empty.  # noqa: E501

        :param fqdn: The fqdn of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def nameservers(self):
        """Gets the nameservers of this IpamsvcDDNSZone.  # noqa: E501

        Optional. Zones nameservers IPv4 addresses.  Each IP shoud be unique across the list of nameservers.  # noqa: E501

        :return: The nameservers of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """Sets the nameservers of this IpamsvcDDNSZone.

        Optional. Zones nameservers IPv4 addresses.  Each IP shoud be unique across the list of nameservers.  # noqa: E501

        :param nameservers: The nameservers of this IpamsvcDDNSZone.  # noqa: E501
        :type: list[str]
        """

        self._nameservers = nameservers

    @property
    def tsig_enabled(self):
        """Gets the tsig_enabled of this IpamsvcDDNSZone.  # noqa: E501

        Optional. True to use a TSIG key for the update.  Defaults to false.  # noqa: E501

        :return: The tsig_enabled of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: bool
        """
        return self._tsig_enabled

    @tsig_enabled.setter
    def tsig_enabled(self, tsig_enabled):
        """Sets the tsig_enabled of this IpamsvcDDNSZone.

        Optional. True to use a TSIG key for the update.  Defaults to false.  # noqa: E501

        :param tsig_enabled: The tsig_enabled of this IpamsvcDDNSZone.  # noqa: E501
        :type: bool
        """

        self._tsig_enabled = tsig_enabled

    @property
    def tsig_key_algo(self):
        """Gets the tsig_key_algo of this IpamsvcDDNSZone.  # noqa: E501

        Optional. TSIG key algorithm.  Allowed values:    hmac_sha256    hmac_md5    hmac_sha1    hmac_sha224    hmac_sha384    hmac_sha512  Defaults to hmac_sha256.  # noqa: E501

        :return: The tsig_key_algo of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._tsig_key_algo

    @tsig_key_algo.setter
    def tsig_key_algo(self, tsig_key_algo):
        """Sets the tsig_key_algo of this IpamsvcDDNSZone.

        Optional. TSIG key algorithm.  Allowed values:    hmac_sha256    hmac_md5    hmac_sha1    hmac_sha224    hmac_sha384    hmac_sha512  Defaults to hmac_sha256.  # noqa: E501

        :param tsig_key_algo: The tsig_key_algo of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """

        self._tsig_key_algo = tsig_key_algo

    @property
    def tsig_key_data(self):
        """Gets the tsig_key_data of this IpamsvcDDNSZone.  # noqa: E501

        Optinal. TSIG key data. Base64, may be empty.  Error if empty and tsig_enable is true.  Defaults to empty.  # noqa: E501

        :return: The tsig_key_data of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._tsig_key_data

    @tsig_key_data.setter
    def tsig_key_data(self, tsig_key_data):
        """Sets the tsig_key_data of this IpamsvcDDNSZone.

        Optinal. TSIG key data. Base64, may be empty.  Error if empty and tsig_enable is true.  Defaults to empty.  # noqa: E501

        :param tsig_key_data: The tsig_key_data of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """

        self._tsig_key_data = tsig_key_data

    @property
    def tsig_key_name(self):
        """Gets the tsig_key_name of this IpamsvcDDNSZone.  # noqa: E501

        Optional. TSIG key name. FQDN, may be empty.  Error if empty and tsig_enable is true.  Defaults to empty.  # noqa: E501

        :return: The tsig_key_name of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._tsig_key_name

    @tsig_key_name.setter
    def tsig_key_name(self, tsig_key_name):
        """Sets the tsig_key_name of this IpamsvcDDNSZone.

        Optional. TSIG key name. FQDN, may be empty.  Error if empty and tsig_enable is true.  Defaults to empty.  # noqa: E501

        :param tsig_key_name: The tsig_key_name of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """

        self._tsig_key_name = tsig_key_name

    @property
    def view(self):
        """Gets the view of this IpamsvcDDNSZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The view of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this IpamsvcDDNSZone.

        The resource identifier.  # noqa: E501

        :param view: The view of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """

        self._view = view

    @property
    def view_name(self):
        """Gets the view_name of this IpamsvcDDNSZone.  # noqa: E501

        Read-only. The name of the view.  # noqa: E501

        :return: The view_name of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """Sets the view_name of this IpamsvcDDNSZone.

        Read-only. The name of the view.  # noqa: E501

        :param view_name: The view_name of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """

        self._view_name = view_name

    @property
    def zone(self):
        """Gets the zone of this IpamsvcDDNSZone.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The zone of this IpamsvcDDNSZone.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this IpamsvcDDNSZone.

        The resource identifier.  # noqa: E501

        :param zone: The zone of this IpamsvcDDNSZone.  # noqa: E501
        :type: str
        """
        if zone is None:
            raise ValueError("Invalid value for `zone`, must not be `None`")  # noqa: E501

        self._zone = zone

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
        if issubclass(IpamsvcDDNSZone, dict):
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
        if not isinstance(other, IpamsvcDDNSZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other