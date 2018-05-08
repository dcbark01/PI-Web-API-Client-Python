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


class PISystemLanding(object):
	swagger_types = {
		'product_title': 'str',
		'product_version': 'str',
		'links': 'PISystemLandingLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'product_title': 'ProductTitle',
		'product_version': 'ProductVersion',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, product_title=None, product_version=None, links=None, web_exception=None):

		self._product_title = None
		self._product_version = None
		self._links = None
		self._web_exception = None

		if product_title is not None:
			self.product_title = product_title
		if product_version is not None:
			self.product_version = product_version
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def product_title(self):
		return self._product_title

	@product_title.setter
	def product_title(self, product_title):
		self._product_title = product_title

	@property
	def product_version(self):
		return self._product_version

	@product_version.setter
	def product_version(self, product_version):
		self._product_version = product_version

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
		if not isinstance(other, PISystemLanding):
			return False
		return self.__dict__ == other.__dict__

