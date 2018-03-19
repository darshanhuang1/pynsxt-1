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

from swagger_client.models.policy_alarm_resource import PolicyAlarmResource  # noqa: F401,E501
from swagger_client.models.policy_realized_resource import PolicyRealizedResource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class RealizedLogicalSwitch(object):
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
        'system_owned': 'bool',
        'display_name': 'str',
        'description': 'str',
        'tags': 'list[Tag]',
        'create_user': 'str',
        'protection': 'str',
        'create_time': 'int',
        'last_modified_time': 'int',
        'last_modified_user': 'str',
        'id': 'str',
        'resource_type': 'str',
        'path': 'str',
        'relative_path': 'str',
        'intent_reference': 'list[str]',
        'realization_specific_identifier': 'str',
        'state': 'str',
        'alarms': 'list[PolicyAlarmResource]',
        'transport_zone_id': 'str',
        'logical_switch_id': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'revision': '_revision',
        'system_owned': '_system_owned',
        'display_name': 'display_name',
        'description': 'description',
        'tags': 'tags',
        'create_user': '_create_user',
        'protection': '_protection',
        'create_time': '_create_time',
        'last_modified_time': '_last_modified_time',
        'last_modified_user': '_last_modified_user',
        'id': 'id',
        'resource_type': 'resource_type',
        'path': 'path',
        'relative_path': 'relative_path',
        'intent_reference': 'intent_reference',
        'realization_specific_identifier': 'realization_specific_identifier',
        'state': 'state',
        'alarms': 'alarms',
        'transport_zone_id': 'transport_zone_id',
        'logical_switch_id': 'logical_switch_id'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, path=None, relative_path=None, intent_reference=None, realization_specific_identifier=None, state=None, alarms=None, transport_zone_id=None, logical_switch_id=None):  # noqa: E501
        """RealizedLogicalSwitch - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._revision = None
        self._system_owned = None
        self._display_name = None
        self._description = None
        self._tags = None
        self._create_user = None
        self._protection = None
        self._create_time = None
        self._last_modified_time = None
        self._last_modified_user = None
        self._id = None
        self._resource_type = None
        self._path = None
        self._relative_path = None
        self._intent_reference = None
        self._realization_specific_identifier = None
        self._state = None
        self._alarms = None
        self._transport_zone_id = None
        self._logical_switch_id = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if revision is not None:
            self.revision = revision
        if system_owned is not None:
            self.system_owned = system_owned
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if create_user is not None:
            self.create_user = create_user
        if protection is not None:
            self.protection = protection
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_modified_user is not None:
            self.last_modified_user = last_modified_user
        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if path is not None:
            self.path = path
        if relative_path is not None:
            self.relative_path = relative_path
        if intent_reference is not None:
            self.intent_reference = intent_reference
        if realization_specific_identifier is not None:
            self.realization_specific_identifier = realization_specific_identifier
        self.state = state
        if alarms is not None:
            self.alarms = alarms
        if transport_zone_id is not None:
            self.transport_zone_id = transport_zone_id
        if logical_switch_id is not None:
            self.logical_switch_id = logical_switch_id

    @property
    def _self(self):
        """Gets the _self of this RealizedLogicalSwitch.  # noqa: E501


        :return: The _self of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this RealizedLogicalSwitch.


        :param _self: The _self of this RealizedLogicalSwitch.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this RealizedLogicalSwitch.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RealizedLogicalSwitch.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this RealizedLogicalSwitch.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this RealizedLogicalSwitch.  # noqa: E501


        :return: The schema of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this RealizedLogicalSwitch.


        :param schema: The schema of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this RealizedLogicalSwitch.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this RealizedLogicalSwitch.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this RealizedLogicalSwitch.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this RealizedLogicalSwitch.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this RealizedLogicalSwitch.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this RealizedLogicalSwitch.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this RealizedLogicalSwitch.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RealizedLogicalSwitch.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this RealizedLogicalSwitch.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RealizedLogicalSwitch.

        Description of this resource  # noqa: E501

        :param description: The description of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this RealizedLogicalSwitch.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RealizedLogicalSwitch.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this RealizedLogicalSwitch.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this RealizedLogicalSwitch.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this RealizedLogicalSwitch.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this RealizedLogicalSwitch.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this RealizedLogicalSwitch.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this RealizedLogicalSwitch.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RealizedLogicalSwitch.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this RealizedLogicalSwitch.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this RealizedLogicalSwitch.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this RealizedLogicalSwitch.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this RealizedLogicalSwitch.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this RealizedLogicalSwitch.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this RealizedLogicalSwitch.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this RealizedLogicalSwitch.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RealizedLogicalSwitch.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this RealizedLogicalSwitch.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RealizedLogicalSwitch.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def path(self):
        """Gets the path of this RealizedLogicalSwitch.  # noqa: E501

        Absolute path of this object  # noqa: E501

        :return: The path of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RealizedLogicalSwitch.

        Absolute path of this object  # noqa: E501

        :param path: The path of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def relative_path(self):
        """Gets the relative_path of this RealizedLogicalSwitch.  # noqa: E501

        Path relative from its parent  # noqa: E501

        :return: The relative_path of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this RealizedLogicalSwitch.

        Path relative from its parent  # noqa: E501

        :param relative_path: The relative_path of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._relative_path = relative_path

    @property
    def intent_reference(self):
        """Gets the intent_reference of this RealizedLogicalSwitch.  # noqa: E501

        Desire state paths of this object  # noqa: E501

        :return: The intent_reference of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: list[str]
        """
        return self._intent_reference

    @intent_reference.setter
    def intent_reference(self, intent_reference):
        """Sets the intent_reference of this RealizedLogicalSwitch.

        Desire state paths of this object  # noqa: E501

        :param intent_reference: The intent_reference of this RealizedLogicalSwitch.  # noqa: E501
        :type: list[str]
        """

        self._intent_reference = intent_reference

    @property
    def realization_specific_identifier(self):
        """Gets the realization_specific_identifier of this RealizedLogicalSwitch.  # noqa: E501

        Realization id of this object  # noqa: E501

        :return: The realization_specific_identifier of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._realization_specific_identifier

    @realization_specific_identifier.setter
    def realization_specific_identifier(self, realization_specific_identifier):
        """Sets the realization_specific_identifier of this RealizedLogicalSwitch.

        Realization id of this object  # noqa: E501

        :param realization_specific_identifier: The realization_specific_identifier of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._realization_specific_identifier = realization_specific_identifier

    @property
    def state(self):
        """Gets the state of this RealizedLogicalSwitch.  # noqa: E501

        Realization state of this object  # noqa: E501

        :return: The state of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RealizedLogicalSwitch.

        Realization state of this object  # noqa: E501

        :param state: The state of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["UNAVAILABLE", "UNREALIZED", "REALIZED", "ERROR"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def alarms(self):
        """Gets the alarms of this RealizedLogicalSwitch.  # noqa: E501

        Alarm info detail  # noqa: E501

        :return: The alarms of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: list[PolicyAlarmResource]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        """Sets the alarms of this RealizedLogicalSwitch.

        Alarm info detail  # noqa: E501

        :param alarms: The alarms of this RealizedLogicalSwitch.  # noqa: E501
        :type: list[PolicyAlarmResource]
        """

        self._alarms = alarms

    @property
    def transport_zone_id(self):
        """Gets the transport_zone_id of this RealizedLogicalSwitch.  # noqa: E501

        Transport zone identifier  # noqa: E501

        :return: The transport_zone_id of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._transport_zone_id

    @transport_zone_id.setter
    def transport_zone_id(self, transport_zone_id):
        """Sets the transport_zone_id of this RealizedLogicalSwitch.

        Transport zone identifier  # noqa: E501

        :param transport_zone_id: The transport_zone_id of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._transport_zone_id = transport_zone_id

    @property
    def logical_switch_id(self):
        """Gets the logical_switch_id of this RealizedLogicalSwitch.  # noqa: E501

        Id of the logical switch  # noqa: E501

        :return: The logical_switch_id of this RealizedLogicalSwitch.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_id

    @logical_switch_id.setter
    def logical_switch_id(self, logical_switch_id):
        """Sets the logical_switch_id of this RealizedLogicalSwitch.

        Id of the logical switch  # noqa: E501

        :param logical_switch_id: The logical_switch_id of this RealizedLogicalSwitch.  # noqa: E501
        :type: str
        """

        self._logical_switch_id = logical_switch_id

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
        if not isinstance(other, RealizedLogicalSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
