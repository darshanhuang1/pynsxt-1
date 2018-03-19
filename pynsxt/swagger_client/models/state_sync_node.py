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


class StateSyncNode(object):
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
        'cluster_node_id': 'str',
        'api_listen_ip': 'str'
    }

    attribute_map = {
        'cluster_node_id': 'cluster_node_id',
        'api_listen_ip': 'api_listen_ip'
    }

    def __init__(self, cluster_node_id=None, api_listen_ip=None):  # noqa: E501
        """StateSyncNode - a model defined in Swagger"""  # noqa: E501

        self._cluster_node_id = None
        self._api_listen_ip = None
        self.discriminator = None

        if cluster_node_id is not None:
            self.cluster_node_id = cluster_node_id
        if api_listen_ip is not None:
            self.api_listen_ip = api_listen_ip

    @property
    def cluster_node_id(self):
        """Gets the cluster_node_id of this StateSyncNode.  # noqa: E501

        Internal identifier provided by the node  # noqa: E501

        :return: The cluster_node_id of this StateSyncNode.  # noqa: E501
        :rtype: str
        """
        return self._cluster_node_id

    @cluster_node_id.setter
    def cluster_node_id(self, cluster_node_id):
        """Sets the cluster_node_id of this StateSyncNode.

        Internal identifier provided by the node  # noqa: E501

        :param cluster_node_id: The cluster_node_id of this StateSyncNode.  # noqa: E501
        :type: str
        """

        self._cluster_node_id = cluster_node_id

    @property
    def api_listen_ip(self):
        """Gets the api_listen_ip of this StateSyncNode.  # noqa: E501

        The IP and port for the public API service on this node  # noqa: E501

        :return: The api_listen_ip of this StateSyncNode.  # noqa: E501
        :rtype: str
        """
        return self._api_listen_ip

    @api_listen_ip.setter
    def api_listen_ip(self, api_listen_ip):
        """Sets the api_listen_ip of this StateSyncNode.

        The IP and port for the public API service on this node  # noqa: E501

        :param api_listen_ip: The api_listen_ip of this StateSyncNode.  # noqa: E501
        :type: str
        """

        self._api_listen_ip = api_listen_ip

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
        if not isinstance(other, StateSyncNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other