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

from swagger_client.models.node_service_properties import NodeServiceProperties  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.ssh_service_properties import SshServiceProperties  # noqa: F401,E501


class NodeSshServiceProperties(object):
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
        'service_name': 'str',
        'service_properties': 'SshServiceProperties'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'service_name': 'service_name',
        'service_properties': 'service_properties'
    }

    def __init__(self, _self=None, links=None, schema=None, service_name=None, service_properties=None):  # noqa: E501
        """NodeSshServiceProperties - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._service_name = None
        self._service_properties = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        self.service_name = service_name
        if service_properties is not None:
            self.service_properties = service_properties

    @property
    def _self(self):
        """Gets the _self of this NodeSshServiceProperties.  # noqa: E501


        :return: The _self of this NodeSshServiceProperties.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this NodeSshServiceProperties.


        :param _self: The _self of this NodeSshServiceProperties.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this NodeSshServiceProperties.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this NodeSshServiceProperties.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NodeSshServiceProperties.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this NodeSshServiceProperties.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this NodeSshServiceProperties.  # noqa: E501


        :return: The schema of this NodeSshServiceProperties.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this NodeSshServiceProperties.


        :param schema: The schema of this NodeSshServiceProperties.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def service_name(self):
        """Gets the service_name of this NodeSshServiceProperties.  # noqa: E501

        Service name  # noqa: E501

        :return: The service_name of this NodeSshServiceProperties.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this NodeSshServiceProperties.

        Service name  # noqa: E501

        :param service_name: The service_name of this NodeSshServiceProperties.  # noqa: E501
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def service_properties(self):
        """Gets the service_properties of this NodeSshServiceProperties.  # noqa: E501

        SSH Service properties  # noqa: E501

        :return: The service_properties of this NodeSshServiceProperties.  # noqa: E501
        :rtype: SshServiceProperties
        """
        return self._service_properties

    @service_properties.setter
    def service_properties(self, service_properties):
        """Sets the service_properties of this NodeSshServiceProperties.

        SSH Service properties  # noqa: E501

        :param service_properties: The service_properties of this NodeSshServiceProperties.  # noqa: E501
        :type: SshServiceProperties
        """

        self._service_properties = service_properties

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
        if not isinstance(other, NodeSshServiceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other