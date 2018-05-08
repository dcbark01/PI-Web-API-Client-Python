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


class PIAnalysisTemplateLinks(object):
	swagger_types = {
		'database': 'str',
		'categories': 'str',
		'analysis_rule': 'str',
		'analysis_rule_plug_in': 'str',
		'time_rule': 'str',
		'time_rule_plug_in': 'str',
		'target': 'str',
		'security': 'str',
		'security_entries': 'str',
	}

	attribute_map = {
		'database': 'Database',
		'categories': 'Categories',
		'analysis_rule': 'AnalysisRule',
		'analysis_rule_plug_in': 'AnalysisRulePlugIn',
		'time_rule': 'TimeRule',
		'time_rule_plug_in': 'TimeRulePlugIn',
		'target': 'Target',
		'security': 'Security',
		'security_entries': 'SecurityEntries',
	}
	def __init__(self, database=None, categories=None, analysis_rule=None, analysis_rule_plug_in=None, time_rule=None, time_rule_plug_in=None, target=None, security=None, security_entries=None):

		self._database = None
		self._categories = None
		self._analysis_rule = None
		self._analysis_rule_plug_in = None
		self._time_rule = None
		self._time_rule_plug_in = None
		self._target = None
		self._security = None
		self._security_entries = None

		if database is not None:
			self.database = database
		if categories is not None:
			self.categories = categories
		if analysis_rule is not None:
			self.analysis_rule = analysis_rule
		if analysis_rule_plug_in is not None:
			self.analysis_rule_plug_in = analysis_rule_plug_in
		if time_rule is not None:
			self.time_rule = time_rule
		if time_rule_plug_in is not None:
			self.time_rule_plug_in = time_rule_plug_in
		if target is not None:
			self.target = target
		if security is not None:
			self.security = security
		if security_entries is not None:
			self.security_entries = security_entries

	@property
	def database(self):
		return self._database

	@database.setter
	def database(self, database):
		self._database = database

	@property
	def categories(self):
		return self._categories

	@categories.setter
	def categories(self, categories):
		self._categories = categories

	@property
	def analysis_rule(self):
		return self._analysis_rule

	@analysis_rule.setter
	def analysis_rule(self, analysis_rule):
		self._analysis_rule = analysis_rule

	@property
	def analysis_rule_plug_in(self):
		return self._analysis_rule_plug_in

	@analysis_rule_plug_in.setter
	def analysis_rule_plug_in(self, analysis_rule_plug_in):
		self._analysis_rule_plug_in = analysis_rule_plug_in

	@property
	def time_rule(self):
		return self._time_rule

	@time_rule.setter
	def time_rule(self, time_rule):
		self._time_rule = time_rule

	@property
	def time_rule_plug_in(self):
		return self._time_rule_plug_in

	@time_rule_plug_in.setter
	def time_rule_plug_in(self, time_rule_plug_in):
		self._time_rule_plug_in = time_rule_plug_in

	@property
	def target(self):
		return self._target

	@target.setter
	def target(self, target):
		self._target = target

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
		if not isinstance(other, PIAnalysisTemplateLinks):
			return False
		return self.__dict__ == other.__dict__

