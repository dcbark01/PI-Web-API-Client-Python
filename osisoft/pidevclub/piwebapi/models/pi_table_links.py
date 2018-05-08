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


class PITableLinks(object):
	swagger_types = {
		'database': 'str',
		'data': 'str',
		'categories': 'str',
		'security': 'str',
		'security_entries': 'str',
	}

	attribute_map = {
		'database': 'Database',
		'data': 'Data',
		'categories': 'Categories',
		'security': 'Security',
		'security_entries': 'SecurityEntries',
	}
	def __init__(self, database=None, data=None, categories=None, security=None, security_entries=None):

		self._database = None
		self._data = None
		self._categories = None
		self._security = None
		self._security_entries = None

		if database is not None:
			self.database = database
		if data is not None:
			self.data = data
		if categories is not None:
			self.categories = categories
		if security is not None:
			self.security = security
		if security_entries is not None:
			self.security_entries = security_entries

	@property
	def database(self):
		return self._database

	@database.setter
	def database(self, database):
		self._database = database

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, data):
		self._data = data

	@property
	def categories(self):
		return self._categories

	@categories.setter
	def categories(self, categories):
		self._categories = categories

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
		if not isinstance(other, PITableLinks):
			return False
		return self.__dict__ == other.__dict__

