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


class QuickSearchRequest(object):
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
        'query': 'str',
        'group_count': 'int',
        'group_size': 'int'
    }

    attribute_map = {
        'query': 'query',
        'group_count': 'group_count',
        'group_size': 'group_size'
    }

    def __init__(self, query=None, group_count=10, group_size=5):  # noqa: E501
        """QuickSearchRequest - a model defined in Swagger"""  # noqa: E501

        self._query = None
        self._group_count = None
        self._group_size = None
        self.discriminator = None

        self.query = query
        if group_count is not None:
            self.group_count = group_count
        if group_size is not None:
            self.group_size = group_size

    @property
    def query(self):
        """Gets the query of this QuickSearchRequest.  # noqa: E501

        Search query  # noqa: E501

        :return: The query of this QuickSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QuickSearchRequest.

        Search query  # noqa: E501

        :param query: The query of this QuickSearchRequest.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def group_count(self):
        """Gets the group_count of this QuickSearchRequest.  # noqa: E501

        Maximum number of groups  # noqa: E501

        :return: The group_count of this QuickSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this QuickSearchRequest.

        Maximum number of groups  # noqa: E501

        :param group_count: The group_count of this QuickSearchRequest.  # noqa: E501
        :type: int
        """
        if group_count is not None and group_count > 100:  # noqa: E501
            raise ValueError("Invalid value for `group_count`, must be a value less than or equal to `100`")  # noqa: E501
        if group_count is not None and group_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `group_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._group_count = group_count

    @property
    def group_size(self):
        """Gets the group_size of this QuickSearchRequest.  # noqa: E501

        Number of items per group  # noqa: E501

        :return: The group_size of this QuickSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._group_size

    @group_size.setter
    def group_size(self, group_size):
        """Sets the group_size of this QuickSearchRequest.

        Number of items per group  # noqa: E501

        :param group_size: The group_size of this QuickSearchRequest.  # noqa: E501
        :type: int
        """
        if group_size is not None and group_size > 100:  # noqa: E501
            raise ValueError("Invalid value for `group_size`, must be a value less than or equal to `100`")  # noqa: E501
        if group_size is not None and group_size < 1:  # noqa: E501
            raise ValueError("Invalid value for `group_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._group_size = group_size

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
        if not isinstance(other, QuickSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other