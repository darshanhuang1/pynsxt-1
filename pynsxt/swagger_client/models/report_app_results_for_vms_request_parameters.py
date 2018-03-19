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


class ReportAppResultsForVmsRequestParameters(object):
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
        'vm_ids': 'list[str]'
    }

    attribute_map = {
        'vm_ids': 'vm_ids'
    }

    def __init__(self, vm_ids=None):  # noqa: E501
        """ReportAppResultsForVmsRequestParameters - a model defined in Swagger"""  # noqa: E501

        self._vm_ids = None
        self.discriminator = None

        if vm_ids is not None:
            self.vm_ids = vm_ids

    @property
    def vm_ids(self):
        """Gets the vm_ids of this ReportAppResultsForVmsRequestParameters.  # noqa: E501

        Vm external Ids  # noqa: E501

        :return: The vm_ids of this ReportAppResultsForVmsRequestParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._vm_ids

    @vm_ids.setter
    def vm_ids(self, vm_ids):
        """Sets the vm_ids of this ReportAppResultsForVmsRequestParameters.

        Vm external Ids  # noqa: E501

        :param vm_ids: The vm_ids of this ReportAppResultsForVmsRequestParameters.  # noqa: E501
        :type: list[str]
        """

        self._vm_ids = vm_ids

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
        if not isinstance(other, ReportAppResultsForVmsRequestParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
