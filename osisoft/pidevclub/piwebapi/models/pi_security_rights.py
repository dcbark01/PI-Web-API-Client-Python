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


class PISecurityRights(object):
	swagger_types = {
		'owner_web_id': 'str',
		'security_item': 'str',
		'user_identity': 'str',
		'links': 'dict(str, str)',
	}

	attribute_map = {
		'owner_web_id': 'OwnerWebId',
		'security_item': 'SecurityItem',
		'user_identity': 'UserIdentity',
		'links': 'Links',
	}
	def __init__(self, owner_web_id=None, security_item=None, user_identity=None, links=None):

		self._owner_web_id = None
		self._security_item = None
		self._user_identity = None
		self._links = None

		if owner_web_id is not None:
			self.owner_web_id = owner_web_id
		if security_item is not None:
			self.security_item = security_item
		if user_identity is not None:
			self.user_identity = user_identity
		if links is not None:
			self.links = links

	@property
	def owner_web_id(self):
		return self._owner_web_id

	@owner_web_id.setter
	def owner_web_id(self, owner_web_id):
		self._owner_web_id = owner_web_id

	@property
	def security_item(self):
		return self._security_item

	@security_item.setter
	def security_item(self, security_item):
		self._security_item = security_item

	@property
	def user_identity(self):
		return self._user_identity

	@user_identity.setter
	def user_identity(self, user_identity):
		self._user_identity = user_identity

	@property
	def links(self):
		return self._links

	@links.setter
	def links(self, links):
		self._links = links

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
		if not isinstance(other, PISecurityRights):
			return False
		return self.__dict__ == other.__dict__

