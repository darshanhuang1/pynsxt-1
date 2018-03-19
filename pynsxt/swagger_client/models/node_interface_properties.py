# coding: utf-8

"""
    NSX API

    VMware NSX REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.node_interface_alias import NodeInterfaceAlias  # noqa: F401,E501


class NodeInterfaceProperties(object):
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
        'source': 'str',
        'admin_status': 'str',
        'link_status': 'str',
        'interface_alias': 'list[NodeInterfaceAlias]',
        'ens_enabled': 'bool',
        'interface_type': 'str',
        'interface_id': 'str',
        'connected_switch': 'str',
        'ens_capable': 'bool',
        'mtu': 'int'
    }

    attribute_map = {
        'source': 'source',
        'admin_status': 'admin_status',
        'link_status': 'link_status',
        'interface_alias': 'interface_alias',
        'ens_enabled': 'ens_enabled',
        'interface_type': 'interface_type',
        'interface_id': 'interface_id',
        'connected_switch': 'connected_switch',
        'ens_capable': 'ens_capable',
        'mtu': 'mtu'
    }

    def __init__(self, source=None, admin_status=None, link_status=None, interface_alias=None, ens_enabled=None, interface_type=None, interface_id=None, connected_switch=None, ens_capable=None, mtu=None):  # noqa: E501
        """NodeInterfaceProperties - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._admin_status = None
        self._link_status = None
        self._interface_alias = None
        self._ens_enabled = None
        self._interface_type = None
        self._interface_id = None
        self._connected_switch = None
        self._ens_capable = None
        self._mtu = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if admin_status is not None:
            self.admin_status = admin_status
        if link_status is not None:
            self.link_status = link_status
        if interface_alias is not None:
            self.interface_alias = interface_alias
        if ens_enabled is not None:
            self.ens_enabled = ens_enabled
        if interface_type is not None:
            self.interface_type = interface_type
        if interface_id is not None:
            self.interface_id = interface_id
        if connected_switch is not None:
            self.connected_switch = connected_switch
        if ens_capable is not None:
            self.ens_capable = ens_capable
        if mtu is not None:
            self.mtu = mtu

    @property
    def source(self):
        """Gets the source of this NodeInterfaceProperties.  # noqa: E501

        Source of status data  # noqa: E501

        :return: The source of this NodeInterfaceProperties.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this NodeInterfaceProperties.

        Source of status data  # noqa: E501

        :param source: The source of this NodeInterfaceProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["realtime", "cached"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def admin_status(self):
        """Gets the admin_status of this NodeInterfaceProperties.  # noqa: E501

        Interface administration status  # noqa: E501

        :return: The admin_status of this NodeInterfaceProperties.  # noqa: E501
        :rtype: str
        """
        return self._admin_status

    @admin_status.setter
    def admin_status(self, admin_status):
        """Sets the admin_status of this NodeInterfaceProperties.

        Interface administration status  # noqa: E501

        :param admin_status: The admin_status of this NodeInterfaceProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if admin_status not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_status` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_status, allowed_values)
            )

        self._admin_status = admin_status

    @property
    def link_status(self):
        """Gets the link_status of this NodeInterfaceProperties.  # noqa: E501

        Interface administration status  # noqa: E501

        :return: The link_status of this NodeInterfaceProperties.  # noqa: E501
        :rtype: str
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        """Sets the link_status of this NodeInterfaceProperties.

        Interface administration status  # noqa: E501

        :param link_status: The link_status of this NodeInterfaceProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if link_status not in allowed_values:
            raise ValueError(
                "Invalid value for `link_status` ({0}), must be one of {1}"  # noqa: E501
                .format(link_status, allowed_values)
            )

        self._link_status = link_status

    @property
    def interface_alias(self):
        """Gets the interface_alias of this NodeInterfaceProperties.  # noqa: E501

        IP Alias  # noqa: E501

        :return: The interface_alias of this NodeInterfaceProperties.  # noqa: E501
        :rtype: list[NodeInterfaceAlias]
        """
        return self._interface_alias

    @interface_alias.setter
    def interface_alias(self, interface_alias):
        """Sets the interface_alias of this NodeInterfaceProperties.

        IP Alias  # noqa: E501

        :param interface_alias: The interface_alias of this NodeInterfaceProperties.  # noqa: E501
        :type: list[NodeInterfaceAlias]
        """

        self._interface_alias = interface_alias

    @property
    def ens_enabled(self):
        """Gets the ens_enabled of this NodeInterfaceProperties.  # noqa: E501

        Indicates whether interface is enabled for Enhanced Networking Stack  # noqa: E501

        :return: The ens_enabled of this NodeInterfaceProperties.  # noqa: E501
        :rtype: bool
        """
        return self._ens_enabled

    @ens_enabled.setter
    def ens_enabled(self, ens_enabled):
        """Sets the ens_enabled of this NodeInterfaceProperties.

        Indicates whether interface is enabled for Enhanced Networking Stack  # noqa: E501

        :param ens_enabled: The ens_enabled of this NodeInterfaceProperties.  # noqa: E501
        :type: bool
        """

        self._ens_enabled = ens_enabled

    @property
    def interface_type(self):
        """Gets the interface_type of this NodeInterfaceProperties.  # noqa: E501

        Interface Type  # noqa: E501

        :return: The interface_type of this NodeInterfaceProperties.  # noqa: E501
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this NodeInterfaceProperties.

        Interface Type  # noqa: E501

        :param interface_type: The interface_type of this NodeInterfaceProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHYSICAL", "VIRTUAL"]  # noqa: E501
        if interface_type not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_type` ({0}), must be one of {1}"  # noqa: E501
                .format(interface_type, allowed_values)
            )

        self._interface_type = interface_type

    @property
    def interface_id(self):
        """Gets the interface_id of this NodeInterfaceProperties.  # noqa: E501

        Interface ID  # noqa: E501

        :return: The interface_id of this NodeInterfaceProperties.  # noqa: E501
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this NodeInterfaceProperties.

        Interface ID  # noqa: E501

        :param interface_id: The interface_id of this NodeInterfaceProperties.  # noqa: E501
        :type: str
        """

        self._interface_id = interface_id

    @property
    def connected_switch(self):
        """Gets the connected_switch of this NodeInterfaceProperties.  # noqa: E501

        Connected switch  # noqa: E501

        :return: The connected_switch of this NodeInterfaceProperties.  # noqa: E501
        :rtype: str
        """
        return self._connected_switch

    @connected_switch.setter
    def connected_switch(self, connected_switch):
        """Sets the connected_switch of this NodeInterfaceProperties.

        Connected switch  # noqa: E501

        :param connected_switch: The connected_switch of this NodeInterfaceProperties.  # noqa: E501
        :type: str
        """

        self._connected_switch = connected_switch

    @property
    def ens_capable(self):
        """Gets the ens_capable of this NodeInterfaceProperties.  # noqa: E501

        Interface capability for Enhanced Networking Stack  # noqa: E501

        :return: The ens_capable of this NodeInterfaceProperties.  # noqa: E501
        :rtype: bool
        """
        return self._ens_capable

    @ens_capable.setter
    def ens_capable(self, ens_capable):
        """Sets the ens_capable of this NodeInterfaceProperties.

        Interface capability for Enhanced Networking Stack  # noqa: E501

        :param ens_capable: The ens_capable of this NodeInterfaceProperties.  # noqa: E501
        :type: bool
        """

        self._ens_capable = ens_capable

    @property
    def mtu(self):
        """Gets the mtu of this NodeInterfaceProperties.  # noqa: E501

        Interface MTU  # noqa: E501

        :return: The mtu of this NodeInterfaceProperties.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this NodeInterfaceProperties.

        Interface MTU  # noqa: E501

        :param mtu: The mtu of this NodeInterfaceProperties.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeInterfaceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
