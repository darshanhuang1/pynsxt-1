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
from swagger_client.models.remote_file_server import RemoteFileServer  # noqa: F401,E501


class BackupConfiguration(object):
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
        'backup_schedule': 'BackupSchedule',
        'remote_file_server': 'RemoteFileServer',
        'passphrase': 'str',
        'backup_enabled': 'bool',
        'inventory_summary_interval': 'int'
    }

    attribute_map = {
        'backup_schedule': 'backup_schedule',
        'remote_file_server': 'remote_file_server',
        'passphrase': 'passphrase',
        'backup_enabled': 'backup_enabled',
        'inventory_summary_interval': 'inventory_summary_interval'
    }

    def __init__(self, backup_schedule=None, remote_file_server=None, passphrase=None, backup_enabled=False, inventory_summary_interval=300):  # noqa: E501
        """BackupConfiguration - a model defined in Swagger"""  # noqa: E501

        self._backup_schedule = None
        self._remote_file_server = None
        self._passphrase = None
        self._backup_enabled = None
        self._inventory_summary_interval = None
        self.discriminator = None

        if backup_schedule is not None:
            self.backup_schedule = backup_schedule
        self.remote_file_server = remote_file_server
        if passphrase is not None:
            self.passphrase = passphrase
        self.backup_enabled = backup_enabled
        self.inventory_summary_interval = inventory_summary_interval

    @property
    def backup_schedule(self):
        """Gets the backup_schedule of this BackupConfiguration.  # noqa: E501

        Set when backups should be taken - on a weekly schedule or at regular intervals.  # noqa: E501

        :return: The backup_schedule of this BackupConfiguration.  # noqa: E501
        :rtype: BackupSchedule
        """
        return self._backup_schedule

    @backup_schedule.setter
    def backup_schedule(self, backup_schedule):
        """Sets the backup_schedule of this BackupConfiguration.

        Set when backups should be taken - on a weekly schedule or at regular intervals.  # noqa: E501

        :param backup_schedule: The backup_schedule of this BackupConfiguration.  # noqa: E501
        :type: BackupSchedule
        """

        self._backup_schedule = backup_schedule

    @property
    def remote_file_server(self):
        """Gets the remote_file_server of this BackupConfiguration.  # noqa: E501

        The server to which backups will be sent.  # noqa: E501

        :return: The remote_file_server of this BackupConfiguration.  # noqa: E501
        :rtype: RemoteFileServer
        """
        return self._remote_file_server

    @remote_file_server.setter
    def remote_file_server(self, remote_file_server):
        """Sets the remote_file_server of this BackupConfiguration.

        The server to which backups will be sent.  # noqa: E501

        :param remote_file_server: The remote_file_server of this BackupConfiguration.  # noqa: E501
        :type: RemoteFileServer
        """
        if remote_file_server is None:
            raise ValueError("Invalid value for `remote_file_server`, must not be `None`")  # noqa: E501

        self._remote_file_server = remote_file_server

    @property
    def passphrase(self):
        """Gets the passphrase of this BackupConfiguration.  # noqa: E501

        Passphrase used to encrypt backup files.  # noqa: E501

        :return: The passphrase of this BackupConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this BackupConfiguration.

        Passphrase used to encrypt backup files.  # noqa: E501

        :param passphrase: The passphrase of this BackupConfiguration.  # noqa: E501
        :type: str
        """

        self._passphrase = passphrase

    @property
    def backup_enabled(self):
        """Gets the backup_enabled of this BackupConfiguration.  # noqa: E501

        true if automated backup is enabled  # noqa: E501

        :return: The backup_enabled of this BackupConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._backup_enabled

    @backup_enabled.setter
    def backup_enabled(self, backup_enabled):
        """Sets the backup_enabled of this BackupConfiguration.

        true if automated backup is enabled  # noqa: E501

        :param backup_enabled: The backup_enabled of this BackupConfiguration.  # noqa: E501
        :type: bool
        """
        if backup_enabled is None:
            raise ValueError("Invalid value for `backup_enabled`, must not be `None`")  # noqa: E501

        self._backup_enabled = backup_enabled

    @property
    def inventory_summary_interval(self):
        """Gets the inventory_summary_interval of this BackupConfiguration.  # noqa: E501

        The minimum number of seconds between each upload of the inventory summary to backup server.  # noqa: E501

        :return: The inventory_summary_interval of this BackupConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._inventory_summary_interval

    @inventory_summary_interval.setter
    def inventory_summary_interval(self, inventory_summary_interval):
        """Sets the inventory_summary_interval of this BackupConfiguration.

        The minimum number of seconds between each upload of the inventory summary to backup server.  # noqa: E501

        :param inventory_summary_interval: The inventory_summary_interval of this BackupConfiguration.  # noqa: E501
        :type: int
        """
        if inventory_summary_interval is None:
            raise ValueError("Invalid value for `inventory_summary_interval`, must not be `None`")  # noqa: E501
        if inventory_summary_interval is not None and inventory_summary_interval > 3600:  # noqa: E501
            raise ValueError("Invalid value for `inventory_summary_interval`, must be a value less than or equal to `3600`")  # noqa: E501
        if inventory_summary_interval is not None and inventory_summary_interval < 30:  # noqa: E501
            raise ValueError("Invalid value for `inventory_summary_interval`, must be a value greater than or equal to `30`")  # noqa: E501

        self._inventory_summary_interval = inventory_summary_interval

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
        if not isinstance(other, BackupConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
