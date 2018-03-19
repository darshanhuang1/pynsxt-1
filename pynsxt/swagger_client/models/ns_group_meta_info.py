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


class NSGroupMetaInfo(object):
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
        'no_of_vms': 'int',
        'ns_group_id': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'no_of_vms': 'no_of_vms',
        'ns_group_id': 'ns_group_id'
    }

    def __init__(self, _self=None, links=None, schema=None, no_of_vms=None, ns_group_id=None):  # noqa: E501
        """NSGroupMetaInfo - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._no_of_vms = None
        self._ns_group_id = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if no_of_vms is not None:
            self.no_of_vms = no_of_vms
        self.ns_group_id = ns_group_id

    @property
    def _self(self):
        """Gets the _self of this NSGroupMetaInfo.  # noqa: E501


        :return: The _self of this NSGroupMetaInfo.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this NSGroupMetaInfo.


        :param _self: The _self of this NSGroupMetaInfo.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this NSGroupMetaInfo.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this NSGroupMetaInfo.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NSGroupMetaInfo.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this NSGroupMetaInfo.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this NSGroupMetaInfo.  # noqa: E501


        :return: The schema of this NSGroupMetaInfo.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NSGroupMetaInfo.


        :param schema: The schema of this NSGroupMetaInfo.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def no_of_vms(self):
        """Gets the no_of_vms of this NSGroupMetaInfo.  # noqa: E501

        Number of VMs discovered for this NSGroup when session was started  # noqa: E501

        :return: The no_of_vms of this NSGroupMetaInfo.  # noqa: E501
        :rtype: int
        """
        return self._no_of_vms

    @no_of_vms.setter
    def no_of_vms(self, no_of_vms):
        """Sets the no_of_vms of this NSGroupMetaInfo.

        Number of VMs discovered for this NSGroup when session was started  # noqa: E501

        :param no_of_vms: The no_of_vms of this NSGroupMetaInfo.  # noqa: E501
        :type: int
        """

        self._no_of_vms = no_of_vms

    @property
    def ns_group_id(self):
        """Gets the ns_group_id of this NSGroupMetaInfo.  # noqa: E501

        ID of the NS Group  # noqa: E501

        :return: The ns_group_id of this NSGroupMetaInfo.  # noqa: E501
        :rtype: str
        """
        return self._ns_group_id

    @ns_group_id.setter
    def ns_group_id(self, ns_group_id):
        """Sets the ns_group_id of this NSGroupMetaInfo.

        ID of the NS Group  # noqa: E501

        :param ns_group_id: The ns_group_id of this NSGroupMetaInfo.  # noqa: E501
        :type: str
        """
        if ns_group_id is None:
            raise ValueError("Invalid value for `ns_group_id`, must not be `None`")  # noqa: E501

        self._ns_group_id = ns_group_id

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
        if not isinstance(other, NSGroupMetaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
