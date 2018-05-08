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


class PIAnnotation(object):
	swagger_types = {
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'value': 'object',
		'creator': 'str',
		'creation_date': 'str',
		'modifier': 'str',
		'modify_date': 'str',
		'links': 'PIAnnotationLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'value': 'Value',
		'creator': 'Creator',
		'creation_date': 'CreationDate',
		'modifier': 'Modifier',
		'modify_date': 'ModifyDate',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, id=None, name=None, description=None, value=None, creator=None, creation_date=None, modifier=None, modify_date=None, links=None, web_exception=None):

		self._id = None
		self._name = None
		self._description = None
		self._value = None
		self._creator = None
		self._creation_date = None
		self._modifier = None
		self._modify_date = None
		self._links = None
		self._web_exception = None

		if id is not None:
			self.id = id
		if name is not None:
			self.name = name
		if description is not None:
			self.description = description
		if value is not None:
			self.value = value
		if creator is not None:
			self.creator = creator
		if creation_date is not None:
			self.creation_date = creation_date
		if modifier is not None:
			self.modifier = modifier
		if modify_date is not None:
			self.modify_date = modify_date
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

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
	def creator(self):
		return self._creator

	@creator.setter
	def creator(self, creator):
		self._creator = creator

	@property
	def creation_date(self):
		return self._creation_date

	@creation_date.setter
	def creation_date(self, creation_date):
		self._creation_date = creation_date

	@property
	def modifier(self):
		return self._modifier

	@modifier.setter
	def modifier(self, modifier):
		self._modifier = modifier

	@property
	def modify_date(self):
		return self._modify_date

	@modify_date.setter
	def modify_date(self, modify_date):
		self._modify_date = modify_date

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
		if not isinstance(other, PIAnnotation):
			return False
		return self.__dict__ == other.__dict__

