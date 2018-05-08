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

class AssetServerApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

	def list(self, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.list_with_http_info(selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.list_with_http_info(selected_fields, web_id_type, **kwargs)
			return data

	def list_with_http_info(self, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['selected_fields', 'web_id_type']
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
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAssetServer',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_by_name(self, name, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_by_name_with_http_info(name, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_by_name_with_http_info(name, selected_fields, web_id_type, **kwargs)
			return data

	def get_by_name_with_http_info(self, name, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['name', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_by_name_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `get_by_name_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'name' in params:
			if (params['name'] is not None):
				query_params['name'] = params['name']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIAssetServer',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_by_path(self, path, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_by_path_with_http_info(path, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_by_path_with_http_info(path, selected_fields, web_id_type, **kwargs)
			return data

	def get_by_path_with_http_info(self, path, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['path', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_by_path_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('path' not in params) or (params['path'] is None):
			raise ValueError("Missing the required parameter `path` when calling `get_by_path_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'path' in params:
			if (params['path'] is not None):
				query_params['path'] = params['path']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIAssetServer',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_with_http_info(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'web_id_type']
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

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIAssetServer',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_analysis_rule_plug_ins(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_analysis_rule_plug_ins_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_analysis_rule_plug_ins_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_analysis_rule_plug_ins_with_http_info(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_analysis_rule_plug_ins_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_analysis_rule_plug_ins_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/analysisruleplugins', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAnalysisRulePlugIn',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_databases(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_databases_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_databases_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_databases_with_http_info(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_databases_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_databases_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/assetdatabases', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAssetDatabase',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_asset_database(self, web_id, database, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_asset_database_with_http_info(web_id, database, web_id_type, **kwargs)
		else:
			(data) = self.create_asset_database_with_http_info(web_id, database, web_id_type, **kwargs)
			return data

	def create_asset_database_with_http_info(self, web_id, database, web_id_type=None, **kwargs):
		all_params = ['web_id', 'database', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_asset_database_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_asset_database_with_http_info`")
		if ('database' not in params) or (params['database'] is None):
			raise ValueError("Missing the required parameter `database` when calling `create_asset_database_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'database' in params:
			body_params = params['database']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/assetdatabases', 'POST',
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


	def get_security(self, web_id, security_item, user_identity, force_refresh=None, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_with_http_info(web_id, security_item, user_identity, force_refresh, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_with_http_info(web_id, security_item, user_identity, force_refresh, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_with_http_info(self, web_id, security_item, user_identity, force_refresh=None, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'security_item', 'user_identity', 'force_refresh', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_with_http_info`")
		if ('security_item' not in params) or (params['security_item'] is None):
			raise ValueError("Missing the required parameter `security_item` when calling `get_security_with_http_info`")
		if ('user_identity' not in params) or (params['user_identity'] is None):
			raise ValueError("Missing the required parameter `user_identity` when calling `get_security_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_item' in params:
			if (params['security_item'] is not None):
				query_params['securityItem'] = params['security_item']
				collection_formats['securityItem'] = 'multi'
		if 'user_identity' in params:
			if (params['user_identity'] is not None):
				query_params['userIdentity'] = params['user_identity']
				collection_formats['userIdentity'] = 'multi'
		if 'force_refresh' in params:
			if (params['force_refresh'] is not None):
				query_params['forceRefresh'] = params['force_refresh']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/security', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityRights',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_security_entries(self, web_id, name_filter=None, security_item=None, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_entries_with_http_info(web_id, name_filter, security_item, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_entries_with_http_info(web_id, name_filter, security_item, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_entries_with_http_info(self, web_id, name_filter=None, security_item=None, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'name_filter', 'security_item', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_entries_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_entries_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'security_item' in params:
			if (params['security_item'] is not None):
				query_params['securityItem'] = params['security_item']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityentries', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityEntry',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_security_entry(self, web_id, security_entry, apply_to_children=None, security_item=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_security_entry_with_http_info(web_id, security_entry, apply_to_children, security_item, web_id_type, **kwargs)
		else:
			(data) = self.create_security_entry_with_http_info(web_id, security_entry, apply_to_children, security_item, web_id_type, **kwargs)
			return data

	def create_security_entry_with_http_info(self, web_id, security_entry, apply_to_children=None, security_item=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'security_entry', 'apply_to_children', 'security_item', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_security_entry_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_security_entry_with_http_info`")
		if ('security_entry' not in params) or (params['security_entry'] is None):
			raise ValueError("Missing the required parameter `security_entry` when calling `create_security_entry_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_entry' in params:
			body_params = params['security_entry']
		if 'apply_to_children' in params:
			if (params['apply_to_children'] is not None):
				query_params['applyToChildren'] = params['apply_to_children']
		if 'security_item' in params:
			if (params['security_item'] is not None):
				query_params['securityItem'] = params['security_item']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityentries', 'POST',
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


	def get_security_entry_by_name(self, name, web_id, security_item=None, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_entry_by_name_with_http_info(name, web_id, security_item, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_entry_by_name_with_http_info(name, web_id, security_item, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_entry_by_name_with_http_info(self, name, web_id, security_item=None, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['name', 'web_id', 'security_item', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_entry_by_name_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `get_security_entry_by_name_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_entry_by_name_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'name' in params:
			if (params['name'] is not None):
				path_params['name'] = params['name']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_item' in params:
			if (params['security_item'] is not None):
				query_params['securityItem'] = params['security_item']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityentries/{name}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PISecurityEntry',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update_security_entry(self, name, web_id, security_entry, apply_to_children=None, security_item=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_security_entry_with_http_info(name, web_id, security_entry, apply_to_children, security_item, **kwargs)
		else:
			(data) = self.update_security_entry_with_http_info(name, web_id, security_entry, apply_to_children, security_item, **kwargs)
			return data

	def update_security_entry_with_http_info(self, name, web_id, security_entry, apply_to_children=None, security_item=None, **kwargs):
		all_params = ['name', 'web_id', 'security_entry', 'apply_to_children', 'security_item']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_security_entry_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `update_security_entry_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `update_security_entry_with_http_info`")
		if ('security_entry' not in params) or (params['security_entry'] is None):
			raise ValueError("Missing the required parameter `security_entry` when calling `update_security_entry_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'name' in params:
			if (params['name'] is not None):
				path_params['name'] = params['name']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_entry' in params:
			body_params = params['security_entry']
		if 'apply_to_children' in params:
			if (params['apply_to_children'] is not None):
				query_params['applyToChildren'] = params['apply_to_children']
		if 'security_item' in params:
			if (params['security_item'] is not None):
				query_params['securityItem'] = params['security_item']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityentries/{name}', 'PUT',
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


	def delete_security_entry(self, name, web_id, apply_to_children=None, security_item=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.delete_security_entry_with_http_info(name, web_id, apply_to_children, security_item, **kwargs)
		else:
			(data) = self.delete_security_entry_with_http_info(name, web_id, apply_to_children, security_item, **kwargs)
			return data

	def delete_security_entry_with_http_info(self, name, web_id, apply_to_children=None, security_item=None, **kwargs):
		all_params = ['name', 'web_id', 'apply_to_children', 'security_item']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method delete_security_entry_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('name' not in params) or (params['name'] is None):
			raise ValueError("Missing the required parameter `name` when calling `delete_security_entry_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `delete_security_entry_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'name' in params:
			if (params['name'] is not None):
				path_params['name'] = params['name']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'apply_to_children' in params:
			if (params['apply_to_children'] is not None):
				query_params['applyToChildren'] = params['apply_to_children']
		if 'security_item' in params:
			if (params['security_item'] is not None):
				query_params['securityItem'] = params['security_item']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityentries/{name}', 'DELETE',
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


	def get_security_identities(self, web_id, field=None, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_identities_with_http_info(web_id, field, max_count, query, selected_fields, sort_field, sort_order, web_id_type, **kwargs)
		else:
			(data) = self.get_security_identities_with_http_info(web_id, field, max_count, query, selected_fields, sort_field, sort_order, web_id_type, **kwargs)
			return data

	def get_security_identities_with_http_info(self, web_id, field=None, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'field', 'max_count', 'query', 'selected_fields', 'sort_field', 'sort_order', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_identities_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_identities_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'field' in params:
			if (params['field'] is not None):
				query_params['field'] = params['field']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'query' in params:
			if (params['query'] is not None):
				query_params['query'] = params['query']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityidentities', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityIdentity',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_security_identity(self, web_id, security_identity, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_security_identity_with_http_info(web_id, security_identity, web_id_type, **kwargs)
		else:
			(data) = self.create_security_identity_with_http_info(web_id, security_identity, web_id_type, **kwargs)
			return data

	def create_security_identity_with_http_info(self, web_id, security_identity, web_id_type=None, **kwargs):
		all_params = ['web_id', 'security_identity', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_security_identity_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_security_identity_with_http_info`")
		if ('security_identity' not in params) or (params['security_identity'] is None):
			raise ValueError("Missing the required parameter `security_identity` when calling `create_security_identity_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_identity' in params:
			body_params = params['security_identity']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityidentities', 'POST',
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


	def get_security_identities_for_user(self, web_id, user_identity, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_identities_for_user_with_http_info(web_id, user_identity, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_identities_for_user_with_http_info(web_id, user_identity, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_identities_for_user_with_http_info(self, web_id, user_identity, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'user_identity', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_identities_for_user_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_identities_for_user_with_http_info`")
		if ('user_identity' not in params) or (params['user_identity'] is None):
			raise ValueError("Missing the required parameter `user_identity` when calling `get_security_identities_for_user_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'user_identity' in params:
			if (params['user_identity'] is not None):
				query_params['userIdentity'] = params['user_identity']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securityidentities', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityIdentity',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_security_mappings(self, web_id, field=None, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_mappings_with_http_info(web_id, field, max_count, query, selected_fields, sort_field, sort_order, web_id_type, **kwargs)
		else:
			(data) = self.get_security_mappings_with_http_info(web_id, field, max_count, query, selected_fields, sort_field, sort_order, web_id_type, **kwargs)
			return data

	def get_security_mappings_with_http_info(self, web_id, field=None, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'field', 'max_count', 'query', 'selected_fields', 'sort_field', 'sort_order', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_security_mappings_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_security_mappings_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'field' in params:
			if (params['field'] is not None):
				query_params['field'] = params['field']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'query' in params:
			if (params['query'] is not None):
				query_params['query'] = params['query']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securitymappings', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSecurityMapping',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_security_mapping(self, web_id, security_mapping, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_security_mapping_with_http_info(web_id, security_mapping, web_id_type, **kwargs)
		else:
			(data) = self.create_security_mapping_with_http_info(web_id, security_mapping, web_id_type, **kwargs)
			return data

	def create_security_mapping_with_http_info(self, web_id, security_mapping, web_id_type=None, **kwargs):
		all_params = ['web_id', 'security_mapping', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_security_mapping_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_security_mapping_with_http_info`")
		if ('security_mapping' not in params) or (params['security_mapping'] is None):
			raise ValueError("Missing the required parameter `security_mapping` when calling `create_security_mapping_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'security_mapping' in params:
			body_params = params['security_mapping']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/securitymappings', 'POST',
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


	def get_time_rule_plug_ins(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_time_rule_plug_ins_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_time_rule_plug_ins_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_time_rule_plug_ins_with_http_info(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_time_rule_plug_ins_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_time_rule_plug_ins_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/timeruleplugins', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsTimeRulePlugIn',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_unit_classes(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_unit_classes_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_unit_classes_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_unit_classes_with_http_info(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_unit_classes_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_unit_classes_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/unitclasses', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsUnitClass',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_unit_class(self, web_id, unit_class, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_unit_class_with_http_info(web_id, unit_class, web_id_type, **kwargs)
		else:
			(data) = self.create_unit_class_with_http_info(web_id, unit_class, web_id_type, **kwargs)
			return data

	def create_unit_class_with_http_info(self, web_id, unit_class, web_id_type=None, **kwargs):
		all_params = ['web_id', 'unit_class', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_unit_class_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_unit_class_with_http_info`")
		if ('unit_class' not in params) or (params['unit_class'] is None):
			raise ValueError("Missing the required parameter `unit_class` when calling `create_unit_class_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				path_params['webId'] = params['web_id']
		if 'unit_class' in params:
			body_params = params['unit_class']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/assetservers/{webId}/unitclasses', 'POST',
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

