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

from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.revisioned_resource import RevisionedResource  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class ManagementConfig(object):
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
        'publish_fqdns': 'bool'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'revision': '_revision',
        'publish_fqdns': 'publish_fqdns'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, publish_fqdns=None):  # noqa: E501
        """ManagementConfig - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._revision = None
        self._publish_fqdns = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if revision is not None:
            self.revision = revision
        self.publish_fqdns = publish_fqdns

    @property
    def _self(self):
        """Gets the _self of this ManagementConfig.  # noqa: E501


        :return: The _self of this ManagementConfig.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ManagementConfig.


        :param _self: The _self of this ManagementConfig.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this ManagementConfig.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this ManagementConfig.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ManagementConfig.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this ManagementConfig.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this ManagementConfig.  # noqa: E501


        :return: The schema of this ManagementConfig.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ManagementConfig.


        :param schema: The schema of this ManagementConfig.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this ManagementConfig.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this ManagementConfig.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ManagementConfig.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this ManagementConfig.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def publish_fqdns(self):
        """Gets the publish_fqdns of this ManagementConfig.  # noqa: E501

        True if Management nodes publish their fqdns(instead of default IP addresses) across NSX for its reachability.  # noqa: E501

        :return: The publish_fqdns of this ManagementConfig.  # noqa: E501
        :rtype: bool
        """
        return self._publish_fqdns

    @publish_fqdns.setter
    def publish_fqdns(self, publish_fqdns):
        """Sets the publish_fqdns of this ManagementConfig.

        True if Management nodes publish their fqdns(instead of default IP addresses) across NSX for its reachability.  # noqa: E501

        :param publish_fqdns: The publish_fqdns of this ManagementConfig.  # noqa: E501
        :type: bool
        """
        if publish_fqdns is None:
            raise ValueError("Invalid value for `publish_fqdns`, must not be `None`")  # noqa: E501

        self._publish_fqdns = publish_fqdns

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
        if not isinstance(other, ManagementConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
