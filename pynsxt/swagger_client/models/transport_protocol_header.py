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

from swagger_client.models.icmp_echo_request_header import IcmpEchoRequestHeader  # noqa: F401,E501
from swagger_client.models.tcp_header import TcpHeader  # noqa: F401,E501
from swagger_client.models.udp_header import UdpHeader  # noqa: F401,E501


class TransportProtocolHeader(object):
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
        'icmp_echo_request_header': 'IcmpEchoRequestHeader',
        'tcp_header': 'TcpHeader',
        'udp_header': 'UdpHeader'
    }

    attribute_map = {
        'icmp_echo_request_header': 'icmp_echo_request_header',
        'tcp_header': 'tcp_header',
        'udp_header': 'udp_header'
    }

    def __init__(self, icmp_echo_request_header=None, tcp_header=None, udp_header=None):  # noqa: E501
        """TransportProtocolHeader - a model defined in Swagger"""  # noqa: E501

        self._icmp_echo_request_header = None
        self._tcp_header = None
        self._udp_header = None
        self.discriminator = None

        if icmp_echo_request_header is not None:
            self.icmp_echo_request_header = icmp_echo_request_header
        if tcp_header is not None:
            self.tcp_header = tcp_header
        if udp_header is not None:
            self.udp_header = udp_header

    @property
    def icmp_echo_request_header(self):
        """Gets the icmp_echo_request_header of this TransportProtocolHeader.  # noqa: E501

        ICMP echo request header  # noqa: E501

        :return: The icmp_echo_request_header of this TransportProtocolHeader.  # noqa: E501
        :rtype: IcmpEchoRequestHeader
        """
        return self._icmp_echo_request_header

    @icmp_echo_request_header.setter
    def icmp_echo_request_header(self, icmp_echo_request_header):
        """Sets the icmp_echo_request_header of this TransportProtocolHeader.

        ICMP echo request header  # noqa: E501

        :param icmp_echo_request_header: The icmp_echo_request_header of this TransportProtocolHeader.  # noqa: E501
        :type: IcmpEchoRequestHeader
        """

        self._icmp_echo_request_header = icmp_echo_request_header

    @property
    def tcp_header(self):
        """Gets the tcp_header of this TransportProtocolHeader.  # noqa: E501

        TCP header  # noqa: E501

        :return: The tcp_header of this TransportProtocolHeader.  # noqa: E501
        :rtype: TcpHeader
        """
        return self._tcp_header

    @tcp_header.setter
    def tcp_header(self, tcp_header):
        """Sets the tcp_header of this TransportProtocolHeader.

        TCP header  # noqa: E501

        :param tcp_header: The tcp_header of this TransportProtocolHeader.  # noqa: E501
        :type: TcpHeader
        """

        self._tcp_header = tcp_header

    @property
    def udp_header(self):
        """Gets the udp_header of this TransportProtocolHeader.  # noqa: E501

        UDP header  # noqa: E501

        :return: The udp_header of this TransportProtocolHeader.  # noqa: E501
        :rtype: UdpHeader
        """
        return self._udp_header

    @udp_header.setter
    def udp_header(self, udp_header):
        """Sets the udp_header of this TransportProtocolHeader.

        UDP header  # noqa: E501

        :param udp_header: The udp_header of this TransportProtocolHeader.  # noqa: E501
        :type: UdpHeader
        """

        self._udp_header = udp_header

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
        if not isinstance(other, TransportProtocolHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
