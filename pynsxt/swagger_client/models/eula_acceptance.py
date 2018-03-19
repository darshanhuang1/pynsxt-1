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


class EULAAcceptance(object):
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
        'acceptance': 'bool'
    }

    attribute_map = {
        'acceptance': 'acceptance'
    }

    def __init__(self, acceptance=None):  # noqa: E501
        """EULAAcceptance - a model defined in Swagger"""  # noqa: E501

        self._acceptance = None
        self.discriminator = None

        self.acceptance = acceptance

    @property
    def acceptance(self):
        """Gets the acceptance of this EULAAcceptance.  # noqa: E501

        End User License Agreement acceptance status  # noqa: E501

        :return: The acceptance of this EULAAcceptance.  # noqa: E501
        :rtype: bool
        """
        return self._acceptance

    @acceptance.setter
    def acceptance(self, acceptance):
        """Sets the acceptance of this EULAAcceptance.

        End User License Agreement acceptance status  # noqa: E501

        :param acceptance: The acceptance of this EULAAcceptance.  # noqa: E501
        :type: bool
        """
        if acceptance is None:
            raise ValueError("Invalid value for `acceptance`, must not be `None`")  # noqa: E501

        self._acceptance = acceptance

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
        if not isinstance(other, EULAAcceptance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other