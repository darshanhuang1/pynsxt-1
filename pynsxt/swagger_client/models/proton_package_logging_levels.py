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


class ProtonPackageLoggingLevels(object):
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
        'logging_level': 'str',
        'package_name': 'str'
    }

    attribute_map = {
        'logging_level': 'logging_level',
        'package_name': 'package_name'
    }

    def __init__(self, logging_level=None, package_name=None):  # noqa: E501
        """ProtonPackageLoggingLevels - a model defined in Swagger"""  # noqa: E501

        self._logging_level = None
        self._package_name = None
        self.discriminator = None

        if logging_level is not None:
            self.logging_level = logging_level
        if package_name is not None:
            self.package_name = package_name

    @property
    def logging_level(self):
        """Gets the logging_level of this ProtonPackageLoggingLevels.  # noqa: E501

        Logging levels per package  # noqa: E501

        :return: The logging_level of this ProtonPackageLoggingLevels.  # noqa: E501
        :rtype: str
        """
        return self._logging_level

    @logging_level.setter
    def logging_level(self, logging_level):
        """Sets the logging_level of this ProtonPackageLoggingLevels.

        Logging levels per package  # noqa: E501

        :param logging_level: The logging_level of this ProtonPackageLoggingLevels.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "WARN", "INFO", "DEBUG", "TRACE"]  # noqa: E501
        if logging_level not in allowed_values:
            raise ValueError(
                "Invalid value for `logging_level` ({0}), must be one of {1}"  # noqa: E501
                .format(logging_level, allowed_values)
            )

        self._logging_level = logging_level

    @property
    def package_name(self):
        """Gets the package_name of this ProtonPackageLoggingLevels.  # noqa: E501

        Package name  # noqa: E501

        :return: The package_name of this ProtonPackageLoggingLevels.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ProtonPackageLoggingLevels.

        Package name  # noqa: E501

        :param package_name: The package_name of this ProtonPackageLoggingLevels.  # noqa: E501
        :type: str
        """

        self._package_name = package_name

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
        if not isinstance(other, ProtonPackageLoggingLevels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
