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

from swagger_client.models.lb_monitor import LbMonitor  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class LbActiveMonitor(object):
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
        'monitor_port': 'str',
        'fall_count': 'int',
        'interval': 'int',
        'rise_count': 'int',
        'timeout': 'int'
    }

    attribute_map = {
        'monitor_port': 'monitor_port',
        'fall_count': 'fall_count',
        'interval': 'interval',
        'rise_count': 'rise_count',
        'timeout': 'timeout'
    }

    def __init__(self, monitor_port=None, fall_count=3, interval=5, rise_count=3, timeout=15):  # noqa: E501
        """LbActiveMonitor - a model defined in Swagger"""  # noqa: E501

        self._monitor_port = None
        self._fall_count = None
        self._interval = None
        self._rise_count = None
        self._timeout = None
        self.discriminator = None

        if monitor_port is not None:
            self.monitor_port = monitor_port
        if fall_count is not None:
            self.fall_count = fall_count
        if interval is not None:
            self.interval = interval
        if rise_count is not None:
            self.rise_count = rise_count
        if timeout is not None:
            self.timeout = timeout

    @property
    def monitor_port(self):
        """Gets the monitor_port of this LbActiveMonitor.  # noqa: E501

        If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported.   # noqa: E501

        :return: The monitor_port of this LbActiveMonitor.  # noqa: E501
        :rtype: str
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this LbActiveMonitor.

        If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported.   # noqa: E501

        :param monitor_port: The monitor_port of this LbActiveMonitor.  # noqa: E501
        :type: str
        """

        self._monitor_port = monitor_port

    @property
    def fall_count(self):
        """Gets the fall_count of this LbActiveMonitor.  # noqa: E501

        num of consecutive checks must fail before marking it down  # noqa: E501

        :return: The fall_count of this LbActiveMonitor.  # noqa: E501
        :rtype: int
        """
        return self._fall_count

    @fall_count.setter
    def fall_count(self, fall_count):
        """Sets the fall_count of this LbActiveMonitor.

        num of consecutive checks must fail before marking it down  # noqa: E501

        :param fall_count: The fall_count of this LbActiveMonitor.  # noqa: E501
        :type: int
        """
        if fall_count is not None and fall_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `fall_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._fall_count = fall_count

    @property
    def interval(self):
        """Gets the interval of this LbActiveMonitor.  # noqa: E501

        the frequency at which the system issues the monitor check (in second)  # noqa: E501

        :return: The interval of this LbActiveMonitor.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this LbActiveMonitor.

        the frequency at which the system issues the monitor check (in second)  # noqa: E501

        :param interval: The interval of this LbActiveMonitor.  # noqa: E501
        :type: int
        """
        if interval is not None and interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._interval = interval

    @property
    def rise_count(self):
        """Gets the rise_count of this LbActiveMonitor.  # noqa: E501

        num of consecutive checks must pass before marking it up  # noqa: E501

        :return: The rise_count of this LbActiveMonitor.  # noqa: E501
        :rtype: int
        """
        return self._rise_count

    @rise_count.setter
    def rise_count(self, rise_count):
        """Sets the rise_count of this LbActiveMonitor.

        num of consecutive checks must pass before marking it up  # noqa: E501

        :param rise_count: The rise_count of this LbActiveMonitor.  # noqa: E501
        :type: int
        """
        if rise_count is not None and rise_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `rise_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rise_count = rise_count

    @property
    def timeout(self):
        """Gets the timeout of this LbActiveMonitor.  # noqa: E501

        the number of seconds the target has in which to respond to the monitor request   # noqa: E501

        :return: The timeout of this LbActiveMonitor.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this LbActiveMonitor.

        the number of seconds the target has in which to respond to the monitor request   # noqa: E501

        :param timeout: The timeout of this LbActiveMonitor.  # noqa: E501
        :type: int
        """
        if timeout is not None and timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._timeout = timeout

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
        if not isinstance(other, LbActiveMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
