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

from swagger_client.models.csv_record import CsvRecord  # noqa: F401,E501


class FeatureUsageCsvRecord(object):
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
        'cpu_usage_count': 'int',
        'feature': 'str',
        'vm_usage_count': 'int'
    }

    attribute_map = {
        'cpu_usage_count': 'cpu_usage_count',
        'feature': 'feature',
        'vm_usage_count': 'vm_usage_count'
    }

    def __init__(self, cpu_usage_count=None, feature=None, vm_usage_count=None):  # noqa: E501
        """FeatureUsageCsvRecord - a model defined in Swagger"""  # noqa: E501

        self._cpu_usage_count = None
        self._feature = None
        self._vm_usage_count = None
        self.discriminator = None

        if cpu_usage_count is not None:
            self.cpu_usage_count = cpu_usage_count
        if feature is not None:
            self.feature = feature
        if vm_usage_count is not None:
            self.vm_usage_count = vm_usage_count

    @property
    def cpu_usage_count(self):
        """Gets the cpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        count of number of cpu sockets used by this feature  # noqa: E501

        :return: The cpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._cpu_usage_count

    @cpu_usage_count.setter
    def cpu_usage_count(self, cpu_usage_count):
        """Sets the cpu_usage_count of this FeatureUsageCsvRecord.

        count of number of cpu sockets used by this feature  # noqa: E501

        :param cpu_usage_count: The cpu_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._cpu_usage_count = cpu_usage_count

    @property
    def feature(self):
        """Gets the feature of this FeatureUsageCsvRecord.  # noqa: E501

        name of the feature  # noqa: E501

        :return: The feature of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this FeatureUsageCsvRecord.

        name of the feature  # noqa: E501

        :param feature: The feature of this FeatureUsageCsvRecord.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def vm_usage_count(self):
        """Gets the vm_usage_count of this FeatureUsageCsvRecord.  # noqa: E501

        count of number of vms used by this feature  # noqa: E501

        :return: The vm_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :rtype: int
        """
        return self._vm_usage_count

    @vm_usage_count.setter
    def vm_usage_count(self, vm_usage_count):
        """Sets the vm_usage_count of this FeatureUsageCsvRecord.

        count of number of vms used by this feature  # noqa: E501

        :param vm_usage_count: The vm_usage_count of this FeatureUsageCsvRecord.  # noqa: E501
        :type: int
        """

        self._vm_usage_count = vm_usage_count

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
        if not isinstance(other, FeatureUsageCsvRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
