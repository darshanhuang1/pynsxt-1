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

from swagger_client.models.key_value_pair import KeyValuePair  # noqa: F401,E501
from swagger_client.models.resource import Resource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.upgrade_unit_group_info import UpgradeUnitGroupInfo  # noqa: F401,E501


class UpgradeUnit(object):
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
        'group': 'UpgradeUnitGroupInfo',
        'warnings': 'list[str]',
        'current_version': 'str',
        'metadata': 'list[KeyValuePair]',
        'type': 'str',
        'id': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'group': 'group',
        'warnings': 'warnings',
        'current_version': 'current_version',
        'metadata': 'metadata',
        'type': 'type',
        'id': 'id',
        'display_name': 'display_name'
    }

    def __init__(self, _self=None, links=None, schema=None, group=None, warnings=None, current_version=None, metadata=None, type=None, id=None, display_name=None):  # noqa: E501
        """UpgradeUnit - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._group = None
        self._warnings = None
        self._current_version = None
        self._metadata = None
        self._type = None
        self._id = None
        self._display_name = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if group is not None:
            self.group = group
        if warnings is not None:
            self.warnings = warnings
        if current_version is not None:
            self.current_version = current_version
        if metadata is not None:
            self.metadata = metadata
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name

    @property
    def _self(self):
        """Gets the _self of this UpgradeUnit.  # noqa: E501


        :return: The _self of this UpgradeUnit.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this UpgradeUnit.


        :param _self: The _self of this UpgradeUnit.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this UpgradeUnit.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this UpgradeUnit.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpgradeUnit.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this UpgradeUnit.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this UpgradeUnit.  # noqa: E501


        :return: The schema of this UpgradeUnit.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this UpgradeUnit.


        :param schema: The schema of this UpgradeUnit.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def group(self):
        """Gets the group of this UpgradeUnit.  # noqa: E501

        Info of the group to which this upgrade unit belongs  # noqa: E501

        :return: The group of this UpgradeUnit.  # noqa: E501
        :rtype: UpgradeUnitGroupInfo
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UpgradeUnit.

        Info of the group to which this upgrade unit belongs  # noqa: E501

        :param group: The group of this UpgradeUnit.  # noqa: E501
        :type: UpgradeUnitGroupInfo
        """

        self._group = group

    @property
    def warnings(self):
        """Gets the warnings of this UpgradeUnit.  # noqa: E501

        List of warnings indicating issues with the upgrade unit that may result in upgrade failure  # noqa: E501

        :return: The warnings of this UpgradeUnit.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this UpgradeUnit.

        List of warnings indicating issues with the upgrade unit that may result in upgrade failure  # noqa: E501

        :param warnings: The warnings of this UpgradeUnit.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

    @property
    def current_version(self):
        """Gets the current_version of this UpgradeUnit.  # noqa: E501

        This is component version e.g. if upgrade unit is of type edge, then this is edge version.  # noqa: E501

        :return: The current_version of this UpgradeUnit.  # noqa: E501
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this UpgradeUnit.

        This is component version e.g. if upgrade unit is of type edge, then this is edge version.  # noqa: E501

        :param current_version: The current_version of this UpgradeUnit.  # noqa: E501
        :type: str
        """

        self._current_version = current_version

    @property
    def metadata(self):
        """Gets the metadata of this UpgradeUnit.  # noqa: E501

        Metadata about upgrade unit  # noqa: E501

        :return: The metadata of this UpgradeUnit.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpgradeUnit.

        Metadata about upgrade unit  # noqa: E501

        :param metadata: The metadata of this UpgradeUnit.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this UpgradeUnit.  # noqa: E501

        Upgrade unit type  # noqa: E501

        :return: The type of this UpgradeUnit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpgradeUnit.

        Upgrade unit type  # noqa: E501

        :param type: The type of this UpgradeUnit.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this UpgradeUnit.  # noqa: E501

        Identifier of the upgrade unit  # noqa: E501

        :return: The id of this UpgradeUnit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpgradeUnit.

        Identifier of the upgrade unit  # noqa: E501

        :param id: The id of this UpgradeUnit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this UpgradeUnit.  # noqa: E501

        Name of the upgrade unit  # noqa: E501

        :return: The display_name of this UpgradeUnit.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpgradeUnit.

        Name of the upgrade unit  # noqa: E501

        :param display_name: The display_name of this UpgradeUnit.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if not isinstance(other, UpgradeUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
