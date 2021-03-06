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

from swagger_client.models.resource import Resource  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501


class AuthenticationPolicyProperties(object):
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
        '_self': 'SelfResourceLink',
        'links': 'list[ResourceLink]',
        'schema': 'str',
        'api_failed_auth_reset_period': 'int',
        'minimum_password_length': 'int',
        'cli_failed_auth_lockout_period': 'int',
        'api_max_auth_failures': 'int',
        'api_failed_auth_lockout_period': 'int',
        'cli_max_auth_failures': 'int'
    }

    attribute_map = {
        '_self': '_self',
        'links': '_links',
        'schema': '_schema',
        'api_failed_auth_reset_period': 'api_failed_auth_reset_period',
        'minimum_password_length': 'minimum_password_length',
        'cli_failed_auth_lockout_period': 'cli_failed_auth_lockout_period',
        'api_max_auth_failures': 'api_max_auth_failures',
        'api_failed_auth_lockout_period': 'api_failed_auth_lockout_period',
        'cli_max_auth_failures': 'cli_max_auth_failures'
    }

    def __init__(self, _self=None, links=None, schema=None, api_failed_auth_reset_period=900, minimum_password_length=8, cli_failed_auth_lockout_period=900, api_max_auth_failures=5, api_failed_auth_lockout_period=900, cli_max_auth_failures=5):  # noqa: E501
        """AuthenticationPolicyProperties - a model defined in Swagger"""  # noqa: E501

        self.__self = None
        self._links = None
        self._schema = None
        self._api_failed_auth_reset_period = None
        self._minimum_password_length = None
        self._cli_failed_auth_lockout_period = None
        self._api_max_auth_failures = None
        self._api_failed_auth_lockout_period = None
        self._cli_max_auth_failures = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if links is not None:
            self.links = links
        if schema is not None:
            self.schema = schema
        if api_failed_auth_reset_period is not None:
            self.api_failed_auth_reset_period = api_failed_auth_reset_period
        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if cli_failed_auth_lockout_period is not None:
            self.cli_failed_auth_lockout_period = cli_failed_auth_lockout_period
        if api_max_auth_failures is not None:
            self.api_max_auth_failures = api_max_auth_failures
        if api_failed_auth_lockout_period is not None:
            self.api_failed_auth_lockout_period = api_failed_auth_lockout_period
        if cli_max_auth_failures is not None:
            self.cli_max_auth_failures = cli_max_auth_failures

    @property
    def _self(self):
        """Gets the _self of this AuthenticationPolicyProperties.  # noqa: E501


        :return: The _self of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: SelfResourceLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this AuthenticationPolicyProperties.


        :param _self: The _self of this AuthenticationPolicyProperties.  # noqa: E501
        :type: SelfResourceLink
        """

        self.__self = _self

    @property
    def links(self):
        """Gets the links of this AuthenticationPolicyProperties.  # noqa: E501

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :return: The links of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AuthenticationPolicyProperties.

        The server will populate this field when returing the resource. Ignored on PUT and POST.  # noqa: E501

        :param links: The links of this AuthenticationPolicyProperties.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

    @property
    def schema(self):
        """Gets the schema of this AuthenticationPolicyProperties.  # noqa: E501


        :return: The schema of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this AuthenticationPolicyProperties.


        :param schema: The schema of this AuthenticationPolicyProperties.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def api_failed_auth_reset_period(self):
        """Gets the api_failed_auth_reset_period of this AuthenticationPolicyProperties.  # noqa: E501

        In order to trigger an account lockout, all authentication failures must occur in this time window. If the reset period expires, the failed login count is reset to zero. Only applies to NSX Manager nodes. Ignored on other node types.  # noqa: E501

        :return: The api_failed_auth_reset_period of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: int
        """
        return self._api_failed_auth_reset_period

    @api_failed_auth_reset_period.setter
    def api_failed_auth_reset_period(self, api_failed_auth_reset_period):
        """Sets the api_failed_auth_reset_period of this AuthenticationPolicyProperties.

        In order to trigger an account lockout, all authentication failures must occur in this time window. If the reset period expires, the failed login count is reset to zero. Only applies to NSX Manager nodes. Ignored on other node types.  # noqa: E501

        :param api_failed_auth_reset_period: The api_failed_auth_reset_period of this AuthenticationPolicyProperties.  # noqa: E501
        :type: int
        """
        if api_failed_auth_reset_period is not None and api_failed_auth_reset_period < 0:  # noqa: E501
            raise ValueError("Invalid value for `api_failed_auth_reset_period`, must be a value greater than or equal to `0`")  # noqa: E501

        self._api_failed_auth_reset_period = api_failed_auth_reset_period

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this AuthenticationPolicyProperties.  # noqa: E501

        Minimum number of characters required in account passwords  # noqa: E501

        :return: The minimum_password_length of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this AuthenticationPolicyProperties.

        Minimum number of characters required in account passwords  # noqa: E501

        :param minimum_password_length: The minimum_password_length of this AuthenticationPolicyProperties.  # noqa: E501
        :type: int
        """
        if minimum_password_length is not None and minimum_password_length < 8:  # noqa: E501
            raise ValueError("Invalid value for `minimum_password_length`, must be a value greater than or equal to `8`")  # noqa: E501

        self._minimum_password_length = minimum_password_length

    @property
    def cli_failed_auth_lockout_period(self):
        """Gets the cli_failed_auth_lockout_period of this AuthenticationPolicyProperties.  # noqa: E501

        Once a lockout occurs, the account remains locked out of the CLI for this time period.  # noqa: E501

        :return: The cli_failed_auth_lockout_period of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: int
        """
        return self._cli_failed_auth_lockout_period

    @cli_failed_auth_lockout_period.setter
    def cli_failed_auth_lockout_period(self, cli_failed_auth_lockout_period):
        """Sets the cli_failed_auth_lockout_period of this AuthenticationPolicyProperties.

        Once a lockout occurs, the account remains locked out of the CLI for this time period.  # noqa: E501

        :param cli_failed_auth_lockout_period: The cli_failed_auth_lockout_period of this AuthenticationPolicyProperties.  # noqa: E501
        :type: int
        """
        if cli_failed_auth_lockout_period is not None and cli_failed_auth_lockout_period < 0:  # noqa: E501
            raise ValueError("Invalid value for `cli_failed_auth_lockout_period`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cli_failed_auth_lockout_period = cli_failed_auth_lockout_period

    @property
    def api_max_auth_failures(self):
        """Gets the api_max_auth_failures of this AuthenticationPolicyProperties.  # noqa: E501

        Only applies to NSX Manager nodes. Ignored on other node types.  # noqa: E501

        :return: The api_max_auth_failures of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: int
        """
        return self._api_max_auth_failures

    @api_max_auth_failures.setter
    def api_max_auth_failures(self, api_max_auth_failures):
        """Sets the api_max_auth_failures of this AuthenticationPolicyProperties.

        Only applies to NSX Manager nodes. Ignored on other node types.  # noqa: E501

        :param api_max_auth_failures: The api_max_auth_failures of this AuthenticationPolicyProperties.  # noqa: E501
        :type: int
        """
        if api_max_auth_failures is not None and api_max_auth_failures < 0:  # noqa: E501
            raise ValueError("Invalid value for `api_max_auth_failures`, must be a value greater than or equal to `0`")  # noqa: E501

        self._api_max_auth_failures = api_max_auth_failures

    @property
    def api_failed_auth_lockout_period(self):
        """Gets the api_failed_auth_lockout_period of this AuthenticationPolicyProperties.  # noqa: E501

        Once a lockout occurs, the account remains locked out of the API for this time period. Only applies to NSX Manager nodes. Ignored on other node types.  # noqa: E501

        :return: The api_failed_auth_lockout_period of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: int
        """
        return self._api_failed_auth_lockout_period

    @api_failed_auth_lockout_period.setter
    def api_failed_auth_lockout_period(self, api_failed_auth_lockout_period):
        """Sets the api_failed_auth_lockout_period of this AuthenticationPolicyProperties.

        Once a lockout occurs, the account remains locked out of the API for this time period. Only applies to NSX Manager nodes. Ignored on other node types.  # noqa: E501

        :param api_failed_auth_lockout_period: The api_failed_auth_lockout_period of this AuthenticationPolicyProperties.  # noqa: E501
        :type: int
        """
        if api_failed_auth_lockout_period is not None and api_failed_auth_lockout_period < 0:  # noqa: E501
            raise ValueError("Invalid value for `api_failed_auth_lockout_period`, must be a value greater than or equal to `0`")  # noqa: E501

        self._api_failed_auth_lockout_period = api_failed_auth_lockout_period

    @property
    def cli_max_auth_failures(self):
        """Gets the cli_max_auth_failures of this AuthenticationPolicyProperties.  # noqa: E501

        Number of authentication failures that trigger CLI lockout  # noqa: E501

        :return: The cli_max_auth_failures of this AuthenticationPolicyProperties.  # noqa: E501
        :rtype: int
        """
        return self._cli_max_auth_failures

    @cli_max_auth_failures.setter
    def cli_max_auth_failures(self, cli_max_auth_failures):
        """Sets the cli_max_auth_failures of this AuthenticationPolicyProperties.

        Number of authentication failures that trigger CLI lockout  # noqa: E501

        :param cli_max_auth_failures: The cli_max_auth_failures of this AuthenticationPolicyProperties.  # noqa: E501
        :type: int
        """
        if cli_max_auth_failures is not None and cli_max_auth_failures < 0:  # noqa: E501
            raise ValueError("Invalid value for `cli_max_auth_failures`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cli_max_auth_failures = cli_max_auth_failures

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
        if not isinstance(other, AuthenticationPolicyProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
