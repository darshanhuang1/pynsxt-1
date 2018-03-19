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

from swagger_client.models.cloud_tag import CloudTag  # noqa: F401,E501
from swagger_client.models.compute_instance_error_message import ComputeInstanceErrorMessage  # noqa: F401,E501
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class CloudVirtualMachine(object):
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
        'gateway_ha_index': 'int',
        'nsx_ip': 'str',
        'gateway_status': 'str',
        'is_gateway': 'bool',
        'is_gateway_active': 'bool',
        'error_messages': 'list[ComputeInstanceErrorMessage]',
        'agent_status': 'str',
        'logical_switch_id': 'str',
        'logical_switch_display_name': 'str',
        'private_ip': 'str',
        'threat_state': 'str',
        'os_details': 'str',
        'managed_by_nsx': 'bool',
        'quarantine_state': 'str',
        'cloud_tags': 'list[CloudTag]',
        'public_ip': 'str',
        'os_type': 'str',
        'agent_version': 'str'
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
        'gateway_ha_index': 'gateway_ha_index',
        'nsx_ip': 'nsx_ip',
        'gateway_status': 'gateway_status',
        'is_gateway': 'is_gateway',
        'is_gateway_active': 'is_gateway_active',
        'error_messages': 'error_messages',
        'agent_status': 'agent_status',
        'logical_switch_id': 'logical_switch_id',
        'logical_switch_display_name': 'logical_switch_display_name',
        'private_ip': 'private_ip',
        'threat_state': 'threat_state',
        'os_details': 'os_details',
        'managed_by_nsx': 'managed_by_nsx',
        'quarantine_state': 'quarantine_state',
        'cloud_tags': 'cloud_tags',
        'public_ip': 'public_ip',
        'os_type': 'os_type',
        'agent_version': 'agent_version'
    }

    discriminator_value_class_map = {
        'AwsVirtualMachine': 'AwsVirtualMachine'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, gateway_ha_index=None, nsx_ip=None, gateway_status=None, is_gateway=None, is_gateway_active=None, error_messages=None, agent_status=None, logical_switch_id=None, logical_switch_display_name=None, private_ip=None, threat_state=None, os_details=None, managed_by_nsx=None, quarantine_state=None, cloud_tags=None, public_ip=None, os_type=None, agent_version=None):  # noqa: E501
        """CloudVirtualMachine - a model defined in Swagger"""  # noqa: E501

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
        self._gateway_ha_index = None
        self._nsx_ip = None
        self._gateway_status = None
        self._is_gateway = None
        self._is_gateway_active = None
        self._error_messages = None
        self._agent_status = None
        self._logical_switch_id = None
        self._logical_switch_display_name = None
        self._private_ip = None
        self._threat_state = None
        self._os_details = None
        self._managed_by_nsx = None
        self._quarantine_state = None
        self._cloud_tags = None
        self._public_ip = None
        self._os_type = None
        self._agent_version = None
        self.discriminator = 'resource_type'

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
        self.resource_type = resource_type
        if gateway_ha_index is not None:
            self.gateway_ha_index = gateway_ha_index
        if nsx_ip is not None:
            self.nsx_ip = nsx_ip
        if gateway_status is not None:
            self.gateway_status = gateway_status
        if is_gateway is not None:
            self.is_gateway = is_gateway
        if is_gateway_active is not None:
            self.is_gateway_active = is_gateway_active
        if error_messages is not None:
            self.error_messages = error_messages
        if agent_status is not None:
            self.agent_status = agent_status
        if logical_switch_id is not None:
            self.logical_switch_id = logical_switch_id
        if logical_switch_display_name is not None:
            self.logical_switch_display_name = logical_switch_display_name
        if private_ip is not None:
            self.private_ip = private_ip
        if threat_state is not None:
            self.threat_state = threat_state
        if os_details is not None:
            self.os_details = os_details
        if managed_by_nsx is not None:
            self.managed_by_nsx = managed_by_nsx
        if quarantine_state is not None:
            self.quarantine_state = quarantine_state
        if cloud_tags is not None:
            self.cloud_tags = cloud_tags
        if public_ip is not None:
            self.public_ip = public_ip
        if os_type is not None:
            self.os_type = os_type
        if agent_version is not None:
            self.agent_version = agent_version

    @property
    def _self(self):
        """Gets the _self of this CloudVirtualMachine.  # noqa: E501


        :return: The _self of this CloudVirtualMachine.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this CloudVirtualMachine.


        :param _self: The _self of this CloudVirtualMachine.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this CloudVirtualMachine.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this CloudVirtualMachine.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CloudVirtualMachine.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this CloudVirtualMachine.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this CloudVirtualMachine.  # noqa: E501


        :return: The schema of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this CloudVirtualMachine.


        :param schema: The schema of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this CloudVirtualMachine.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this CloudVirtualMachine.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this CloudVirtualMachine.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this CloudVirtualMachine.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this CloudVirtualMachine.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this CloudVirtualMachine.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this CloudVirtualMachine.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this CloudVirtualMachine.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this CloudVirtualMachine.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CloudVirtualMachine.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CloudVirtualMachine.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudVirtualMachine.

        Description of this resource  # noqa: E501

        :param description: The description of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this CloudVirtualMachine.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this CloudVirtualMachine.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudVirtualMachine.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this CloudVirtualMachine.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this CloudVirtualMachine.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this CloudVirtualMachine.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this CloudVirtualMachine.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this CloudVirtualMachine.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this CloudVirtualMachine.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this CloudVirtualMachine.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CloudVirtualMachine.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this CloudVirtualMachine.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this CloudVirtualMachine.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this CloudVirtualMachine.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this CloudVirtualMachine.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this CloudVirtualMachine.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this CloudVirtualMachine.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this CloudVirtualMachine.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this CloudVirtualMachine.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudVirtualMachine.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this CloudVirtualMachine.  # noqa: E501

        Possible values are in the form of VirtualMachine prefixed by cloud name. For example, AwsVirtualMachine or AzureVirtualMachine.   # noqa: E501

        :return: The resource_type of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CloudVirtualMachine.

        Possible values are in the form of VirtualMachine prefixed by cloud name. For example, AwsVirtualMachine or AzureVirtualMachine.   # noqa: E501

        :param resource_type: The resource_type of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AwsVirtualMachine", "AzureVirtualMachine"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def gateway_ha_index(self):
        """Gets the gateway_ha_index of this CloudVirtualMachine.  # noqa: E501

        Index of HA that indicates whether gateway is primary or secondary. If index is 0, then it is primary gateway. Else secondary gateway.   # noqa: E501

        :return: The gateway_ha_index of this CloudVirtualMachine.  # noqa: E501
        :rtype: int
        """
        return self._gateway_ha_index

    @gateway_ha_index.setter
    def gateway_ha_index(self, gateway_ha_index):
        """Sets the gateway_ha_index of this CloudVirtualMachine.

        Index of HA that indicates whether gateway is primary or secondary. If index is 0, then it is primary gateway. Else secondary gateway.   # noqa: E501

        :param gateway_ha_index: The gateway_ha_index of this CloudVirtualMachine.  # noqa: E501
        :type: int
        """

        self._gateway_ha_index = gateway_ha_index

    @property
    def nsx_ip(self):
        """Gets the nsx_ip of this CloudVirtualMachine.  # noqa: E501

        IP address provided by Nsx  # noqa: E501

        :return: The nsx_ip of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._nsx_ip

    @nsx_ip.setter
    def nsx_ip(self, nsx_ip):
        """Sets the nsx_ip of this CloudVirtualMachine.

        IP address provided by Nsx  # noqa: E501

        :param nsx_ip: The nsx_ip of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._nsx_ip = nsx_ip

    @property
    def gateway_status(self):
        """Gets the gateway_status of this CloudVirtualMachine.  # noqa: E501

        Gateway Status  # noqa: E501

        :return: The gateway_status of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._gateway_status

    @gateway_status.setter
    def gateway_status(self, gateway_status):
        """Sets the gateway_status of this CloudVirtualMachine.

        Gateway Status  # noqa: E501

        :param gateway_status: The gateway_status of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "DEPLOYING", "NOT_AVAILABLE", "UNDEPLOYING"]  # noqa: E501
        if gateway_status not in allowed_values:
            raise ValueError(
                "Invalid value for `gateway_status` ({0}), must be one of {1}"  # noqa: E501
                .format(gateway_status, allowed_values)
            )

        self._gateway_status = gateway_status

    @property
    def is_gateway(self):
        """Gets the is_gateway of this CloudVirtualMachine.  # noqa: E501

        Flag to identify if this VM is a gateway node  # noqa: E501

        :return: The is_gateway of this CloudVirtualMachine.  # noqa: E501
        :rtype: bool
        """
        return self._is_gateway

    @is_gateway.setter
    def is_gateway(self, is_gateway):
        """Sets the is_gateway of this CloudVirtualMachine.

        Flag to identify if this VM is a gateway node  # noqa: E501

        :param is_gateway: The is_gateway of this CloudVirtualMachine.  # noqa: E501
        :type: bool
        """

        self._is_gateway = is_gateway

    @property
    def is_gateway_active(self):
        """Gets the is_gateway_active of this CloudVirtualMachine.  # noqa: E501

        Flag to identify if this VM is an active gateway node  # noqa: E501

        :return: The is_gateway_active of this CloudVirtualMachine.  # noqa: E501
        :rtype: bool
        """
        return self._is_gateway_active

    @is_gateway_active.setter
    def is_gateway_active(self, is_gateway_active):
        """Sets the is_gateway_active of this CloudVirtualMachine.

        Flag to identify if this VM is an active gateway node  # noqa: E501

        :param is_gateway_active: The is_gateway_active of this CloudVirtualMachine.  # noqa: E501
        :type: bool
        """

        self._is_gateway_active = is_gateway_active

    @property
    def error_messages(self):
        """Gets the error_messages of this CloudVirtualMachine.  # noqa: E501

        These error messages are recent and are maximum of 1 hour old.   # noqa: E501

        :return: The error_messages of this CloudVirtualMachine.  # noqa: E501
        :rtype: list[ComputeInstanceErrorMessage]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        """Sets the error_messages of this CloudVirtualMachine.

        These error messages are recent and are maximum of 1 hour old.   # noqa: E501

        :param error_messages: The error_messages of this CloudVirtualMachine.  # noqa: E501
        :type: list[ComputeInstanceErrorMessage]
        """

        self._error_messages = error_messages

    @property
    def agent_status(self):
        """Gets the agent_status of this CloudVirtualMachine.  # noqa: E501

        Agent Status  # noqa: E501

        :return: The agent_status of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this CloudVirtualMachine.

        Agent Status  # noqa: E501

        :param agent_status: The agent_status of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "NO_AGENT"]  # noqa: E501
        if agent_status not in allowed_values:
            raise ValueError(
                "Invalid value for `agent_status` ({0}), must be one of {1}"  # noqa: E501
                .format(agent_status, allowed_values)
            )

        self._agent_status = agent_status

    @property
    def logical_switch_id(self):
        """Gets the logical_switch_id of this CloudVirtualMachine.  # noqa: E501

        Logical Switch ID  # noqa: E501

        :return: The logical_switch_id of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_id

    @logical_switch_id.setter
    def logical_switch_id(self, logical_switch_id):
        """Sets the logical_switch_id of this CloudVirtualMachine.

        Logical Switch ID  # noqa: E501

        :param logical_switch_id: The logical_switch_id of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._logical_switch_id = logical_switch_id

    @property
    def logical_switch_display_name(self):
        """Gets the logical_switch_display_name of this CloudVirtualMachine.  # noqa: E501

        Logical Switch display name  # noqa: E501

        :return: The logical_switch_display_name of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_display_name

    @logical_switch_display_name.setter
    def logical_switch_display_name(self, logical_switch_display_name):
        """Sets the logical_switch_display_name of this CloudVirtualMachine.

        Logical Switch display name  # noqa: E501

        :param logical_switch_display_name: The logical_switch_display_name of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._logical_switch_display_name = logical_switch_display_name

    @property
    def private_ip(self):
        """Gets the private_ip of this CloudVirtualMachine.  # noqa: E501

        Private IP address of the virtual machine  # noqa: E501

        :return: The private_ip of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this CloudVirtualMachine.

        Private IP address of the virtual machine  # noqa: E501

        :param private_ip: The private_ip of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def threat_state(self):
        """Gets the threat_state of this CloudVirtualMachine.  # noqa: E501

        Indicates the threat state of the VM. NORMAL - This state implies no threat has been detected and VM is functioning as expected. THREAT - This state implies quarantine enabling threat has been detected. INVALID - This state implies either VM is unmanaged or threat related information is not available.   # noqa: E501

        :return: The threat_state of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._threat_state

    @threat_state.setter
    def threat_state(self, threat_state):
        """Sets the threat_state of this CloudVirtualMachine.

        Indicates the threat state of the VM. NORMAL - This state implies no threat has been detected and VM is functioning as expected. THREAT - This state implies quarantine enabling threat has been detected. INVALID - This state implies either VM is unmanaged or threat related information is not available.   # noqa: E501

        :param threat_state: The threat_state of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["NORMAL", "THREAT", "INVALID"]  # noqa: E501
        if threat_state not in allowed_values:
            raise ValueError(
                "Invalid value for `threat_state` ({0}), must be one of {1}"  # noqa: E501
                .format(threat_state, allowed_values)
            )

        self._threat_state = threat_state

    @property
    def os_details(self):
        """Gets the os_details of this CloudVirtualMachine.  # noqa: E501

        Operating system details  # noqa: E501

        :return: The os_details of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._os_details

    @os_details.setter
    def os_details(self, os_details):
        """Sets the os_details of this CloudVirtualMachine.

        Operating system details  # noqa: E501

        :param os_details: The os_details of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._os_details = os_details

    @property
    def managed_by_nsx(self):
        """Gets the managed_by_nsx of this CloudVirtualMachine.  # noqa: E501

        Indicate if vm is managed by NSX or not  # noqa: E501

        :return: The managed_by_nsx of this CloudVirtualMachine.  # noqa: E501
        :rtype: bool
        """
        return self._managed_by_nsx

    @managed_by_nsx.setter
    def managed_by_nsx(self, managed_by_nsx):
        """Sets the managed_by_nsx of this CloudVirtualMachine.

        Indicate if vm is managed by NSX or not  # noqa: E501

        :param managed_by_nsx: The managed_by_nsx of this CloudVirtualMachine.  # noqa: E501
        :type: bool
        """

        self._managed_by_nsx = managed_by_nsx

    @property
    def quarantine_state(self):
        """Gets the quarantine_state of this CloudVirtualMachine.  # noqa: E501

        Indicates the quarantine state of the VM. QUARANTINED - This state implies VM is moved to quarantine security group because some threat has been detected. NOT_QUARANTINED - This state implies no quarantine action has been taken. UNKNOWN - This state implies either quarantine policy is disabled or quarantine information is not available. OVERRIDDEN - This state implies VM is associated with vm_override_sg which overrides any action based on threat detection.   # noqa: E501

        :return: The quarantine_state of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_state

    @quarantine_state.setter
    def quarantine_state(self, quarantine_state):
        """Sets the quarantine_state of this CloudVirtualMachine.

        Indicates the quarantine state of the VM. QUARANTINED - This state implies VM is moved to quarantine security group because some threat has been detected. NOT_QUARANTINED - This state implies no quarantine action has been taken. UNKNOWN - This state implies either quarantine policy is disabled or quarantine information is not available. OVERRIDDEN - This state implies VM is associated with vm_override_sg which overrides any action based on threat detection.   # noqa: E501

        :param quarantine_state: The quarantine_state of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["QUARANTINED", "NOT_QUARANTINED", "UNKNOWN", "OVERRIDDEN"]  # noqa: E501
        if quarantine_state not in allowed_values:
            raise ValueError(
                "Invalid value for `quarantine_state` ({0}), must be one of {1}"  # noqa: E501
                .format(quarantine_state, allowed_values)
            )

        self._quarantine_state = quarantine_state

    @property
    def cloud_tags(self):
        """Gets the cloud_tags of this CloudVirtualMachine.  # noqa: E501

        Cloud tags for the virtual machine  # noqa: E501

        :return: The cloud_tags of this CloudVirtualMachine.  # noqa: E501
        :rtype: list[CloudTag]
        """
        return self._cloud_tags

    @cloud_tags.setter
    def cloud_tags(self, cloud_tags):
        """Sets the cloud_tags of this CloudVirtualMachine.

        Cloud tags for the virtual machine  # noqa: E501

        :param cloud_tags: The cloud_tags of this CloudVirtualMachine.  # noqa: E501
        :type: list[CloudTag]
        """

        self._cloud_tags = cloud_tags

    @property
    def public_ip(self):
        """Gets the public_ip of this CloudVirtualMachine.  # noqa: E501

        Public IP address of the virtual machine  # noqa: E501

        :return: The public_ip of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this CloudVirtualMachine.

        Public IP address of the virtual machine  # noqa: E501

        :param public_ip: The public_ip of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def os_type(self):
        """Gets the os_type of this CloudVirtualMachine.  # noqa: E501

        Operating system of the virtual machine  # noqa: E501

        :return: The os_type of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CloudVirtualMachine.

        Operating system of the virtual machine  # noqa: E501

        :param os_type: The os_type of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def agent_version(self):
        """Gets the agent_version of this CloudVirtualMachine.  # noqa: E501

        Agent version details  # noqa: E501

        :return: The agent_version of this CloudVirtualMachine.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this CloudVirtualMachine.

        Agent version details  # noqa: E501

        :param agent_version: The agent_version of this CloudVirtualMachine.  # noqa: E501
        :type: str
        """

        self._agent_version = agent_version

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, CloudVirtualMachine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
