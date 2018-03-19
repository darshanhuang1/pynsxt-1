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

from swagger_client.models.host_switch_spec import HostSwitchSpec  # noqa: F401,E501
from swagger_client.models.preconfigured_host_switch import PreconfiguredHostSwitch  # noqa: F401,E501


class PreconfiguredHostSwitchSpec(object):
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
        'host_switches': 'list[PreconfiguredHostSwitch]'
    }

    attribute_map = {
        'host_switches': 'host_switches'
    }

    def __init__(self, host_switches=None):  # noqa: E501
        """PreconfiguredHostSwitchSpec - a model defined in Swagger"""  # noqa: E501

        self._host_switches = None
        self.discriminator = None

        self.host_switches = host_switches

    @property
    def host_switches(self):
        """Gets the host_switches of this PreconfiguredHostSwitchSpec.  # noqa: E501

        Preconfigured Transport Node host switches  # noqa: E501

        :return: The host_switches of this PreconfiguredHostSwitchSpec.  # noqa: E501
        :rtype: list[PreconfiguredHostSwitch]
        """
        return self._host_switches

    @host_switches.setter
    def host_switches(self, host_switches):
        """Sets the host_switches of this PreconfiguredHostSwitchSpec.

        Preconfigured Transport Node host switches  # noqa: E501

        :param host_switches: The host_switches of this PreconfiguredHostSwitchSpec.  # noqa: E501
        :type: list[PreconfiguredHostSwitch]
        """
        if host_switches is None:
            raise ValueError("Invalid value for `host_switches`, must not be `None`")  # noqa: E501

        self._host_switches = host_switches

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
        if not isinstance(other, PreconfiguredHostSwitchSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
