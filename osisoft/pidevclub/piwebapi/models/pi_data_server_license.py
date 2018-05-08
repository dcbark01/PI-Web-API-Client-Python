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


class PIDataServerLicense(object):
	swagger_types = {
		'amount_left': 'str',
		'amount_used': 'str',
		'name': 'str',
		'total_amount': 'str',
		'links': 'PIDataServerLicenseLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'amount_left': 'AmountLeft',
		'amount_used': 'AmountUsed',
		'name': 'Name',
		'total_amount': 'TotalAmount',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, amount_left=None, amount_used=None, name=None, total_amount=None, links=None, web_exception=None):

		self._amount_left = None
		self._amount_used = None
		self._name = None
		self._total_amount = None
		self._links = None
		self._web_exception = None

		if amount_left is not None:
			self.amount_left = amount_left
		if amount_used is not None:
			self.amount_used = amount_used
		if name is not None:
			self.name = name
		if total_amount is not None:
			self.total_amount = total_amount
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def amount_left(self):
		return self._amount_left

	@amount_left.setter
	def amount_left(self, amount_left):
		self._amount_left = amount_left

	@property
	def amount_used(self):
		return self._amount_used

	@amount_used.setter
	def amount_used(self, amount_used):
		self._amount_used = amount_used

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def total_amount(self):
		return self._total_amount

	@total_amount.setter
	def total_amount(self, total_amount):
		self._total_amount = total_amount

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
		if not isinstance(other, PIDataServerLicense):
			return False
		return self.__dict__ == other.__dict__

