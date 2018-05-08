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


class PIValueQuery(object):
	swagger_types = {
		'attribute_name': 'str',
		'attribute_u_o_m': 'str',
		'attribute_value': 'object',
		'search_operator': 'str',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'attribute_name': 'AttributeName',
		'attribute_u_o_m': 'AttributeUOM',
		'attribute_value': 'AttributeValue',
		'search_operator': 'SearchOperator',
		'web_exception': 'WebException',
	}
	def __init__(self, attribute_name=None, attribute_u_o_m=None, attribute_value=None, search_operator=None, web_exception=None):

		self._attribute_name = None
		self._attribute_u_o_m = None
		self._attribute_value = None
		self._search_operator = None
		self._web_exception = None

		if attribute_name is not None:
			self.attribute_name = attribute_name
		if attribute_u_o_m is not None:
			self.attribute_u_o_m = attribute_u_o_m
		if attribute_value is not None:
			self.attribute_value = attribute_value
		if search_operator is not None:
			self.search_operator = search_operator
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def attribute_name(self):
		return self._attribute_name

	@attribute_name.setter
	def attribute_name(self, attribute_name):
		self._attribute_name = attribute_name

	@property
	def attribute_u_o_m(self):
		return self._attribute_u_o_m

	@attribute_u_o_m.setter
	def attribute_u_o_m(self, attribute_u_o_m):
		self._attribute_u_o_m = attribute_u_o_m

	@property
	def attribute_value(self):
		return self._attribute_value

	@attribute_value.setter
	def attribute_value(self, attribute_value):
		self._attribute_value = attribute_value

	@property
	def search_operator(self):
		return self._search_operator

	@search_operator.setter
	def search_operator(self, search_operator):
		self._search_operator = search_operator

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
		if not isinstance(other, PIValueQuery):
			return False
		return self.__dict__ == other.__dict__

