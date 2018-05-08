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


class PIWebException(object):
	swagger_types = {
		'status_code': 'int',
		'errors': 'list[str]',
	}

	attribute_map = {
		'status_code': 'StatusCode',
		'errors': 'Errors',
	}
	def __init__(self, status_code=None, errors=None):

		self._status_code = None
		self._errors = None

		if status_code is not None:
			self.status_code = status_code
		if errors is not None:
			self.errors = errors

	@property
	def status_code(self):
		return self._status_code

	@status_code.setter
	def status_code(self, status_code):
		self._status_code = status_code

	@property
	def errors(self):
		return self._errors

	@errors.setter
	def errors(self, errors):
		self._errors = errors

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
		if not isinstance(other, PIWebException):
			return False
		return self.__dict__ == other.__dict__

