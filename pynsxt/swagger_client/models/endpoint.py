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


class Endpoint(object):
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
        'ip': 'str',
        'subnet_mask': 'str',
        'default_gateway': 'str',
        'label': 'int',
        'device_name': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'subnet_mask': 'subnet_mask',
        'default_gateway': 'default_gateway',
        'label': 'label',
        'device_name': 'device_name'
    }

    def __init__(self, ip=None, subnet_mask=None, default_gateway=None, label=None, device_name=None):  # noqa: E501
        """Endpoint - a model defined in Swagger"""  # noqa: E501

        self._ip = None
        self._subnet_mask = None
        self._default_gateway = None
        self._label = None
        self._device_name = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask
        if default_gateway is not None:
            self.default_gateway = default_gateway
        if label is not None:
            self.label = label
        if device_name is not None:
            self.device_name = device_name

    @property
    def ip(self):
        """Gets the ip of this Endpoint.  # noqa: E501

        Depending upon the EndpointIpConfig used in HostSwitch, IP could be allocated either from DHCP (default) or from Static IP Pool.  # noqa: E501

        :return: The ip of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Endpoint.

        Depending upon the EndpointIpConfig used in HostSwitch, IP could be allocated either from DHCP (default) or from Static IP Pool.  # noqa: E501

        :param ip: The ip of this Endpoint.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this Endpoint.  # noqa: E501

        Subnet mask  # noqa: E501

        :return: The subnet_mask of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this Endpoint.

        Subnet mask  # noqa: E501

        :param subnet_mask: The subnet_mask of this Endpoint.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

    @property
    def default_gateway(self):
        """Gets the default_gateway of this Endpoint.  # noqa: E501

        Gateway IP  # noqa: E501

        :return: The default_gateway of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._default_gateway

    @default_gateway.setter
    def default_gateway(self, default_gateway):
        """Sets the default_gateway of this Endpoint.

        Gateway IP  # noqa: E501

        :param default_gateway: The default_gateway of this Endpoint.  # noqa: E501
        :type: str
        """

        self._default_gateway = default_gateway

    @property
    def label(self):
        """Gets the label of this Endpoint.  # noqa: E501

        Unique label for this Endpoint  # noqa: E501

        :return: The label of this Endpoint.  # noqa: E501
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Endpoint.

        Unique label for this Endpoint  # noqa: E501

        :param label: The label of this Endpoint.  # noqa: E501
        :type: int
        """

        self._label = label

    @property
    def device_name(self):
        """Gets the device_name of this Endpoint.  # noqa: E501

        Name of the virtual tunnel endpoint  # noqa: E501

        :return: The device_name of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this Endpoint.

        Name of the virtual tunnel endpoint  # noqa: E501

        :param device_name: The device_name of this Endpoint.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

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
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
