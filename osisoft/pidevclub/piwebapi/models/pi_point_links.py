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
from pprint import pformat
from six import iteritems


class PIPointLinks(object):
	swagger_types = {
		'data_server': 'str',
		'attributes': 'str',
		'interpolated_data': 'str',
		'recorded_data': 'str',
		'plot_data': 'str',
		'summary_data': 'str',
		'value': 'str',
		'end_value': 'str',
	}

	attribute_map = {
		'data_server': 'DataServer',
		'attributes': 'Attributes',
		'interpolated_data': 'InterpolatedData',
		'recorded_data': 'RecordedData',
		'plot_data': 'PlotData',
		'summary_data': 'SummaryData',
		'value': 'Value',
		'end_value': 'EndValue',
	}
	def __init__(self, data_server=None, attributes=None, interpolated_data=None, recorded_data=None, plot_data=None, summary_data=None, value=None, end_value=None):

		self._data_server = None
		self._attributes = None
		self._interpolated_data = None
		self._recorded_data = None
		self._plot_data = None
		self._summary_data = None
		self._value = None
		self._end_value = None

		if data_server is not None:
			self.data_server = data_server
		if attributes is not None:
			self.attributes = attributes
		if interpolated_data is not None:
			self.interpolated_data = interpolated_data
		if recorded_data is not None:
			self.recorded_data = recorded_data
		if plot_data is not None:
			self.plot_data = plot_data
		if summary_data is not None:
			self.summary_data = summary_data
		if value is not None:
			self.value = value
		if end_value is not None:
			self.end_value = end_value

	@property
	def data_server(self):
		return self._data_server

	@data_server.setter
	def data_server(self, data_server):
		self._data_server = data_server

	@property
	def attributes(self):
		return self._attributes

	@attributes.setter
	def attributes(self, attributes):
		self._attributes = attributes

	@property
	def interpolated_data(self):
		return self._interpolated_data

	@interpolated_data.setter
	def interpolated_data(self, interpolated_data):
		self._interpolated_data = interpolated_data

	@property
	def recorded_data(self):
		return self._recorded_data

	@recorded_data.setter
	def recorded_data(self, recorded_data):
		self._recorded_data = recorded_data

	@property
	def plot_data(self):
		return self._plot_data

	@plot_data.setter
	def plot_data(self, plot_data):
		self._plot_data = plot_data

	@property
	def summary_data(self):
		return self._summary_data

	@summary_data.setter
	def summary_data(self, summary_data):
		self._summary_data = summary_data

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

	@property
	def end_value(self):
		return self._end_value

	@end_value.setter
	def end_value(self, end_value):
		self._end_value = end_value

	def to_dict(self):
		result = {}
		for attr, _ in iteritems(self.swagger_types):
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
		return pformat(self.to_dict())

	def __repr__(self):
		return self.to_str()

	def __ne__(self, other):
		return not self == other

	def __eq__(self, other):
		if not isinstance(other, PIPointLinks):
			return False
		return self.__dict__ == other.__dict__

