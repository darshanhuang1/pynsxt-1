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

from swagger_client.models.lb_rule_condition import LbRuleCondition  # noqa: F401,E501


class LbIpHeaderCondition(object):
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
        'source_address': 'str'
    }

    attribute_map = {
        'source_address': 'source_address'
    }

    def __init__(self, source_address=None):  # noqa: E501
        """LbIpHeaderCondition - a model defined in Swagger"""  # noqa: E501

        self._source_address = None
        self.discriminator = None

        self.source_address = source_address

    @property
    def source_address(self):
        """Gets the source_address of this LbIpHeaderCondition.  # noqa: E501

        Source IP address of HTTP message  # noqa: E501

        :return: The source_address of this LbIpHeaderCondition.  # noqa: E501
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """Sets the source_address of this LbIpHeaderCondition.

        Source IP address of HTTP message  # noqa: E501

        :param source_address: The source_address of this LbIpHeaderCondition.  # noqa: E501
        :type: str
        """
        if source_address is None:
            raise ValueError("Invalid value for `source_address`, must not be `None`")  # noqa: E501

        self._source_address = source_address

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
        if not isinstance(other, LbIpHeaderCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
