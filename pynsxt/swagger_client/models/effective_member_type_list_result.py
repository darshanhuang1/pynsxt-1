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


class EffectiveMemberTypeListResult(object):
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
        'results': 'list[str]',
        'result_count': 'int'
    }

    attribute_map = {
        'results': 'results',
        'result_count': 'result_count'
    }

    def __init__(self, results=None, result_count=None):  # noqa: E501
        """EffectiveMemberTypeListResult - a model defined in Swagger"""  # noqa: E501

        self._results = None
        self._result_count = None
        self.discriminator = None

        self.results = results
        if result_count is not None:
            self.result_count = result_count

    @property
    def results(self):
        """Gets the results of this EffectiveMemberTypeListResult.  # noqa: E501

        Collection of member types for the given NSGroup  # noqa: E501

        :return: The results of this EffectiveMemberTypeListResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this EffectiveMemberTypeListResult.

        Collection of member types for the given NSGroup  # noqa: E501

        :param results: The results of this EffectiveMemberTypeListResult.  # noqa: E501
        :type: list[str]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501
        allowed_values = ["NSGroup", "IPSet", "MACSet", "LogicalSwitch", "LogicalPort", "VirtualMachine"]  # noqa: E501
        if not set(results).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `results` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(results) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._results = results

    @property
    def result_count(self):
        """Gets the result_count of this EffectiveMemberTypeListResult.  # noqa: E501

        Count of the member types in the results array  # noqa: E501

        :return: The result_count of this EffectiveMemberTypeListResult.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this EffectiveMemberTypeListResult.

        Count of the member types in the results array  # noqa: E501

        :param result_count: The result_count of this EffectiveMemberTypeListResult.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

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
        if not isinstance(other, EffectiveMemberTypeListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
