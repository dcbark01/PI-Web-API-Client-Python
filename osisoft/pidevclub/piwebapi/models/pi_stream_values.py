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


class PIStreamValues(object):
	swagger_types = {
		'web_id': 'str',
		'name': 'str',
		'path': 'str',
		'items': 'list[PITimedValue]',
		'units_abbreviation': 'str',
		'links': 'PIStreamValuesLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'name': 'Name',
		'path': 'Path',
		'items': 'Items',
		'units_abbreviation': 'UnitsAbbreviation',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, name=None, path=None, items=None, units_abbreviation=None, links=None, web_exception=None):

		self._web_id = None
		self._name = None
		self._path = None
		self._items = None
		self._units_abbreviation = None
		self._links = None
		self._web_exception = None

		if web_id is not None:
			self.web_id = web_id
		if name is not None:
			self.name = name
		if path is not None:
			self.path = path
		if items is not None:
			self.items = items
		if units_abbreviation is not None:
			self.units_abbreviation = units_abbreviation
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def web_id(self):
		return self._web_id

	@web_id.setter
	def web_id(self, web_id):
		self._web_id = web_id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, items):
		self._items = items

	@property
	def units_abbreviation(self):
		return self._units_abbreviation

	@units_abbreviation.setter
	def units_abbreviation(self, units_abbreviation):
		self._units_abbreviation = units_abbreviation

	@property
	def links(self):
		return self._links

	@links.setter
	def links(self, links):
		self._links = links

	@property
	def web_exception(self):
		return self._web_exception

	@web_exception.setter
	def web_exception(self, web_exception):
		self._web_exception = web_exception

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
		if not isinstance(other, PIStreamValues):
			return False
		return self.__dict__ == other.__dict__

