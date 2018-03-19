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

from swagger_client.models.resource import Resource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class VniRange(object):
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
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'start': 'int',
        'end': 'int'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, _self=None, links=None, schema=None, start=None, end=None):  # noqa: E501
        """VniRange - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._start = None
        self._end = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        self.start = start
        self.end = end

    @property
    def _self(self):
        """Gets the _self of this VniRange.  # noqa: E501


        :return: The _self of this VniRange.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this VniRange.


        :param _self: The _self of this VniRange.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this VniRange.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this VniRange.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VniRange.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this VniRange.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this VniRange.  # noqa: E501


        :return: The schema of this VniRange.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this VniRange.


        :param schema: The schema of this VniRange.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def start(self):
        """Gets the start of this VniRange.  # noqa: E501

        Start value for vni range to be used for virtual networks  # noqa: E501

        :return: The start of this VniRange.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VniRange.

        Start value for vni range to be used for virtual networks  # noqa: E501

        :param start: The start of this VniRange.  # noqa: E501
        :type: int
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        if start is not None and start > 16777215:  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a value less than or equal to `16777215`")  # noqa: E501
        if start is not None and start < 5000:  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a value greater than or equal to `5000`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this VniRange.  # noqa: E501

        End value for vni range to be used for virtual networks  # noqa: E501

        :return: The end of this VniRange.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this VniRange.

        End value for vni range to be used for virtual networks  # noqa: E501

        :param end: The end of this VniRange.  # noqa: E501
        :type: int
        """
        if end is None:
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501
        if end is not None and end > 16777215:  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a value less than or equal to `16777215`")  # noqa: E501
        if end is not None and end < 5000:  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a value greater than or equal to `5000`")  # noqa: E501

        self._end = end

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
        if not isinstance(other, VniRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
