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


class PIItemEventFrame(object):
	swagger_types = {
		'identifier': 'str',
		'identifier_type': 'str',
		'object': 'PIEventFrame',
		'exception': 'PIErrors',
	}

	attribute_map = {
		'identifier': 'Identifier',
		'identifier_type': 'IdentifierType',
		'object': 'Object',
		'exception': 'Exception',
	}
	def __init__(self, identifier=None, identifier_type=None, object=None, exception=None):

		self._identifier = None
		self._identifier_type = None
		self._object = None
		self._exception = None

		if identifier is not None:
			self.identifier = identifier
		if identifier_type is not None:
			self.identifier_type = identifier_type
		if object is not None:
			self.object = object
		if exception is not None:
			self.exception = exception

	@property
	def identifier(self):
		return self._identifier

	@identifier.setter
	def identifier(self, identifier):
		self._identifier = identifier

	@property
	def identifier_type(self):
		return self._identifier_type

	@identifier_type.setter
	def identifier_type(self, identifier_type):
		self._identifier_type = identifier_type

	@property
	def object(self):
		return self._object

	@object.setter
	def object(self, object):
		self._object = object

	@property
	def exception(self):
		return self._exception

	@exception.setter
	def exception(self, exception):
		self._exception = exception

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
		if not isinstance(other, PIItemEventFrame):
			return False
		return self.__dict__ == other.__dict__

