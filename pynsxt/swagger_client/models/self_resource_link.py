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

from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501


class SelfResourceLink(object):
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
        'action': 'str',
        'href': 'str',
        'rel': 'str'
    }

    attribute_map = {
        'action': 'action',
        'href': 'href',
        'rel': 'rel'
    }

    def __init__(self, action=None, href=None, rel=None):  # noqa: E501
        """SelfResourceLink - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._href = None
        self._rel = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel

    @property
    def action(self):
        """Gets the action of this SelfResourceLink.  # noqa: E501

        Optional action  # noqa: E501

        :return: The action of this SelfResourceLink.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SelfResourceLink.

        Optional action  # noqa: E501

        :param action: The action of this SelfResourceLink.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def href(self):
        """Gets the href of this SelfResourceLink.  # noqa: E501


        :return: The href of this SelfResourceLink.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SelfResourceLink.


        :param href: The href of this SelfResourceLink.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def rel(self):
        """Gets the rel of this SelfResourceLink.  # noqa: E501

        Custom relation type (follows RFC 5988 where appropriate definitions exist)  # noqa: E501

        :return: The rel of this SelfResourceLink.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this SelfResourceLink.

        Custom relation type (follows RFC 5988 where appropriate definitions exist)  # noqa: E501

        :param rel: The rel of this SelfResourceLink.  # noqa: E501
        :type: str
        """

        self._rel = rel

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
        if not isinstance(other, SelfResourceLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
