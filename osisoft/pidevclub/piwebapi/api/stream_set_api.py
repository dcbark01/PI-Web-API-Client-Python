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

class StreamSetApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

	def get_channel(self, web_id, category_name=None, heartbeat_rate=None, include_initial_values=None, name_filter=None, search_full_hierarchy=None, show_excluded=None, show_hidden=None, template_name=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_channel_with_http_info(web_id, category_name, heartbeat_rate, include_initial_values, name_filter, search_full_hierarchy, show_excluded, show_hidden, template_name, web_id_type, **kwargs)
		else:
			(data) = self.get_channel_with_http_info(web_id, category_name, heartbeat_rate, include_initial_values, name_filter, search_full_hierarchy, show_excluded, show_hidden, template_name, web_id_type, **kwargs)
			return data

	def get_channel_with_http_info(self, web_id, category_name=None, heartbeat_rate=None, include_initial_values=None, name_filter=None, search_full_hierarchy=None, show_excluded=None, show_hidden=None, template_name=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'heartbeat_rate', 'include_initial_values', 'name_filter', 'search_full_hierarchy', 'show_excluded', 'show_hidden', 'template_name', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_channel_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_channel_with_http_info`")

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
		if 'heartbeat_rate' in params:
			if (params['heartbeat_rate'] is not None):
				query_params['heartbeatRate'] = params['heartbeat_rate']
		if 'include_initial_values' in params:
			if (params['include_initial_values'] is not None):
				query_params['includeInitialValues'] = params['include_initial_values']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'search_full_hierarchy' in params:
			if (params['search_full_hierarchy'] is not None):
				query_params['searchFullHierarchy'] = params['search_full_hierarchy']
		if 'show_excluded' in params:
			if (params['show_excluded'] is not None):
				query_params['showExcluded'] = params['show_excluded']
		if 'show_hidden' in params:
			if (params['show_hidden'] is not None):
				query_params['showHidden'] = params['show_hidden']
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

		return self.api_client.call_api('/streamsets/{webId}/channel', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_end(self, web_id, category_name=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, template_name=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_end_with_http_info(web_id, category_name, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, template_name, web_id_type, **kwargs)
		else:
			(data) = self.get_end_with_http_info(web_id, category_name, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, template_name, web_id_type, **kwargs)
			return data

	def get_end_with_http_info(self, web_id, category_name=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, template_name=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'template_name', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_end_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_end_with_http_info`")

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

		return self.api_client.call_api('/streamsets/{webId}/end', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_interpolated(self, web_id, category_name=None, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, sync_time=None, sync_time_boundary_type=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_interpolated_with_http_info(web_id, category_name, end_time, filter_expression, include_filtered_values, interval, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_time, sync_time, sync_time_boundary_type, template_name, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_interpolated_with_http_info(web_id, category_name, end_time, filter_expression, include_filtered_values, interval, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_time, sync_time, sync_time_boundary_type, template_name, time_zone, web_id_type, **kwargs)
			return data

	def get_interpolated_with_http_info(self, web_id, category_name=None, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, sync_time=None, sync_time_boundary_type=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'start_time', 'sync_time', 'sync_time_boundary_type', 'template_name', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_interpolated_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_interpolated_with_http_info`")

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
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'include_filtered_values' in params:
			if (params['include_filtered_values'] is not None):
				query_params['includeFilteredValues'] = params['include_filtered_values']
		if 'interval' in params:
			if (params['interval'] is not None):
				query_params['interval'] = params['interval']
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
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'sync_time' in params:
			if (params['sync_time'] is not None):
				query_params['syncTime'] = params['sync_time']
		if 'sync_time_boundary_type' in params:
			if (params['sync_time_boundary_type'] is not None):
				query_params['syncTimeBoundaryType'] = params['sync_time_boundary_type']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/interpolated', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_interpolated_at_times(self, web_id, time, category_name=None, filter_expression=None, include_filtered_values=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_order=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_interpolated_at_times_with_http_info(web_id, time, category_name, filter_expression, include_filtered_values, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_order, template_name, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_interpolated_at_times_with_http_info(web_id, time, category_name, filter_expression, include_filtered_values, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_order, template_name, time_zone, web_id_type, **kwargs)
			return data

	def get_interpolated_at_times_with_http_info(self, web_id, time, category_name=None, filter_expression=None, include_filtered_values=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_order=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'time', 'category_name', 'filter_expression', 'include_filtered_values', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_order', 'template_name', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_interpolated_at_times_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_interpolated_at_times_with_http_info`")
		if ('time' not in params) or (params['time'] is None):
			raise ValueError("Missing the required parameter `time` when calling `get_interpolated_at_times_with_http_info`")

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
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
				collection_formats['time'] = 'multi'
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'include_filtered_values' in params:
			if (params['include_filtered_values'] is not None):
				query_params['includeFilteredValues'] = params['include_filtered_values']
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
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/interpolatedattimes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_plot(self, web_id, category_name=None, end_time=None, intervals=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_plot_with_http_info(web_id, category_name, end_time, intervals, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_time, template_name, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_plot_with_http_info(web_id, category_name, end_time, intervals, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_time, template_name, time_zone, web_id_type, **kwargs)
			return data

	def get_plot_with_http_info(self, web_id, category_name=None, end_time=None, intervals=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'end_time', 'intervals', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'start_time', 'template_name', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_plot_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_plot_with_http_info`")

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
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'intervals' in params:
			if (params['intervals'] is not None):
				query_params['intervals'] = params['intervals']
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
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/plot', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded(self, web_id, boundary_type=None, category_name=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_with_http_info(web_id, boundary_type, category_name, end_time, filter_expression, include_filtered_values, max_count, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_time, template_name, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_recorded_with_http_info(web_id, boundary_type, category_name, end_time, filter_expression, include_filtered_values, max_count, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, start_time, template_name, time_zone, web_id_type, **kwargs)
			return data

	def get_recorded_with_http_info(self, web_id, boundary_type=None, category_name=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'boundary_type', 'category_name', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'start_time', 'template_name', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_recorded_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_recorded_with_http_info`")

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
		if 'boundary_type' in params:
			if (params['boundary_type'] is not None):
				query_params['boundaryType'] = params['boundary_type']
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'include_filtered_values' in params:
			if (params['include_filtered_values'] is not None):
				query_params['includeFilteredValues'] = params['include_filtered_values']
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
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/recorded', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update_values(self, web_id, values, buffer_option=None, update_option=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_values_with_http_info(web_id, values, buffer_option, update_option, **kwargs)
		else:
			(data) = self.update_values_with_http_info(web_id, values, buffer_option, update_option, **kwargs)
			return data

	def update_values_with_http_info(self, web_id, values, buffer_option=None, update_option=None, **kwargs):
		all_params = ['web_id', 'values', 'buffer_option', 'update_option']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_values_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `update_values_with_http_info`")
		if ('values' not in params) or (params['values'] is None):
			raise ValueError("Missing the required parameter `values` when calling `update_values_with_http_info`")

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
		if 'values' in params:
			body_params = params['values']
		if 'buffer_option' in params:
			if (params['buffer_option'] is not None):
				query_params['bufferOption'] = params['buffer_option']
		if 'update_option' in params:
			if (params['update_option'] is not None):
				query_params['updateOption'] = params['update_option']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/recorded', 'POST',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsItemsSubstatus',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded_at_time(self, web_id, time, category_name=None, name_filter=None, retrieval_mode=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_at_time_with_http_info(web_id, time, category_name, name_filter, retrieval_mode, search_full_hierarchy, selected_fields, show_excluded, show_hidden, template_name, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_recorded_at_time_with_http_info(web_id, time, category_name, name_filter, retrieval_mode, search_full_hierarchy, selected_fields, show_excluded, show_hidden, template_name, time_zone, web_id_type, **kwargs)
			return data

	def get_recorded_at_time_with_http_info(self, web_id, time, category_name=None, name_filter=None, retrieval_mode=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'time', 'category_name', 'name_filter', 'retrieval_mode', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'template_name', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_recorded_at_time_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_recorded_at_time_with_http_info`")
		if ('time' not in params) or (params['time'] is None):
			raise ValueError("Missing the required parameter `time` when calling `get_recorded_at_time_with_http_info`")

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
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'retrieval_mode' in params:
			if (params['retrieval_mode'] is not None):
				query_params['retrievalMode'] = params['retrieval_mode']
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
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/recordedattime', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded_at_times(self, web_id, time, category_name=None, name_filter=None, retrieval_mode=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_order=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_at_times_with_http_info(web_id, time, category_name, name_filter, retrieval_mode, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_order, template_name, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_recorded_at_times_with_http_info(web_id, time, category_name, name_filter, retrieval_mode, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_order, template_name, time_zone, web_id_type, **kwargs)
			return data

	def get_recorded_at_times_with_http_info(self, web_id, time, category_name=None, name_filter=None, retrieval_mode=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_order=None, template_name=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'time', 'category_name', 'name_filter', 'retrieval_mode', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_order', 'template_name', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_recorded_at_times_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_recorded_at_times_with_http_info`")
		if ('time' not in params) or (params['time'] is None):
			raise ValueError("Missing the required parameter `time` when calling `get_recorded_at_times_with_http_info`")

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
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
				collection_formats['time'] = 'multi'
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'retrieval_mode' in params:
			if (params['retrieval_mode'] is not None):
				query_params['retrievalMode'] = params['retrieval_mode']
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
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/recordedattimes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_summaries(self, web_id, calculation_basis=None, category_name=None, end_time=None, filter_expression=None, name_filter=None, sample_interval=None, sample_type=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, start_time=None, summary_duration=None, summary_type=None, template_name=None, time_type=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_summaries_with_http_info(web_id, calculation_basis, category_name, end_time, filter_expression, name_filter, sample_interval, sample_type, search_full_hierarchy, selected_fields, show_excluded, show_hidden, start_time, summary_duration, summary_type, template_name, time_type, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_summaries_with_http_info(web_id, calculation_basis, category_name, end_time, filter_expression, name_filter, sample_interval, sample_type, search_full_hierarchy, selected_fields, show_excluded, show_hidden, start_time, summary_duration, summary_type, template_name, time_type, time_zone, web_id_type, **kwargs)
			return data

	def get_summaries_with_http_info(self, web_id, calculation_basis=None, category_name=None, end_time=None, filter_expression=None, name_filter=None, sample_interval=None, sample_type=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, start_time=None, summary_duration=None, summary_type=None, template_name=None, time_type=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'calculation_basis', 'category_name', 'end_time', 'filter_expression', 'name_filter', 'sample_interval', 'sample_type', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'start_time', 'summary_duration', 'summary_type', 'template_name', 'time_type', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_summaries_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_summaries_with_http_info`")

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
		if 'calculation_basis' in params:
			if (params['calculation_basis'] is not None):
				query_params['calculationBasis'] = params['calculation_basis']
		if 'category_name' in params:
			if (params['category_name'] is not None):
				query_params['categoryName'] = params['category_name']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'name_filter' in params:
			if (params['name_filter'] is not None):
				query_params['nameFilter'] = params['name_filter']
		if 'sample_interval' in params:
			if (params['sample_interval'] is not None):
				query_params['sampleInterval'] = params['sample_interval']
		if 'sample_type' in params:
			if (params['sample_type'] is not None):
				query_params['sampleType'] = params['sample_type']
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
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'summary_duration' in params:
			if (params['summary_duration'] is not None):
				query_params['summaryDuration'] = params['summary_duration']
		if 'summary_type' in params:
			if (params['summary_type'] is not None):
				query_params['summaryType'] = params['summary_type']
				collection_formats['summaryType'] = 'multi'
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time_type' in params:
			if (params['time_type'] is not None):
				query_params['timeType'] = params['time_type']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/summary', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamSummaries',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_values(self, web_id, category_name=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, template_name=None, time=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_values_with_http_info(web_id, category_name, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, template_name, time, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_values_with_http_info(web_id, category_name, name_filter, search_full_hierarchy, selected_fields, show_excluded, show_hidden, sort_field, sort_order, template_name, time, time_zone, web_id_type, **kwargs)
			return data

	def get_values_with_http_info(self, web_id, category_name=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, template_name=None, time=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'category_name', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'template_name', 'time', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_values_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_values_with_http_info`")

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
		if 'template_name' in params:
			if (params['template_name'] is not None):
				query_params['templateName'] = params['template_name']
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/value', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update_value(self, web_id, values, buffer_option=None, update_option=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_value_with_http_info(web_id, values, buffer_option, update_option, **kwargs)
		else:
			(data) = self.update_value_with_http_info(web_id, values, buffer_option, update_option, **kwargs)
			return data

	def update_value_with_http_info(self, web_id, values, buffer_option=None, update_option=None, **kwargs):
		all_params = ['web_id', 'values', 'buffer_option', 'update_option']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_value_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `update_value_with_http_info`")
		if ('values' not in params) or (params['values'] is None):
			raise ValueError("Missing the required parameter `values` when calling `update_value_with_http_info`")

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
		if 'values' in params:
			body_params = params['values']
		if 'buffer_option' in params:
			if (params['buffer_option'] is not None):
				query_params['bufferOption'] = params['buffer_option']
		if 'update_option' in params:
			if (params['update_option'] is not None):
				query_params['updateOption'] = params['update_option']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/{webId}/value', 'POST',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSubstatus',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_channel_ad_hoc(self, web_id, heartbeat_rate=None, include_initial_values=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_channel_ad_hoc_with_http_info(web_id, heartbeat_rate, include_initial_values, web_id_type, **kwargs)
		else:
			(data) = self.get_channel_ad_hoc_with_http_info(web_id, heartbeat_rate, include_initial_values, web_id_type, **kwargs)
			return data

	def get_channel_ad_hoc_with_http_info(self, web_id, heartbeat_rate=None, include_initial_values=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'heartbeat_rate', 'include_initial_values', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_channel_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_channel_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'heartbeat_rate' in params:
			if (params['heartbeat_rate'] is not None):
				query_params['heartbeatRate'] = params['heartbeat_rate']
		if 'include_initial_values' in params:
			if (params['include_initial_values'] is not None):
				query_params['includeInitialValues'] = params['include_initial_values']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/channel', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_end_ad_hoc(self, web_id, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_end_ad_hoc_with_http_info(web_id, selected_fields, sort_field, sort_order, web_id_type, **kwargs)
		else:
			(data) = self.get_end_ad_hoc_with_http_info(web_id, selected_fields, sort_field, sort_order, web_id_type, **kwargs)
			return data

	def get_end_ad_hoc_with_http_info(self, web_id, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'sort_field', 'sort_order', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_end_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_end_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
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

		return self.api_client.call_api('/streamsets/end', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_interpolated_ad_hoc(self, web_id, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_interpolated_ad_hoc_with_http_info(web_id, end_time, filter_expression, include_filtered_values, interval, selected_fields, sort_field, sort_order, start_time, sync_time, sync_time_boundary_type, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_interpolated_ad_hoc_with_http_info(web_id, end_time, filter_expression, include_filtered_values, interval, selected_fields, sort_field, sort_order, start_time, sync_time, sync_time_boundary_type, time_zone, web_id_type, **kwargs)
			return data

	def get_interpolated_ad_hoc_with_http_info(self, web_id, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'selected_fields', 'sort_field', 'sort_order', 'start_time', 'sync_time', 'sync_time_boundary_type', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_interpolated_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_interpolated_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'include_filtered_values' in params:
			if (params['include_filtered_values'] is not None):
				query_params['includeFilteredValues'] = params['include_filtered_values']
		if 'interval' in params:
			if (params['interval'] is not None):
				query_params['interval'] = params['interval']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'sync_time' in params:
			if (params['sync_time'] is not None):
				query_params['syncTime'] = params['sync_time']
		if 'sync_time_boundary_type' in params:
			if (params['sync_time_boundary_type'] is not None):
				query_params['syncTimeBoundaryType'] = params['sync_time_boundary_type']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/interpolated', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_interpolated_at_times_ad_hoc(self, time, web_id, filter_expression=None, include_filtered_values=None, selected_fields=None, sort_order=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_interpolated_at_times_ad_hoc_with_http_info(time, web_id, filter_expression, include_filtered_values, selected_fields, sort_order, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_interpolated_at_times_ad_hoc_with_http_info(time, web_id, filter_expression, include_filtered_values, selected_fields, sort_order, time_zone, web_id_type, **kwargs)
			return data

	def get_interpolated_at_times_ad_hoc_with_http_info(self, time, web_id, filter_expression=None, include_filtered_values=None, selected_fields=None, sort_order=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['time', 'web_id', 'filter_expression', 'include_filtered_values', 'selected_fields', 'sort_order', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_interpolated_at_times_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('time' not in params) or (params['time'] is None):
			raise ValueError("Missing the required parameter `time` when calling `get_interpolated_at_times_ad_hoc_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_interpolated_at_times_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
				collection_formats['time'] = 'multi'
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'include_filtered_values' in params:
			if (params['include_filtered_values'] is not None):
				query_params['includeFilteredValues'] = params['include_filtered_values']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/interpolatedattimes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_plot_ad_hoc(self, web_id, end_time=None, intervals=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_plot_ad_hoc_with_http_info(web_id, end_time, intervals, selected_fields, sort_field, sort_order, start_time, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_plot_ad_hoc_with_http_info(web_id, end_time, intervals, selected_fields, sort_field, sort_order, start_time, time_zone, web_id_type, **kwargs)
			return data

	def get_plot_ad_hoc_with_http_info(self, web_id, end_time=None, intervals=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'end_time', 'intervals', 'selected_fields', 'sort_field', 'sort_order', 'start_time', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_plot_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_plot_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'intervals' in params:
			if (params['intervals'] is not None):
				query_params['intervals'] = params['intervals']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/plot', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded_ad_hoc(self, web_id, boundary_type=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_ad_hoc_with_http_info(web_id, boundary_type, end_time, filter_expression, include_filtered_values, max_count, selected_fields, sort_field, sort_order, start_time, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_recorded_ad_hoc_with_http_info(web_id, boundary_type, end_time, filter_expression, include_filtered_values, max_count, selected_fields, sort_field, sort_order, start_time, time_zone, web_id_type, **kwargs)
			return data

	def get_recorded_ad_hoc_with_http_info(self, web_id, boundary_type=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'boundary_type', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'selected_fields', 'sort_field', 'sort_order', 'start_time', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_recorded_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_recorded_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'boundary_type' in params:
			if (params['boundary_type'] is not None):
				query_params['boundaryType'] = params['boundary_type']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'include_filtered_values' in params:
			if (params['include_filtered_values'] is not None):
				query_params['includeFilteredValues'] = params['include_filtered_values']
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
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/recorded', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update_values_ad_hoc(self, values, buffer_option=None, update_option=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_values_ad_hoc_with_http_info(values, buffer_option, update_option, **kwargs)
		else:
			(data) = self.update_values_ad_hoc_with_http_info(values, buffer_option, update_option, **kwargs)
			return data

	def update_values_ad_hoc_with_http_info(self, values, buffer_option=None, update_option=None, **kwargs):
		all_params = ['values', 'buffer_option', 'update_option']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_values_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('values' not in params) or (params['values'] is None):
			raise ValueError("Missing the required parameter `values` when calling `update_values_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'values' in params:
			body_params = params['values']
		if 'buffer_option' in params:
			if (params['buffer_option'] is not None):
				query_params['bufferOption'] = params['buffer_option']
		if 'update_option' in params:
			if (params['update_option'] is not None):
				query_params['updateOption'] = params['update_option']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/recorded', 'POST',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsItemsSubstatus',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded_at_time_ad_hoc(self, time, web_id, retrieval_mode=None, selected_fields=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_at_time_ad_hoc_with_http_info(time, web_id, retrieval_mode, selected_fields, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_recorded_at_time_ad_hoc_with_http_info(time, web_id, retrieval_mode, selected_fields, time_zone, web_id_type, **kwargs)
			return data

	def get_recorded_at_time_ad_hoc_with_http_info(self, time, web_id, retrieval_mode=None, selected_fields=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['time', 'web_id', 'retrieval_mode', 'selected_fields', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_recorded_at_time_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('time' not in params) or (params['time'] is None):
			raise ValueError("Missing the required parameter `time` when calling `get_recorded_at_time_ad_hoc_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_recorded_at_time_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'retrieval_mode' in params:
			if (params['retrieval_mode'] is not None):
				query_params['retrievalMode'] = params['retrieval_mode']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/recordedattime', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded_at_times_ad_hoc(self, time, web_id, retrieval_mode=None, selected_fields=None, sort_order=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_at_times_ad_hoc_with_http_info(time, web_id, retrieval_mode, selected_fields, sort_order, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_recorded_at_times_ad_hoc_with_http_info(time, web_id, retrieval_mode, selected_fields, sort_order, time_zone, web_id_type, **kwargs)
			return data

	def get_recorded_at_times_ad_hoc_with_http_info(self, time, web_id, retrieval_mode=None, selected_fields=None, sort_order=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['time', 'web_id', 'retrieval_mode', 'selected_fields', 'sort_order', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_recorded_at_times_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('time' not in params) or (params['time'] is None):
			raise ValueError("Missing the required parameter `time` when calling `get_recorded_at_times_ad_hoc_with_http_info`")
		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_recorded_at_times_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
				collection_formats['time'] = 'multi'
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'retrieval_mode' in params:
			if (params['retrieval_mode'] is not None):
				query_params['retrievalMode'] = params['retrieval_mode']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/recordedattimes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_summaries_ad_hoc(self, web_id, calculation_basis=None, end_time=None, filter_expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_summaries_ad_hoc_with_http_info(web_id, calculation_basis, end_time, filter_expression, sample_interval, sample_type, selected_fields, start_time, summary_duration, summary_type, time_type, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_summaries_ad_hoc_with_http_info(web_id, calculation_basis, end_time, filter_expression, sample_interval, sample_type, selected_fields, start_time, summary_duration, summary_type, time_type, time_zone, web_id_type, **kwargs)
			return data

	def get_summaries_ad_hoc_with_http_info(self, web_id, calculation_basis=None, end_time=None, filter_expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'calculation_basis', 'end_time', 'filter_expression', 'sample_interval', 'sample_type', 'selected_fields', 'start_time', 'summary_duration', 'summary_type', 'time_type', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_summaries_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_summaries_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'calculation_basis' in params:
			if (params['calculation_basis'] is not None):
				query_params['calculationBasis'] = params['calculation_basis']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'filter_expression' in params:
			if (params['filter_expression'] is not None):
				query_params['filterExpression'] = params['filter_expression']
		if 'sample_interval' in params:
			if (params['sample_interval'] is not None):
				query_params['sampleInterval'] = params['sample_interval']
		if 'sample_type' in params:
			if (params['sample_type'] is not None):
				query_params['sampleType'] = params['sample_type']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'summary_duration' in params:
			if (params['summary_duration'] is not None):
				query_params['summaryDuration'] = params['summary_duration']
		if 'summary_type' in params:
			if (params['summary_type'] is not None):
				query_params['summaryType'] = params['summary_type']
				collection_formats['summaryType'] = 'multi'
		if 'time_type' in params:
			if (params['time_type'] is not None):
				query_params['timeType'] = params['time_type']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/summary', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamSummaries',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_values_ad_hoc(self, web_id, selected_fields=None, sort_field=None, sort_order=None, time=None, time_zone=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_values_ad_hoc_with_http_info(web_id, selected_fields, sort_field, sort_order, time, time_zone, web_id_type, **kwargs)
		else:
			(data) = self.get_values_ad_hoc_with_http_info(web_id, selected_fields, sort_field, sort_order, time, time_zone, web_id_type, **kwargs)
			return data

	def get_values_ad_hoc_with_http_info(self, web_id, selected_fields=None, sort_field=None, sort_order=None, time=None, time_zone=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'selected_fields', 'sort_field', 'sort_order', 'time', 'time_zone', 'web_id_type']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_values_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_values_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']
				collection_formats['webId'] = 'multi'
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_field' in params:
			if (params['sort_field'] is not None):
				query_params['sortField'] = params['sort_field']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/value', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsStreamValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update_value_ad_hoc(self, values, buffer_option=None, update_option=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_value_ad_hoc_with_http_info(values, buffer_option, update_option, **kwargs)
		else:
			(data) = self.update_value_ad_hoc_with_http_info(values, buffer_option, update_option, **kwargs)
			return data

	def update_value_ad_hoc_with_http_info(self, values, buffer_option=None, update_option=None, **kwargs):
		all_params = ['values', 'buffer_option', 'update_option']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method update_value_ad_hoc_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('values' not in params) or (params['values'] is None):
			raise ValueError("Missing the required parameter `values` when calling `update_value_ad_hoc_with_http_info`")

		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'values' in params:
			body_params = params['values']
		if 'buffer_option' in params:
			if (params['buffer_option'] is not None):
				query_params['bufferOption'] = params['buffer_option']
		if 'update_option' in params:
			if (params['update_option'] is not None):
				query_params['updateOption'] = params['update_option']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streamsets/value', 'POST',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSubstatus',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)

