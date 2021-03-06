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


class ApiServicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_tasks(self, **kwargs):  # noqa: E501
        """Get information about all tasks  # noqa: E501

        Get information about all tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_tasks(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included to result of query
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param str request_uri: Request URI(s) to include in query result
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :param str status: Status(es) to include in query result
        :param str user: Names of users to include in query result
        :return: TaskListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_tasks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_tasks_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """Get information about all tasks  # noqa: E501

        Get information about all tasks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_tasks_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cursor: Opaque cursor to be used for getting next page of records (supplied by current result page)
        :param str included_fields: Comma separated list of fields that should be included to result of query
        :param int page_size: Maximum number of results to return in this page (server may return fewer)
        :param str request_uri: Request URI(s) to include in query result
        :param bool sort_ascending:
        :param str sort_by: Field by which records are sorted
        :param str status: Status(es) to include in query result
        :param str user: Names of users to include in query result
        :return: TaskListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor', 'included_fields', 'page_size', 'request_uri', 'sort_ascending', 'sort_by', 'status', 'user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 1000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `list_tasks`, must be a value less than or equal to `1000`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `list_tasks`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'included_fields' in params:
            query_params.append(('included_fields', params['included_fields']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'request_uri' in params:
            query_params.append(('request_uri', params['request_uri']))  # noqa: E501
        if 'sort_ascending' in params:
            query_params.append(('sort_ascending', params['sort_ascending']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'user' in params:
            query_params.append(('user', params['user']))  # noqa: E501

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
            '/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskListResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_authentication_policy_properties(self, **kwargs):  # noqa: E501
        """Read node authentication policy configuration  # noqa: E501

        Returns information about the currently configured authentication policies on the node.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_authentication_policy_properties(async=True)
        >>> result = thread.get()

        :param async bool
        :return: AuthenticationPolicyProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.read_authentication_policy_properties_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_authentication_policy_properties_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_authentication_policy_properties_with_http_info(self, **kwargs):  # noqa: E501
        """Read node authentication policy configuration  # noqa: E501

        Returns information about the currently configured authentication policies on the node.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_authentication_policy_properties_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: AuthenticationPolicyProperties
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
                    " to method read_authentication_policy_properties" % key
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
            '/node/aaa/auth-policy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationPolicyProperties',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_task_properties(self, task_id, **kwargs):  # noqa: E501
        """Get information about the specified task  # noqa: E501

        Get information about the specified task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_task_properties(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: ID of task to read (required)
        :return: TaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.read_task_properties_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_task_properties_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def read_task_properties_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Get information about the specified task  # noqa: E501

        Get information about the specified task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_task_properties_with_http_info(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: ID of task to read (required)
        :return: TaskProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_task_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `read_task_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task-id'] = params['task_id']  # noqa: E501

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
            '/tasks/{task-id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskProperties',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_task_result(self, task_id, **kwargs):  # noqa: E501
        """Get the response of a task  # noqa: E501

        Get the response of a task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_task_result(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: ID of task to read (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.read_task_result_with_http_info(task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_task_result_with_http_info(task_id, **kwargs)  # noqa: E501
            return data

    def read_task_result_with_http_info(self, task_id, **kwargs):  # noqa: E501
        """Get the response of a task  # noqa: E501

        Get the response of a task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_task_result_with_http_info(task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str task_id: ID of task to read (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_task_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `read_task_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['task-id'] = params['task_id']  # noqa: E501

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
            '/tasks/{task-id}/response', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_batch_request(self, batch_request, **kwargs):  # noqa: E501
        """Register a Collection of API Calls at a Single End Point  # noqa: E501

        Enables you to make multiple API requests using a single request. The batch API takes in an array of logical HTTP requests represented as JSON arrays. Each request has a method (GET, PUT, POST, or DELETE), a relative_url (the portion of the URL after https://&lt;nsx-mgr&gt;/api/), optional headers array (corresponding to HTTP headers) and an optional body (for POST and PUT requests). The batch API returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array and an optional body (which is a JSON-encoded string).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.register_batch_request(batch_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param BatchRequest batch_request: (required)
        :param bool atomic: transactional atomicity for the batch of requests embedded in the batch list
        :return: BatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.register_batch_request_with_http_info(batch_request, **kwargs)  # noqa: E501
        else:
            (data) = self.register_batch_request_with_http_info(batch_request, **kwargs)  # noqa: E501
            return data

    def register_batch_request_with_http_info(self, batch_request, **kwargs):  # noqa: E501
        """Register a Collection of API Calls at a Single End Point  # noqa: E501

        Enables you to make multiple API requests using a single request. The batch API takes in an array of logical HTTP requests represented as JSON arrays. Each request has a method (GET, PUT, POST, or DELETE), a relative_url (the portion of the URL after https://&lt;nsx-mgr&gt;/api/), optional headers array (corresponding to HTTP headers) and an optional body (for POST and PUT requests). The batch API returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array and an optional body (which is a JSON-encoded string).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.register_batch_request_with_http_info(batch_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param BatchRequest batch_request: (required)
        :param bool atomic: transactional atomicity for the batch of requests embedded in the batch list
        :return: BatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_request', 'atomic']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_batch_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_request' is set
        if ('batch_request' not in params or
                params['batch_request'] is None):
            raise ValueError("Missing the required parameter `batch_request` when calling `register_batch_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'atomic' in params:
            query_params.append(('atomic', params['atomic']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_request' in params:
            body_params = params['batch_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/batch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_authentication_policy_properties(self, authentication_policy_properties, **kwargs):  # noqa: E501
        """Update node authentication policy configuration  # noqa: E501

        Update the currently configured authentication policy on the node. If any of api_max_auth_failures, api_failed_auth_reset_period, or api_failed_auth_lockout_period are modified, the http service is automatically restarted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_authentication_policy_properties(authentication_policy_properties, async=True)
        >>> result = thread.get()

        :param async bool
        :param AuthenticationPolicyProperties authentication_policy_properties: (required)
        :return: AuthenticationPolicyProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_authentication_policy_properties_with_http_info(authentication_policy_properties, **kwargs)  # noqa: E501
        else:
            (data) = self.update_authentication_policy_properties_with_http_info(authentication_policy_properties, **kwargs)  # noqa: E501
            return data

    def update_authentication_policy_properties_with_http_info(self, authentication_policy_properties, **kwargs):  # noqa: E501
        """Update node authentication policy configuration  # noqa: E501

        Update the currently configured authentication policy on the node. If any of api_max_auth_failures, api_failed_auth_reset_period, or api_failed_auth_lockout_period are modified, the http service is automatically restarted.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_authentication_policy_properties_with_http_info(authentication_policy_properties, async=True)
        >>> result = thread.get()

        :param async bool
        :param AuthenticationPolicyProperties authentication_policy_properties: (required)
        :return: AuthenticationPolicyProperties
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authentication_policy_properties']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_authentication_policy_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authentication_policy_properties' is set
        if ('authentication_policy_properties' not in params or
                params['authentication_policy_properties'] is None):
            raise ValueError("Missing the required parameter `authentication_policy_properties` when calling `update_authentication_policy_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authentication_policy_properties' in params:
            body_params = params['authentication_policy_properties']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/node/aaa/auth-policy', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthenticationPolicyProperties',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
