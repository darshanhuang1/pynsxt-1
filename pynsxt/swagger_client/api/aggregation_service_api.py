# coding: utf-8

"""
    NSX API

    VMware NSX REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AggregationServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_aggregation_service_global_config(self, **kwargs):  # noqa: E501
        """Read global health performance monitoring configuration  # noqa: E501

        Read global health performance monitoring configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_aggregation_service_global_config(async=True)
        >>> result = thread.get()

        :param async bool
        :return: GlobalCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_aggregation_service_global_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_aggregation_service_global_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_aggregation_service_global_config_with_http_info(self, **kwargs):  # noqa: E501
        """Read global health performance monitoring configuration  # noqa: E501

        Read global health performance monitoring configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_aggregation_service_global_config_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: GlobalCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aggregation_service_global_config" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hpm/global-config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GlobalCollectionConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_feature_stack_configuration(self, feature_stack_name, **kwargs):  # noqa: E501
        """Read health performance monitoring configuration for feature stack  # noqa: E501

        Returns the complete set of client type data collection configuration records for the specified feature stack.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_stack_configuration(feature_stack_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str feature_stack_name: (required)
        :return: FeatureStackCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_feature_stack_configuration_with_http_info(feature_stack_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_feature_stack_configuration_with_http_info(feature_stack_name, **kwargs)  # noqa: E501
            return data

    def get_feature_stack_configuration_with_http_info(self, feature_stack_name, **kwargs):  # noqa: E501
        """Read health performance monitoring configuration for feature stack  # noqa: E501

        Returns the complete set of client type data collection configuration records for the specified feature stack.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_feature_stack_configuration_with_http_info(feature_stack_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str feature_stack_name: (required)
        :return: FeatureStackCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feature_stack_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_feature_stack_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'feature_stack_name' is set
        if ('feature_stack_name' not in params or
                params['feature_stack_name'] is None):
            raise ValueError("Missing the required parameter `feature_stack_name` when calling `get_feature_stack_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'feature_stack_name' in params:
            path_params['feature-stack-name'] = params['feature_stack_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hpm/features/{feature-stack-name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureStackCollectionConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_feature_stack_configurations(self, **kwargs):  # noqa: E501
        """List all health performance monitoring feature stacks  # noqa: E501

        List all health performance monitoring feature stacks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_feature_stack_configurations(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FeatureStackCollectionConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_feature_stack_configurations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_feature_stack_configurations_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_feature_stack_configurations_with_http_info(self, **kwargs):  # noqa: E501
        """List all health performance monitoring feature stacks  # noqa: E501

        List all health performance monitoring feature stacks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_feature_stack_configurations_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: FeatureStackCollectionConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_feature_stack_configurations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hpm/features', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureStackCollectionConfigurationList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_aggregation_service_feature_stack_configuration_reset_collection_frequency(self, feature_stack_name, action, **kwargs):  # noqa: E501
        """Reset the data collection frequency configuration setting to the default values  # noqa: E501

        Reset the data collection frequency configuration setting to the default values  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_aggregation_service_feature_stack_configuration_reset_collection_frequency(feature_stack_name, action, async=True)
        >>> result = thread.get()

        :param async bool
        :param str feature_stack_name: (required)
        :param str action: (required)
        :return: FeatureStackCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reset_aggregation_service_feature_stack_configuration_reset_collection_frequency_with_http_info(feature_stack_name, action, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_aggregation_service_feature_stack_configuration_reset_collection_frequency_with_http_info(feature_stack_name, action, **kwargs)  # noqa: E501
            return data

    def reset_aggregation_service_feature_stack_configuration_reset_collection_frequency_with_http_info(self, feature_stack_name, action, **kwargs):  # noqa: E501
        """Reset the data collection frequency configuration setting to the default values  # noqa: E501

        Reset the data collection frequency configuration setting to the default values  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_aggregation_service_feature_stack_configuration_reset_collection_frequency_with_http_info(feature_stack_name, action, async=True)
        >>> result = thread.get()

        :param async bool
        :param str feature_stack_name: (required)
        :param str action: (required)
        :return: FeatureStackCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feature_stack_name', 'action']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_aggregation_service_feature_stack_configuration_reset_collection_frequency" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'feature_stack_name' is set
        if ('feature_stack_name' not in params or
                params['feature_stack_name'] is None):
            raise ValueError("Missing the required parameter `feature_stack_name` when calling `reset_aggregation_service_feature_stack_configuration_reset_collection_frequency`")  # noqa: E501
        # verify the required parameter 'action' is set
        if ('action' not in params or
                params['action'] is None):
            raise ValueError("Missing the required parameter `action` when calling `reset_aggregation_service_feature_stack_configuration_reset_collection_frequency`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'feature_stack_name' in params:
            path_params['feature-stack-name'] = params['feature_stack_name']  # noqa: E501

        query_params = []
        if 'action' in params:
            query_params.append(('action', params['action']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hpm/features/{feature-stack-name}?action=reset_collection_frequency', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureStackCollectionConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_aggregation_service_global_config(self, global_collection_configuration, **kwargs):  # noqa: E501
        """Set the global configuration for aggregation service related data collection  # noqa: E501

        Set the global configuration for aggregation service related data collection  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_aggregation_service_global_config(global_collection_configuration, async=True)
        >>> result = thread.get()

        :param async bool
        :param GlobalCollectionConfiguration global_collection_configuration: (required)
        :return: GlobalCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_aggregation_service_global_config_with_http_info(global_collection_configuration, **kwargs)  # noqa: E501
        else:
            (data) = self.update_aggregation_service_global_config_with_http_info(global_collection_configuration, **kwargs)  # noqa: E501
            return data

    def update_aggregation_service_global_config_with_http_info(self, global_collection_configuration, **kwargs):  # noqa: E501
        """Set the global configuration for aggregation service related data collection  # noqa: E501

        Set the global configuration for aggregation service related data collection  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_aggregation_service_global_config_with_http_info(global_collection_configuration, async=True)
        >>> result = thread.get()

        :param async bool
        :param GlobalCollectionConfiguration global_collection_configuration: (required)
        :return: GlobalCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['global_collection_configuration']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_aggregation_service_global_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'global_collection_configuration' is set
        if ('global_collection_configuration' not in params or
                params['global_collection_configuration'] is None):
            raise ValueError("Missing the required parameter `global_collection_configuration` when calling `update_aggregation_service_global_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'global_collection_configuration' in params:
            body_params = params['global_collection_configuration']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hpm/global-config', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GlobalCollectionConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_feature_stack_configuration(self, feature_stack_name, feature_stack_collection_configuration, **kwargs):  # noqa: E501
        """Update health performance monitoring configuration for feature stack  # noqa: E501

        Apply the data collection configuration for the specified feature stack.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_feature_stack_configuration(feature_stack_name, feature_stack_collection_configuration, async=True)
        >>> result = thread.get()

        :param async bool
        :param str feature_stack_name: (required)
        :param FeatureStackCollectionConfiguration feature_stack_collection_configuration: (required)
        :return: FeatureStackCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_feature_stack_configuration_with_http_info(feature_stack_name, feature_stack_collection_configuration, **kwargs)  # noqa: E501
        else:
            (data) = self.update_feature_stack_configuration_with_http_info(feature_stack_name, feature_stack_collection_configuration, **kwargs)  # noqa: E501
            return data

    def update_feature_stack_configuration_with_http_info(self, feature_stack_name, feature_stack_collection_configuration, **kwargs):  # noqa: E501
        """Update health performance monitoring configuration for feature stack  # noqa: E501

        Apply the data collection configuration for the specified feature stack.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_feature_stack_configuration_with_http_info(feature_stack_name, feature_stack_collection_configuration, async=True)
        >>> result = thread.get()

        :param async bool
        :param str feature_stack_name: (required)
        :param FeatureStackCollectionConfiguration feature_stack_collection_configuration: (required)
        :return: FeatureStackCollectionConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feature_stack_name', 'feature_stack_collection_configuration']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_feature_stack_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'feature_stack_name' is set
        if ('feature_stack_name' not in params or
                params['feature_stack_name'] is None):
            raise ValueError("Missing the required parameter `feature_stack_name` when calling `update_feature_stack_configuration`")  # noqa: E501
        # verify the required parameter 'feature_stack_collection_configuration' is set
        if ('feature_stack_collection_configuration' not in params or
                params['feature_stack_collection_configuration'] is None):
            raise ValueError("Missing the required parameter `feature_stack_collection_configuration` when calling `update_feature_stack_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'feature_stack_name' in params:
            path_params['feature-stack-name'] = params['feature_stack_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'feature_stack_collection_configuration' in params:
            body_params = params['feature_stack_collection_configuration']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/hpm/features/{feature-stack-name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeatureStackCollectionConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
