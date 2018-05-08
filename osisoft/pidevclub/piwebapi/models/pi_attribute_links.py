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


class PIAttributeLinks(object):
	swagger_types = {
		'attributes': 'str',
		'element': 'str',
		'event_frame': 'str',
		'parent': 'str',
		'template': 'str',
		'interpolated_data': 'str',
		'recorded_data': 'str',
		'plot_data': 'str',
		'summary_data': 'str',
		'value': 'str',
		'end_value': 'str',
		'point': 'str',
		'categories': 'str',
		'enumeration_set': 'str',
		'enumeration_values': 'str',
		'trait': 'str',
	}

	attribute_map = {
		'attributes': 'Attributes',
		'element': 'Element',
		'event_frame': 'EventFrame',
		'parent': 'Parent',
		'template': 'Template',
		'interpolated_data': 'InterpolatedData',
		'recorded_data': 'RecordedData',
		'plot_data': 'PlotData',
		'summary_data': 'SummaryData',
		'value': 'Value',
		'end_value': 'EndValue',
		'point': 'Point',
		'categories': 'Categories',
		'enumeration_set': 'EnumerationSet',
		'enumeration_values': 'EnumerationValues',
		'trait': 'Trait',
	}
	def __init__(self, attributes=None, element=None, event_frame=None, parent=None, template=None, interpolated_data=None, recorded_data=None, plot_data=None, summary_data=None, value=None, end_value=None, point=None, categories=None, enumeration_set=None, enumeration_values=None, trait=None):

		self._attributes = None
		self._element = None
		self._event_frame = None
		self._parent = None
		self._template = None
		self._interpolated_data = None
		self._recorded_data = None
		self._plot_data = None
		self._summary_data = None
		self._value = None
		self._end_value = None
		self._point = None
		self._categories = None
		self._enumeration_set = None
		self._enumeration_values = None
		self._trait = None

		if attributes is not None:
			self.attributes = attributes
		if element is not None:
			self.element = element
		if event_frame is not None:
			self.event_frame = event_frame
		if parent is not None:
			self.parent = parent
		if template is not None:
			self.template = template
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
		if point is not None:
			self.point = point
		if categories is not None:
			self.categories = categories
		if enumeration_set is not None:
			self.enumeration_set = enumeration_set
		if enumeration_values is not None:
			self.enumeration_values = enumeration_values
		if trait is not None:
			self.trait = trait

	@property
	def attributes(self):
		return self._attributes

	@attributes.setter
	def attributes(self, attributes):
		self._attributes = attributes

	@property
	def element(self):
		return self._element

	@element.setter
	def element(self, element):
		self._element = element

	@property
	def event_frame(self):
		return self._event_frame

	@event_frame.setter
	def event_frame(self, event_frame):
		self._event_frame = event_frame

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
	def point(self):
		return self._point

	@point.setter
	def point(self, point):
		self._point = point

	@property
	def categories(self):
		return self._categories

	@categories.setter
	def categories(self, categories):
		self._categories = categories

	@property
	def enumeration_set(self):
		return self._enumeration_set

	@enumeration_set.setter
	def enumeration_set(self, enumeration_set):
		self._enumeration_set = enumeration_set

	@property
	def enumeration_values(self):
		return self._enumeration_values

	@enumeration_values.setter
	def enumeration_values(self, enumeration_values):
		self._enumeration_values = enumeration_values

	@property
	def trait(self):
		return self._trait

	@trait.setter
	def trait(self, trait):
		self._trait = trait

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
		if not isinstance(other, PIAttributeLinks):
			return False
		return self.__dict__ == other.__dict__

