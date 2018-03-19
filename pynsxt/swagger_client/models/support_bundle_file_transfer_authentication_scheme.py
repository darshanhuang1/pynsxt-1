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


class SupportBundleFileTransferAuthenticationScheme(object):
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
        'username': 'str',
        'scheme_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'username': 'username',
        'scheme_name': 'scheme_name',
        'password': 'password'
    }

    def __init__(self, username=None, scheme_name=None, password=None):  # noqa: E501
        """SupportBundleFileTransferAuthenticationScheme - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._scheme_name = None
        self._password = None
        self.discriminator = None

        self.username = username
        self.scheme_name = scheme_name
        self.password = password

    @property
    def username(self):
        """Gets the username of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501

        User name to authenticate with  # noqa: E501

        :return: The username of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SupportBundleFileTransferAuthenticationScheme.

        User name to authenticate with  # noqa: E501

        :param username: The username of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def scheme_name(self):
        """Gets the scheme_name of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501

        Authentication scheme name  # noqa: E501

        :return: The scheme_name of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501
        :rtype: str
        """
        return self._scheme_name

    @scheme_name.setter
    def scheme_name(self, scheme_name):
        """Sets the scheme_name of this SupportBundleFileTransferAuthenticationScheme.

        Authentication scheme name  # noqa: E501

        :param scheme_name: The scheme_name of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501
        :type: str
        """
        if scheme_name is None:
            raise ValueError("Invalid value for `scheme_name`, must not be `None`")  # noqa: E501
        allowed_values = ["PASSWORD"]  # noqa: E501
        if scheme_name not in allowed_values:
            raise ValueError(
                "Invalid value for `scheme_name` ({0}), must be one of {1}"  # noqa: E501
                .format(scheme_name, allowed_values)
            )

        self._scheme_name = scheme_name

    @property
    def password(self):
        """Gets the password of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501

        Password to authenticate with  # noqa: E501

        :return: The password of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SupportBundleFileTransferAuthenticationScheme.

        Password to authenticate with  # noqa: E501

        :param password: The password of this SupportBundleFileTransferAuthenticationScheme.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if not isinstance(other, SupportBundleFileTransferAuthenticationScheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
