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


class PIRequest(object):
	swagger_types = {
		'method': 'str',
		'resource': 'str',
		'request_template': 'PIRequestTemplate',
		'parameters': 'list[str]',
		'headers': 'dict(str, str)',
		'content': 'str',
		'parent_ids': 'list[str]',
	}

	attribute_map = {
		'method': 'Method',
		'resource': 'Resource',
		'request_template': 'RequestTemplate',
		'parameters': 'Parameters',
		'headers': 'Headers',
		'content': 'Content',
		'parent_ids': 'ParentIds',
	}
	def __init__(self, method=None, resource=None, request_template=None, parameters=None, headers=None, content=None, parent_ids=None):

		self._method = None
		self._resource = None
		self._request_template = None
		self._parameters = None
		self._headers = None
		self._content = None
		self._parent_ids = None

		if method is not None:
			self.method = method
		if resource is not None:
			self.resource = resource
		if request_template is not None:
			self.request_template = request_template
		if parameters is not None:
			self.parameters = parameters
		if headers is not None:
			self.headers = headers
		if content is not None:
			self.content = content
		if parent_ids is not None:
			self.parent_ids = parent_ids

	@property
	def method(self):
		return self._method

	@method.setter
	def method(self, method):
		self._method = method

	@property
	def resource(self):
		return self._resource

	@resource.setter
	def resource(self, resource):
		self._resource = resource

	@property
	def request_template(self):
		return self._request_template

	@request_template.setter
	def request_template(self, request_template):
		self._request_template = request_template

	@property
	def parameters(self):
		return self._parameters

	@parameters.setter
	def parameters(self, parameters):
		self._parameters = parameters

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

	@property
	def parent_ids(self):
		return self._parent_ids

	@parent_ids.setter
	def parent_ids(self, parent_ids):
		self._parent_ids = parent_ids

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
		if not isinstance(other, PIRequest):
			return False
		return self.__dict__ == other.__dict__

