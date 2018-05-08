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

class CalculationApi(object):
	def __init__(self, api_client):
		self.api_client = api_client

	def get_at_intervals(self, end_time=None, expression=None, sample_interval=None, selected_fields=None, start_time=None, web_id=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_at_intervals_with_http_info(end_time, expression, sample_interval, selected_fields, start_time, web_id, **kwargs)
		else:
			(data) = self.get_at_intervals_with_http_info(end_time, expression, sample_interval, selected_fields, start_time, web_id, **kwargs)
			return data

	def get_at_intervals_with_http_info(self, end_time=None, expression=None, sample_interval=None, selected_fields=None, start_time=None, web_id=None, **kwargs):
		all_params = ['end_time', 'expression', 'sample_interval', 'selected_fields', 'start_time', 'web_id']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_at_intervals_with_http_info" % key
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
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'expression' in params:
			if (params['expression'] is not None):
				query_params['expression'] = params['expression']
		if 'sample_interval' in params:
			if (params['sample_interval'] is not None):
				query_params['sampleInterval'] = params['sample_interval']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/calculation/intervals', 'GET',
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


	def get_at_recorded(self, end_time=None, expression=None, selected_fields=None, start_time=None, web_id=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_at_recorded_with_http_info(end_time, expression, selected_fields, start_time, web_id, **kwargs)
		else:
			(data) = self.get_at_recorded_with_http_info(end_time, expression, selected_fields, start_time, web_id, **kwargs)
			return data

	def get_at_recorded_with_http_info(self, end_time=None, expression=None, selected_fields=None, start_time=None, web_id=None, **kwargs):
		all_params = ['end_time', 'expression', 'selected_fields', 'start_time', 'web_id']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_at_recorded_with_http_info" % key
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
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'expression' in params:
			if (params['expression'] is not None):
				query_params['expression'] = params['expression']
		if 'selected_fields' in params:
			if (params['selected_fields'] is not None):
				query_params['selectedFields'] = params['selected_fields']
		if 'start_time' in params:
			if (params['start_time'] is not None):
				query_params['startTime'] = params['start_time']
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/calculation/recorded', 'GET',
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


	def get_summary(self, calculation_basis=None, end_time=None, expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, web_id=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_summary_with_http_info(calculation_basis, end_time, expression, sample_interval, sample_type, selected_fields, start_time, summary_duration, summary_type, time_type, web_id, **kwargs)
		else:
			(data) = self.get_summary_with_http_info(calculation_basis, end_time, expression, sample_interval, sample_type, selected_fields, start_time, summary_duration, summary_type, time_type, web_id, **kwargs)
			return data

	def get_summary_with_http_info(self, calculation_basis=None, end_time=None, expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, web_id=None, **kwargs):
		all_params = ['calculation_basis', 'end_time', 'expression', 'sample_interval', 'sample_type', 'selected_fields', 'start_time', 'summary_duration', 'summary_type', 'time_type', 'web_id']
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


		collection_formats = {}

		query_params = {}

		path_params = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'calculation_basis' in params:
			if (params['calculation_basis'] is not None):
				query_params['calculationBasis'] = params['calculation_basis']
		if 'end_time' in params:
			if (params['end_time'] is not None):
				query_params['endTime'] = params['end_time']
		if 'expression' in params:
			if (params['expression'] is not None):
				query_params['expression'] = params['expression']
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
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/calculation/summary', 'GET',
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


	def get_at_times(self, expression=None, selected_fields=None, sort_order=None, time=None, web_id=None, **kwargs):
		kwargs['_return_http_data_only'] = True
		if kwargs.get('callback'):
			return self.get_at_times_with_http_info(expression, selected_fields, sort_order, time, web_id, **kwargs)
		else:
			(data) = self.get_at_times_with_http_info(expression, selected_fields, sort_order, time, web_id, **kwargs)
			return data

	def get_at_times_with_http_info(self, expression=None, selected_fields=None, sort_order=None, time=None, web_id=None, **kwargs):
		all_params = ['expression', 'selected_fields', 'sort_order', 'time', 'web_id']
		all_params.append('callback')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')

		params = locals()
		for key, val in iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_at_times_with_http_info" % key
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
		if 'expression' in params:
			if (params['expression'] is not None):
				query_params['expression'] = params['expression']
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
		if 'web_id' in params:
			if (params['web_id'] is not None):
				query_params['webId'] = params['web_id']

		header_params['Accept'] = self.api_client.\
			select_header_accept(['application/json', 'text/json', 'text/html', 'application/x-ms-application'])


		header_params['Content-Type'] = self.api_client.\
			select_header_content_type([])

		return self.api_client.call_api('/calculation/times', 'GET',
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

