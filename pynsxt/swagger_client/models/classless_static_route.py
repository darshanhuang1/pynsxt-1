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


class ClasslessStaticRoute(object):
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
        'next_hop': 'str',
        'network': 'str'
    }

    attribute_map = {
        'next_hop': 'next_hop',
        'network': 'network'
    }

    def __init__(self, next_hop=None, network=None):  # noqa: E501
        """ClasslessStaticRoute - a model defined in Swagger"""  # noqa: E501

        self._next_hop = None
        self._network = None
        self.discriminator = None

        self.next_hop = next_hop
        self.network = network

    @property
    def next_hop(self):
        """Gets the next_hop of this ClasslessStaticRoute.  # noqa: E501

        router  # noqa: E501

        :return: The next_hop of this ClasslessStaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._next_hop

    @next_hop.setter
    def next_hop(self, next_hop):
        """Sets the next_hop of this ClasslessStaticRoute.

        router  # noqa: E501

        :param next_hop: The next_hop of this ClasslessStaticRoute.  # noqa: E501
        :type: str
        """
        if next_hop is None:
            raise ValueError("Invalid value for `next_hop`, must not be `None`")  # noqa: E501

        self._next_hop = next_hop

    @property
    def network(self):
        """Gets the network of this ClasslessStaticRoute.  # noqa: E501

        destination in cidr  # noqa: E501

        :return: The network of this ClasslessStaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this ClasslessStaticRoute.

        destination in cidr  # noqa: E501

        :param network: The network of this ClasslessStaticRoute.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

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
        if not isinstance(other, ClasslessStaticRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
