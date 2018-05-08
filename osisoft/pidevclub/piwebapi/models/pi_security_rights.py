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


class PISecurityRights(object):
	swagger_types = {
		'owner_web_id': 'str',
		'security_item': 'str',
		'user_identity': 'str',
		'links': 'PISecurityRightsLinks',
		'can_annotate': 'bool',
		'can_delete': 'bool',
		'can_execute': 'bool',
		'can_read': 'bool',
		'can_read_data': 'bool',
		'can_subscribe': 'bool',
		'can_subscribe_others': 'bool',
		'can_write': 'bool',
		'can_write_data': 'bool',
		'has_admin': 'bool',
		'rights': 'list[str]',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'owner_web_id': 'OwnerWebId',
		'security_item': 'SecurityItem',
		'user_identity': 'UserIdentity',
		'links': 'Links',
		'can_annotate': 'CanAnnotate',
		'can_delete': 'CanDelete',
		'can_execute': 'CanExecute',
		'can_read': 'CanRead',
		'can_read_data': 'CanReadData',
		'can_subscribe': 'CanSubscribe',
		'can_subscribe_others': 'CanSubscribeOthers',
		'can_write': 'CanWrite',
		'can_write_data': 'CanWriteData',
		'has_admin': 'HasAdmin',
		'rights': 'Rights',
		'web_exception': 'WebException',
	}
	def __init__(self, owner_web_id=None, security_item=None, user_identity=None, links=None, can_annotate=None, can_delete=None, can_execute=None, can_read=None, can_read_data=None, can_subscribe=None, can_subscribe_others=None, can_write=None, can_write_data=None, has_admin=None, rights=None, web_exception=None):

		self._owner_web_id = None
		self._security_item = None
		self._user_identity = None
		self._links = None
		self._can_annotate = None
		self._can_delete = None
		self._can_execute = None
		self._can_read = None
		self._can_read_data = None
		self._can_subscribe = None
		self._can_subscribe_others = None
		self._can_write = None
		self._can_write_data = None
		self._has_admin = None
		self._rights = None
		self._web_exception = None

		if owner_web_id is not None:
			self.owner_web_id = owner_web_id
		if security_item is not None:
			self.security_item = security_item
		if user_identity is not None:
			self.user_identity = user_identity
		if links is not None:
			self.links = links
		if can_annotate is not None:
			self.can_annotate = can_annotate
		if can_delete is not None:
			self.can_delete = can_delete
		if can_execute is not None:
			self.can_execute = can_execute
		if can_read is not None:
			self.can_read = can_read
		if can_read_data is not None:
			self.can_read_data = can_read_data
		if can_subscribe is not None:
			self.can_subscribe = can_subscribe
		if can_subscribe_others is not None:
			self.can_subscribe_others = can_subscribe_others
		if can_write is not None:
			self.can_write = can_write
		if can_write_data is not None:
			self.can_write_data = can_write_data
		if has_admin is not None:
			self.has_admin = has_admin
		if rights is not None:
			self.rights = rights
		if web_exception is not None:
			self.web_exception = web_exception

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

	@property
	def can_annotate(self):
		return self._can_annotate

	@can_annotate.setter
	def can_annotate(self, can_annotate):
		self._can_annotate = can_annotate

	@property
	def can_delete(self):
		return self._can_delete

	@can_delete.setter
	def can_delete(self, can_delete):
		self._can_delete = can_delete

	@property
	def can_execute(self):
		return self._can_execute

	@can_execute.setter
	def can_execute(self, can_execute):
		self._can_execute = can_execute

	@property
	def can_read(self):
		return self._can_read

	@can_read.setter
	def can_read(self, can_read):
		self._can_read = can_read

	@property
	def can_read_data(self):
		return self._can_read_data

	@can_read_data.setter
	def can_read_data(self, can_read_data):
		self._can_read_data = can_read_data

	@property
	def can_subscribe(self):
		return self._can_subscribe

	@can_subscribe.setter
	def can_subscribe(self, can_subscribe):
		self._can_subscribe = can_subscribe

	@property
	def can_subscribe_others(self):
		return self._can_subscribe_others

	@can_subscribe_others.setter
	def can_subscribe_others(self, can_subscribe_others):
		self._can_subscribe_others = can_subscribe_others

	@property
	def can_write(self):
		return self._can_write

	@can_write.setter
	def can_write(self, can_write):
		self._can_write = can_write

	@property
	def can_write_data(self):
		return self._can_write_data

	@can_write_data.setter
	def can_write_data(self, can_write_data):
		self._can_write_data = can_write_data

	@property
	def has_admin(self):
		return self._has_admin

	@has_admin.setter
	def has_admin(self, has_admin):
		self._has_admin = has_admin

	@property
	def rights(self):
		return self._rights

	@rights.setter
	def rights(self, rights):
		self._rights = rights

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
		if not isinstance(other, PISecurityRights):
			return False
		return self.__dict__ == other.__dict__

