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


class PIUnitClassLinks(object):
	swagger_types = {
		'canonical_unit': 'str',
		'units': 'str',
		'asset_server': 'str',
	}

	attribute_map = {
		'canonical_unit': 'CanonicalUnit',
		'units': 'Units',
		'asset_server': 'AssetServer',
	}
	def __init__(self, canonical_unit=None, units=None, asset_server=None):

		self._canonical_unit = None
		self._units = None
		self._asset_server = None

		if canonical_unit is not None:
			self.canonical_unit = canonical_unit
		if units is not None:
			self.units = units
		if asset_server is not None:
			self.asset_server = asset_server

	@property
	def canonical_unit(self):
		return self._canonical_unit

	@canonical_unit.setter
	def canonical_unit(self, canonical_unit):
		self._canonical_unit = canonical_unit

	@property
	def units(self):
		return self._units

	@units.setter
	def units(self, units):
		self._units = units

	@property
	def asset_server(self):
		return self._asset_server

	@asset_server.setter
	def asset_server(self, asset_server):
		self._asset_server = asset_server

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
		if not isinstance(other, PIUnitClassLinks):
			return False
		return self.__dict__ == other.__dict__

