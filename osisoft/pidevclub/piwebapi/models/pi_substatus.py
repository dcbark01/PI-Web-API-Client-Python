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


class PISubstatus(object):
	swagger_types = {
		'substatus': 'int',
		'message': 'str',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'substatus': 'Substatus',
		'message': 'Message',
		'web_exception': 'WebException',
	}
	def __init__(self, substatus=None, message=None, web_exception=None):

		self._substatus = None
		self._message = None
		self._web_exception = None

		if substatus is not None:
			self.substatus = substatus
		if message is not None:
			self.message = message
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def substatus(self):
		return self._substatus

	@substatus.setter
	def substatus(self, substatus):
		self._substatus = substatus

	@property
	def message(self):
		return self._message

	@message.setter
	def message(self, message):
		self._message = message

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
		if not isinstance(other, PISubstatus):
			return False
		return self.__dict__ == other.__dict__

