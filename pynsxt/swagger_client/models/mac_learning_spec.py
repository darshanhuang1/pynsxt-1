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


class MacLearningSpec(object):
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
        'limit': 'int',
        'aging_time': 'int',
        'enabled': 'bool',
        'limit_policy': 'str',
        'unicast_flooding_allowed': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'aging_time': 'aging_time',
        'enabled': 'enabled',
        'limit_policy': 'limit_policy',
        'unicast_flooding_allowed': 'unicast_flooding_allowed'
    }

    def __init__(self, limit=4096, aging_time=300, enabled=None, limit_policy='ALLOW', unicast_flooding_allowed=True):  # noqa: E501
        """MacLearningSpec - a model defined in Swagger"""  # noqa: E501

        self._limit = None
        self._aging_time = None
        self._enabled = None
        self._limit_policy = None
        self._unicast_flooding_allowed = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if aging_time is not None:
            self.aging_time = aging_time
        self.enabled = enabled
        if limit_policy is not None:
            self.limit_policy = limit_policy
        if unicast_flooding_allowed is not None:
            self.unicast_flooding_allowed = unicast_flooding_allowed

    @property
    def limit(self):
        """Gets the limit of this MacLearningSpec.  # noqa: E501

        The maximum number of MAC addresses that can be learned on this port  # noqa: E501

        :return: The limit of this MacLearningSpec.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this MacLearningSpec.

        The maximum number of MAC addresses that can be learned on this port  # noqa: E501

        :param limit: The limit of this MacLearningSpec.  # noqa: E501
        :type: int
        """
        if limit is not None and limit > 4096:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `4096`")  # noqa: E501
        if limit is not None and limit < 0:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limit = limit

    @property
    def aging_time(self):
        """Gets the aging_time of this MacLearningSpec.  # noqa: E501

        Aging time in sec for learned MAC address  # noqa: E501

        :return: The aging_time of this MacLearningSpec.  # noqa: E501
        :rtype: int
        """
        return self._aging_time

    @aging_time.setter
    def aging_time(self, aging_time):
        """Sets the aging_time of this MacLearningSpec.

        Aging time in sec for learned MAC address  # noqa: E501

        :param aging_time: The aging_time of this MacLearningSpec.  # noqa: E501
        :type: int
        """

        self._aging_time = aging_time

    @property
    def enabled(self):
        """Gets the enabled of this MacLearningSpec.  # noqa: E501

        Allowing source MAC address learning  # noqa: E501

        :return: The enabled of this MacLearningSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MacLearningSpec.

        Allowing source MAC address learning  # noqa: E501

        :param enabled: The enabled of this MacLearningSpec.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def limit_policy(self):
        """Gets the limit_policy of this MacLearningSpec.  # noqa: E501

        The policy after MAC Limit is exceeded  # noqa: E501

        :return: The limit_policy of this MacLearningSpec.  # noqa: E501
        :rtype: str
        """
        return self._limit_policy

    @limit_policy.setter
    def limit_policy(self, limit_policy):
        """Sets the limit_policy of this MacLearningSpec.

        The policy after MAC Limit is exceeded  # noqa: E501

        :param limit_policy: The limit_policy of this MacLearningSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOW", "DROP"]  # noqa: E501
        if limit_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `limit_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(limit_policy, allowed_values)
            )

        self._limit_policy = limit_policy

    @property
    def unicast_flooding_allowed(self):
        """Gets the unicast_flooding_allowed of this MacLearningSpec.  # noqa: E501

        Allowing flooding for unlearned MAC for ingress traffic  # noqa: E501

        :return: The unicast_flooding_allowed of this MacLearningSpec.  # noqa: E501
        :rtype: bool
        """
        return self._unicast_flooding_allowed

    @unicast_flooding_allowed.setter
    def unicast_flooding_allowed(self, unicast_flooding_allowed):
        """Sets the unicast_flooding_allowed of this MacLearningSpec.

        Allowing flooding for unlearned MAC for ingress traffic  # noqa: E501

        :param unicast_flooding_allowed: The unicast_flooding_allowed of this MacLearningSpec.  # noqa: E501
        :type: bool
        """

        self._unicast_flooding_allowed = unicast_flooding_allowed

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
        if not isinstance(other, MacLearningSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
