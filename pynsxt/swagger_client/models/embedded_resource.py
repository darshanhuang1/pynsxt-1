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

from swagger_client.models.owner_resource_link import OwnerResourceLink  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.revisioned_resource import RevisionedResource  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class EmbeddedResource(object):
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
        'revision': 'int',
        'owner': 'OwnerResourceLink',
        'display_name': 'str',
        'id': 'str',
        'resource_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'revision': '_revision',
        'owner': '_owner',
        'display_name': 'display_name',
        'id': 'id',
        'resource_type': 'resource_type',
        'description': 'description'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, owner=None, display_name=None, id=None, resource_type=None, description=None):  # noqa: E501
        """EmbeddedResource - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._revision = None
        self._owner = None
        self._display_name = None
        self._id = None
        self._resource_type = None
        self._description = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if revision is not None:
            self.revision = revision
        if owner is not None:
            self.owner = owner
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if description is not None:
            self.description = description

    @property
    def _self(self):
        """Gets the _self of this EmbeddedResource.  # noqa: E501


        :return: The _self of this EmbeddedResource.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this EmbeddedResource.


        :param _self: The _self of this EmbeddedResource.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this EmbeddedResource.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this EmbeddedResource.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EmbeddedResource.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this EmbeddedResource.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this EmbeddedResource.  # noqa: E501


        :return: The schema of this EmbeddedResource.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this EmbeddedResource.


        :param schema: The schema of this EmbeddedResource.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this EmbeddedResource.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this EmbeddedResource.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this EmbeddedResource.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this EmbeddedResource.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def owner(self):
        """Gets the owner of this EmbeddedResource.  # noqa: E501


        :return: The owner of this EmbeddedResource.  # noqa: E501
        :rtype: OwnerResourceLink
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this EmbeddedResource.


        :param owner: The owner of this EmbeddedResource.  # noqa: E501
        :type: OwnerResourceLink
        """

        self._owner = owner

    @property
    def display_name(self):
        """Gets the display_name of this EmbeddedResource.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this EmbeddedResource.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EmbeddedResource.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this EmbeddedResource.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this EmbeddedResource.  # noqa: E501

        Identifier of the resource  # noqa: E501

        :return: The id of this EmbeddedResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmbeddedResource.

        Identifier of the resource  # noqa: E501

        :param id: The id of this EmbeddedResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this EmbeddedResource.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this EmbeddedResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this EmbeddedResource.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this EmbeddedResource.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def description(self):
        """Gets the description of this EmbeddedResource.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this EmbeddedResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EmbeddedResource.

        Description of this resource  # noqa: E501

        :param description: The description of this EmbeddedResource.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, EmbeddedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other