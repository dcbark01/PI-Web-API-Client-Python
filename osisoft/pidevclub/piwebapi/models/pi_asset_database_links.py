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


class PIAssetDatabaseLinks(object):
	swagger_types = {
		'elements': 'str',
		'element_templates': 'str',
		'event_frames': 'str',
		'asset_server': 'str',
		'element_categories': 'str',
		'attribute_categories': 'str',
		'table_categories': 'str',
		'analysis_categories': 'str',
		'analysis_templates': 'str',
		'enumeration_sets': 'str',
		'tables': 'str',
		'security': 'str',
		'security_entries': 'str',
	}

	attribute_map = {
		'elements': 'Elements',
		'element_templates': 'ElementTemplates',
		'event_frames': 'EventFrames',
		'asset_server': 'AssetServer',
		'element_categories': 'ElementCategories',
		'attribute_categories': 'AttributeCategories',
		'table_categories': 'TableCategories',
		'analysis_categories': 'AnalysisCategories',
		'analysis_templates': 'AnalysisTemplates',
		'enumeration_sets': 'EnumerationSets',
		'tables': 'Tables',
		'security': 'Security',
		'security_entries': 'SecurityEntries',
	}
	def __init__(self, elements=None, element_templates=None, event_frames=None, asset_server=None, element_categories=None, attribute_categories=None, table_categories=None, analysis_categories=None, analysis_templates=None, enumeration_sets=None, tables=None, security=None, security_entries=None):

		self._elements = None
		self._element_templates = None
		self._event_frames = None
		self._asset_server = None
		self._element_categories = None
		self._attribute_categories = None
		self._table_categories = None
		self._analysis_categories = None
		self._analysis_templates = None
		self._enumeration_sets = None
		self._tables = None
		self._security = None
		self._security_entries = None

		if elements is not None:
			self.elements = elements
		if element_templates is not None:
			self.element_templates = element_templates
		if event_frames is not None:
			self.event_frames = event_frames
		if asset_server is not None:
			self.asset_server = asset_server
		if element_categories is not None:
			self.element_categories = element_categories
		if attribute_categories is not None:
			self.attribute_categories = attribute_categories
		if table_categories is not None:
			self.table_categories = table_categories
		if analysis_categories is not None:
			self.analysis_categories = analysis_categories
		if analysis_templates is not None:
			self.analysis_templates = analysis_templates
		if enumeration_sets is not None:
			self.enumeration_sets = enumeration_sets
		if tables is not None:
			self.tables = tables
		if security is not None:
			self.security = security
		if security_entries is not None:
			self.security_entries = security_entries

	@property
	def elements(self):
		return self._elements

	@elements.setter
	def elements(self, elements):
		self._elements = elements

	@property
	def element_templates(self):
		return self._element_templates

	@element_templates.setter
	def element_templates(self, element_templates):
		self._element_templates = element_templates

	@property
	def event_frames(self):
		return self._event_frames

	@event_frames.setter
	def event_frames(self, event_frames):
		self._event_frames = event_frames

	@property
	def asset_server(self):
		return self._asset_server

	@asset_server.setter
	def asset_server(self, asset_server):
		self._asset_server = asset_server

	@property
	def element_categories(self):
		return self._element_categories

	@element_categories.setter
	def element_categories(self, element_categories):
		self._element_categories = element_categories

	@property
	def attribute_categories(self):
		return self._attribute_categories

	@attribute_categories.setter
	def attribute_categories(self, attribute_categories):
		self._attribute_categories = attribute_categories

	@property
	def table_categories(self):
		return self._table_categories

	@table_categories.setter
	def table_categories(self, table_categories):
		self._table_categories = table_categories

	@property
	def analysis_categories(self):
		return self._analysis_categories

	@analysis_categories.setter
	def analysis_categories(self, analysis_categories):
		self._analysis_categories = analysis_categories

	@property
	def analysis_templates(self):
		return self._analysis_templates

	@analysis_templates.setter
	def analysis_templates(self, analysis_templates):
		self._analysis_templates = analysis_templates

	@property
	def enumeration_sets(self):
		return self._enumeration_sets

	@enumeration_sets.setter
	def enumeration_sets(self, enumeration_sets):
		self._enumeration_sets = enumeration_sets

	@property
	def tables(self):
		return self._tables

	@tables.setter
	def tables(self, tables):
		self._tables = tables

	@property
	def security(self):
		return self._security

	@security.setter
	def security(self, security):
		self._security = security

	@property
	def security_entries(self):
		return self._security_entries

	@security_entries.setter
	def security_entries(self, security_entries):
		self._security_entries = security_entries

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
		if not isinstance(other, PIAssetDatabaseLinks):
			return False
		return self.__dict__ == other.__dict__

