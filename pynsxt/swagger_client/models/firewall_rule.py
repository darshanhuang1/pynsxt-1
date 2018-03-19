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

from swagger_client.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
from swagger_client.models.firewall_service import FirewallService  # noqa: F401,E501
from swagger_client.models.owner_resource_link import OwnerResourceLink  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.resource_reference import ResourceReference  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class FirewallRule(object):
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
        'description': 'str',
        'is_default': 'bool',
        'direction': 'str',
        'rule_tag': 'str',
        'ip_protocol': 'str',
        'notes': 'str',
        'applied_tos': 'list[ResourceReference]',
        'logged': 'bool',
        'disabled': 'bool',
        'sources': 'list[ResourceReference]',
        'services': 'list[FirewallService]',
        'action': 'str',
        'sources_excluded': 'bool',
        'destinations_excluded': 'bool',
        'destinations': 'list[ResourceReference]'
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
        'description': 'description',
        'is_default': 'is_default',
        'direction': 'direction',
        'rule_tag': 'rule_tag',
        'ip_protocol': 'ip_protocol',
        'notes': 'notes',
        'applied_tos': 'applied_tos',
        'logged': 'logged',
        'disabled': 'disabled',
        'sources': 'sources',
        'services': 'services',
        'action': 'action',
        'sources_excluded': 'sources_excluded',
        'destinations_excluded': 'destinations_excluded',
        'destinations': 'destinations'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, owner=None, display_name=None, id=None, resource_type=None, description=None, is_default=None, direction='IN_OUT', rule_tag=None, ip_protocol='IPV4_IPV6', notes=None, applied_tos=None, logged=False, disabled=False, sources=None, services=None, action=None, sources_excluded=False, destinations_excluded=False, destinations=None):  # noqa: E501
        """FirewallRule - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._revision = None
        self._owner = None
        self._display_name = None
        self._id = None
        self._resource_type = None
        self._description = None
        self._is_default = None
        self._direction = None
        self._rule_tag = None
        self._ip_protocol = None
        self._notes = None
        self._applied_tos = None
        self._logged = None
        self._disabled = None
        self._sources = None
        self._services = None
        self._action = None
        self._sources_excluded = None
        self._destinations_excluded = None
        self._destinations = None
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
        if is_default is not None:
            self.is_default = is_default
        if direction is not None:
            self.direction = direction
        if rule_tag is not None:
            self.rule_tag = rule_tag
        if ip_protocol is not None:
            self.ip_protocol = ip_protocol
        if notes is not None:
            self.notes = notes
        if applied_tos is not None:
            self.applied_tos = applied_tos
        if logged is not None:
            self.logged = logged
        if disabled is not None:
            self.disabled = disabled
        if sources is not None:
            self.sources = sources
        if services is not None:
            self.services = services
        self.action = action
        if sources_excluded is not None:
            self.sources_excluded = sources_excluded
        if destinations_excluded is not None:
            self.destinations_excluded = destinations_excluded
        if destinations is not None:
            self.destinations = destinations

    @property
    def _self(self):
        """Gets the _self of this FirewallRule.  # noqa: E501


        :return: The _self of this FirewallRule.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this FirewallRule.


        :param _self: The _self of this FirewallRule.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this FirewallRule.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this FirewallRule.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FirewallRule.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this FirewallRule.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this FirewallRule.  # noqa: E501


        :return: The schema of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this FirewallRule.


        :param schema: The schema of this FirewallRule.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this FirewallRule.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this FirewallRule.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this FirewallRule.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this FirewallRule.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def owner(self):
        """Gets the owner of this FirewallRule.  # noqa: E501


        :return: The owner of this FirewallRule.  # noqa: E501
        :rtype: OwnerResourceLink
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FirewallRule.


        :param owner: The owner of this FirewallRule.  # noqa: E501
        :type: OwnerResourceLink
        """

        self._owner = owner

    @property
    def display_name(self):
        """Gets the display_name of this FirewallRule.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FirewallRule.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this FirewallRule.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this FirewallRule.  # noqa: E501

        Identifier of the resource  # noqa: E501

        :return: The id of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirewallRule.

        Identifier of the resource  # noqa: E501

        :param id: The id of this FirewallRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this FirewallRule.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FirewallRule.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this FirewallRule.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def description(self):
        """Gets the description of this FirewallRule.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirewallRule.

        Description of this resource  # noqa: E501

        :param description: The description of this FirewallRule.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def is_default(self):
        """Gets the is_default of this FirewallRule.  # noqa: E501

        Flag to indicate whether rule is default.  # noqa: E501

        :return: The is_default of this FirewallRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this FirewallRule.

        Flag to indicate whether rule is default.  # noqa: E501

        :param is_default: The is_default of this FirewallRule.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def direction(self):
        """Gets the direction of this FirewallRule.  # noqa: E501

        Rule direction in case of stateless firewall rules. This will only considered if section level parameter is set to stateless. Default to IN_OUT if not specified.  # noqa: E501

        :return: The direction of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this FirewallRule.

        Rule direction in case of stateless firewall rules. This will only considered if section level parameter is set to stateless. Default to IN_OUT if not specified.  # noqa: E501

        :param direction: The direction of this FirewallRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN", "OUT", "IN_OUT"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def rule_tag(self):
        """Gets the rule_tag of this FirewallRule.  # noqa: E501

        User level field which will be printed in CLI and packet logs.  # noqa: E501

        :return: The rule_tag of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_tag

    @rule_tag.setter
    def rule_tag(self, rule_tag):
        """Sets the rule_tag of this FirewallRule.

        User level field which will be printed in CLI and packet logs.  # noqa: E501

        :param rule_tag: The rule_tag of this FirewallRule.  # noqa: E501
        :type: str
        """
        if rule_tag is not None and len(rule_tag) > 32:
            raise ValueError("Invalid value for `rule_tag`, length must be less than or equal to `32`")  # noqa: E501

        self._rule_tag = rule_tag

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this FirewallRule.  # noqa: E501

        Type of IP packet that should be matched while enforcing the rule.  # noqa: E501

        :return: The ip_protocol of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this FirewallRule.

        Type of IP packet that should be matched while enforcing the rule.  # noqa: E501

        :param ip_protocol: The ip_protocol of this FirewallRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["IPV4", "IPV6", "IPV4_IPV6"]  # noqa: E501
        if ip_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(ip_protocol, allowed_values)
            )

        self._ip_protocol = ip_protocol

    @property
    def notes(self):
        """Gets the notes of this FirewallRule.  # noqa: E501

        User notes specific to the rule.  # noqa: E501

        :return: The notes of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this FirewallRule.

        User notes specific to the rule.  # noqa: E501

        :param notes: The notes of this FirewallRule.  # noqa: E501
        :type: str
        """
        if notes is not None and len(notes) > 2048:
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `2048`")  # noqa: E501

        self._notes = notes

    @property
    def applied_tos(self):
        """Gets the applied_tos of this FirewallRule.  # noqa: E501

        List of object where rule will be enforced. The section level field overrides this one. Null will be treated as any.  # noqa: E501

        :return: The applied_tos of this FirewallRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """Sets the applied_tos of this FirewallRule.

        List of object where rule will be enforced. The section level field overrides this one. Null will be treated as any.  # noqa: E501

        :param applied_tos: The applied_tos of this FirewallRule.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._applied_tos = applied_tos

    @property
    def logged(self):
        """Gets the logged of this FirewallRule.  # noqa: E501

        Flag to enable packet logging. Default is disabled.  # noqa: E501

        :return: The logged of this FirewallRule.  # noqa: E501
        :rtype: bool
        """
        return self._logged

    @logged.setter
    def logged(self, logged):
        """Sets the logged of this FirewallRule.

        Flag to enable packet logging. Default is disabled.  # noqa: E501

        :param logged: The logged of this FirewallRule.  # noqa: E501
        :type: bool
        """

        self._logged = logged

    @property
    def disabled(self):
        """Gets the disabled of this FirewallRule.  # noqa: E501

        Flag to disable rule. Disabled will only be persisted but never provisioned/realized.  # noqa: E501

        :return: The disabled of this FirewallRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this FirewallRule.

        Flag to disable rule. Disabled will only be persisted but never provisioned/realized.  # noqa: E501

        :param disabled: The disabled of this FirewallRule.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def sources(self):
        """Gets the sources of this FirewallRule.  # noqa: E501

        List of sources. Null will be treated as any.  # noqa: E501

        :return: The sources of this FirewallRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this FirewallRule.

        List of sources. Null will be treated as any.  # noqa: E501

        :param sources: The sources of this FirewallRule.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._sources = sources

    @property
    def services(self):
        """Gets the services of this FirewallRule.  # noqa: E501

        List of the services. Null will be treated as any.  # noqa: E501

        :return: The services of this FirewallRule.  # noqa: E501
        :rtype: list[FirewallService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this FirewallRule.

        List of the services. Null will be treated as any.  # noqa: E501

        :param services: The services of this FirewallRule.  # noqa: E501
        :type: list[FirewallService]
        """

        self._services = services

    @property
    def action(self):
        """Gets the action of this FirewallRule.  # noqa: E501

        Action enforced on the packets which matches the firewall rule.  # noqa: E501

        :return: The action of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this FirewallRule.

        Action enforced on the packets which matches the firewall rule.  # noqa: E501

        :param action: The action of this FirewallRule.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["ALLOW", "DROP", "REJECT"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def sources_excluded(self):
        """Gets the sources_excluded of this FirewallRule.  # noqa: E501

        Negation of the source.  # noqa: E501

        :return: The sources_excluded of this FirewallRule.  # noqa: E501
        :rtype: bool
        """
        return self._sources_excluded

    @sources_excluded.setter
    def sources_excluded(self, sources_excluded):
        """Sets the sources_excluded of this FirewallRule.

        Negation of the source.  # noqa: E501

        :param sources_excluded: The sources_excluded of this FirewallRule.  # noqa: E501
        :type: bool
        """

        self._sources_excluded = sources_excluded

    @property
    def destinations_excluded(self):
        """Gets the destinations_excluded of this FirewallRule.  # noqa: E501

        Negation of the destination.  # noqa: E501

        :return: The destinations_excluded of this FirewallRule.  # noqa: E501
        :rtype: bool
        """
        return self._destinations_excluded

    @destinations_excluded.setter
    def destinations_excluded(self, destinations_excluded):
        """Sets the destinations_excluded of this FirewallRule.

        Negation of the destination.  # noqa: E501

        :param destinations_excluded: The destinations_excluded of this FirewallRule.  # noqa: E501
        :type: bool
        """

        self._destinations_excluded = destinations_excluded

    @property
    def destinations(self):
        """Gets the destinations of this FirewallRule.  # noqa: E501

        List of the destinations. Null will be treated as any.  # noqa: E501

        :return: The destinations of this FirewallRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this FirewallRule.

        List of the destinations. Null will be treated as any.  # noqa: E501

        :param destinations: The destinations of this FirewallRule.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._destinations = destinations

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
        if not isinstance(other, FirewallRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
