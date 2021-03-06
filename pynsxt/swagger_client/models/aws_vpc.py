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

from swagger_client.models.aws_gateway_info import AwsGatewayInfo  # noqa: F401,E501
from swagger_client.models.instance_stats import InstanceStats  # noqa: F401,E501
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501
from swagger_client.models.transport_zone_info import TransportZoneInfo  # noqa: F401,E501


class AwsVpc(object):
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
        'gateway_info': 'AwsGatewayInfo',
        'ami_id': 'str',
        'instance_stats': 'InstanceStats',
        'region_id': 'str',
        'op_status': 'str',
        'cidr': 'str',
        'is_management_vpc': 'bool',
        'transport_zones': 'list[TransportZoneInfo]'
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
        'gateway_info': 'gateway_info',
        'ami_id': 'ami_id',
        'instance_stats': 'instance_stats',
        'region_id': 'region_id',
        'op_status': 'op_status',
        'cidr': 'cidr',
        'is_management_vpc': 'is_management_vpc',
        'transport_zones': 'transport_zones'
    }

    def __init__(self, _self=None, links=None, schema=None, revision=None, system_owned=None, display_name=None, description=None, tags=None, create_user=None, protection=None, create_time=None, last_modified_time=None, last_modified_user=None, id=None, resource_type=None, gateway_info=None, ami_id=None, instance_stats=None, region_id=None, op_status=None, cidr=None, is_management_vpc=False, transport_zones=None):  # noqa: E501
        """AwsVpc - a model defined in Swagger"""  # noqa: E501

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
        self._gateway_info = None
        self._ami_id = None
        self._instance_stats = None
        self._region_id = None
        self._op_status = None
        self._cidr = None
        self._is_management_vpc = None
        self._transport_zones = None
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
        if gateway_info is not None:
            self.gateway_info = gateway_info
        if ami_id is not None:
            self.ami_id = ami_id
        if instance_stats is not None:
            self.instance_stats = instance_stats
        if region_id is not None:
            self.region_id = region_id
        if op_status is not None:
            self.op_status = op_status
        if cidr is not None:
            self.cidr = cidr
        if is_management_vpc is not None:
            self.is_management_vpc = is_management_vpc
        if transport_zones is not None:
            self.transport_zones = transport_zones

    @property
    def _self(self):
        """Gets the _self of this AwsVpc.  # noqa: E501


        :return: The _self of this AwsVpc.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this AwsVpc.


        :param _self: The _self of this AwsVpc.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this AwsVpc.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this AwsVpc.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AwsVpc.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this AwsVpc.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this AwsVpc.  # noqa: E501


        :return: The schema of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this AwsVpc.


        :param schema: The schema of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def revision(self):
        """Gets the revision of this AwsVpc.  # noqa: E501

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :return: The revision of this AwsVpc.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this AwsVpc.

        The _revision property describes the current revision of the resource. To prevent clients from overwriting each other's changes, PUT operations must include the current _revision of the resource, which clients should obtain by issuing a GET operation. If the _revision provided in a PUT request is missing or stale, the operation will be rejected.  # noqa: E501

        :param revision: The revision of this AwsVpc.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def system_owned(self):
        """Gets the system_owned of this AwsVpc.  # noqa: E501

        Indicates system owned resource  # noqa: E501

        :return: The system_owned of this AwsVpc.  # noqa: E501
        :rtype: bool
        """
        return self._system_owned

    @system_owned.setter
    def system_owned(self, system_owned):
        """Sets the system_owned of this AwsVpc.

        Indicates system owned resource  # noqa: E501

        :param system_owned: The system_owned of this AwsVpc.  # noqa: E501
        :type: bool
        """

        self._system_owned = system_owned

    @property
    def display_name(self):
        """Gets the display_name of this AwsVpc.  # noqa: E501

        Defaults to ID if not set  # noqa: E501

        :return: The display_name of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AwsVpc.

        Defaults to ID if not set  # noqa: E501

        :param display_name: The display_name of this AwsVpc.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this AwsVpc.  # noqa: E501

        Description of this resource  # noqa: E501

        :return: The description of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwsVpc.

        Description of this resource  # noqa: E501

        :param description: The description of this AwsVpc.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this AwsVpc.  # noqa: E501

        Opaque identifiers meaningful to the API user  # noqa: E501

        :return: The tags of this AwsVpc.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AwsVpc.

        Opaque identifiers meaningful to the API user  # noqa: E501

        :param tags: The tags of this AwsVpc.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def create_user(self):
        """Gets the create_user of this AwsVpc.  # noqa: E501

        ID of the user who created this resource  # noqa: E501

        :return: The create_user of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this AwsVpc.

        ID of the user who created this resource  # noqa: E501

        :param create_user: The create_user of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._create_user = create_user

    @property
    def protection(self):
        """Gets the protection of this AwsVpc.  # noqa: E501

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :return: The protection of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._protection

    @protection.setter
    def protection(self, protection):
        """Sets the protection of this AwsVpc.

        Protection status is one of the following: PROTECTED - the client who retrieved the entity is not allowed             to modify it. NOT_PROTECTED - the client who retrieved the entity is allowed                 to modify it REQUIRE_OVERRIDE - the client who retrieved the entity is a super                    user and can modify it, but only when providing                    the request header X-Allow-Overwrite=true. UNKNOWN - the _protection field could not be determined for this           entity.   # noqa: E501

        :param protection: The protection of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._protection = protection

    @property
    def create_time(self):
        """Gets the create_time of this AwsVpc.  # noqa: E501

        Timestamp of resource creation  # noqa: E501

        :return: The create_time of this AwsVpc.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AwsVpc.

        Timestamp of resource creation  # noqa: E501

        :param create_time: The create_time of this AwsVpc.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this AwsVpc.  # noqa: E501

        Timestamp of last modification  # noqa: E501

        :return: The last_modified_time of this AwsVpc.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this AwsVpc.

        Timestamp of last modification  # noqa: E501

        :param last_modified_time: The last_modified_time of this AwsVpc.  # noqa: E501
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_user(self):
        """Gets the last_modified_user of this AwsVpc.  # noqa: E501

        ID of the user who last modified this resource  # noqa: E501

        :return: The last_modified_user of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_user

    @last_modified_user.setter
    def last_modified_user(self, last_modified_user):
        """Sets the last_modified_user of this AwsVpc.

        ID of the user who last modified this resource  # noqa: E501

        :param last_modified_user: The last_modified_user of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._last_modified_user = last_modified_user

    @property
    def id(self):
        """Gets the id of this AwsVpc.  # noqa: E501

        Unique identifier of this resource  # noqa: E501

        :return: The id of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsVpc.

        Unique identifier of this resource  # noqa: E501

        :param id: The id of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_type(self):
        """Gets the resource_type of this AwsVpc.  # noqa: E501

        The type of this resource.  # noqa: E501

        :return: The resource_type of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AwsVpc.

        The type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def gateway_info(self):
        """Gets the gateway_info of this AwsVpc.  # noqa: E501

        Gateway details for the Vpc  # noqa: E501

        :return: The gateway_info of this AwsVpc.  # noqa: E501
        :rtype: AwsGatewayInfo
        """
        return self._gateway_info

    @gateway_info.setter
    def gateway_info(self, gateway_info):
        """Sets the gateway_info of this AwsVpc.

        Gateway details for the Vpc  # noqa: E501

        :param gateway_info: The gateway_info of this AwsVpc.  # noqa: E501
        :type: AwsGatewayInfo
        """

        self._gateway_info = gateway_info

    @property
    def ami_id(self):
        """Gets the ami_id of this AwsVpc.  # noqa: E501

        AMI id  # noqa: E501

        :return: The ami_id of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._ami_id

    @ami_id.setter
    def ami_id(self, ami_id):
        """Sets the ami_id of this AwsVpc.

        AMI id  # noqa: E501

        :param ami_id: The ami_id of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._ami_id = ami_id

    @property
    def instance_stats(self):
        """Gets the instance_stats of this AwsVpc.  # noqa: E501

        Managed, unmanaged and error instance counts for the Vpc  # noqa: E501

        :return: The instance_stats of this AwsVpc.  # noqa: E501
        :rtype: InstanceStats
        """
        return self._instance_stats

    @instance_stats.setter
    def instance_stats(self, instance_stats):
        """Sets the instance_stats of this AwsVpc.

        Managed, unmanaged and error instance counts for the Vpc  # noqa: E501

        :param instance_stats: The instance_stats of this AwsVpc.  # noqa: E501
        :type: InstanceStats
        """

        self._instance_stats = instance_stats

    @property
    def region_id(self):
        """Gets the region_id of this AwsVpc.  # noqa: E501

        Id of the AWS region  # noqa: E501

        :return: The region_id of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AwsVpc.

        Id of the AWS region  # noqa: E501

        :param region_id: The region_id of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def op_status(self):
        """Gets the op_status of this AwsVpc.  # noqa: E501

        State of the Vpc  # noqa: E501

        :return: The op_status of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._op_status

    @op_status.setter
    def op_status(self, op_status):
        """Sets the op_status of this AwsVpc.

        State of the Vpc  # noqa: E501

        :param op_status: The op_status of this AwsVpc.  # noqa: E501
        :type: str
        """
        allowed_values = ["NSX_MANAGED", "NSX_UNMANAGED"]  # noqa: E501
        if op_status not in allowed_values:
            raise ValueError(
                "Invalid value for `op_status` ({0}), must be one of {1}"  # noqa: E501
                .format(op_status, allowed_values)
            )

        self._op_status = op_status

    @property
    def cidr(self):
        """Gets the cidr of this AwsVpc.  # noqa: E501

        IPV4 CIDR Block for the Vpc  # noqa: E501

        :return: The cidr of this AwsVpc.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this AwsVpc.

        IPV4 CIDR Block for the Vpc  # noqa: E501

        :param cidr: The cidr of this AwsVpc.  # noqa: E501
        :type: str
        """

        self._cidr = cidr

    @property
    def is_management_vpc(self):
        """Gets the is_management_vpc of this AwsVpc.  # noqa: E501

        Flag to identify if this is the management Vpc  # noqa: E501

        :return: The is_management_vpc of this AwsVpc.  # noqa: E501
        :rtype: bool
        """
        return self._is_management_vpc

    @is_management_vpc.setter
    def is_management_vpc(self, is_management_vpc):
        """Sets the is_management_vpc of this AwsVpc.

        Flag to identify if this is the management Vpc  # noqa: E501

        :param is_management_vpc: The is_management_vpc of this AwsVpc.  # noqa: E501
        :type: bool
        """

        self._is_management_vpc = is_management_vpc

    @property
    def transport_zones(self):
        """Gets the transport_zones of this AwsVpc.  # noqa: E501

        Transport zones for the Vpc  # noqa: E501

        :return: The transport_zones of this AwsVpc.  # noqa: E501
        :rtype: list[TransportZoneInfo]
        """
        return self._transport_zones

    @transport_zones.setter
    def transport_zones(self, transport_zones):
        """Sets the transport_zones of this AwsVpc.

        Transport zones for the Vpc  # noqa: E501

        :param transport_zones: The transport_zones of this AwsVpc.  # noqa: E501
        :type: list[TransportZoneInfo]
        """

        self._transport_zones = transport_zones

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
        if not isinstance(other, AwsVpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
