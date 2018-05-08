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


class PIPaginationLinks(object):
	swagger_types = {
		'first': 'str',
		'previous': 'str',
		'next': 'str',
		'last': 'str',
	}

	attribute_map = {
		'first': 'First',
		'previous': 'Previous',
		'next': 'Next',
		'last': 'Last',
	}
	def __init__(self, first=None, previous=None, next=None, last=None):

		self._first = None
		self._previous = None
		self._next = None
		self._last = None

		if first is not None:
			self.first = first
		if previous is not None:
			self.previous = previous
		if next is not None:
			self.next = next
		if last is not None:
			self.last = last

	@property
	def first(self):
		return self._first

	@first.setter
	def first(self, first):
		self._first = first

	@property
	def previous(self):
		return self._previous

	@previous.setter
	def previous(self, previous):
		self._previous = previous

	@property
	def next(self):
		return self._next

	@next.setter
	def next(self, next):
		self._next = next

	@property
	def last(self):
		return self._last

	@last.setter
	def last(self, last):
		self._last = last

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
		if not isinstance(other, PIPaginationLinks):
			return False
		return self.__dict__ == other.__dict__

