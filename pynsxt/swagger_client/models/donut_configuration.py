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

from swagger_client.models.datasource import Datasource  # noqa: F401,E501
from swagger_client.models.donut_section import DonutSection  # noqa: F401,E501
from swagger_client.models.footer import Footer  # noqa: F401,E501
from swagger_client.models.label import Label  # noqa: F401,E501
from swagger_client.models.resource_link import ResourceLink  # noqa: F401,E501
from swagger_client.models.self_resource_link import SelfResourceLink  # noqa: F401,E501
from swagger_client.models.tag import Tag  # noqa: F401,E501
from swagger_client.models.widget_configuration import WidgetConfiguration  # noqa: F401,E501


class DonutConfiguration(object):
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
        'navigation': 'str',
        'display_count': 'bool',
        'sections': 'list[DonutSection]',
        'label': 'Label'
    }

    attribute_map = {
        'navigation': 'navigation',
        'display_count': 'display_count',
        'sections': 'sections',
        'label': 'label'
    }

    def __init__(self, navigation=None, display_count=True, sections=None, label=None):  # noqa: E501
        """DonutConfiguration - a model defined in Swagger"""  # noqa: E501

        self._navigation = None
        self._display_count = None
        self._sections = None
        self._label = None
        self.discriminator = None

        if navigation is not None:
            self.navigation = navigation
        if display_count is not None:
            self.display_count = display_count
        self.sections = sections
        self.label = label

    @property
    def navigation(self):
        """Gets the navigation of this DonutConfiguration.  # noqa: E501

        Hyperlink of the specified UI page that provides details.  # noqa: E501

        :return: The navigation of this DonutConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._navigation

    @navigation.setter
    def navigation(self, navigation):
        """Sets the navigation of this DonutConfiguration.

        Hyperlink of the specified UI page that provides details.  # noqa: E501

        :param navigation: The navigation of this DonutConfiguration.  # noqa: E501
        :type: str
        """

        self._navigation = navigation

    @property
    def display_count(self):
        """Gets the display_count of this DonutConfiguration.  # noqa: E501

        If true, displays the count of entities in the donut  # noqa: E501

        :return: The display_count of this DonutConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._display_count

    @display_count.setter
    def display_count(self, display_count):
        """Sets the display_count of this DonutConfiguration.

        If true, displays the count of entities in the donut  # noqa: E501

        :param display_count: The display_count of this DonutConfiguration.  # noqa: E501
        :type: bool
        """

        self._display_count = display_count

    @property
    def sections(self):
        """Gets the sections of this DonutConfiguration.  # noqa: E501

        Sections  # noqa: E501

        :return: The sections of this DonutConfiguration.  # noqa: E501
        :rtype: list[DonutSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this DonutConfiguration.

        Sections  # noqa: E501

        :param sections: The sections of this DonutConfiguration.  # noqa: E501
        :type: list[DonutSection]
        """
        if sections is None:
            raise ValueError("Invalid value for `sections`, must not be `None`")  # noqa: E501

        self._sections = sections

    @property
    def label(self):
        """Gets the label of this DonutConfiguration.  # noqa: E501

        Displayed at the middle of the donut, by default. It labels the entities of donut.  # noqa: E501

        :return: The label of this DonutConfiguration.  # noqa: E501
        :rtype: Label
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DonutConfiguration.

        Displayed at the middle of the donut, by default. It labels the entities of donut.  # noqa: E501

        :param label: The label of this DonutConfiguration.  # noqa: E501
        :type: Label
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

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
        if not isinstance(other, DonutConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
