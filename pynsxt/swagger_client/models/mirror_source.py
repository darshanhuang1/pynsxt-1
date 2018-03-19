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


class MirrorSource(object):
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
        'resource_type': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type'
    }

    discriminator_value_class_map = {
        'VlanMirrorSource': 'VlanMirrorSource',
        'PnicMirrorSource': 'PnicMirrorSource',
        'LogicalPortMirrorSource': 'LogicalPortMirrorSource'
    }

    def __init__(self, resource_type=None):  # noqa: E501
        """MirrorSource - a model defined in Swagger"""  # noqa: E501

        self._resource_type = None
        self.discriminator = 'resource_type'

        self.resource_type = resource_type

    @property
    def resource_type(self):
        """Gets the resource_type of this MirrorSource.  # noqa: E501

        Resource types of mirror source  # noqa: E501

        :return: The resource_type of this MirrorSource.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MirrorSource.

        Resource types of mirror source  # noqa: E501

        :param resource_type: The resource_type of this MirrorSource.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LogicalPortMirrorSource", "PnicMirrorSource", "VlanMirrorSource"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, MirrorSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
