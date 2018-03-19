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

from swagger_client.models.csv_list_result import CsvListResult  # noqa: F401,E501
from swagger_client.models.mac_table_csv_record import MacTableCsvRecord  # noqa: F401,E501


class MacAddressCsvListResult(object):
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
        'file_name': 'str',
        'last_update_timestamp': 'int',
        'results': 'list[MacTableCsvRecord]'
    }

    attribute_map = {
        'file_name': 'file_name',
        'last_update_timestamp': 'last_update_timestamp',
        'results': 'results'
    }

    def __init__(self, file_name=None, last_update_timestamp=None, results=None):  # noqa: E501
        """MacAddressCsvListResult - a model defined in Swagger"""  # noqa: E501

        self._file_name = None
        self._last_update_timestamp = None
        self._results = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if results is not None:
            self.results = results

    @property
    def file_name(self):
        """Gets the file_name of this MacAddressCsvListResult.  # noqa: E501

        File name set by HTTP server if API  returns CSV result as a file.  # noqa: E501

        :return: The file_name of this MacAddressCsvListResult.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this MacAddressCsvListResult.

        File name set by HTTP server if API  returns CSV result as a file.  # noqa: E501

        :param file_name: The file_name of this MacAddressCsvListResult.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this MacAddressCsvListResult.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this MacAddressCsvListResult.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this MacAddressCsvListResult.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this MacAddressCsvListResult.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def results(self):
        """Gets the results of this MacAddressCsvListResult.  # noqa: E501


        :return: The results of this MacAddressCsvListResult.  # noqa: E501
        :rtype: list[MacTableCsvRecord]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this MacAddressCsvListResult.


        :param results: The results of this MacAddressCsvListResult.  # noqa: E501
        :type: list[MacTableCsvRecord]
        """

        self._results = results

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
        if not isinstance(other, MacAddressCsvListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
