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


class PIEnumerationValue(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'value': 'int',
		'path': 'str',
		'links': 'dict(str, str)',
		'serialize_web_id': 'bool',
		'serialize_id': 'bool',
		'serialize_description': 'bool',
		'serialize_path': 'bool',
		'serialize_links': 'bool',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'value': 'Value',
		'path': 'Path',
		'links': 'Links',
		'serialize_web_id': 'SerializeWebId',
		'serialize_id': 'SerializeId',
		'serialize_description': 'SerializeDescription',
		'serialize_path': 'SerializePath',
		'serialize_links': 'SerializeLinks',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, value=None, path=None, links=None, serialize_web_id=None, serialize_id=None, serialize_description=None, serialize_path=None, serialize_links=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._value = None
		self._path = None
		self._links = None
		self._serialize_web_id = None
		self._serialize_id = None
		self._serialize_description = None
		self._serialize_path = None
		self._serialize_links = None

		if web_id is not None:
			self.web_id = web_id
		if id is not None:
			self.id = id
		if name is not None:
			self.name = name
		if description is not None:
			self.description = description
		if value is not None:
			self.value = value
		if path is not None:
			self.path = path
		if links is not None:
			self.links = links
		if serialize_web_id is not None:
			self.serialize_web_id = serialize_web_id
		if serialize_id is not None:
			self.serialize_id = serialize_id
		if serialize_description is not None:
			self.serialize_description = serialize_description
		if serialize_path is not None:
			self.serialize_path = serialize_path
		if serialize_links is not None:
			self.serialize_links = serialize_links

	@property
	def web_id(self):
		return self._web_id

	@web_id.setter
	def web_id(self, web_id):
		self._web_id = web_id

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def links(self):
		return self._links

	@links.setter
	def links(self, links):
		self._links = links

	@property
	def serialize_web_id(self):
		return self._serialize_web_id

	@serialize_web_id.setter
	def serialize_web_id(self, serialize_web_id):
		self._serialize_web_id = serialize_web_id

	@property
	def serialize_id(self):
		return self._serialize_id

	@serialize_id.setter
	def serialize_id(self, serialize_id):
		self._serialize_id = serialize_id

	@property
	def serialize_description(self):
		return self._serialize_description

	@serialize_description.setter
	def serialize_description(self, serialize_description):
		self._serialize_description = serialize_description

	@property
	def serialize_path(self):
		return self._serialize_path

	@serialize_path.setter
	def serialize_path(self, serialize_path):
		self._serialize_path = serialize_path

	@property
	def serialize_links(self):
		return self._serialize_links

	@serialize_links.setter
	def serialize_links(self, serialize_links):
		self._serialize_links = serialize_links

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
		if not isinstance(other, PIEnumerationValue):
			return False
		return self.__dict__ == other.__dict__

