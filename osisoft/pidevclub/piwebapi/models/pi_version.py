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


class PIVersion(object):
	swagger_types = {
		'full_version': 'str',
		'major_minor_revision': 'str',
		'build': 'str',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'full_version': 'FullVersion',
		'major_minor_revision': 'MajorMinorRevision',
		'build': 'Build',
		'web_exception': 'WebException',
	}
	def __init__(self, full_version=None, major_minor_revision=None, build=None, web_exception=None):

		self._full_version = None
		self._major_minor_revision = None
		self._build = None
		self._web_exception = None

		if full_version is not None:
			self.full_version = full_version
		if major_minor_revision is not None:
			self.major_minor_revision = major_minor_revision
		if build is not None:
			self.build = build
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def full_version(self):
		return self._full_version

	@full_version.setter
	def full_version(self, full_version):
		self._full_version = full_version

	@property
	def major_minor_revision(self):
		return self._major_minor_revision

	@major_minor_revision.setter
	def major_minor_revision(self, major_minor_revision):
		self._major_minor_revision = major_minor_revision

	@property
	def build(self):
		return self._build

	@build.setter
	def build(self, build):
		self._build = build

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
		if not isinstance(other, PIVersion):
			return False
		return self.__dict__ == other.__dict__

