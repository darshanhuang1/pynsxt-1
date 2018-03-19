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


class BatchResponseItem(object):
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
        'body': 'object',
        'headers': 'object',
        'code': 'int'
    }

    attribute_map = {
        'body': 'body',
        'headers': 'headers',
        'code': 'code'
    }

    def __init__(self, body=None, headers=None, code=None):  # noqa: E501
        """BatchResponseItem - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._headers = None
        self._code = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if headers is not None:
            self.headers = headers
        self.code = code

    @property
    def body(self):
        """Gets the body of this BatchResponseItem.  # noqa: E501

        object returned by api  # noqa: E501

        :return: The body of this BatchResponseItem.  # noqa: E501
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchResponseItem.

        object returned by api  # noqa: E501

        :param body: The body of this BatchResponseItem.  # noqa: E501
        :type: object
        """

        self._body = body

    @property
    def headers(self):
        """Gets the headers of this BatchResponseItem.  # noqa: E501

        The headers returned by the API call  # noqa: E501

        :return: The headers of this BatchResponseItem.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this BatchResponseItem.

        The headers returned by the API call  # noqa: E501

        :param headers: The headers of this BatchResponseItem.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def code(self):
        """Gets the code of this BatchResponseItem.  # noqa: E501

        http status code  # noqa: E501

        :return: The code of this BatchResponseItem.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BatchResponseItem.

        http status code  # noqa: E501

        :param code: The code of this BatchResponseItem.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, BatchResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
