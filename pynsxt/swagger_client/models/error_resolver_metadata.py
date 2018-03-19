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

from swagger_client.models.error_resolver_system_metadata import ErrorResolverSystemMetadata  # noqa: F401,E501
from swagger_client.models.error_resolver_user_metadata import ErrorResolverUserMetadata  # noqa: F401,E501


class ErrorResolverMetadata(object):
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
        'error_id': 'int',
        'system_metadata': 'ErrorResolverSystemMetadata',
        'entity_id': 'str',
        'user_metadata': 'ErrorResolverUserMetadata'
    }

    attribute_map = {
        'error_id': 'error_id',
        'system_metadata': 'system_metadata',
        'entity_id': 'entity_id',
        'user_metadata': 'user_metadata'
    }

    def __init__(self, error_id=None, system_metadata=None, entity_id=None, user_metadata=None):  # noqa: E501
        """ErrorResolverMetadata - a model defined in Swagger"""  # noqa: E501

        self._error_id = None
        self._system_metadata = None
        self._entity_id = None
        self._user_metadata = None
        self.discriminator = None

        self.error_id = error_id
        if system_metadata is not None:
            self.system_metadata = system_metadata
        self.entity_id = entity_id
        if user_metadata is not None:
            self.user_metadata = user_metadata

    @property
    def error_id(self):
        """Gets the error_id of this ErrorResolverMetadata.  # noqa: E501

        The error id as reported by the entity where the error occurred.  # noqa: E501

        :return: The error_id of this ErrorResolverMetadata.  # noqa: E501
        :rtype: int
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """Sets the error_id of this ErrorResolverMetadata.

        The error id as reported by the entity where the error occurred.  # noqa: E501

        :param error_id: The error_id of this ErrorResolverMetadata.  # noqa: E501
        :type: int
        """
        if error_id is None:
            raise ValueError("Invalid value for `error_id`, must not be `None`")  # noqa: E501

        self._error_id = error_id

    @property
    def system_metadata(self):
        """Gets the system_metadata of this ErrorResolverMetadata.  # noqa: E501

        This can come from some external system like syslog collector  # noqa: E501

        :return: The system_metadata of this ErrorResolverMetadata.  # noqa: E501
        :rtype: ErrorResolverSystemMetadata
        """
        return self._system_metadata

    @system_metadata.setter
    def system_metadata(self, system_metadata):
        """Sets the system_metadata of this ErrorResolverMetadata.

        This can come from some external system like syslog collector  # noqa: E501

        :param system_metadata: The system_metadata of this ErrorResolverMetadata.  # noqa: E501
        :type: ErrorResolverSystemMetadata
        """

        self._system_metadata = system_metadata

    @property
    def entity_id(self):
        """Gets the entity_id of this ErrorResolverMetadata.  # noqa: E501

        The entity/node UUID where the error has occurred.  # noqa: E501

        :return: The entity_id of this ErrorResolverMetadata.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ErrorResolverMetadata.

        The entity/node UUID where the error has occurred.  # noqa: E501

        :param entity_id: The entity_id of this ErrorResolverMetadata.  # noqa: E501
        :type: str
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def user_metadata(self):
        """Gets the user_metadata of this ErrorResolverMetadata.  # noqa: E501

        User supplied metadata that might be required by the resolver  # noqa: E501

        :return: The user_metadata of this ErrorResolverMetadata.  # noqa: E501
        :rtype: ErrorResolverUserMetadata
        """
        return self._user_metadata

    @user_metadata.setter
    def user_metadata(self, user_metadata):
        """Sets the user_metadata of this ErrorResolverMetadata.

        User supplied metadata that might be required by the resolver  # noqa: E501

        :param user_metadata: The user_metadata of this ErrorResolverMetadata.  # noqa: E501
        :type: ErrorResolverUserMetadata
        """

        self._user_metadata = user_metadata

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
        if not isinstance(other, ErrorResolverMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
