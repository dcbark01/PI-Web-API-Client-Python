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


class PISecurityEntry(object):
	swagger_types = {
		'name': 'str',
		'security_identity_name': 'str',
		'allow_rights': 'list[str]',
		'deny_rights': 'list[str]',
		'links': 'PISecurityEntryLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'name': 'Name',
		'security_identity_name': 'SecurityIdentityName',
		'allow_rights': 'AllowRights',
		'deny_rights': 'DenyRights',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, name=None, security_identity_name=None, allow_rights=None, deny_rights=None, links=None, web_exception=None):

		self._name = None
		self._security_identity_name = None
		self._allow_rights = None
		self._deny_rights = None
		self._links = None
		self._web_exception = None

		if name is not None:
			self.name = name
		if security_identity_name is not None:
			self.security_identity_name = security_identity_name
		if allow_rights is not None:
			self.allow_rights = allow_rights
		if deny_rights is not None:
			self.deny_rights = deny_rights
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def security_identity_name(self):
		return self._security_identity_name

	@security_identity_name.setter
	def security_identity_name(self, security_identity_name):
		self._security_identity_name = security_identity_name

	@property
	def allow_rights(self):
		return self._allow_rights

	@allow_rights.setter
	def allow_rights(self, allow_rights):
		self._allow_rights = allow_rights

	@property
	def deny_rights(self):
		return self._deny_rights

	@deny_rights.setter
	def deny_rights(self, deny_rights):
		self._deny_rights = deny_rights

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
		if not isinstance(other, PISecurityEntry):
			return False
		return self.__dict__ == other.__dict__

