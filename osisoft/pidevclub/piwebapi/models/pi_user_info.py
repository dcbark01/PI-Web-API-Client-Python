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


class PIUserInfo(object):
	swagger_types = {
		'identity_type': 'str',
		'name': 'str',
		'is_authenticated': 'bool',
		's_i_d': 'str',
		'impersonation_level': 'str',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'identity_type': 'IdentityType',
		'name': 'Name',
		'is_authenticated': 'IsAuthenticated',
		's_i_d': 'SID',
		'impersonation_level': 'ImpersonationLevel',
		'web_exception': 'WebException',
	}
	def __init__(self, identity_type=None, name=None, is_authenticated=None, s_i_d=None, impersonation_level=None, web_exception=None):

		self._identity_type = None
		self._name = None
		self._is_authenticated = None
		self._s_i_d = None
		self._impersonation_level = None
		self._web_exception = None

		if identity_type is not None:
			self.identity_type = identity_type
		if name is not None:
			self.name = name
		if is_authenticated is not None:
			self.is_authenticated = is_authenticated
		if s_i_d is not None:
			self.s_i_d = s_i_d
		if impersonation_level is not None:
			self.impersonation_level = impersonation_level
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def identity_type(self):
		return self._identity_type

	@identity_type.setter
	def identity_type(self, identity_type):
		self._identity_type = identity_type

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def is_authenticated(self):
		return self._is_authenticated

	@is_authenticated.setter
	def is_authenticated(self, is_authenticated):
		self._is_authenticated = is_authenticated

	@property
	def s_i_d(self):
		return self._s_i_d

	@s_i_d.setter
	def s_i_d(self, s_i_d):
		self._s_i_d = s_i_d

	@property
	def impersonation_level(self):
		return self._impersonation_level

	@impersonation_level.setter
	def impersonation_level(self, impersonation_level):
		self._impersonation_level = impersonation_level

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
		if not isinstance(other, PIUserInfo):
			return False
		return self.__dict__ == other.__dict__

