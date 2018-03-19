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

from swagger_client.models.list_result import ListResult  # noqa: F401,E501
from swagger_client.models.realized_group_ui_resource import RealizedGroupUIResource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class RealizedGroupUIResourceListResult(object):
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
        'cursor': 'str',
        'sort_ascending': 'bool',
        'sort_by': 'str',
        'result_count': 'int',
        'results': 'list[RealizedGroupUIResource]'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'cursor': 'cursor',
        'sort_ascending': 'sort_ascending',
        'sort_by': 'sort_by',
        'result_count': 'result_count',
        'results': 'results'
    }

    def __init__(self, _self=None, links=None, schema=None, cursor=None, sort_ascending=None, sort_by=None, result_count=None, results=None):  # noqa: E501
        """RealizedGroupUIResourceListResult - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._cursor = None
        self._sort_ascending = None
        self._sort_by = None
        self._result_count = None
        self._results = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if cursor is not None:
            self.cursor = cursor
        if sort_ascending is not None:
            self.sort_ascending = sort_ascending
        if sort_by is not None:
            self.sort_by = sort_by
        if result_count is not None:
            self.result_count = result_count
        self.results = results

    @property
    def _self(self):
        """Gets the _self of this RealizedGroupUIResourceListResult.  # noqa: E501


        :return: The _self of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this RealizedGroupUIResourceListResult.


        :param _self: The _self of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this RealizedGroupUIResourceListResult.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RealizedGroupUIResourceListResult.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this RealizedGroupUIResourceListResult.  # noqa: E501


        :return: The schema of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this RealizedGroupUIResourceListResult.


        :param schema: The schema of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def cursor(self):
        """Gets the cursor of this RealizedGroupUIResourceListResult.  # noqa: E501

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :return: The cursor of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this RealizedGroupUIResourceListResult.

        Opaque cursor to be used for getting next page of records (supplied by current result page)  # noqa: E501

        :param cursor: The cursor of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def sort_ascending(self):
        """Gets the sort_ascending of this RealizedGroupUIResourceListResult.  # noqa: E501


        :return: The sort_ascending of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: bool
        """
        return self._sort_ascending

    @sort_ascending.setter
    def sort_ascending(self, sort_ascending):
        """Sets the sort_ascending of this RealizedGroupUIResourceListResult.


        :param sort_ascending: The sort_ascending of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: bool
        """

        self._sort_ascending = sort_ascending

    @property
    def sort_by(self):
        """Gets the sort_by of this RealizedGroupUIResourceListResult.  # noqa: E501

        Field by which records are sorted  # noqa: E501

        :return: The sort_by of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this RealizedGroupUIResourceListResult.

        Field by which records are sorted  # noqa: E501

        :param sort_by: The sort_by of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: str
        """

        self._sort_by = sort_by

    @property
    def result_count(self):
        """Gets the result_count of this RealizedGroupUIResourceListResult.  # noqa: E501

        Count of results found (across all pages), set only on first page  # noqa: E501

        :return: The result_count of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this RealizedGroupUIResourceListResult.

        Count of results found (across all pages), set only on first page  # noqa: E501

        :param result_count: The result_count of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

    @property
    def results(self):
        """Gets the results of this RealizedGroupUIResourceListResult.  # noqa: E501

        Intent and realized group list results  # noqa: E501

        :return: The results of this RealizedGroupUIResourceListResult.  # noqa: E501
        :rtype: list[RealizedGroupUIResource]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this RealizedGroupUIResourceListResult.

        Intent and realized group list results  # noqa: E501

        :param results: The results of this RealizedGroupUIResourceListResult.  # noqa: E501
        :type: list[RealizedGroupUIResource]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, RealizedGroupUIResourceListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
