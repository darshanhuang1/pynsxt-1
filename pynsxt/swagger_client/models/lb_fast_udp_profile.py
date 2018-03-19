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

from swagger_client.models.lb_app_profile import LbAppProfile  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class LbFastUdpProfile(object):
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
        'idle_timeout': 'int',
        'flow_mirroring_enabled': 'bool'
    }

    attribute_map = {
        'idle_timeout': 'idle_timeout',
        'flow_mirroring_enabled': 'flow_mirroring_enabled'
    }

    def __init__(self, idle_timeout=300, flow_mirroring_enabled=False):  # noqa: E501
        """LbFastUdpProfile - a model defined in Swagger"""  # noqa: E501

        self._idle_timeout = None
        self._flow_mirroring_enabled = None
        self.discriminator = None

        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if flow_mirroring_enabled is not None:
            self.flow_mirroring_enabled = flow_mirroring_enabled

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this LbFastUdpProfile.  # noqa: E501

        Though UDP is a connectionless protocol, for the purposes of load balancing, all UDP packets with the same flow signature (source and destination IP/ports and IP protocol) received within the idle timeout period are considered to belong to the same connection and are sent to the same backend server. If no packets are received for idle timeout period, the connection (association between flow signature and the selected server) is cleaned up.   # noqa: E501

        :return: The idle_timeout of this LbFastUdpProfile.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this LbFastUdpProfile.

        Though UDP is a connectionless protocol, for the purposes of load balancing, all UDP packets with the same flow signature (source and destination IP/ports and IP protocol) received within the idle timeout period are considered to belong to the same connection and are sent to the same backend server. If no packets are received for idle timeout period, the connection (association between flow signature and the selected server) is cleaned up.   # noqa: E501

        :param idle_timeout: The idle_timeout of this LbFastUdpProfile.  # noqa: E501
        :type: int
        """
        if idle_timeout is not None and idle_timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `idle_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._idle_timeout = idle_timeout

    @property
    def flow_mirroring_enabled(self):
        """Gets the flow_mirroring_enabled of this LbFastUdpProfile.  # noqa: E501

        If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.   # noqa: E501

        :return: The flow_mirroring_enabled of this LbFastUdpProfile.  # noqa: E501
        :rtype: bool
        """
        return self._flow_mirroring_enabled

    @flow_mirroring_enabled.setter
    def flow_mirroring_enabled(self, flow_mirroring_enabled):
        """Sets the flow_mirroring_enabled of this LbFastUdpProfile.

        If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.   # noqa: E501

        :param flow_mirroring_enabled: The flow_mirroring_enabled of this LbFastUdpProfile.  # noqa: E501
        :type: bool
        """

        self._flow_mirroring_enabled = flow_mirroring_enabled

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
        if not isinstance(other, LbFastUdpProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other