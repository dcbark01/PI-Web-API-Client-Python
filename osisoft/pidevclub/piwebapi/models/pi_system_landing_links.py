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


class PISystemLandingLinks(object):
	swagger_types = {
		'cache_instances': 'str',
		'configuration': 'str',
		'user_info': 'str',
		'versions': 'str',
		'status': 'str',
	}

	attribute_map = {
		'cache_instances': 'CacheInstances',
		'configuration': 'Configuration',
		'user_info': 'UserInfo',
		'versions': 'Versions',
		'status': 'Status',
	}
	def __init__(self, cache_instances=None, configuration=None, user_info=None, versions=None, status=None):

		self._cache_instances = None
		self._configuration = None
		self._user_info = None
		self._versions = None
		self._status = None

		if cache_instances is not None:
			self.cache_instances = cache_instances
		if configuration is not None:
			self.configuration = configuration
		if user_info is not None:
			self.user_info = user_info
		if versions is not None:
			self.versions = versions
		if status is not None:
			self.status = status

	@property
	def cache_instances(self):
		return self._cache_instances

	@cache_instances.setter
	def cache_instances(self, cache_instances):
		self._cache_instances = cache_instances

	@property
	def configuration(self):
		return self._configuration

	@configuration.setter
	def configuration(self, configuration):
		self._configuration = configuration

	@property
	def user_info(self):
		return self._user_info

	@user_info.setter
	def user_info(self, user_info):
		self._user_info = user_info

	@property
	def versions(self):
		return self._versions

	@versions.setter
	def versions(self, versions):
		self._versions = versions

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		self._status = status

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
		if not isinstance(other, PISystemLandingLinks):
			return False
		return self.__dict__ == other.__dict__

