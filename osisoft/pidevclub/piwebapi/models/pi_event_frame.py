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


class PIEventFrame(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'path': 'str',
		'template_name': 'str',
		'has_children': 'bool',
		'category_names': 'list[str]',
		'extended_properties': 'dict(str, PIValue)',
		'start_time': 'str',
		'end_time': 'str',
		'severity': 'str',
		'acknowledged_by': 'str',
		'acknowledged_date': 'str',
		'can_be_acknowledged': 'bool',
		'is_acknowledged': 'bool',
		'is_annotated': 'bool',
		'is_locked': 'bool',
		'are_values_captured': 'bool',
		'ref_element_web_ids': 'list[str]',
		'security': 'PISecurity',
		'links': 'PIEventFrameLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'path': 'Path',
		'template_name': 'TemplateName',
		'has_children': 'HasChildren',
		'category_names': 'CategoryNames',
		'extended_properties': 'ExtendedProperties',
		'start_time': 'StartTime',
		'end_time': 'EndTime',
		'severity': 'Severity',
		'acknowledged_by': 'AcknowledgedBy',
		'acknowledged_date': 'AcknowledgedDate',
		'can_be_acknowledged': 'CanBeAcknowledged',
		'is_acknowledged': 'IsAcknowledged',
		'is_annotated': 'IsAnnotated',
		'is_locked': 'IsLocked',
		'are_values_captured': 'AreValuesCaptured',
		'ref_element_web_ids': 'RefElementWebIds',
		'security': 'Security',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, path=None, template_name=None, has_children=None, category_names=None, extended_properties=None, start_time=None, end_time=None, severity=None, acknowledged_by=None, acknowledged_date=None, can_be_acknowledged=None, is_acknowledged=None, is_annotated=None, is_locked=None, are_values_captured=None, ref_element_web_ids=None, security=None, links=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._path = None
		self._template_name = None
		self._has_children = None
		self._category_names = None
		self._extended_properties = None
		self._start_time = None
		self._end_time = None
		self._severity = None
		self._acknowledged_by = None
		self._acknowledged_date = None
		self._can_be_acknowledged = None
		self._is_acknowledged = None
		self._is_annotated = None
		self._is_locked = None
		self._are_values_captured = None
		self._ref_element_web_ids = None
		self._security = None
		self._links = None
		self._web_exception = None

		if web_id is not None:
			self.web_id = web_id
		if id is not None:
			self.id = id
		if name is not None:
			self.name = name
		if description is not None:
			self.description = description
		if path is not None:
			self.path = path
		if template_name is not None:
			self.template_name = template_name
		if has_children is not None:
			self.has_children = has_children
		if category_names is not None:
			self.category_names = category_names
		if extended_properties is not None:
			self.extended_properties = extended_properties
		if start_time is not None:
			self.start_time = start_time
		if end_time is not None:
			self.end_time = end_time
		if severity is not None:
			self.severity = severity
		if acknowledged_by is not None:
			self.acknowledged_by = acknowledged_by
		if acknowledged_date is not None:
			self.acknowledged_date = acknowledged_date
		if can_be_acknowledged is not None:
			self.can_be_acknowledged = can_be_acknowledged
		if is_acknowledged is not None:
			self.is_acknowledged = is_acknowledged
		if is_annotated is not None:
			self.is_annotated = is_annotated
		if is_locked is not None:
			self.is_locked = is_locked
		if are_values_captured is not None:
			self.are_values_captured = are_values_captured
		if ref_element_web_ids is not None:
			self.ref_element_web_ids = ref_element_web_ids
		if security is not None:
			self.security = security
		if links is not None:
			self.links = links
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def web_id(self):
		return self._web_id

	@web_id.setter
	def web_id(self, web_id):
		self._web_id = web_id

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def template_name(self):
		return self._template_name

	@template_name.setter
	def template_name(self, template_name):
		self._template_name = template_name

	@property
	def has_children(self):
		return self._has_children

	@has_children.setter
	def has_children(self, has_children):
		self._has_children = has_children

	@property
	def category_names(self):
		return self._category_names

	@category_names.setter
	def category_names(self, category_names):
		self._category_names = category_names

	@property
	def extended_properties(self):
		return self._extended_properties

	@extended_properties.setter
	def extended_properties(self, extended_properties):
		self._extended_properties = extended_properties

	@property
	def start_time(self):
		return self._start_time

	@start_time.setter
	def start_time(self, start_time):
		self._start_time = start_time

	@property
	def end_time(self):
		return self._end_time

	@end_time.setter
	def end_time(self, end_time):
		self._end_time = end_time

	@property
	def severity(self):
		return self._severity

	@severity.setter
	def severity(self, severity):
		self._severity = severity

	@property
	def acknowledged_by(self):
		return self._acknowledged_by

	@acknowledged_by.setter
	def acknowledged_by(self, acknowledged_by):
		self._acknowledged_by = acknowledged_by

	@property
	def acknowledged_date(self):
		return self._acknowledged_date

	@acknowledged_date.setter
	def acknowledged_date(self, acknowledged_date):
		self._acknowledged_date = acknowledged_date

	@property
	def can_be_acknowledged(self):
		return self._can_be_acknowledged

	@can_be_acknowledged.setter
	def can_be_acknowledged(self, can_be_acknowledged):
		self._can_be_acknowledged = can_be_acknowledged

	@property
	def is_acknowledged(self):
		return self._is_acknowledged

	@is_acknowledged.setter
	def is_acknowledged(self, is_acknowledged):
		self._is_acknowledged = is_acknowledged

	@property
	def is_annotated(self):
		return self._is_annotated

	@is_annotated.setter
	def is_annotated(self, is_annotated):
		self._is_annotated = is_annotated

	@property
	def is_locked(self):
		return self._is_locked

	@is_locked.setter
	def is_locked(self, is_locked):
		self._is_locked = is_locked

	@property
	def are_values_captured(self):
		return self._are_values_captured

	@are_values_captured.setter
	def are_values_captured(self, are_values_captured):
		self._are_values_captured = are_values_captured

	@property
	def ref_element_web_ids(self):
		return self._ref_element_web_ids

	@ref_element_web_ids.setter
	def ref_element_web_ids(self, ref_element_web_ids):
		self._ref_element_web_ids = ref_element_web_ids

	@property
	def security(self):
		return self._security

	@security.setter
	def security(self, security):
		self._security = security

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
		if not isinstance(other, PIEventFrame):
			return False
		return self.__dict__ == other.__dict__

