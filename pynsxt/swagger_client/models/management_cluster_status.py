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

from swagger_client.models.cluster_initialization_node_info import ClusterInitializationNodeInfo  # noqa: F401,E501
from swagger_client.models.management_plane_base_node_info import ManagementPlaneBaseNodeInfo  # noqa: F401,E501


class ManagementClusterStatus(object):
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
        'status': 'str',
        'offline_nodes': 'list[ManagementPlaneBaseNodeInfo]',
        'required_members_for_initialization': 'list[ClusterInitializationNodeInfo]',
        'online_nodes': 'list[ManagementPlaneBaseNodeInfo]'
    }

    attribute_map = {
        'status': 'status',
        'offline_nodes': 'offline_nodes',
        'required_members_for_initialization': 'required_members_for_initialization',
        'online_nodes': 'online_nodes'
    }

    def __init__(self, status=None, offline_nodes=None, required_members_for_initialization=None, online_nodes=None):  # noqa: E501
        """ManagementClusterStatus - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._offline_nodes = None
        self._required_members_for_initialization = None
        self._online_nodes = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if offline_nodes is not None:
            self.offline_nodes = offline_nodes
        if required_members_for_initialization is not None:
            self.required_members_for_initialization = required_members_for_initialization
        if online_nodes is not None:
            self.online_nodes = online_nodes

    @property
    def status(self):
        """Gets the status of this ManagementClusterStatus.  # noqa: E501

        The current status of the management cluster  # noqa: E501

        :return: The status of this ManagementClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ManagementClusterStatus.

        The current status of the management cluster  # noqa: E501

        :param status: The status of this ManagementClusterStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["INITIALIZING", "UNSTABLE", "STABLE", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def offline_nodes(self):
        """Gets the offline_nodes of this ManagementClusterStatus.  # noqa: E501

        Current missing management plane nodes  # noqa: E501

        :return: The offline_nodes of this ManagementClusterStatus.  # noqa: E501
        :rtype: list[ManagementPlaneBaseNodeInfo]
        """
        return self._offline_nodes

    @offline_nodes.setter
    def offline_nodes(self, offline_nodes):
        """Sets the offline_nodes of this ManagementClusterStatus.

        Current missing management plane nodes  # noqa: E501

        :param offline_nodes: The offline_nodes of this ManagementClusterStatus.  # noqa: E501
        :type: list[ManagementPlaneBaseNodeInfo]
        """

        self._offline_nodes = offline_nodes

    @property
    def required_members_for_initialization(self):
        """Gets the required_members_for_initialization of this ManagementClusterStatus.  # noqa: E501

        The details of the cluster nodes required for cluster initialization  # noqa: E501

        :return: The required_members_for_initialization of this ManagementClusterStatus.  # noqa: E501
        :rtype: list[ClusterInitializationNodeInfo]
        """
        return self._required_members_for_initialization

    @required_members_for_initialization.setter
    def required_members_for_initialization(self, required_members_for_initialization):
        """Sets the required_members_for_initialization of this ManagementClusterStatus.

        The details of the cluster nodes required for cluster initialization  # noqa: E501

        :param required_members_for_initialization: The required_members_for_initialization of this ManagementClusterStatus.  # noqa: E501
        :type: list[ClusterInitializationNodeInfo]
        """

        self._required_members_for_initialization = required_members_for_initialization

    @property
    def online_nodes(self):
        """Gets the online_nodes of this ManagementClusterStatus.  # noqa: E501

        Current alive management plane nodes  # noqa: E501

        :return: The online_nodes of this ManagementClusterStatus.  # noqa: E501
        :rtype: list[ManagementPlaneBaseNodeInfo]
        """
        return self._online_nodes

    @online_nodes.setter
    def online_nodes(self, online_nodes):
        """Sets the online_nodes of this ManagementClusterStatus.

        Current alive management plane nodes  # noqa: E501

        :param online_nodes: The online_nodes of this ManagementClusterStatus.  # noqa: E501
        :type: list[ManagementPlaneBaseNodeInfo]
        """

        self._online_nodes = online_nodes

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
        if not isinstance(other, ManagementClusterStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
