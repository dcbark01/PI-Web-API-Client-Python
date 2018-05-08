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


class PIElementLinks(object):
	swagger_types = {
		'analyses': 'str',
		'attributes': 'str',
		'elements': 'str',
		'database': 'str',
		'parent': 'str',
		'template': 'str',
		'categories': 'str',
		'default_attribute': 'str',
		'event_frames': 'str',
		'interpolated_data': 'str',
		'recorded_data': 'str',
		'plot_data': 'str',
		'summary_data': 'str',
		'value': 'str',
		'end_value': 'str',
		'security': 'str',
		'security_entries': 'str',
	}

	attribute_map = {
		'analyses': 'Analyses',
		'attributes': 'Attributes',
		'elements': 'Elements',
		'database': 'Database',
		'parent': 'Parent',
		'template': 'Template',
		'categories': 'Categories',
		'default_attribute': 'DefaultAttribute',
		'event_frames': 'EventFrames',
		'interpolated_data': 'InterpolatedData',
		'recorded_data': 'RecordedData',
		'plot_data': 'PlotData',
		'summary_data': 'SummaryData',
		'value': 'Value',
		'end_value': 'EndValue',
		'security': 'Security',
		'security_entries': 'SecurityEntries',
	}
	def __init__(self, analyses=None, attributes=None, elements=None, database=None, parent=None, template=None, categories=None, default_attribute=None, event_frames=None, interpolated_data=None, recorded_data=None, plot_data=None, summary_data=None, value=None, end_value=None, security=None, security_entries=None):

		self._analyses = None
		self._attributes = None
		self._elements = None
		self._database = None
		self._parent = None
		self._template = None
		self._categories = None
		self._default_attribute = None
		self._event_frames = None
		self._interpolated_data = None
		self._recorded_data = None
		self._plot_data = None
		self._summary_data = None
		self._value = None
		self._end_value = None
		self._security = None
		self._security_entries = None

		if analyses is not None:
			self.analyses = analyses
		if attributes is not None:
			self.attributes = attributes
		if elements is not None:
			self.elements = elements
		if database is not None:
			self.database = database
		if parent is not None:
			self.parent = parent
		if template is not None:
			self.template = template
		if categories is not None:
			self.categories = categories
		if default_attribute is not None:
			self.default_attribute = default_attribute
		if event_frames is not None:
			self.event_frames = event_frames
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
		if security is not None:
			self.security = security
		if security_entries is not None:
			self.security_entries = security_entries

	@property
	def analyses(self):
		return self._analyses

	@analyses.setter
	def analyses(self, analyses):
		self._analyses = analyses

	@property
	def attributes(self):
		return self._attributes

	@attributes.setter
	def attributes(self, attributes):
		self._attributes = attributes

	@property
	def elements(self):
		return self._elements

	@elements.setter
	def elements(self, elements):
		self._elements = elements

	@property
	def database(self):
		return self._database

	@database.setter
	def database(self, database):
		self._database = database

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent

	@property
	def template(self):
		return self._template

	@template.setter
	def template(self, template):
		self._template = template

	@property
	def categories(self):
		return self._categories

	@categories.setter
	def categories(self, categories):
		self._categories = categories

	@property
	def default_attribute(self):
		return self._default_attribute

	@default_attribute.setter
	def default_attribute(self, default_attribute):
		self._default_attribute = default_attribute

	@property
	def event_frames(self):
		return self._event_frames

	@event_frames.setter
	def event_frames(self, event_frames):
		self._event_frames = event_frames

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

	@property
	def security(self):
		return self._security

	@security.setter
	def security(self, security):
		self._security = security

	@property
	def security_entries(self):
		return self._security_entries

	@security_entries.setter
	def security_entries(self, security_entries):
		self._security_entries = security_entries

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
		if not isinstance(other, PIElementLinks):
			return False
		return self.__dict__ == other.__dict__

