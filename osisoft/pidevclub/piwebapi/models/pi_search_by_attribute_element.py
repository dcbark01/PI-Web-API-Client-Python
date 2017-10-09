# coding: utf-8

"""
	Copyright 2017 OSIsoft, LLC
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
import re


class PISearchByAttributeElement(object):
	swagger_types = {
		'search_root': 'object',
		'element_template': 'object',
		'value_queries': 'list[PIAttributeValueQuery]',
	}

	attribute_map = {
		'search_root': 'SearchRoot',
		'element_template': 'ElementTemplate',
		'value_queries': 'ValueQueries',
	}
	def __init__(self, search_root=None, element_template=None, value_queries=None):

		self._search_root = None
		self._element_template = None
		self._value_queries = None

		if search_root is not None:
			self.search_root = search_root
		if element_template is not None:
			self.element_template = element_template
		if value_queries is not None:
			self.value_queries = value_queries

	@property
	def search_root(self):
		return self._search_root

	@search_root.setter
	def search_root(self, search_root):
		self._search_root = search_root

	@property
	def element_template(self):
		return self._element_template

	@element_template.setter
	def element_template(self, element_template):
		self._element_template = element_template

	@property
	def value_queries(self):
		return self._value_queries

	@value_queries.setter
	def value_queries(self, value_queries):
		self._value_queries = value_queries

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
		if not isinstance(other, PISearchByAttributeElement):
			return False
		return self.__dict__ == other.__dict__

