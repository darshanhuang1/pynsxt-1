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


class Dscp(object):
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
        'priority': 'int',
        'mode': 'str'
    }

    attribute_map = {
        'priority': 'priority',
        'mode': 'mode'
    }

    def __init__(self, priority=0, mode=None):  # noqa: E501
        """Dscp - a model defined in Swagger"""  # noqa: E501

        self._priority = None
        self._mode = None
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if mode is not None:
            self.mode = mode

    @property
    def priority(self):
        """Gets the priority of this Dscp.  # noqa: E501

        Internal Forwarding Priority  # noqa: E501

        :return: The priority of this Dscp.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Dscp.

        Internal Forwarding Priority  # noqa: E501

        :param priority: The priority of this Dscp.  # noqa: E501
        :type: int
        """
        if priority is not None and priority > 63:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `63`")  # noqa: E501
        if priority is not None and priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._priority = priority

    @property
    def mode(self):
        """Gets the mode of this Dscp.  # noqa: E501

        Trust settings  # noqa: E501

        :return: The mode of this Dscp.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Dscp.

        Trust settings  # noqa: E501

        :param mode: The mode of this Dscp.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRUSTED", "UNTRUSTED"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

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
        if not isinstance(other, Dscp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
