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

from swagger_client.models.controller_node_aggregate_info import ControllerNodeAggregateInfo  # noqa: F401,E501
from swagger_client.models.management_node_aggregate_info import ManagementNodeAggregateInfo  # noqa: F401,E501


class ClustersAggregateInfo(object):
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
        'management_cluster': 'list[ManagementNodeAggregateInfo]',
        'controller_cluster': 'list[ControllerNodeAggregateInfo]'
    }

    attribute_map = {
        'management_cluster': 'management_cluster',
        'controller_cluster': 'controller_cluster'
    }

    def __init__(self, management_cluster=None, controller_cluster=None):  # noqa: E501
        """ClustersAggregateInfo - a model defined in Swagger"""  # noqa: E501

        self._management_cluster = None
        self._controller_cluster = None
        self.discriminator = None

        self.management_cluster = management_cluster
        self.controller_cluster = controller_cluster

    @property
    def management_cluster(self):
        """Gets the management_cluster of this ClustersAggregateInfo.  # noqa: E501

        Array of Management Nodes  # noqa: E501

        :return: The management_cluster of this ClustersAggregateInfo.  # noqa: E501
        :rtype: list[ManagementNodeAggregateInfo]
        """
        return self._management_cluster

    @management_cluster.setter
    def management_cluster(self, management_cluster):
        """Sets the management_cluster of this ClustersAggregateInfo.

        Array of Management Nodes  # noqa: E501

        :param management_cluster: The management_cluster of this ClustersAggregateInfo.  # noqa: E501
        :type: list[ManagementNodeAggregateInfo]
        """
        if management_cluster is None:
            raise ValueError("Invalid value for `management_cluster`, must not be `None`")  # noqa: E501

        self._management_cluster = management_cluster

    @property
    def controller_cluster(self):
        """Gets the controller_cluster of this ClustersAggregateInfo.  # noqa: E501

        Array of Controller Nodes  # noqa: E501

        :return: The controller_cluster of this ClustersAggregateInfo.  # noqa: E501
        :rtype: list[ControllerNodeAggregateInfo]
        """
        return self._controller_cluster

    @controller_cluster.setter
    def controller_cluster(self, controller_cluster):
        """Sets the controller_cluster of this ClustersAggregateInfo.

        Array of Controller Nodes  # noqa: E501

        :param controller_cluster: The controller_cluster of this ClustersAggregateInfo.  # noqa: E501
        :type: list[ControllerNodeAggregateInfo]
        """
        if controller_cluster is None:
            raise ValueError("Invalid value for `controller_cluster`, must not be `None`")  # noqa: E501

        self._controller_cluster = controller_cluster

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
        if not isinstance(other, ClustersAggregateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
