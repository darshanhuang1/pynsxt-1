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

from swagger_client.models.lb_statistics_counter import LbStatisticsCounter  # noqa: F401,E501


class LbVirtualServerStatistics(object):
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
        'last_update_timestamp': 'int',
        'statistics': 'LbStatisticsCounter',
        'virtual_server_id': 'str'
    }

    attribute_map = {
        'last_update_timestamp': 'last_update_timestamp',
        'statistics': 'statistics',
        'virtual_server_id': 'virtual_server_id'
    }

    def __init__(self, last_update_timestamp=None, statistics=None, virtual_server_id=None):  # noqa: E501
        """LbVirtualServerStatistics - a model defined in Swagger"""  # noqa: E501

        self._last_update_timestamp = None
        self._statistics = None
        self._virtual_server_id = None
        self.discriminator = None

        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        self.statistics = statistics
        self.virtual_server_id = virtual_server_id

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this LbVirtualServerStatistics.  # noqa: E501

        Timestamp when the data was last updated  # noqa: E501

        :return: The last_update_timestamp of this LbVirtualServerStatistics.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this LbVirtualServerStatistics.

        Timestamp when the data was last updated  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this LbVirtualServerStatistics.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def statistics(self):
        """Gets the statistics of this LbVirtualServerStatistics.  # noqa: E501

        Virtual server statistics counter  # noqa: E501

        :return: The statistics of this LbVirtualServerStatistics.  # noqa: E501
        :rtype: LbStatisticsCounter
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this LbVirtualServerStatistics.

        Virtual server statistics counter  # noqa: E501

        :param statistics: The statistics of this LbVirtualServerStatistics.  # noqa: E501
        :type: LbStatisticsCounter
        """
        if statistics is None:
            raise ValueError("Invalid value for `statistics`, must not be `None`")  # noqa: E501

        self._statistics = statistics

    @property
    def virtual_server_id(self):
        """Gets the virtual_server_id of this LbVirtualServerStatistics.  # noqa: E501

        load balancer virtual server identifier  # noqa: E501

        :return: The virtual_server_id of this LbVirtualServerStatistics.  # noqa: E501
        :rtype: str
        """
        return self._virtual_server_id

    @virtual_server_id.setter
    def virtual_server_id(self, virtual_server_id):
        """Sets the virtual_server_id of this LbVirtualServerStatistics.

        load balancer virtual server identifier  # noqa: E501

        :param virtual_server_id: The virtual_server_id of this LbVirtualServerStatistics.  # noqa: E501
        :type: str
        """
        if virtual_server_id is None:
            raise ValueError("Invalid value for `virtual_server_id`, must not be `None`")  # noqa: E501

        self._virtual_server_id = virtual_server_id

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
        if not isinstance(other, LbVirtualServerStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
