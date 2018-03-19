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

from swagger_client.models.base_switching_profile import BaseSwitchingProfile  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class PortMirroringSwitchingProfile(object):
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
        'snap_length': 'int',
        'direction': 'str',
        'key': 'int',
        'destinations': 'list[str]'
    }

    attribute_map = {
        'snap_length': 'snap_length',
        'direction': 'direction',
        'key': 'key',
        'destinations': 'destinations'
    }

    def __init__(self, snap_length=None, direction=None, key=None, destinations=None):  # noqa: E501
        """PortMirroringSwitchingProfile - a model defined in Swagger"""  # noqa: E501

        self._snap_length = None
        self._direction = None
        self._key = None
        self._destinations = None
        self.discriminator = None

        if snap_length is not None:
            self.snap_length = snap_length
        if direction is not None:
            self.direction = direction
        if key is not None:
            self.key = key
        if destinations is not None:
            self.destinations = destinations

    @property
    def snap_length(self):
        """Gets the snap_length of this PortMirroringSwitchingProfile.  # noqa: E501

        If this property not set, original package will not be truncated.  # noqa: E501

        :return: The snap_length of this PortMirroringSwitchingProfile.  # noqa: E501
        :rtype: int
        """
        return self._snap_length

    @snap_length.setter
    def snap_length(self, snap_length):
        """Sets the snap_length of this PortMirroringSwitchingProfile.

        If this property not set, original package will not be truncated.  # noqa: E501

        :param snap_length: The snap_length of this PortMirroringSwitchingProfile.  # noqa: E501
        :type: int
        """
        if snap_length is not None and snap_length > 65535:  # noqa: E501
            raise ValueError("Invalid value for `snap_length`, must be a value less than or equal to `65535`")  # noqa: E501
        if snap_length is not None and snap_length < 60:  # noqa: E501
            raise ValueError("Invalid value for `snap_length`, must be a value greater than or equal to `60`")  # noqa: E501

        self._snap_length = snap_length

    @property
    def direction(self):
        """Gets the direction of this PortMirroringSwitchingProfile.  # noqa: E501

        port mirroring direction  # noqa: E501

        :return: The direction of this PortMirroringSwitchingProfile.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this PortMirroringSwitchingProfile.

        port mirroring direction  # noqa: E501

        :param direction: The direction of this PortMirroringSwitchingProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["INGRESS", "EGRESS", "BIDIRECTIONAL"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def key(self):
        """Gets the key of this PortMirroringSwitchingProfile.  # noqa: E501

        User-configurable 32-bit key  # noqa: E501

        :return: The key of this PortMirroringSwitchingProfile.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PortMirroringSwitchingProfile.

        User-configurable 32-bit key  # noqa: E501

        :param key: The key of this PortMirroringSwitchingProfile.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def destinations(self):
        """Gets the destinations of this PortMirroringSwitchingProfile.  # noqa: E501

        List of destination addresses  # noqa: E501

        :return: The destinations of this PortMirroringSwitchingProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this PortMirroringSwitchingProfile.

        List of destination addresses  # noqa: E501

        :param destinations: The destinations of this PortMirroringSwitchingProfile.  # noqa: E501
        :type: list[str]
        """

        self._destinations = destinations

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
        if not isinstance(other, PortMirroringSwitchingProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
