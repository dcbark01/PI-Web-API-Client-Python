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


class PITimeRuleLinks(object):
	swagger_types = {
		'analysis': 'str',
		'analysis_template': 'str',
		'plug_in': 'str',
	}

	attribute_map = {
		'analysis': 'Analysis',
		'analysis_template': 'AnalysisTemplate',
		'plug_in': 'PlugIn',
	}
	def __init__(self, analysis=None, analysis_template=None, plug_in=None):

		self._analysis = None
		self._analysis_template = None
		self._plug_in = None

		if analysis is not None:
			self.analysis = analysis
		if analysis_template is not None:
			self.analysis_template = analysis_template
		if plug_in is not None:
			self.plug_in = plug_in

	@property
	def analysis(self):
		return self._analysis

	@analysis.setter
	def analysis(self, analysis):
		self._analysis = analysis

	@property
	def analysis_template(self):
		return self._analysis_template

	@analysis_template.setter
	def analysis_template(self, analysis_template):
		self._analysis_template = analysis_template

	@property
	def plug_in(self):
		return self._plug_in

	@plug_in.setter
	def plug_in(self, plug_in):
		self._plug_in = plug_in

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
		if not isinstance(other, PITimeRuleLinks):
			return False
		return self.__dict__ == other.__dict__

