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

from swagger_client.models.logical_router_port_statistics_per_node import LogicalRouterPortStatisticsPerNode  # noqa: F401,E501


class LogicalRouterPortStatistics(object):
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
        'per_node_statistics': 'list[LogicalRouterPortStatisticsPerNode]',
        'logical_router_port_id': 'str'
    }

    attribute_map = {
        'per_node_statistics': 'per_node_statistics',
        'logical_router_port_id': 'logical_router_port_id'
    }

    def __init__(self, per_node_statistics=None, logical_router_port_id=None):  # noqa: E501
        """LogicalRouterPortStatistics - a model defined in Swagger"""  # noqa: E501

        self._per_node_statistics = None
        self._logical_router_port_id = None
        self.discriminator = None

        if per_node_statistics is not None:
            self.per_node_statistics = per_node_statistics
        self.logical_router_port_id = logical_router_port_id

    @property
    def per_node_statistics(self):
        """Gets the per_node_statistics of this LogicalRouterPortStatistics.  # noqa: E501

        Per Node Statistics  # noqa: E501

        :return: The per_node_statistics of this LogicalRouterPortStatistics.  # noqa: E501
        :rtype: list[LogicalRouterPortStatisticsPerNode]
        """
        return self._per_node_statistics

    @per_node_statistics.setter
    def per_node_statistics(self, per_node_statistics):
        """Sets the per_node_statistics of this LogicalRouterPortStatistics.

        Per Node Statistics  # noqa: E501

        :param per_node_statistics: The per_node_statistics of this LogicalRouterPortStatistics.  # noqa: E501
        :type: list[LogicalRouterPortStatisticsPerNode]
        """

        self._per_node_statistics = per_node_statistics

    @property
    def logical_router_port_id(self):
        """Gets the logical_router_port_id of this LogicalRouterPortStatistics.  # noqa: E501

        The ID of the logical router port  # noqa: E501

        :return: The logical_router_port_id of this LogicalRouterPortStatistics.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_port_id

    @logical_router_port_id.setter
    def logical_router_port_id(self, logical_router_port_id):
        """Sets the logical_router_port_id of this LogicalRouterPortStatistics.

        The ID of the logical router port  # noqa: E501

        :param logical_router_port_id: The logical_router_port_id of this LogicalRouterPortStatistics.  # noqa: E501
        :type: str
        """
        if logical_router_port_id is None:
            raise ValueError("Invalid value for `logical_router_port_id`, must not be `None`")  # noqa: E501

        self._logical_router_port_id = logical_router_port_id

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
        if not isinstance(other, LogicalRouterPortStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
