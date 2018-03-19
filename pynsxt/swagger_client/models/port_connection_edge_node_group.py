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

from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501
from swagger_client.models.port_connection_entity import PortConnectionEntity  # noqa: F401,E501
from swagger_client.models.transport_node import TransportNode  # noqa: F401,E501


class PortConnectionEdgeNodeGroup(object):
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
        'resource': 'ManagedResource',
        'id': 'str',
        'edge_nodes': 'list[TransportNode]',
        'logical_router_id': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'id': 'id',
        'edge_nodes': 'edge_nodes',
        'logical_router_id': 'logical_router_id'
    }

    def __init__(self, resource=None, id=None, edge_nodes=None, logical_router_id=None):  # noqa: E501
        """PortConnectionEdgeNodeGroup - a model defined in Swagger"""  # noqa: E501

        self._resource = None
        self._id = None
        self._edge_nodes = None
        self._logical_router_id = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if id is not None:
            self.id = id
        if edge_nodes is not None:
            self.edge_nodes = edge_nodes
        self.logical_router_id = logical_router_id

    @property
    def resource(self):
        """Gets the resource of this PortConnectionEdgeNodeGroup.  # noqa: E501

        Resource reference with details of the entity  # noqa: E501

        :return: The resource of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :rtype: ManagedResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this PortConnectionEdgeNodeGroup.

        Resource reference with details of the entity  # noqa: E501

        :param resource: The resource of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :type: ManagedResource
        """

        self._resource = resource

    @property
    def id(self):
        """Gets the id of this PortConnectionEdgeNodeGroup.  # noqa: E501

        Resource ID is mapped to this. (ID is Generated for Edge node groups, since resource will be null)  # noqa: E501

        :return: The id of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortConnectionEdgeNodeGroup.

        Resource ID is mapped to this. (ID is Generated for Edge node groups, since resource will be null)  # noqa: E501

        :param id: The id of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def edge_nodes(self):
        """Gets the edge_nodes of this PortConnectionEdgeNodeGroup.  # noqa: E501


        :return: The edge_nodes of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :rtype: list[TransportNode]
        """
        return self._edge_nodes

    @edge_nodes.setter
    def edge_nodes(self, edge_nodes):
        """Sets the edge_nodes of this PortConnectionEdgeNodeGroup.


        :param edge_nodes: The edge_nodes of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :type: list[TransportNode]
        """

        self._edge_nodes = edge_nodes

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this PortConnectionEdgeNodeGroup.  # noqa: E501

        Id of the logical router  # noqa: E501

        :return: The logical_router_id of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this PortConnectionEdgeNodeGroup.

        Id of the logical router  # noqa: E501

        :param logical_router_id: The logical_router_id of this PortConnectionEdgeNodeGroup.  # noqa: E501
        :type: str
        """
        if logical_router_id is None:
            raise ValueError("Invalid value for `logical_router_id`, must not be `None`")  # noqa: E501

        self._logical_router_id = logical_router_id

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
        if not isinstance(other, PortConnectionEdgeNodeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other