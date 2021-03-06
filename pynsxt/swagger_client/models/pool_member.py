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


class PoolMember(object):
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
        'max_concurrent_connections': 'int',
        'admin_state': 'str',
        'backup_member': 'bool',
        'weight': 'int',
        'display_name': 'str',
        'ip_address': 'str',
        'port': 'str'
    }

    attribute_map = {
        'max_concurrent_connections': 'max_concurrent_connections',
        'admin_state': 'admin_state',
        'backup_member': 'backup_member',
        'weight': 'weight',
        'display_name': 'display_name',
        'ip_address': 'ip_address',
        'port': 'port'
    }

    def __init__(self, max_concurrent_connections=None, admin_state='ENABLED', backup_member=False, weight=1, display_name=None, ip_address=None, port=None):  # noqa: E501
        """PoolMember - a model defined in Swagger"""  # noqa: E501

        self._max_concurrent_connections = None
        self._admin_state = None
        self._backup_member = None
        self._weight = None
        self._display_name = None
        self._ip_address = None
        self._port = None
        self.discriminator = None

        if max_concurrent_connections is not None:
            self.max_concurrent_connections = max_concurrent_connections
        if admin_state is not None:
            self.admin_state = admin_state
        if backup_member is not None:
            self.backup_member = backup_member
        if weight is not None:
            self.weight = weight
        if display_name is not None:
            self.display_name = display_name
        self.ip_address = ip_address
        if port is not None:
            self.port = port

    @property
    def max_concurrent_connections(self):
        """Gets the max_concurrent_connections of this PoolMember.  # noqa: E501

        To ensure members are not overloaded, connections to a member can be capped by the load balancer. When a member reaches this limit, it is skipped during server selection. If it is not specified, it means that connections are unlimited.   # noqa: E501

        :return: The max_concurrent_connections of this PoolMember.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrent_connections

    @max_concurrent_connections.setter
    def max_concurrent_connections(self, max_concurrent_connections):
        """Sets the max_concurrent_connections of this PoolMember.

        To ensure members are not overloaded, connections to a member can be capped by the load balancer. When a member reaches this limit, it is skipped during server selection. If it is not specified, it means that connections are unlimited.   # noqa: E501

        :param max_concurrent_connections: The max_concurrent_connections of this PoolMember.  # noqa: E501
        :type: int
        """
        if max_concurrent_connections is not None and max_concurrent_connections < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_concurrent_connections`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_concurrent_connections = max_concurrent_connections

    @property
    def admin_state(self):
        """Gets the admin_state of this PoolMember.  # noqa: E501

        member admin state  # noqa: E501

        :return: The admin_state of this PoolMember.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this PoolMember.

        member admin state  # noqa: E501

        :param admin_state: The admin_state of this PoolMember.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "GRACEFUL_DISABLED"]  # noqa: E501
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def backup_member(self):
        """Gets the backup_member of this PoolMember.  # noqa: E501

        Backup servers are typically configured with a sorry page indicating to the user that the application is currently unavailable. While the pool is active (a specified minimum number of pool members are active) BACKUP members are skipped during server selection. When the pool is inactive, incoming connections are sent to only the BACKUP member(s).   # noqa: E501

        :return: The backup_member of this PoolMember.  # noqa: E501
        :rtype: bool
        """
        return self._backup_member

    @backup_member.setter
    def backup_member(self, backup_member):
        """Sets the backup_member of this PoolMember.

        Backup servers are typically configured with a sorry page indicating to the user that the application is currently unavailable. While the pool is active (a specified minimum number of pool members are active) BACKUP members are skipped during server selection. When the pool is inactive, incoming connections are sent to only the BACKUP member(s).   # noqa: E501

        :param backup_member: The backup_member of this PoolMember.  # noqa: E501
        :type: bool
        """

        self._backup_member = backup_member

    @property
    def weight(self):
        """Gets the weight of this PoolMember.  # noqa: E501

        Pool member weight is used for WEIGHTED_ROUND_ROBIN balancing algorithm. The weight value would be ignored in other algorithms.   # noqa: E501

        :return: The weight of this PoolMember.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PoolMember.

        Pool member weight is used for WEIGHTED_ROUND_ROBIN balancing algorithm. The weight value would be ignored in other algorithms.   # noqa: E501

        :param weight: The weight of this PoolMember.  # noqa: E501
        :type: int
        """
        if weight is not None and weight > 255:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must be a value less than or equal to `255`")  # noqa: E501
        if weight is not None and weight < 1:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must be a value greater than or equal to `1`")  # noqa: E501

        self._weight = weight

    @property
    def display_name(self):
        """Gets the display_name of this PoolMember.  # noqa: E501

        pool member name  # noqa: E501

        :return: The display_name of this PoolMember.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PoolMember.

        pool member name  # noqa: E501

        :param display_name: The display_name of this PoolMember.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def ip_address(self):
        """Gets the ip_address of this PoolMember.  # noqa: E501

        pool member IP address  # noqa: E501

        :return: The ip_address of this PoolMember.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PoolMember.

        pool member IP address  # noqa: E501

        :param ip_address: The ip_address of this PoolMember.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def port(self):
        """Gets the port of this PoolMember.  # noqa: E501

        If port is specified, all connections will be sent to this port. Only single port is supported. If unset, the same port the client connected to will be used, it could be overrode by default_pool_member_port setting in virtual server. The port should not specified for port range case.   # noqa: E501

        :return: The port of this PoolMember.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PoolMember.

        If port is specified, all connections will be sent to this port. Only single port is supported. If unset, the same port the client connected to will be used, it could be overrode by default_pool_member_port setting in virtual server. The port should not specified for port range case.   # noqa: E501

        :param port: The port of this PoolMember.  # noqa: E501
        :type: str
        """

        self._port = port

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
        if not isinstance(other, PoolMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
