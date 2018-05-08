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


class PISystemStatus(object):
	swagger_types = {
		'up_time_in_minutes': 'float',
		'state': 'str',
		'cache_instances': 'int',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'up_time_in_minutes': 'UpTimeInMinutes',
		'state': 'State',
		'cache_instances': 'CacheInstances',
		'web_exception': 'WebException',
	}
	def __init__(self, up_time_in_minutes=None, state=None, cache_instances=None, web_exception=None):

		self._up_time_in_minutes = None
		self._state = None
		self._cache_instances = None
		self._web_exception = None

		if up_time_in_minutes is not None:
			self.up_time_in_minutes = up_time_in_minutes
		if state is not None:
			self.state = state
		if cache_instances is not None:
			self.cache_instances = cache_instances
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def up_time_in_minutes(self):
		return self._up_time_in_minutes

	@up_time_in_minutes.setter
	def up_time_in_minutes(self, up_time_in_minutes):
		self._up_time_in_minutes = up_time_in_minutes

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, state):
		self._state = state

	@property
	def cache_instances(self):
		return self._cache_instances

	@cache_instances.setter
	def cache_instances(self, cache_instances):
		self._cache_instances = cache_instances

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
		if not isinstance(other, PISystemStatus):
			return False
		return self.__dict__ == other.__dict__

