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


class PILandingLinks(object):
	swagger_types = {
		'asset_servers': 'str',
		'data_servers': 'str',
		'search': 'str',
		'system': 'str',
	}

	attribute_map = {
		'asset_servers': 'AssetServers',
		'data_servers': 'DataServers',
		'search': 'Search',
		'system': 'System',
	}
	def __init__(self, asset_servers=None, data_servers=None, search=None, system=None):

		self._asset_servers = None
		self._data_servers = None
		self._search = None
		self._system = None

		if asset_servers is not None:
			self.asset_servers = asset_servers
		if data_servers is not None:
			self.data_servers = data_servers
		if search is not None:
			self.search = search
		if system is not None:
			self.system = system

	@property
	def asset_servers(self):
		return self._asset_servers

	@asset_servers.setter
	def asset_servers(self, asset_servers):
		self._asset_servers = asset_servers

	@property
	def data_servers(self):
		return self._data_servers

	@data_servers.setter
	def data_servers(self, data_servers):
		self._data_servers = data_servers

	@property
	def search(self):
		return self._search

	@search.setter
	def search(self, search):
		self._search = search

	@property
	def system(self):
		return self._system

	@system.setter
	def system(self, system):
		self._system = system

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
		if not isinstance(other, PILandingLinks):
			return False
		return self.__dict__ == other.__dict__

