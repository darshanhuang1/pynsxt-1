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


class LogicalRouterPortCounters(object):
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
        'dropped_packets': 'int',
        'total_bytes': 'int',
        'total_packets': 'int'
    }

    attribute_map = {
        'dropped_packets': 'dropped_packets',
        'total_bytes': 'total_bytes',
        'total_packets': 'total_packets'
    }

    def __init__(self, dropped_packets=None, total_bytes=None, total_packets=None):  # noqa: E501
        """LogicalRouterPortCounters - a model defined in Swagger"""  # noqa: E501

        self._dropped_packets = None
        self._total_bytes = None
        self._total_packets = None
        self.discriminator = None

        if dropped_packets is not None:
            self.dropped_packets = dropped_packets
        if total_bytes is not None:
            self.total_bytes = total_bytes
        if total_packets is not None:
            self.total_packets = total_packets

    @property
    def dropped_packets(self):
        """Gets the dropped_packets of this LogicalRouterPortCounters.  # noqa: E501

        The number of dropped packets  # noqa: E501

        :return: The dropped_packets of this LogicalRouterPortCounters.  # noqa: E501
        :rtype: int
        """
        return self._dropped_packets

    @dropped_packets.setter
    def dropped_packets(self, dropped_packets):
        """Sets the dropped_packets of this LogicalRouterPortCounters.

        The number of dropped packets  # noqa: E501

        :param dropped_packets: The dropped_packets of this LogicalRouterPortCounters.  # noqa: E501
        :type: int
        """

        self._dropped_packets = dropped_packets

    @property
    def total_bytes(self):
        """Gets the total_bytes of this LogicalRouterPortCounters.  # noqa: E501

        The total number of bytes  # noqa: E501

        :return: The total_bytes of this LogicalRouterPortCounters.  # noqa: E501
        :rtype: int
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this LogicalRouterPortCounters.

        The total number of bytes  # noqa: E501

        :param total_bytes: The total_bytes of this LogicalRouterPortCounters.  # noqa: E501
        :type: int
        """

        self._total_bytes = total_bytes

    @property
    def total_packets(self):
        """Gets the total_packets of this LogicalRouterPortCounters.  # noqa: E501

        The total number of packets  # noqa: E501

        :return: The total_packets of this LogicalRouterPortCounters.  # noqa: E501
        :rtype: int
        """
        return self._total_packets

    @total_packets.setter
    def total_packets(self, total_packets):
        """Sets the total_packets of this LogicalRouterPortCounters.

        The total number of packets  # noqa: E501

        :param total_packets: The total_packets of this LogicalRouterPortCounters.  # noqa: E501
        :type: int
        """

        self._total_packets = total_packets

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
        if not isinstance(other, LogicalRouterPortCounters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
