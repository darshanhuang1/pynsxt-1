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


class ClientSslProfileBinding(object):
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
        'client_auth': 'str',
        'ssl_profile_id': 'str',
        'certificate_chain_depth': 'int',
        'client_auth_ca_ids': 'list[str]',
        'default_certificate_id': 'str',
        'sni_certificate_ids': 'list[str]',
        'client_auth_crl_ids': 'list[str]'
    }

    attribute_map = {
        'client_auth': 'client_auth',
        'ssl_profile_id': 'ssl_profile_id',
        'certificate_chain_depth': 'certificate_chain_depth',
        'client_auth_ca_ids': 'client_auth_ca_ids',
        'default_certificate_id': 'default_certificate_id',
        'sni_certificate_ids': 'sni_certificate_ids',
        'client_auth_crl_ids': 'client_auth_crl_ids'
    }

    def __init__(self, client_auth='IGNORE', ssl_profile_id=None, certificate_chain_depth=3, client_auth_ca_ids=None, default_certificate_id=None, sni_certificate_ids=None, client_auth_crl_ids=None):  # noqa: E501
        """ClientSslProfileBinding - a model defined in Swagger"""  # noqa: E501

        self._client_auth = None
        self._ssl_profile_id = None
        self._certificate_chain_depth = None
        self._client_auth_ca_ids = None
        self._default_certificate_id = None
        self._sni_certificate_ids = None
        self._client_auth_crl_ids = None
        self.discriminator = None

        if client_auth is not None:
            self.client_auth = client_auth
        if ssl_profile_id is not None:
            self.ssl_profile_id = ssl_profile_id
        if certificate_chain_depth is not None:
            self.certificate_chain_depth = certificate_chain_depth
        if client_auth_ca_ids is not None:
            self.client_auth_ca_ids = client_auth_ca_ids
        self.default_certificate_id = default_certificate_id
        if sni_certificate_ids is not None:
            self.sni_certificate_ids = sni_certificate_ids
        if client_auth_crl_ids is not None:
            self.client_auth_crl_ids = client_auth_crl_ids

    @property
    def client_auth(self):
        """Gets the client_auth of this ClientSslProfileBinding.  # noqa: E501

        client authentication mode  # noqa: E501

        :return: The client_auth of this ClientSslProfileBinding.  # noqa: E501
        :rtype: str
        """
        return self._client_auth

    @client_auth.setter
    def client_auth(self, client_auth):
        """Sets the client_auth of this ClientSslProfileBinding.

        client authentication mode  # noqa: E501

        :param client_auth: The client_auth of this ClientSslProfileBinding.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUIRED", "IGNORE"]  # noqa: E501
        if client_auth not in allowed_values:
            raise ValueError(
                "Invalid value for `client_auth` ({0}), must be one of {1}"  # noqa: E501
                .format(client_auth, allowed_values)
            )

        self._client_auth = client_auth

    @property
    def ssl_profile_id(self):
        """Gets the ssl_profile_id of this ClientSslProfileBinding.  # noqa: E501

        Client SSL profile defines reusable, application-independent client side SSL properties.   # noqa: E501

        :return: The ssl_profile_id of this ClientSslProfileBinding.  # noqa: E501
        :rtype: str
        """
        return self._ssl_profile_id

    @ssl_profile_id.setter
    def ssl_profile_id(self, ssl_profile_id):
        """Sets the ssl_profile_id of this ClientSslProfileBinding.

        Client SSL profile defines reusable, application-independent client side SSL properties.   # noqa: E501

        :param ssl_profile_id: The ssl_profile_id of this ClientSslProfileBinding.  # noqa: E501
        :type: str
        """

        self._ssl_profile_id = ssl_profile_id

    @property
    def certificate_chain_depth(self):
        """Gets the certificate_chain_depth of this ClientSslProfileBinding.  # noqa: E501

        authentication depth is used to set the verification depth in the client certificates chain.   # noqa: E501

        :return: The certificate_chain_depth of this ClientSslProfileBinding.  # noqa: E501
        :rtype: int
        """
        return self._certificate_chain_depth

    @certificate_chain_depth.setter
    def certificate_chain_depth(self, certificate_chain_depth):
        """Sets the certificate_chain_depth of this ClientSslProfileBinding.

        authentication depth is used to set the verification depth in the client certificates chain.   # noqa: E501

        :param certificate_chain_depth: The certificate_chain_depth of this ClientSslProfileBinding.  # noqa: E501
        :type: int
        """
        if certificate_chain_depth is not None and certificate_chain_depth < 1:  # noqa: E501
            raise ValueError("Invalid value for `certificate_chain_depth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._certificate_chain_depth = certificate_chain_depth

    @property
    def client_auth_ca_ids(self):
        """Gets the client_auth_ca_ids of this ClientSslProfileBinding.  # noqa: E501

        If client auth type is REQUIRED, client certificate must be signed by one of the trusted Certificate Authorities (CAs), also referred to as root CAs, whose self signed certificates are specified.   # noqa: E501

        :return: The client_auth_ca_ids of this ClientSslProfileBinding.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_auth_ca_ids

    @client_auth_ca_ids.setter
    def client_auth_ca_ids(self, client_auth_ca_ids):
        """Sets the client_auth_ca_ids of this ClientSslProfileBinding.

        If client auth type is REQUIRED, client certificate must be signed by one of the trusted Certificate Authorities (CAs), also referred to as root CAs, whose self signed certificates are specified.   # noqa: E501

        :param client_auth_ca_ids: The client_auth_ca_ids of this ClientSslProfileBinding.  # noqa: E501
        :type: list[str]
        """

        self._client_auth_ca_ids = client_auth_ca_ids

    @property
    def default_certificate_id(self):
        """Gets the default_certificate_id of this ClientSslProfileBinding.  # noqa: E501

        A default certificate should be specified which will be used if the server does not host multiple hostnames on the same IP address or if the client does not support SNI extension.   # noqa: E501

        :return: The default_certificate_id of this ClientSslProfileBinding.  # noqa: E501
        :rtype: str
        """
        return self._default_certificate_id

    @default_certificate_id.setter
    def default_certificate_id(self, default_certificate_id):
        """Sets the default_certificate_id of this ClientSslProfileBinding.

        A default certificate should be specified which will be used if the server does not host multiple hostnames on the same IP address or if the client does not support SNI extension.   # noqa: E501

        :param default_certificate_id: The default_certificate_id of this ClientSslProfileBinding.  # noqa: E501
        :type: str
        """
        if default_certificate_id is None:
            raise ValueError("Invalid value for `default_certificate_id`, must not be `None`")  # noqa: E501

        self._default_certificate_id = default_certificate_id

    @property
    def sni_certificate_ids(self):
        """Gets the sni_certificate_ids of this ClientSslProfileBinding.  # noqa: E501

        Client-side SSL profile binding allows multiple certificates, for different hostnames, to be bound to the same virtual server.   # noqa: E501

        :return: The sni_certificate_ids of this ClientSslProfileBinding.  # noqa: E501
        :rtype: list[str]
        """
        return self._sni_certificate_ids

    @sni_certificate_ids.setter
    def sni_certificate_ids(self, sni_certificate_ids):
        """Sets the sni_certificate_ids of this ClientSslProfileBinding.

        Client-side SSL profile binding allows multiple certificates, for different hostnames, to be bound to the same virtual server.   # noqa: E501

        :param sni_certificate_ids: The sni_certificate_ids of this ClientSslProfileBinding.  # noqa: E501
        :type: list[str]
        """

        self._sni_certificate_ids = sni_certificate_ids

    @property
    def client_auth_crl_ids(self):
        """Gets the client_auth_crl_ids of this ClientSslProfileBinding.  # noqa: E501

        A Certificate Revocation List (CRL) can be specified in the client-side SSL profile binding to disallow compromised client certificates.   # noqa: E501

        :return: The client_auth_crl_ids of this ClientSslProfileBinding.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_auth_crl_ids

    @client_auth_crl_ids.setter
    def client_auth_crl_ids(self, client_auth_crl_ids):
        """Sets the client_auth_crl_ids of this ClientSslProfileBinding.

        A Certificate Revocation List (CRL) can be specified in the client-side SSL profile binding to disallow compromised client certificates.   # noqa: E501

        :param client_auth_crl_ids: The client_auth_crl_ids of this ClientSslProfileBinding.  # noqa: E501
        :type: list[str]
        """

        self._client_auth_crl_ids = client_auth_crl_ids

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
        if not isinstance(other, ClientSslProfileBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
