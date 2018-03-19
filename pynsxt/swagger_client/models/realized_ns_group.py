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

from swagger_client.models.policy_alarm_resource import PolicyAlarmResource  # noqa: F401,E501
from swagger_client.models.realized_group import RealizedGroup  # noqa: F401,E501
from swagger_client.models.realized_ns_group_member_evaluation import RealizedNSGroupMemberEvaluation  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class RealizedNSGroup(object):
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
        'evaluations': 'list[RealizedNSGroupMemberEvaluation]'
    }

    attribute_map = {
        'evaluations': 'evaluations'
    }

    def __init__(self, evaluations=None):  # noqa: E501
        """RealizedNSGroup - a model defined in Swagger"""  # noqa: E501

        self._evaluations = None
        self.discriminator = None

        if evaluations is not None:
            self.evaluations = evaluations

    @property
    def evaluations(self):
        """Gets the evaluations of this RealizedNSGroup.  # noqa: E501

        Reference to the evaluated members of the NSGroup.   # noqa: E501

        :return: The evaluations of this RealizedNSGroup.  # noqa: E501
        :rtype: list[RealizedNSGroupMemberEvaluation]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        """Sets the evaluations of this RealizedNSGroup.

        Reference to the evaluated members of the NSGroup.   # noqa: E501

        :param evaluations: The evaluations of this RealizedNSGroup.  # noqa: E501
        :type: list[RealizedNSGroupMemberEvaluation]
        """

        self._evaluations = evaluations

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
        if not isinstance(other, RealizedNSGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
