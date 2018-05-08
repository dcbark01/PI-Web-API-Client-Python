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


class PISecurityEntryLinks(object):
	swagger_types = {
		'securable_object': 'str',
		'security_identity': 'str',
	}

	attribute_map = {
		'securable_object': 'SecurableObject',
		'security_identity': 'SecurityIdentity',
	}
	def __init__(self, securable_object=None, security_identity=None):

		self._securable_object = None
		self._security_identity = None

		if securable_object is not None:
			self.securable_object = securable_object
		if security_identity is not None:
			self.security_identity = security_identity

	@property
	def securable_object(self):
		return self._securable_object

	@securable_object.setter
	def securable_object(self, securable_object):
		self._securable_object = securable_object

	@property
	def security_identity(self):
		return self._security_identity

	@security_identity.setter
	def security_identity(self, security_identity):
		self._security_identity = security_identity

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
		if not isinstance(other, PISecurityEntryLinks):
			return False
		return self.__dict__ == other.__dict__

