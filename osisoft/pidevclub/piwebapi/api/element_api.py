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

class ElementApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

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

		return self.api_client.call_api('/elements', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIElement',
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

		return self.api_client.call_api('/elements/{webId}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update(self, web_id, element, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_with_http_info(web_id, element, **kwargs)
		else:
			(data) = self.update_with_http_info(web_id, element, **kwargs)
			return data

	def update_with_http_info(self, web_id, element, **kwargs):
		all_params = ['web_id', 'element']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `update_with_http_info`")
		if ('element' not in params) or (params['element'] is None):
			raise ValueError("Missing the required parameter `element` when calling `update_with_http_info`")

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
		if 'element' in params:
			body_params = params['element']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}', 'PATCH',
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


	def delete(self, web_id, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.delete_with_http_info(web_id, **kwargs)
		else:
			(data) = self.delete_with_http_info(web_id, **kwargs)
			return data

	def delete_with_http_info(self, web_id, **kwargs):
		all_params = ['web_id']
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

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `delete_with_http_info`")

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

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}', 'DELETE',
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


	def get_analyses(self, web_id, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_analyses_with_http_info(web_id, max_count, selected_fields, sort_field, sort_order, start_index, web_id_type, **kwargs)
		else:
			(data) = self.get_analyses_with_http_info(web_id, max_count, selected_fields, sort_field, sort_order, start_index, web_id_type, **kwargs)
			return data

	def get_analyses_with_http_info(self, web_id, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'max_count', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_analyses_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_analyses_with_http_info`")

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
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/analyses', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAnalysis',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_analysis(self, web_id, analysis, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_analysis_with_http_info(web_id, analysis, web_id_type, **kwargs)
		else:
			(data) = self.create_analysis_with_http_info(web_id, analysis, web_id_type, **kwargs)
			return data

	def create_analysis_with_http_info(self, web_id, analysis, web_id_type=None, **kwargs):
		all_params = ['web_id', 'analysis', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_analysis_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_analysis_with_http_info`")
		if ('analysis' not in params) or (params['analysis'] is None):
			raise ValueError("Missing the required parameter `analysis` when calling `create_analysis_with_http_info`")

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
		if 'analysis' in params:
			body_params = params['analysis']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/analyses', 'POST',
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


	def get_attributes(self, web_id, category_name=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_index=None, template_name=None, value_type=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_attributes_with_http_info(web_id, category_name, max_count, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_index, template_name, value_type, web_id_type, **kwargs)
		else:
			(data) = self.get_attributes_with_http_info(web_id, category_name, max_count, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_index, template_name, value_type, web_id_type, **kwargs)
			return data

	def get_attributes_with_http_info(self, web_id, category_name=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_index=None, template_name=None, value_type=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'start_index', 'template_name', 'value_type', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_attributes_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_attributes_with_http_info`")

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
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'search_full_hierarchy' in params:
			if (params['search_full_hierarchy'] is not None):
				query_params['searchFullHierarchy'] = params['search_full_hierarchy']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'show_excluded' in params:
			if (params['show_excluded'] is not None):
				query_params['showExcluded'] = params['show_excluded']
		if 'show_hidden' in params:
			if (params['show_hidden'] is not None):
				query_params['showHidden'] = params['show_hidden']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'value_type' in params:
			if (params['value_type'] is not None):
				query_params['valueType'] = params['value_type']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/attributes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAttribute',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_attribute(self, web_id, attribute, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_attribute_with_http_info(web_id, attribute, web_id_type, **kwargs)
		else:
			(data) = self.create_attribute_with_http_info(web_id, attribute, web_id_type, **kwargs)
			return data

	def create_attribute_with_http_info(self, web_id, attribute, web_id_type=None, **kwargs):
		all_params = ['web_id', 'attribute', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_attribute_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_attribute_with_http_info`")
		if ('attribute' not in params) or (params['attribute'] is None):
			raise ValueError("Missing the required parameter `attribute` when calling `create_attribute_with_http_info`")

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
		if 'attribute' in params:
			body_params = params['attribute']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/attributes', 'POST',
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


	def get_categories(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_categories_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_categories_with_http_info(web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_categories_with_http_info(self, web_id, selected_fields=None, web_id_type=None, **kwargs):
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
					" to method get_categories_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_categories_with_http_info`")

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

		return self.api_client.call_api('/elements/{webId}/categories', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsElementCategory',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_config(self, web_id, include_child_elements=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_config_with_http_info(web_id, include_child_elements, **kwargs)
		else:
			(data) = self.create_config_with_http_info(web_id, include_child_elements, **kwargs)
			return data

	def create_config_with_http_info(self, web_id, include_child_elements=None, **kwargs):
		all_params = ['web_id', 'include_child_elements']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_config_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_config_with_http_info`")

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
		if 'include_child_elements' in params:
			if (params['include_child_elements'] is not None):
				query_params['includeChildElements'] = params['include_child_elements']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/config', 'POST',
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


	def find_element_attributes(self, web_id, attribute_category=None, attribute_description_filter=None, attribute_name_filter=None, attribute_type=None, element_category=None, element_description_filter=None, element_name_filter=None, element_template=None, element_type=None, max_count=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.find_element_attributes_with_http_info(web_id, attribute_category, attribute_description_filter, attribute_name_filter, attribute_type, element_category, element_description_filter, element_name_filter, element_template, element_type, max_count, search_full_hierarchy, selected_fields, sort_field, sort_order, start_index, web_id_type, **kwargs)
		else:
			(data) = self.find_element_attributes_with_http_info(web_id, attribute_category, attribute_description_filter, attribute_name_filter, attribute_type, element_category, element_description_filter, element_name_filter, element_template, element_type, max_count, search_full_hierarchy, selected_fields, sort_field, sort_order, start_index, web_id_type, **kwargs)
			return data

	def find_element_attributes_with_http_info(self, web_id, attribute_category=None, attribute_description_filter=None, attribute_name_filter=None, attribute_type=None, element_category=None, element_description_filter=None, element_name_filter=None, element_template=None, element_type=None, max_count=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'attribute_category', 'attribute_description_filter', 'attribute_name_filter', 'attribute_type', 'element_category', 'element_description_filter', 'element_name_filter', 'element_template', 'element_type', 'max_count', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method find_element_attributes_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `find_element_attributes_with_http_info`")

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
		if 'attribute_category' in params:
			if (params['attribute_category'] is not None):
				query_params['attributeCategory'] = params['attribute_category']
		if 'attribute_description_filter' in params:
			if (params['attribute_description_filter'] is not None):
				query_params['attributeDescriptionFilter'] = params['attribute_description_filter']
		if 'attribute_name_filter' in params:
			if (params['attribute_name_filter'] is not None):
				query_params['attributeNameFilter'] = params['attribute_name_filter']
		if 'attribute_type' in params:
			if (params['attribute_type'] is not None):
				query_params['attributeType'] = params['attribute_type']
		if 'element_category' in params:
			if (params['element_category'] is not None):
				query_params['elementCategory'] = params['element_category']
		if 'element_description_filter' in params:
			if (params['element_description_filter'] is not None):
				query_params['elementDescriptionFilter'] = params['element_description_filter']
		if 'element_name_filter' in params:
			if (params['element_name_filter'] is not None):
				query_params['elementNameFilter'] = params['element_name_filter']
		if 'element_template' in params:
			if (params['element_template'] is not None):
				query_params['elementTemplate'] = params['element_template']
		if 'element_type' in params:
			if (params['element_type'] is not None):
				query_params['elementType'] = params['element_type']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'search_full_hierarchy' in params:
			if (params['search_full_hierarchy'] is not None):
				query_params['searchFullHierarchy'] = params['search_full_hierarchy']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/elementattributes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsAttribute',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_elements(self, web_id, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_elements_with_http_info(web_id, category_name, description_filter, element_type, max_count, name_filter, search_full_hierarchy, selected_fields, sort_field, sort_order, start_index, template_name, web_id_type, **kwargs)
		else:
			(data) = self.get_elements_with_http_info(web_id, category_name, description_filter, element_type, max_count, name_filter, search_full_hierarchy, selected_fields, sort_field, sort_order, start_index, template_name, web_id_type, **kwargs)
			return data

	def get_elements_with_http_info(self, web_id, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'description_filter', 'element_type', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'template_name', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_elements_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_elements_with_http_info`")

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
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'description_filter' in params:
			if (params['description_filter'] is not None):
				query_params['descriptionFilter'] = params['description_filter']
		if 'element_type' in params:
			if (params['element_type'] is not None):
				query_params['elementType'] = params['element_type']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'search_full_hierarchy' in params:
			if (params['search_full_hierarchy'] is not None):
				query_params['searchFullHierarchy'] = params['search_full_hierarchy']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/elements', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_element(self, web_id, element, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_element_with_http_info(web_id, element, web_id_type, **kwargs)
		else:
			(data) = self.create_element_with_http_info(web_id, element, web_id_type, **kwargs)
			return data

	def create_element_with_http_info(self, web_id, element, web_id_type=None, **kwargs):
		all_params = ['web_id', 'element', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_element_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `create_element_with_http_info`")
		if ('element' not in params) or (params['element'] is None):
			raise ValueError("Missing the required parameter `element` when calling `create_element_with_http_info`")

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
		if 'element' in params:
			body_params = params['element']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/elements', 'POST',
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


	def get_event_frames(self, web_id, can_be_acknowledged=None, category_name=None, end_time=None, is_acknowledged=None, max_count=None, name_filter=None, search_mode=None, selected_fields=None, severity=None, sort_field=None, sort_order=None, start_index=None, start_time=None, template_name=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_event_frames_with_http_info(web_id, can_be_acknowledged, category_name, end_time, is_acknowledged, max_count, name_filter, search_mode, selected_fields, severity, sort_field, sort_order, start_index, start_time, template_name, web_id_type, **kwargs)
		else:
			(data) = self.get_event_frames_with_http_info(web_id, can_be_acknowledged, category_name, end_time, is_acknowledged, max_count, name_filter, search_mode, selected_fields, severity, sort_field, sort_order, start_index, start_time, template_name, web_id_type, **kwargs)
			return data

	def get_event_frames_with_http_info(self, web_id, can_be_acknowledged=None, category_name=None, end_time=None, is_acknowledged=None, max_count=None, name_filter=None, search_mode=None, selected_fields=None, severity=None, sort_field=None, sort_order=None, start_index=None, start_time=None, template_name=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'can_be_acknowledged', 'category_name', 'end_time', 'is_acknowledged', 'max_count', 'name_filter', 'search_mode', 'selected_fields', 'severity', 'sort_field', 'sort_order', 'start_index', 'start_time', 'template_name', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_event_frames_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_event_frames_with_http_info`")

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
		if 'can_be_acknowledged' in params:
			if (params['can_be_acknowledged'] is not None):
				query_params['canBeAcknowledged'] = params['can_be_acknowledged']
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'is_acknowledged' in params:
			if (params['is_acknowledged'] is not None):
				query_params['isAcknowledged'] = params['is_acknowledged']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'search_mode' in params:
			if (params['search_mode'] is not None):
				query_params['searchMode'] = params['search_mode']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'severity' in params:
			if (params['severity'] is not None):
				query_params['severity'] = params['severity']
				collection_formats['severity'] = 'multi'
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/eventframes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsEventFrame',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_referenced_elements(self, web_id, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_referenced_elements_with_http_info(web_id, category_name, description_filter, element_type, max_count, name_filter, selected_fields, sort_field, sort_order, start_index, template_name, web_id_type, **kwargs)
		else:
			(data) = self.get_referenced_elements_with_http_info(web_id, category_name, description_filter, element_type, max_count, name_filter, selected_fields, sort_field, sort_order, start_index, template_name, web_id_type, **kwargs)
			return data

	def get_referenced_elements_with_http_info(self, web_id, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'description_filter', 'element_type', 'max_count', 'name_filter', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'template_name', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_referenced_elements_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_referenced_elements_with_http_info`")

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
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'description_filter' in params:
			if (params['description_filter'] is not None):
				query_params['descriptionFilter'] = params['description_filter']
		if 'element_type' in params:
			if (params['element_type'] is not None):
				query_params['elementType'] = params['element_type']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/referencedelements', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def add_referenced_element(self, web_id, referenced_element_web_id, reference_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.add_referenced_element_with_http_info(web_id, referenced_element_web_id, reference_type, **kwargs)
		else:
			(data) = self.add_referenced_element_with_http_info(web_id, referenced_element_web_id, reference_type, **kwargs)
			return data

	def add_referenced_element_with_http_info(self, web_id, referenced_element_web_id, reference_type=None, **kwargs):
		all_params = ['web_id', 'referenced_element_web_id', 'reference_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method add_referenced_element_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `add_referenced_element_with_http_info`")
		if ('referenced_element_web_id' not in params) or (params['referenced_element_web_id'] is None):
			raise ValueError("Missing the required parameter `referenced_element_web_id` when calling `add_referenced_element_with_http_info`")

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
		if 'referenced_element_web_id' in params:
			if (params['referenced_element_web_id'] is not None):
				query_params['referencedElementWebId'] = params['referenced_element_web_id']
				collection_formats['referencedElementWebId'] = 'multi'
		if 'reference_type' in params:
			if (params['reference_type'] is not None):
				query_params['referenceType'] = params['reference_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/referencedelements', 'POST',
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


	def remove_referenced_element(self, web_id, referenced_element_web_id, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.remove_referenced_element_with_http_info(web_id, referenced_element_web_id, **kwargs)
		else:
			(data) = self.remove_referenced_element_with_http_info(web_id, referenced_element_web_id, **kwargs)
			return data

	def remove_referenced_element_with_http_info(self, web_id, referenced_element_web_id, **kwargs):
		all_params = ['web_id', 'referenced_element_web_id']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method remove_referenced_element_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `remove_referenced_element_with_http_info`")
		if ('referenced_element_web_id' not in params) or (params['referenced_element_web_id'] is None):
			raise ValueError("Missing the required parameter `referenced_element_web_id` when calling `remove_referenced_element_with_http_info`")

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
		if 'referenced_element_web_id' in params:
			if (params['referenced_element_web_id'] is not None):
				query_params['referencedElementWebId'] = params['referenced_element_web_id']
				collection_formats['referencedElementWebId'] = 'multi'

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/referencedelements', 'DELETE',
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


	def get_security(self, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_with_http_info(web_id, user_identity, force_refresh, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_with_http_info(web_id, user_identity, force_refresh, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_with_http_info(self, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'user_identity', 'force_refresh', 'selected_fields', 'web_id_type']
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

		return self.api_client.call_api('/elements/{webId}/security', 'GET',
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


	def get_security_entries(self, web_id, name_filter=None, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_entries_with_http_info(web_id, name_filter, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_entries_with_http_info(web_id, name_filter, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_entries_with_http_info(self, web_id, name_filter=None, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'name_filter', 'selected_fields', 'web_id_type']
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

		return self.api_client.call_api('/elements/{webId}/securityentries', 'GET',
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


	def create_security_entry(self, web_id, security_entry, apply_to_children=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_security_entry_with_http_info(web_id, security_entry, apply_to_children, web_id_type, **kwargs)
		else:
			(data) = self.create_security_entry_with_http_info(web_id, security_entry, apply_to_children, web_id_type, **kwargs)
			return data

	def create_security_entry_with_http_info(self, web_id, security_entry, apply_to_children=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'security_entry', 'apply_to_children', 'web_id_type']
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
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/securityentries', 'POST',
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


	def get_security_entry_by_name(self, name, web_id, selected_fields=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_security_entry_by_name_with_http_info(name, web_id, selected_fields, web_id_type, **kwargs)
		else:
			(data) = self.get_security_entry_by_name_with_http_info(name, web_id, selected_fields, web_id_type, **kwargs)
			return data

	def get_security_entry_by_name_with_http_info(self, name, web_id, selected_fields=None, web_id_type=None, **kwargs):
		all_params = ['name', 'web_id', 'selected_fields', 'web_id_type']
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

		return self.api_client.call_api('/elements/{webId}/securityentries/{name}', 'GET',
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


	def update_security_entry(self, name, web_id, security_entry, apply_to_children=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_security_entry_with_http_info(name, web_id, security_entry, apply_to_children, **kwargs)
		else:
			(data) = self.update_security_entry_with_http_info(name, web_id, security_entry, apply_to_children, **kwargs)
			return data

	def update_security_entry_with_http_info(self, name, web_id, security_entry, apply_to_children=None, **kwargs):
		all_params = ['name', 'web_id', 'security_entry', 'apply_to_children']
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

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/securityentries/{name}', 'PUT',
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


	def delete_security_entry(self, name, web_id, apply_to_children=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.delete_security_entry_with_http_info(name, web_id, apply_to_children, **kwargs)
		else:
			(data) = self.delete_security_entry_with_http_info(name, web_id, apply_to_children, **kwargs)
			return data

	def delete_security_entry_with_http_info(self, name, web_id, apply_to_children=None, **kwargs):
		all_params = ['name', 'web_id', 'apply_to_children']
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

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/{webId}/securityentries/{name}', 'DELETE',
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


	def get_multiple(self, as_parallel=None, include_mode=None, path=None, selected_fields=None, web_id=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_multiple_with_http_info(as_parallel, include_mode, path, selected_fields, web_id, web_id_type, **kwargs)
		else:
			(data) = self.get_multiple_with_http_info(as_parallel, include_mode, path, selected_fields, web_id, web_id_type, **kwargs)
			return data

	def get_multiple_with_http_info(self, as_parallel=None, include_mode=None, path=None, selected_fields=None, web_id=None, web_id_type=None, **kwargs):
		all_params = ['as_parallel', 'include_mode', 'path', 'selected_fields', 'web_id', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_multiple_with_http_info" % key
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
		if 'as_parallel' in params:
			if (params['as_parallel'] is not None):
				query_params['asParallel'] = params['as_parallel']
		if 'include_mode' in params:
			if (params['include_mode'] is not None):
				query_params['includeMode'] = params['include_mode']
		if 'path' in params:
			if (params['path'] is not None):
				query_params['path'] = params['path']
				collection_formats['path'] = 'multi'
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/multiple', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsItemElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_elements_query(self, database_web_id=None, max_count=None, query=None, selected_fields=None, start_index=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_elements_query_with_http_info(database_web_id, max_count, query, selected_fields, start_index, web_id_type, **kwargs)
		else:
			(data) = self.get_elements_query_with_http_info(database_web_id, max_count, query, selected_fields, start_index, web_id_type, **kwargs)
			return data

	def get_elements_query_with_http_info(self, database_web_id=None, max_count=None, query=None, selected_fields=None, start_index=None, web_id_type=None, **kwargs):
		all_params = ['database_web_id', 'max_count', 'query', 'selected_fields', 'start_index', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_elements_query_with_http_info" % key
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
		if 'database_web_id' in params:
			if (params['database_web_id'] is not None):
				query_params['databaseWebId'] = params['database_web_id']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'query' in params:
			if (params['query'] is not None):
				query_params['query'] = params['query']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/search', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def create_search_by_attribute(self, query, no_results=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.create_search_by_attribute_with_http_info(query, no_results, web_id_type, **kwargs)
		else:
			(data) = self.create_search_by_attribute_with_http_info(query, no_results, web_id_type, **kwargs)
			return data

	def create_search_by_attribute_with_http_info(self, query, no_results=None, web_id_type=None, **kwargs):
		all_params = ['query', 'no_results', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_search_by_attribute_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('query' not in params) or (params['query'] is None):
			raise ValueError("Missing the required parameter `query` when calling `create_search_by_attribute_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'query' in params:
			body_params = params['query']
		if 'no_results' in params:
			if (params['no_results'] is not None):
				query_params['noResults'] = params['no_results']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/searchbyattribute', 'POST',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def execute_search_by_attribute(self, search_id, category_name=None, description_filter=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.execute_search_by_attribute_with_http_info(search_id, category_name, description_filter, max_count, name_filter, search_full_hierarchy, selected_fields, sort_field, sort_order, start_index, web_id_type, **kwargs)
		else:
			(data) = self.execute_search_by_attribute_with_http_info(search_id, category_name, description_filter, max_count, name_filter, search_full_hierarchy, selected_fields, sort_field, sort_order, start_index, web_id_type, **kwargs)
			return data

	def execute_search_by_attribute_with_http_info(self, search_id, category_name=None, description_filter=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None, **kwargs):
		all_params = ['search_id', 'category_name', 'description_filter', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method execute_search_by_attribute_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('search_id' not in params) or (params['search_id'] is None):
			raise ValueError("Missing the required parameter `search_id` when calling `execute_search_by_attribute_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'search_id' in params:
			if (params['search_id'] is not None):
				path_params['searchId'] = params['search_id']
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'description_filter' in params:
			if (params['description_filter'] is not None):
				query_params['descriptionFilter'] = params['description_filter']
		if 'max_count' in params:
			if (params['max_count'] is not None):
				query_params['maxCount'] = params['max_count']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'search_full_hierarchy' in params:
			if (params['search_full_hierarchy'] is not None):
				query_params['searchFullHierarchy'] = params['search_full_hierarchy']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_index' in params:
			if (params['start_index'] is not None):
				query_params['startIndex'] = params['start_index']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/elements/searchbyattribute/{searchId}', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsElement',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)

