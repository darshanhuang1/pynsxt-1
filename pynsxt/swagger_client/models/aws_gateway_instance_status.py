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


class AwsGatewayInstanceStatus(object):
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
        'gateway_tn_id': 'str',
        'gateway_ha_index': 'int',
        'error_message': 'str',
        'gateway_name': 'str',
        'gateway_status': 'str',
        'gateway_instance_id': 'str',
        'is_gateway_active': 'bool',
        'public_ip': 'str',
        'deployment_step': 'str',
        'error_code': 'int',
        'private_ip': 'str',
        'gateway_node_id': 'str'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'gateway_tn_id': 'gateway_tn_id',
        'gateway_ha_index': 'gateway_ha_index',
        'error_message': 'error_message',
        'gateway_name': 'gateway_name',
        'gateway_status': 'gateway_status',
        'gateway_instance_id': 'gateway_instance_id',
        'is_gateway_active': 'is_gateway_active',
        'public_ip': 'public_ip',
        'deployment_step': 'deployment_step',
        'error_code': 'error_code',
        'private_ip': 'private_ip',
        'gateway_node_id': 'gateway_node_id'
    }

    def __init__(self, _self=None, links=None, schema=None, gateway_tn_id=None, gateway_ha_index=None, error_message=None, gateway_name=None, gateway_status=None, gateway_instance_id=None, is_gateway_active=None, public_ip=None, deployment_step=None, error_code=None, private_ip=None, gateway_node_id=None):  # noqa: E501
        """AwsGatewayInstanceStatus - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._gateway_tn_id = None
        self._gateway_ha_index = None
        self._error_message = None
        self._gateway_name = None
        self._gateway_status = None
        self._gateway_instance_id = None
        self._is_gateway_active = None
        self._public_ip = None
        self._deployment_step = None
        self._error_code = None
        self._private_ip = None
        self._gateway_node_id = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if gateway_tn_id is not None:
            self.gateway_tn_id = gateway_tn_id
        if gateway_ha_index is not None:
            self.gateway_ha_index = gateway_ha_index
        if error_message is not None:
            self.error_message = error_message
        if gateway_name is not None:
            self.gateway_name = gateway_name
        if gateway_status is not None:
            self.gateway_status = gateway_status
        if gateway_instance_id is not None:
            self.gateway_instance_id = gateway_instance_id
        if is_gateway_active is not None:
            self.is_gateway_active = is_gateway_active
        if public_ip is not None:
            self.public_ip = public_ip
        if deployment_step is not None:
            self.deployment_step = deployment_step
        if error_code is not None:
            self.error_code = error_code
        if private_ip is not None:
            self.private_ip = private_ip
        if gateway_node_id is not None:
            self.gateway_node_id = gateway_node_id

    @property
    def _self(self):
        """Gets the _self of this AwsGatewayInstanceStatus.  # noqa: E501


        :return: The _self of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this AwsGatewayInstanceStatus.


        :param _self: The _self of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this AwsGatewayInstanceStatus.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AwsGatewayInstanceStatus.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this AwsGatewayInstanceStatus.  # noqa: E501


        :return: The schema of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this AwsGatewayInstanceStatus.


        :param schema: The schema of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def gateway_tn_id(self):
        """Gets the gateway_tn_id of this AwsGatewayInstanceStatus.  # noqa: E501

        NSX transport node id of the public cloud gateway  # noqa: E501

        :return: The gateway_tn_id of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._gateway_tn_id

    @gateway_tn_id.setter
    def gateway_tn_id(self, gateway_tn_id):
        """Sets the gateway_tn_id of this AwsGatewayInstanceStatus.

        NSX transport node id of the public cloud gateway  # noqa: E501

        :param gateway_tn_id: The gateway_tn_id of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._gateway_tn_id = gateway_tn_id

    @property
    def gateway_ha_index(self):
        """Gets the gateway_ha_index of this AwsGatewayInstanceStatus.  # noqa: E501

        Index of HA that indicates whether gateway is primary or secondary. If index is 0, then it is primary gateway. Else secondary gateway.   # noqa: E501

        :return: The gateway_ha_index of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: int
        """
        return self._gateway_ha_index

    @gateway_ha_index.setter
    def gateway_ha_index(self, gateway_ha_index):
        """Sets the gateway_ha_index of this AwsGatewayInstanceStatus.

        Index of HA that indicates whether gateway is primary or secondary. If index is 0, then it is primary gateway. Else secondary gateway.   # noqa: E501

        :param gateway_ha_index: The gateway_ha_index of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: int
        """

        self._gateway_ha_index = gateway_ha_index

    @property
    def error_message(self):
        """Gets the error_message of this AwsGatewayInstanceStatus.  # noqa: E501

        Error message for gateway deployment/undeployment failure  # noqa: E501

        :return: The error_message of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this AwsGatewayInstanceStatus.

        Error message for gateway deployment/undeployment failure  # noqa: E501

        :param error_message: The error_message of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def gateway_name(self):
        """Gets the gateway_name of this AwsGatewayInstanceStatus.  # noqa: E501

        Name of the gateway instance  # noqa: E501

        :return: The gateway_name of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._gateway_name

    @gateway_name.setter
    def gateway_name(self, gateway_name):
        """Sets the gateway_name of this AwsGatewayInstanceStatus.

        Name of the gateway instance  # noqa: E501

        :param gateway_name: The gateway_name of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._gateway_name = gateway_name

    @property
    def gateway_status(self):
        """Gets the gateway_status of this AwsGatewayInstanceStatus.  # noqa: E501

        Gateway instance status  # noqa: E501

        :return: The gateway_status of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._gateway_status

    @gateway_status.setter
    def gateway_status(self, gateway_status):
        """Sets the gateway_status of this AwsGatewayInstanceStatus.

        Gateway instance status  # noqa: E501

        :param gateway_status: The gateway_status of this AwsGatewayInstanceStatus.  # noqa: E501
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
    def gateway_instance_id(self):
        """Gets the gateway_instance_id of this AwsGatewayInstanceStatus.  # noqa: E501

        ID of the gateway instance  # noqa: E501

        :return: The gateway_instance_id of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._gateway_instance_id

    @gateway_instance_id.setter
    def gateway_instance_id(self, gateway_instance_id):
        """Sets the gateway_instance_id of this AwsGatewayInstanceStatus.

        ID of the gateway instance  # noqa: E501

        :param gateway_instance_id: The gateway_instance_id of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._gateway_instance_id = gateway_instance_id

    @property
    def is_gateway_active(self):
        """Gets the is_gateway_active of this AwsGatewayInstanceStatus.  # noqa: E501

        Flag to identify if this is an active gateway  # noqa: E501

        :return: The is_gateway_active of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_gateway_active

    @is_gateway_active.setter
    def is_gateway_active(self, is_gateway_active):
        """Sets the is_gateway_active of this AwsGatewayInstanceStatus.

        Flag to identify if this is an active gateway  # noqa: E501

        :param is_gateway_active: The is_gateway_active of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: bool
        """

        self._is_gateway_active = is_gateway_active

    @property
    def public_ip(self):
        """Gets the public_ip of this AwsGatewayInstanceStatus.  # noqa: E501

        Public IP address of the virtual machine  # noqa: E501

        :return: The public_ip of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this AwsGatewayInstanceStatus.

        Public IP address of the virtual machine  # noqa: E501

        :param public_ip: The public_ip of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def deployment_step(self):
        """Gets the deployment_step of this AwsGatewayInstanceStatus.  # noqa: E501

        Different states of gateway deployment  # noqa: E501

        :return: The deployment_step of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._deployment_step

    @deployment_step.setter
    def deployment_step(self, deployment_step):
        """Sets the deployment_step of this AwsGatewayInstanceStatus.

        Different states of gateway deployment  # noqa: E501

        :param deployment_step: The deployment_step of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATING_SECURITY_GROUPS", "LAUNCHING_GATEWAY", "ATTACHING_NETWORK_INTERFACES", "CONFIGURING_GATEWAY", "CREATING_LOGICAL_NETWORK_CONSTRUCTS", "DEPLOYMENT_SUCCESSFUL", "DEPLOYMENT_FAILED", "UNCONFIGURING_GATEWAY", "RELEASING_EIPS", "TERMINATING_GATEWAY", "DELETING_SECURITY_GROUPS", "UNDEPLOYMENT_SUCCESSFUL", "UNDEPLOYMENT_FAILED", "NOT_APPLICABLE"]  # noqa: E501
        if deployment_step not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_step` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_step, allowed_values)
            )

        self._deployment_step = deployment_step

    @property
    def error_code(self):
        """Gets the error_code of this AwsGatewayInstanceStatus.  # noqa: E501

        Error code for gateway deployment/undeployment failure  # noqa: E501

        :return: The error_code of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this AwsGatewayInstanceStatus.

        Error code for gateway deployment/undeployment failure  # noqa: E501

        :param error_code: The error_code of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def private_ip(self):
        """Gets the private_ip of this AwsGatewayInstanceStatus.  # noqa: E501

        Private IP address of the virtual machine  # noqa: E501

        :return: The private_ip of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this AwsGatewayInstanceStatus.

        Private IP address of the virtual machine  # noqa: E501

        :param private_ip: The private_ip of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def gateway_node_id(self):
        """Gets the gateway_node_id of this AwsGatewayInstanceStatus.  # noqa: E501

        NSX Node ID of the public cloud gateway  # noqa: E501

        :return: The gateway_node_id of this AwsGatewayInstanceStatus.  # noqa: E501
        :rtype: str
        """
        return self._gateway_node_id

    @gateway_node_id.setter
    def gateway_node_id(self, gateway_node_id):
        """Sets the gateway_node_id of this AwsGatewayInstanceStatus.

        NSX Node ID of the public cloud gateway  # noqa: E501

        :param gateway_node_id: The gateway_node_id of this AwsGatewayInstanceStatus.  # noqa: E501
        :type: str
        """

        self._gateway_node_id = gateway_node_id

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
        if not isinstance(other, AwsGatewayInstanceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
