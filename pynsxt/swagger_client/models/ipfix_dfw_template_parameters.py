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


class IpfixDfwTemplateParameters(object):
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
        'source_icmp_type': 'bool',
        'icmp_code': 'bool',
        'destination_transport_port': 'bool',
        'octet_delta_count': 'bool',
        'vif_uuid': 'bool',
        'protocol_identifier': 'bool',
        'firewall_event': 'bool',
        'flow_direction': 'bool',
        'flow_end': 'bool',
        'source_transport_port': 'bool',
        'packet_delta_count': 'bool',
        'destination_address': 'bool',
        'source_address': 'bool',
        'rule_id': 'bool',
        'flow_start': 'bool'
    }

    attribute_map = {
        'source_icmp_type': 'source_icmp_type',
        'icmp_code': 'icmp_code',
        'destination_transport_port': 'destination_transport_port',
        'octet_delta_count': 'octet_delta_count',
        'vif_uuid': 'vif_uuid',
        'protocol_identifier': 'protocol_identifier',
        'firewall_event': 'firewall_event',
        'flow_direction': 'flow_direction',
        'flow_end': 'flow_end',
        'source_transport_port': 'source_transport_port',
        'packet_delta_count': 'packet_delta_count',
        'destination_address': 'destination_address',
        'source_address': 'source_address',
        'rule_id': 'rule_id',
        'flow_start': 'flow_start'
    }

    def __init__(self, source_icmp_type=True, icmp_code=True, destination_transport_port=True, octet_delta_count=True, vif_uuid=True, protocol_identifier=True, firewall_event=True, flow_direction=True, flow_end=True, source_transport_port=True, packet_delta_count=True, destination_address=True, source_address=True, rule_id=True, flow_start=True):  # noqa: E501
        """IpfixDfwTemplateParameters - a model defined in Swagger"""  # noqa: E501

        self._source_icmp_type = None
        self._icmp_code = None
        self._destination_transport_port = None
        self._octet_delta_count = None
        self._vif_uuid = None
        self._protocol_identifier = None
        self._firewall_event = None
        self._flow_direction = None
        self._flow_end = None
        self._source_transport_port = None
        self._packet_delta_count = None
        self._destination_address = None
        self._source_address = None
        self._rule_id = None
        self._flow_start = None
        self.discriminator = None

        if source_icmp_type is not None:
            self.source_icmp_type = source_icmp_type
        if icmp_code is not None:
            self.icmp_code = icmp_code
        if destination_transport_port is not None:
            self.destination_transport_port = destination_transport_port
        if octet_delta_count is not None:
            self.octet_delta_count = octet_delta_count
        if vif_uuid is not None:
            self.vif_uuid = vif_uuid
        if protocol_identifier is not None:
            self.protocol_identifier = protocol_identifier
        if firewall_event is not None:
            self.firewall_event = firewall_event
        if flow_direction is not None:
            self.flow_direction = flow_direction
        if flow_end is not None:
            self.flow_end = flow_end
        if source_transport_port is not None:
            self.source_transport_port = source_transport_port
        if packet_delta_count is not None:
            self.packet_delta_count = packet_delta_count
        if destination_address is not None:
            self.destination_address = destination_address
        if source_address is not None:
            self.source_address = source_address
        if rule_id is not None:
            self.rule_id = rule_id
        if flow_start is not None:
            self.flow_start = flow_start

    @property
    def source_icmp_type(self):
        """Gets the source_icmp_type of this IpfixDfwTemplateParameters.  # noqa: E501

        Type of the IPv4 ICMP message.   # noqa: E501

        :return: The source_icmp_type of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._source_icmp_type

    @source_icmp_type.setter
    def source_icmp_type(self, source_icmp_type):
        """Sets the source_icmp_type of this IpfixDfwTemplateParameters.

        Type of the IPv4 ICMP message.   # noqa: E501

        :param source_icmp_type: The source_icmp_type of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._source_icmp_type = source_icmp_type

    @property
    def icmp_code(self):
        """Gets the icmp_code of this IpfixDfwTemplateParameters.  # noqa: E501

        Code of the IPv4 ICMP message.   # noqa: E501

        :return: The icmp_code of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._icmp_code

    @icmp_code.setter
    def icmp_code(self, icmp_code):
        """Sets the icmp_code of this IpfixDfwTemplateParameters.

        Code of the IPv4 ICMP message.   # noqa: E501

        :param icmp_code: The icmp_code of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._icmp_code = icmp_code

    @property
    def destination_transport_port(self):
        """Gets the destination_transport_port of this IpfixDfwTemplateParameters.  # noqa: E501

        The destination transport port of a monitored network flow.   # noqa: E501

        :return: The destination_transport_port of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._destination_transport_port

    @destination_transport_port.setter
    def destination_transport_port(self, destination_transport_port):
        """Sets the destination_transport_port of this IpfixDfwTemplateParameters.

        The destination transport port of a monitored network flow.   # noqa: E501

        :param destination_transport_port: The destination_transport_port of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._destination_transport_port = destination_transport_port

    @property
    def octet_delta_count(self):
        """Gets the octet_delta_count of this IpfixDfwTemplateParameters.  # noqa: E501

        The number of octets since the previous report (if any) in incoming packets for this flow at the observation point. The number of octets include IP header(s) and payload.   # noqa: E501

        :return: The octet_delta_count of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._octet_delta_count

    @octet_delta_count.setter
    def octet_delta_count(self, octet_delta_count):
        """Sets the octet_delta_count of this IpfixDfwTemplateParameters.

        The number of octets since the previous report (if any) in incoming packets for this flow at the observation point. The number of octets include IP header(s) and payload.   # noqa: E501

        :param octet_delta_count: The octet_delta_count of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._octet_delta_count = octet_delta_count

    @property
    def vif_uuid(self):
        """Gets the vif_uuid of this IpfixDfwTemplateParameters.  # noqa: E501

        VIF UUID - enterprise specific Information Element that uniquely identifies VIF.   # noqa: E501

        :return: The vif_uuid of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._vif_uuid

    @vif_uuid.setter
    def vif_uuid(self, vif_uuid):
        """Sets the vif_uuid of this IpfixDfwTemplateParameters.

        VIF UUID - enterprise specific Information Element that uniquely identifies VIF.   # noqa: E501

        :param vif_uuid: The vif_uuid of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._vif_uuid = vif_uuid

    @property
    def protocol_identifier(self):
        """Gets the protocol_identifier of this IpfixDfwTemplateParameters.  # noqa: E501

        The value of the protocol number in the IP packet header.   # noqa: E501

        :return: The protocol_identifier of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._protocol_identifier

    @protocol_identifier.setter
    def protocol_identifier(self, protocol_identifier):
        """Sets the protocol_identifier of this IpfixDfwTemplateParameters.

        The value of the protocol number in the IP packet header.   # noqa: E501

        :param protocol_identifier: The protocol_identifier of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._protocol_identifier = protocol_identifier

    @property
    def firewall_event(self):
        """Gets the firewall_event of this IpfixDfwTemplateParameters.  # noqa: E501

        Five valid values are allowed: 1. Flow Created. 2. Flow Deleted. 3. Flow Denied. 4. Flow Alert (not used in DropKick implementation). 5. Flow Update.   # noqa: E501

        :return: The firewall_event of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._firewall_event

    @firewall_event.setter
    def firewall_event(self, firewall_event):
        """Sets the firewall_event of this IpfixDfwTemplateParameters.

        Five valid values are allowed: 1. Flow Created. 2. Flow Deleted. 3. Flow Denied. 4. Flow Alert (not used in DropKick implementation). 5. Flow Update.   # noqa: E501

        :param firewall_event: The firewall_event of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._firewall_event = firewall_event

    @property
    def flow_direction(self):
        """Gets the flow_direction of this IpfixDfwTemplateParameters.  # noqa: E501

        Two valid values are allowed: 1. 0x00: igress flow to VM. 2. 0x01: egress flow from VM.   # noqa: E501

        :return: The flow_direction of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._flow_direction

    @flow_direction.setter
    def flow_direction(self, flow_direction):
        """Sets the flow_direction of this IpfixDfwTemplateParameters.

        Two valid values are allowed: 1. 0x00: igress flow to VM. 2. 0x01: egress flow from VM.   # noqa: E501

        :param flow_direction: The flow_direction of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._flow_direction = flow_direction

    @property
    def flow_end(self):
        """Gets the flow_end of this IpfixDfwTemplateParameters.  # noqa: E501

        The absolute timestamp (seconds) of the last packet of this flow.   # noqa: E501

        :return: The flow_end of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._flow_end

    @flow_end.setter
    def flow_end(self, flow_end):
        """Sets the flow_end of this IpfixDfwTemplateParameters.

        The absolute timestamp (seconds) of the last packet of this flow.   # noqa: E501

        :param flow_end: The flow_end of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._flow_end = flow_end

    @property
    def source_transport_port(self):
        """Gets the source_transport_port of this IpfixDfwTemplateParameters.  # noqa: E501

        The source transport port of a monitored network flow.   # noqa: E501

        :return: The source_transport_port of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._source_transport_port

    @source_transport_port.setter
    def source_transport_port(self, source_transport_port):
        """Sets the source_transport_port of this IpfixDfwTemplateParameters.

        The source transport port of a monitored network flow.   # noqa: E501

        :param source_transport_port: The source_transport_port of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._source_transport_port = source_transport_port

    @property
    def packet_delta_count(self):
        """Gets the packet_delta_count of this IpfixDfwTemplateParameters.  # noqa: E501

        The number of incoming packets since the previous report (if any) for this flow at the observation point.   # noqa: E501

        :return: The packet_delta_count of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._packet_delta_count

    @packet_delta_count.setter
    def packet_delta_count(self, packet_delta_count):
        """Sets the packet_delta_count of this IpfixDfwTemplateParameters.

        The number of incoming packets since the previous report (if any) for this flow at the observation point.   # noqa: E501

        :param packet_delta_count: The packet_delta_count of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._packet_delta_count = packet_delta_count

    @property
    def destination_address(self):
        """Gets the destination_address of this IpfixDfwTemplateParameters.  # noqa: E501

        The destination IP address of a monitored network flow.   # noqa: E501

        :return: The destination_address of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """Sets the destination_address of this IpfixDfwTemplateParameters.

        The destination IP address of a monitored network flow.   # noqa: E501

        :param destination_address: The destination_address of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._destination_address = destination_address

    @property
    def source_address(self):
        """Gets the source_address of this IpfixDfwTemplateParameters.  # noqa: E501

        The source IP address of a monitored network flow.   # noqa: E501

        :return: The source_address of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """Sets the source_address of this IpfixDfwTemplateParameters.

        The source IP address of a monitored network flow.   # noqa: E501

        :param source_address: The source_address of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._source_address = source_address

    @property
    def rule_id(self):
        """Gets the rule_id of this IpfixDfwTemplateParameters.  # noqa: E501

        Firewall rule Id - enterprise specific Information Element that uniquely identifies firewall rule.   # noqa: E501

        :return: The rule_id of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this IpfixDfwTemplateParameters.

        Firewall rule Id - enterprise specific Information Element that uniquely identifies firewall rule.   # noqa: E501

        :param rule_id: The rule_id of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._rule_id = rule_id

    @property
    def flow_start(self):
        """Gets the flow_start of this IpfixDfwTemplateParameters.  # noqa: E501

        The absolute timestamp (seconds) of the first packet of this flow.   # noqa: E501

        :return: The flow_start of this IpfixDfwTemplateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._flow_start

    @flow_start.setter
    def flow_start(self, flow_start):
        """Sets the flow_start of this IpfixDfwTemplateParameters.

        The absolute timestamp (seconds) of the first packet of this flow.   # noqa: E501

        :param flow_start: The flow_start of this IpfixDfwTemplateParameters.  # noqa: E501
        :type: bool
        """

        self._flow_start = flow_start

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
        if not isinstance(other, IpfixDfwTemplateParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
