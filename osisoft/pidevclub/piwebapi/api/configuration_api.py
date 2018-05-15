# coding: utf-8

"""
	Copyright 2018 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from __future__ import absolute_import
from six import iteritems

class ConfigurationApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

	def list(self, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.list_with_http_info(**kwargs)
		else:
			(data) = self.list_with_http_info(**kwargs)
			return data

	def list_with_http_info(self, **kwargs):
		all_params = []
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method list_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']


		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/system/configuration', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='dict(str, object)',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get(self, key, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_with_http_info(key, **kwargs)
		else:
			(data) = self.get_with_http_info(key, **kwargs)
			return data

	def get_with_http_info(self, key, **kwargs):
		all_params = ['key']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('key' not in params) or (params['key'] is None):
			raise ValueError("Missing the required parameter `key` when calling `get_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'key' in params:
			if (params['key'] is not None):
				path_params['key'] = params['key']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/system/configuration/{key}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='object',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def delete(self, key, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.delete_with_http_info(key, **kwargs)
		else:
			(data) = self.delete_with_http_info(key, **kwargs)
			return data

	def delete_with_http_info(self, key, **kwargs):
		all_params = ['key']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method delete_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('key' not in params) or (params['key'] is None):
			raise ValueError("Missing the required parameter `key` when calling `delete_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'key' in params:
			if (params['key'] is not None):
				path_params['key'] = params['key']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/system/configuration/{key}', 'DELETE',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type =None,
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)

