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


class PIResponse(object):
	swagger_types = {
		'status': 'int',
		'headers': 'dict(str, str)',
		'content': 'object',
	}

	attribute_map = {
		'status': 'Status',
		'headers': 'Headers',
		'content': 'Content',
	}
	def __init__(self, status=None, headers=None, content=None):

		self._status = None
		self._headers = None
		self._content = None

		if status is not None:
			self.status = status
		if headers is not None:
			self.headers = headers
		if content is not None:
			self.content = content

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		self._status = status

	@property
	def headers(self):
		return self._headers

	@headers.setter
	def headers(self, headers):
		self._headers = headers

	@property
	def content(self):
		return self._content

	@content.setter
	def content(self, content):
		self._content = content

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
		if not isinstance(other, PIResponse):
			return False
		return self.__dict__ == other.__dict__

