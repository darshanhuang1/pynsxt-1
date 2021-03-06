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


class StartAppDiscoverySessionParameters(object):
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
        'ns_group_ids': 'list[str]',
        'app_profile_ids': 'list[str]'
    }

    attribute_map = {
        'ns_group_ids': 'ns_group_ids',
        'app_profile_ids': 'app_profile_ids'
    }

    def __init__(self, ns_group_ids=None, app_profile_ids=None):  # noqa: E501
        """StartAppDiscoverySessionParameters - a model defined in Swagger"""  # noqa: E501

        self._ns_group_ids = None
        self._app_profile_ids = None
        self.discriminator = None

        self.ns_group_ids = ns_group_ids
        if app_profile_ids is not None:
            self.app_profile_ids = app_profile_ids

    @property
    def ns_group_ids(self):
        """Gets the ns_group_ids of this StartAppDiscoverySessionParameters.  # noqa: E501

        NSGroup Ids  # noqa: E501

        :return: The ns_group_ids of this StartAppDiscoverySessionParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._ns_group_ids

    @ns_group_ids.setter
    def ns_group_ids(self, ns_group_ids):
        """Sets the ns_group_ids of this StartAppDiscoverySessionParameters.

        NSGroup Ids  # noqa: E501

        :param ns_group_ids: The ns_group_ids of this StartAppDiscoverySessionParameters.  # noqa: E501
        :type: list[str]
        """
        if ns_group_ids is None:
            raise ValueError("Invalid value for `ns_group_ids`, must not be `None`")  # noqa: E501

        self._ns_group_ids = ns_group_ids

    @property
    def app_profile_ids(self):
        """Gets the app_profile_ids of this StartAppDiscoverySessionParameters.  # noqa: E501

        App Profile Ids  # noqa: E501

        :return: The app_profile_ids of this StartAppDiscoverySessionParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_profile_ids

    @app_profile_ids.setter
    def app_profile_ids(self, app_profile_ids):
        """Sets the app_profile_ids of this StartAppDiscoverySessionParameters.

        App Profile Ids  # noqa: E501

        :param app_profile_ids: The app_profile_ids of this StartAppDiscoverySessionParameters.  # noqa: E501
        :type: list[str]
        """

        self._app_profile_ids = app_profile_ids

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
        if not isinstance(other, StartAppDiscoverySessionParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
