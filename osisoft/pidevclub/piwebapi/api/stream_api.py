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

class StreamApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

	def get_channel(self, web_id, heartbeat_rate=None, include_initial_values=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_channel_with_http_info(web_id, heartbeat_rate, include_initial_values, web_id_type, **kwargs)
		else:
			(data) = self.get_channel_with_http_info(web_id, heartbeat_rate, include_initial_values, web_id_type, **kwargs)
			return data

	def get_channel_with_http_info(self, web_id, heartbeat_rate=None, include_initial_values=None, web_id_type=None, **kwargs):
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

		return self.api_client.call_api('/streams/{webId}/channel', 'GET',
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


	def get_end(self, web_id, desired_units=None, selected_fields=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_end_with_http_info(web_id, desired_units, selected_fields, **kwargs)
		else:
			(data) = self.get_end_with_http_info(web_id, desired_units, selected_fields, **kwargs)
			return data

	def get_end_with_http_info(self, web_id, desired_units=None, selected_fields=None, **kwargs):
		all_params = ['web_id', 'desired_units', 'selected_fields']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/end', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_interpolated(self, web_id, desired_units=None, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, selected_fields=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_interpolated_with_http_info(web_id, desired_units, end_time, filter_expression, include_filtered_values, interval, selected_fields, start_time, sync_time, sync_time_boundary_type, time_zone, **kwargs)
		else:
			(data) = self.get_interpolated_with_http_info(web_id, desired_units, end_time, filter_expression, include_filtered_values, interval, selected_fields, start_time, sync_time, sync_time_boundary_type, time_zone, **kwargs)
			return data

	def get_interpolated_with_http_info(self, web_id, desired_units=None, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, selected_fields=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'desired_units', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'selected_fields', 'start_time', 'sync_time', 'sync_time_boundary_type', 'time_zone']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
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

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/interpolated', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_interpolated_at_times(self, web_id, desired_units=None, filter_expression=None, include_filtered_values=None, selected_fields=None, sort_order=None, time=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_interpolated_at_times_with_http_info(web_id, desired_units, filter_expression, include_filtered_values, selected_fields, sort_order, time, time_zone, **kwargs)
		else:
			(data) = self.get_interpolated_at_times_with_http_info(web_id, desired_units, filter_expression, include_filtered_values, selected_fields, sort_order, time, time_zone, **kwargs)
			return data

	def get_interpolated_at_times_with_http_info(self, web_id, desired_units=None, filter_expression=None, include_filtered_values=None, selected_fields=None, sort_order=None, time=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'desired_units', 'filter_expression', 'include_filtered_values', 'selected_fields', 'sort_order', 'time', 'time_zone']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
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
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
				collection_formats['time'] = 'multi'
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/interpolatedattimes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_plot(self, web_id, desired_units=None, end_time=None, intervals=None, selected_fields=None, start_time=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_plot_with_http_info(web_id, desired_units, end_time, intervals, selected_fields, start_time, time_zone, **kwargs)
		else:
			(data) = self.get_plot_with_http_info(web_id, desired_units, end_time, intervals, selected_fields, start_time, time_zone, **kwargs)
			return data

	def get_plot_with_http_info(self, web_id, desired_units=None, end_time=None, intervals=None, selected_fields=None, start_time=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'desired_units', 'end_time', 'intervals', 'selected_fields', 'start_time', 'time_zone']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'intervals' in params:
			if (params['intervals'] is not None):
				query_params['intervals'] = params['intervals']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/plot', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded(self, web_id, boundary_type=None, desired_units=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, start_time=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_with_http_info(web_id, boundary_type, desired_units, end_time, filter_expression, include_filtered_values, max_count, selected_fields, start_time, time_zone, **kwargs)
		else:
			(data) = self.get_recorded_with_http_info(web_id, boundary_type, desired_units, end_time, filter_expression, include_filtered_values, max_count, selected_fields, start_time, time_zone, **kwargs)
			return data

	def get_recorded_with_http_info(self, web_id, boundary_type=None, desired_units=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, start_time=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'boundary_type', 'desired_units', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'selected_fields', 'start_time', 'time_zone']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
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
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/recorded', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValues',
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

		return self.api_client.call_api('/streams/{webId}/recorded', 'POST',
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


	def get_recorded_at_time(self, web_id, time, desired_units=None, retrieval_mode=None, selected_fields=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_at_time_with_http_info(web_id, time, desired_units, retrieval_mode, selected_fields, time_zone, **kwargs)
		else:
			(data) = self.get_recorded_at_time_with_http_info(web_id, time, desired_units, retrieval_mode, selected_fields, time_zone, **kwargs)
			return data

	def get_recorded_at_time_with_http_info(self, web_id, time, desired_units=None, retrieval_mode=None, selected_fields=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'time', 'desired_units', 'retrieval_mode', 'selected_fields', 'time_zone']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
		if 'retrieval_mode' in params:
			if (params['retrieval_mode'] is not None):
				query_params['retrievalMode'] = params['retrieval_mode']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/recordedattime', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_recorded_at_times(self, web_id, desired_units=None, retrieval_mode=None, selected_fields=None, sort_order=None, time=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_recorded_at_times_with_http_info(web_id, desired_units, retrieval_mode, selected_fields, sort_order, time, time_zone, **kwargs)
		else:
			(data) = self.get_recorded_at_times_with_http_info(web_id, desired_units, retrieval_mode, selected_fields, sort_order, time, time_zone, **kwargs)
			return data

	def get_recorded_at_times_with_http_info(self, web_id, desired_units=None, retrieval_mode=None, selected_fields=None, sort_order=None, time=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'desired_units', 'retrieval_mode', 'selected_fields', 'sort_order', 'time', 'time_zone']
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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
		if 'retrieval_mode' in params:
			if (params['retrieval_mode'] is not None):
				query_params['retrievalMode'] = params['retrieval_mode']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'sort_order' in params:
			if (params['sort_order'] is not None):
				query_params['sortOrder'] = params['sort_order']
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
				collection_formats['time'] = 'multi'
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/recordedattimes', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValues',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_summary(self, web_id, calculation_basis=None, end_time=None, filter_expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_summary_with_http_info(web_id, calculation_basis, end_time, filter_expression, sample_interval, sample_type, selected_fields, start_time, summary_duration, summary_type, time_type, time_zone, **kwargs)
		else:
			(data) = self.get_summary_with_http_info(web_id, calculation_basis, end_time, filter_expression, sample_interval, sample_type, selected_fields, start_time, summary_duration, summary_type, time_type, time_zone, **kwargs)
			return data

	def get_summary_with_http_info(self, web_id, calculation_basis=None, end_time=None, filter_expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'calculation_basis', 'end_time', 'filter_expression', 'sample_interval', 'sample_type', 'selected_fields', 'start_time', 'summary_duration', 'summary_type', 'time_type', 'time_zone']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_summary_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_summary_with_http_info`")

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

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/summary', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PIItemsSummaryValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def get_value(self, web_id, desired_units=None, selected_fields=None, time=None, time_zone=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_value_with_http_info(web_id, desired_units, selected_fields, time, time_zone, **kwargs)
		else:
			(data) = self.get_value_with_http_info(web_id, desired_units, selected_fields, time, time_zone, **kwargs)
			return data

	def get_value_with_http_info(self, web_id, desired_units=None, selected_fields=None, time=None, time_zone=None, **kwargs):
		all_params = ['web_id', 'desired_units', 'selected_fields', 'time', 'time_zone']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_value_with_http_info" % key
				)
			params[key] = val
		del params['kwargs']

		if ('web_id' not in params) or (params['web_id'] is None):
			raise ValueError("Missing the required parameter `web_id` when calling `get_value_with_http_info`")

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
		if 'desired_units' in params:
			if (params['desired_units'] is not None):
				query_params['desiredUnits'] = params['desired_units']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'time' in params:
			if (params['time'] is not None):
				query_params['time'] = params['time']
		if 'time_zone' in params:
			if (params['time_zone'] is not None):
				query_params['timeZone'] = params['time_zone']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/value', 'GET',
				path_params,
				query_params,
				header_params,
				body =body_params,
				post_params =form_params,
				files =local_var_files,
				response_type ='PITimedValue',
				callback =params.get('callback'),
				_return_http_data_only =params.get('_return_http_data_only'),
				_preload_content =params.get('_preload_content', True),
				_request_timeout=params.get('_request_timeout'),
				collection_formats =collection_formats)


	def update_value(self, web_id, value, buffer_option=None, update_option=None, web_id_type=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.update_value_with_http_info(web_id, value, buffer_option, update_option, web_id_type, **kwargs)
		else:
			(data) = self.update_value_with_http_info(web_id, value, buffer_option, update_option, web_id_type, **kwargs)
			return data

	def update_value_with_http_info(self, web_id, value, buffer_option=None, update_option=None, web_id_type=None, **kwargs):
		all_params = ['web_id', 'value', 'buffer_option', 'update_option', 'web_id_type']
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
		if ('value' not in params) or (params['value'] is None):
			raise ValueError("Missing the required parameter `value` when calling `update_value_with_http_info`")

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
		if 'value' in params:
			body_params = params['value']
		if 'buffer_option' in params:
			if (params['buffer_option'] is not None):
				query_params['bufferOption'] = params['buffer_option']
		if 'update_option' in params:
			if (params['update_option'] is not None):
				query_params['updateOption'] = params['update_option']
		if 'web_id_type' in params:
			if (params['web_id_type'] is not None):
				query_params['webIdType'] = params['web_id_type']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/streams/{webId}/value', 'POST',
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

