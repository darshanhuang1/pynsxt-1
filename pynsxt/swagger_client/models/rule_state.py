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

from swagger_client.models.configuration_state import ConfigurationState  # noqa: F401,E501
from swagger_client.models.configuration_state_element import ConfigurationStateElement  # noqa: F401,E501


class RuleState(object):
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
        'state': 'str',
        'details': 'list[ConfigurationStateElement]',
        'failure_code': 'int',
        'failure_message': 'str',
        'revision_desired': 'int'
    }

    attribute_map = {
        'state': 'state',
        'details': 'details',
        'failure_code': 'failure_code',
        'failure_message': 'failure_message',
        'revision_desired': 'revision_desired'
    }

    def __init__(self, state=None, details=None, failure_code=None, failure_message=None, revision_desired=None):  # noqa: E501
        """RuleState - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._details = None
        self._failure_code = None
        self._failure_message = None
        self._revision_desired = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if details is not None:
            self.details = details
        if failure_code is not None:
            self.failure_code = failure_code
        if failure_message is not None:
            self.failure_message = failure_message
        if revision_desired is not None:
            self.revision_desired = revision_desired

    @property
    def state(self):
        """Gets the state of this RuleState.  # noqa: E501

        Gives details of state of desired configuration  # noqa: E501

        :return: The state of this RuleState.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RuleState.

        Gives details of state of desired configuration  # noqa: E501

        :param state: The state of this RuleState.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "in_progress", "success", "failed", "partial_success", "orphaned"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def details(self):
        """Gets the details of this RuleState.  # noqa: E501

        Array of configuration state of various sub systems  # noqa: E501

        :return: The details of this RuleState.  # noqa: E501
        :rtype: list[ConfigurationStateElement]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this RuleState.

        Array of configuration state of various sub systems  # noqa: E501

        :param details: The details of this RuleState.  # noqa: E501
        :type: list[ConfigurationStateElement]
        """

        self._details = details

    @property
    def failure_code(self):
        """Gets the failure_code of this RuleState.  # noqa: E501

        Error code  # noqa: E501

        :return: The failure_code of this RuleState.  # noqa: E501
        :rtype: int
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, failure_code):
        """Sets the failure_code of this RuleState.

        Error code  # noqa: E501

        :param failure_code: The failure_code of this RuleState.  # noqa: E501
        :type: int
        """

        self._failure_code = failure_code

    @property
    def failure_message(self):
        """Gets the failure_message of this RuleState.  # noqa: E501

        Error message in case of failure  # noqa: E501

        :return: The failure_message of this RuleState.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this RuleState.

        Error message in case of failure  # noqa: E501

        :param failure_message: The failure_message of this RuleState.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

    @property
    def revision_desired(self):
        """Gets the revision_desired of this RuleState.  # noqa: E501

        revision number of the desired state  # noqa: E501

        :return: The revision_desired of this RuleState.  # noqa: E501
        :rtype: int
        """
        return self._revision_desired

    @revision_desired.setter
    def revision_desired(self, revision_desired):
        """Sets the revision_desired of this RuleState.

        revision number of the desired state  # noqa: E501

        :param revision_desired: The revision_desired of this RuleState.  # noqa: E501
        :type: int
        """

        self._revision_desired = revision_desired

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
        if not isinstance(other, RuleState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
