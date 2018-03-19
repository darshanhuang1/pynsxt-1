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

from swagger_client.models.backup_schedule import BackupSchedule  # noqa: F401,E501


class IntervalBackupSchedule(object):
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
        'seconds_between_backups': 'int'
    }

    attribute_map = {
        'seconds_between_backups': 'seconds_between_backups'
    }

    def __init__(self, seconds_between_backups=3600):  # noqa: E501
        """IntervalBackupSchedule - a model defined in Swagger"""  # noqa: E501

        self._seconds_between_backups = None
        self.discriminator = None

        self.seconds_between_backups = seconds_between_backups

    @property
    def seconds_between_backups(self):
        """Gets the seconds_between_backups of this IntervalBackupSchedule.  # noqa: E501


        :return: The seconds_between_backups of this IntervalBackupSchedule.  # noqa: E501
        :rtype: int
        """
        return self._seconds_between_backups

    @seconds_between_backups.setter
    def seconds_between_backups(self, seconds_between_backups):
        """Sets the seconds_between_backups of this IntervalBackupSchedule.


        :param seconds_between_backups: The seconds_between_backups of this IntervalBackupSchedule.  # noqa: E501
        :type: int
        """
        if seconds_between_backups is None:
            raise ValueError("Invalid value for `seconds_between_backups`, must not be `None`")  # noqa: E501
        if seconds_between_backups is not None and seconds_between_backups > 86400:  # noqa: E501
            raise ValueError("Invalid value for `seconds_between_backups`, must be a value less than or equal to `86400`")  # noqa: E501
        if seconds_between_backups is not None and seconds_between_backups < 300:  # noqa: E501
            raise ValueError("Invalid value for `seconds_between_backups`, must be a value greater than or equal to `300`")  # noqa: E501

        self._seconds_between_backups = seconds_between_backups

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
        if not isinstance(other, IntervalBackupSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
