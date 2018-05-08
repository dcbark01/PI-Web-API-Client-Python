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


class PIAssetServerLinks(object):
	swagger_types = {
		'databases': 'str',
		'security_identities': 'str',
		'security_mappings': 'str',
		'unit_classes': 'str',
		'analysis_rule_plug_ins': 'str',
		'time_rule_plug_ins': 'str',
		'security': 'str',
		'security_entries': 'str',
	}

	attribute_map = {
		'databases': 'Databases',
		'security_identities': 'SecurityIdentities',
		'security_mappings': 'SecurityMappings',
		'unit_classes': 'UnitClasses',
		'analysis_rule_plug_ins': 'AnalysisRulePlugIns',
		'time_rule_plug_ins': 'TimeRulePlugIns',
		'security': 'Security',
		'security_entries': 'SecurityEntries',
	}
	def __init__(self, databases=None, security_identities=None, security_mappings=None, unit_classes=None, analysis_rule_plug_ins=None, time_rule_plug_ins=None, security=None, security_entries=None):

		self._databases = None
		self._security_identities = None
		self._security_mappings = None
		self._unit_classes = None
		self._analysis_rule_plug_ins = None
		self._time_rule_plug_ins = None
		self._security = None
		self._security_entries = None

		if databases is not None:
			self.databases = databases
		if security_identities is not None:
			self.security_identities = security_identities
		if security_mappings is not None:
			self.security_mappings = security_mappings
		if unit_classes is not None:
			self.unit_classes = unit_classes
		if analysis_rule_plug_ins is not None:
			self.analysis_rule_plug_ins = analysis_rule_plug_ins
		if time_rule_plug_ins is not None:
			self.time_rule_plug_ins = time_rule_plug_ins
		if security is not None:
			self.security = security
		if security_entries is not None:
			self.security_entries = security_entries

	@property
	def databases(self):
		return self._databases

	@databases.setter
	def databases(self, databases):
		self._databases = databases

	@property
	def security_identities(self):
		return self._security_identities

	@security_identities.setter
	def security_identities(self, security_identities):
		self._security_identities = security_identities

	@property
	def security_mappings(self):
		return self._security_mappings

	@security_mappings.setter
	def security_mappings(self, security_mappings):
		self._security_mappings = security_mappings

	@property
	def unit_classes(self):
		return self._unit_classes

	@unit_classes.setter
	def unit_classes(self, unit_classes):
		self._unit_classes = unit_classes

	@property
	def analysis_rule_plug_ins(self):
		return self._analysis_rule_plug_ins

	@analysis_rule_plug_ins.setter
	def analysis_rule_plug_ins(self, analysis_rule_plug_ins):
		self._analysis_rule_plug_ins = analysis_rule_plug_ins

	@property
	def time_rule_plug_ins(self):
		return self._time_rule_plug_ins

	@time_rule_plug_ins.setter
	def time_rule_plug_ins(self, time_rule_plug_ins):
		self._time_rule_plug_ins = time_rule_plug_ins

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
		if not isinstance(other, PIAssetServerLinks):
			return False
		return self.__dict__ == other.__dict__

