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

from swagger_client.models.lb_cookie_time import LbCookieTime  # noqa: F401,E501
from swagger_client.models.lb_persistence_profile import LbPersistenceProfile  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501


class LbCookiePersistenceProfile(object):
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
        'cookie_garble': 'bool',
        'cookie_fallback': 'bool',
        'cookie_mode': 'str',
        'cookie_domain': 'str',
        'cookie_name': 'str',
        'cookie_time': 'LbCookieTime',
        'cookie_path': 'str'
    }

    attribute_map = {
        'cookie_garble': 'cookie_garble',
        'cookie_fallback': 'cookie_fallback',
        'cookie_mode': 'cookie_mode',
        'cookie_domain': 'cookie_domain',
        'cookie_name': 'cookie_name',
        'cookie_time': 'cookie_time',
        'cookie_path': 'cookie_path'
    }

    def __init__(self, cookie_garble=True, cookie_fallback=True, cookie_mode='INSERT', cookie_domain=None, cookie_name=None, cookie_time=None, cookie_path=None):  # noqa: E501
        """LbCookiePersistenceProfile - a model defined in Swagger"""  # noqa: E501

        self._cookie_garble = None
        self._cookie_fallback = None
        self._cookie_mode = None
        self._cookie_domain = None
        self._cookie_name = None
        self._cookie_time = None
        self._cookie_path = None
        self.discriminator = None

        if cookie_garble is not None:
            self.cookie_garble = cookie_garble
        if cookie_fallback is not None:
            self.cookie_fallback = cookie_fallback
        if cookie_mode is not None:
            self.cookie_mode = cookie_mode
        if cookie_domain is not None:
            self.cookie_domain = cookie_domain
        self.cookie_name = cookie_name
        if cookie_time is not None:
            self.cookie_time = cookie_time
        if cookie_path is not None:
            self.cookie_path = cookie_path

    @property
    def cookie_garble(self):
        """Gets the cookie_garble of this LbCookiePersistenceProfile.  # noqa: E501

        If garble is set to true, cookie value (server IP and port) would be encrypted. If garble is set to false, cookie value would be plain text.   # noqa: E501

        :return: The cookie_garble of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._cookie_garble

    @cookie_garble.setter
    def cookie_garble(self, cookie_garble):
        """Sets the cookie_garble of this LbCookiePersistenceProfile.

        If garble is set to true, cookie value (server IP and port) would be encrypted. If garble is set to false, cookie value would be plain text.   # noqa: E501

        :param cookie_garble: The cookie_garble of this LbCookiePersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._cookie_garble = cookie_garble

    @property
    def cookie_fallback(self):
        """Gets the cookie_fallback of this LbCookiePersistenceProfile.  # noqa: E501

        If fallback is true, once the cookie points to a server that is down (i.e. admin state DISABLED or healthcheck state is DOWN), then a new server is selected by default to handle that request. If fallback is false, it will cause the request to be rejected if cookie points to a server   # noqa: E501

        :return: The cookie_fallback of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: bool
        """
        return self._cookie_fallback

    @cookie_fallback.setter
    def cookie_fallback(self, cookie_fallback):
        """Sets the cookie_fallback of this LbCookiePersistenceProfile.

        If fallback is true, once the cookie points to a server that is down (i.e. admin state DISABLED or healthcheck state is DOWN), then a new server is selected by default to handle that request. If fallback is false, it will cause the request to be rejected if cookie points to a server   # noqa: E501

        :param cookie_fallback: The cookie_fallback of this LbCookiePersistenceProfile.  # noqa: E501
        :type: bool
        """

        self._cookie_fallback = cookie_fallback

    @property
    def cookie_mode(self):
        """Gets the cookie_mode of this LbCookiePersistenceProfile.  # noqa: E501

        cookie persistence mode  # noqa: E501

        :return: The cookie_mode of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_mode

    @cookie_mode.setter
    def cookie_mode(self, cookie_mode):
        """Sets the cookie_mode of this LbCookiePersistenceProfile.

        cookie persistence mode  # noqa: E501

        :param cookie_mode: The cookie_mode of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["INSERT", "PREFIX", "REWRITE"]  # noqa: E501
        if cookie_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `cookie_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(cookie_mode, allowed_values)
            )

        self._cookie_mode = cookie_mode

    @property
    def cookie_domain(self):
        """Gets the cookie_domain of this LbCookiePersistenceProfile.  # noqa: E501

        HTTP cookie domain could be configured, only available for insert mode.   # noqa: E501

        :return: The cookie_domain of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_domain

    @cookie_domain.setter
    def cookie_domain(self, cookie_domain):
        """Sets the cookie_domain of this LbCookiePersistenceProfile.

        HTTP cookie domain could be configured, only available for insert mode.   # noqa: E501

        :param cookie_domain: The cookie_domain of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """

        self._cookie_domain = cookie_domain

    @property
    def cookie_name(self):
        """Gets the cookie_name of this LbCookiePersistenceProfile.  # noqa: E501

        cookie name  # noqa: E501

        :return: The cookie_name of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """Sets the cookie_name of this LbCookiePersistenceProfile.

        cookie name  # noqa: E501

        :param cookie_name: The cookie_name of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """
        if cookie_name is None:
            raise ValueError("Invalid value for `cookie_name`, must not be `None`")  # noqa: E501

        self._cookie_name = cookie_name

    @property
    def cookie_time(self):
        """Gets the cookie_time of this LbCookiePersistenceProfile.  # noqa: E501

        Both session cookie and persistence cookie are supported, if not specified, it's a session cookie. It expires when the browser is closed.   # noqa: E501

        :return: The cookie_time of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: LbCookieTime
        """
        return self._cookie_time

    @cookie_time.setter
    def cookie_time(self, cookie_time):
        """Sets the cookie_time of this LbCookiePersistenceProfile.

        Both session cookie and persistence cookie are supported, if not specified, it's a session cookie. It expires when the browser is closed.   # noqa: E501

        :param cookie_time: The cookie_time of this LbCookiePersistenceProfile.  # noqa: E501
        :type: LbCookieTime
        """

        self._cookie_time = cookie_time

    @property
    def cookie_path(self):
        """Gets the cookie_path of this LbCookiePersistenceProfile.  # noqa: E501

        HTTP cookie path could be set, only available for insert mode.   # noqa: E501

        :return: The cookie_path of this LbCookiePersistenceProfile.  # noqa: E501
        :rtype: str
        """
        return self._cookie_path

    @cookie_path.setter
    def cookie_path(self, cookie_path):
        """Sets the cookie_path of this LbCookiePersistenceProfile.

        HTTP cookie path could be set, only available for insert mode.   # noqa: E501

        :param cookie_path: The cookie_path of this LbCookiePersistenceProfile.  # noqa: E501
        :type: str
        """

        self._cookie_path = cookie_path

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
        if not isinstance(other, LbCookiePersistenceProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
