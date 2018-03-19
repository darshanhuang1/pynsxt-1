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


class UpgradeHistory(object):
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
        'timestamp': 'int',
        'target_version': 'str',
        'initial_version': 'str',
        'upgrade_status': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'target_version': 'target_version',
        'initial_version': 'initial_version',
        'upgrade_status': 'upgrade_status'
    }

    def __init__(self, timestamp=None, target_version=None, initial_version=None, upgrade_status=None):  # noqa: E501
        """UpgradeHistory - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._target_version = None
        self._initial_version = None
        self._upgrade_status = None
        self.discriminator = None

        self.timestamp = timestamp
        self.target_version = target_version
        self.initial_version = initial_version
        self.upgrade_status = upgrade_status

    @property
    def timestamp(self):
        """Gets the timestamp of this UpgradeHistory.  # noqa: E501

        Timestamp (in milliseconds since epoch) when the upgrade was performed  # noqa: E501

        :return: The timestamp of this UpgradeHistory.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpgradeHistory.

        Timestamp (in milliseconds since epoch) when the upgrade was performed  # noqa: E501

        :param timestamp: The timestamp of this UpgradeHistory.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def target_version(self):
        """Gets the target_version of this UpgradeHistory.  # noqa: E501

        Version being upgraded to  # noqa: E501

        :return: The target_version of this UpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this UpgradeHistory.

        Version being upgraded to  # noqa: E501

        :param target_version: The target_version of this UpgradeHistory.  # noqa: E501
        :type: str
        """
        if target_version is None:
            raise ValueError("Invalid value for `target_version`, must not be `None`")  # noqa: E501

        self._target_version = target_version

    @property
    def initial_version(self):
        """Gets the initial_version of this UpgradeHistory.  # noqa: E501

        Version before the upgrade started  # noqa: E501

        :return: The initial_version of this UpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._initial_version

    @initial_version.setter
    def initial_version(self, initial_version):
        """Sets the initial_version of this UpgradeHistory.

        Version before the upgrade started  # noqa: E501

        :param initial_version: The initial_version of this UpgradeHistory.  # noqa: E501
        :type: str
        """
        if initial_version is None:
            raise ValueError("Invalid value for `initial_version`, must not be `None`")  # noqa: E501

        self._initial_version = initial_version

    @property
    def upgrade_status(self):
        """Gets the upgrade_status of this UpgradeHistory.  # noqa: E501

        Status of the upgrade  # noqa: E501

        :return: The upgrade_status of this UpgradeHistory.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """Sets the upgrade_status of this UpgradeHistory.

        Status of the upgrade  # noqa: E501

        :param upgrade_status: The upgrade_status of this UpgradeHistory.  # noqa: E501
        :type: str
        """
        if upgrade_status is None:
            raise ValueError("Invalid value for `upgrade_status`, must not be `None`")  # noqa: E501
        allowed_values = ["STARTED", "SUCCESS", "FAILED"]  # noqa: E501
        if upgrade_status not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_status` ({0}), must be one of {1}"  # noqa: E501
                .format(upgrade_status, allowed_values)
            )

        self._upgrade_status = upgrade_status

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
        if not isinstance(other, UpgradeHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
