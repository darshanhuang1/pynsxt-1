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


class AppDiscoveryAppProfileResultSummary(object):
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
        'app_profile_id': 'str',
        'display_name': 'str',
        'installed_apps_count': 'int'
    }

    attribute_map = {
        'app_profile_id': 'app_profile_id',
        'display_name': 'display_name',
        'installed_apps_count': 'installed_apps_count'
    }

    def __init__(self, app_profile_id=None, display_name=None, installed_apps_count=None):  # noqa: E501
        """AppDiscoveryAppProfileResultSummary - a model defined in Swagger"""  # noqa: E501

        self._app_profile_id = None
        self._display_name = None
        self._installed_apps_count = None
        self.discriminator = None

        if app_profile_id is not None:
            self.app_profile_id = app_profile_id
        if display_name is not None:
            self.display_name = display_name
        if installed_apps_count is not None:
            self.installed_apps_count = installed_apps_count

    @property
    def app_profile_id(self):
        """Gets the app_profile_id of this AppDiscoveryAppProfileResultSummary.  # noqa: E501

        ID of the App Profile  # noqa: E501

        :return: The app_profile_id of this AppDiscoveryAppProfileResultSummary.  # noqa: E501
        :rtype: str
        """
        return self._app_profile_id

    @app_profile_id.setter
    def app_profile_id(self, app_profile_id):
        """Sets the app_profile_id of this AppDiscoveryAppProfileResultSummary.

        ID of the App Profile  # noqa: E501

        :param app_profile_id: The app_profile_id of this AppDiscoveryAppProfileResultSummary.  # noqa: E501
        :type: str
        """

        self._app_profile_id = app_profile_id

    @property
    def display_name(self):
        """Gets the display_name of this AppDiscoveryAppProfileResultSummary.  # noqa: E501

        Name of the App Profile  # noqa: E501

        :return: The display_name of this AppDiscoveryAppProfileResultSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AppDiscoveryAppProfileResultSummary.

        Name of the App Profile  # noqa: E501

        :param display_name: The display_name of this AppDiscoveryAppProfileResultSummary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def installed_apps_count(self):
        """Gets the installed_apps_count of this AppDiscoveryAppProfileResultSummary.  # noqa: E501

        Number of apps installed that belongs to this App Profile  # noqa: E501

        :return: The installed_apps_count of this AppDiscoveryAppProfileResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._installed_apps_count

    @installed_apps_count.setter
    def installed_apps_count(self, installed_apps_count):
        """Sets the installed_apps_count of this AppDiscoveryAppProfileResultSummary.

        Number of apps installed that belongs to this App Profile  # noqa: E501

        :param installed_apps_count: The installed_apps_count of this AppDiscoveryAppProfileResultSummary.  # noqa: E501
        :type: int
        """

        self._installed_apps_count = installed_apps_count

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
        if not isinstance(other, AppDiscoveryAppProfileResultSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
