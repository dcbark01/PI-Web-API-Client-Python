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


class PIAnalysis(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'path': 'str',
		'analysis_rule_plug_in_name': 'str',
		'auto_created': 'bool',
		'category_names': 'list[str]',
		'group_id': 'int',
		'has_notification': 'bool',
		'has_target': 'bool',
		'has_template': 'bool',
		'is_configured': 'bool',
		'is_time_rule_defined_by_template': 'bool',
		'maximum_queue_size': 'int',
		'output_time': 'str',
		'priority': 'str',
		'publish_results': 'bool',
		'status': 'str',
		'target_web_id': 'str',
		'template_name': 'str',
		'time_rule_plug_in_name': 'str',
		'links': 'PIAnalysisLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'path': 'Path',
		'analysis_rule_plug_in_name': 'AnalysisRulePlugInName',
		'auto_created': 'AutoCreated',
		'category_names': 'CategoryNames',
		'group_id': 'GroupId',
		'has_notification': 'HasNotification',
		'has_target': 'HasTarget',
		'has_template': 'HasTemplate',
		'is_configured': 'IsConfigured',
		'is_time_rule_defined_by_template': 'IsTimeRuleDefinedByTemplate',
		'maximum_queue_size': 'MaximumQueueSize',
		'output_time': 'OutputTime',
		'priority': 'Priority',
		'publish_results': 'PublishResults',
		'status': 'Status',
		'target_web_id': 'TargetWebId',
		'template_name': 'TemplateName',
		'time_rule_plug_in_name': 'TimeRulePlugInName',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, path=None, analysis_rule_plug_in_name=None, auto_created=None, category_names=None, group_id=None, has_notification=None, has_target=None, has_template=None, is_configured=None, is_time_rule_defined_by_template=None, maximum_queue_size=None, output_time=None, priority=None, publish_results=None, status=None, target_web_id=None, template_name=None, time_rule_plug_in_name=None, links=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._path = None
		self._analysis_rule_plug_in_name = None
		self._auto_created = None
		self._category_names = None
		self._group_id = None
		self._has_notification = None
		self._has_target = None
		self._has_template = None
		self._is_configured = None
		self._is_time_rule_defined_by_template = None
		self._maximum_queue_size = None
		self._output_time = None
		self._priority = None
		self._publish_results = None
		self._status = None
		self._target_web_id = None
		self._template_name = None
		self._time_rule_plug_in_name = None
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
		if analysis_rule_plug_in_name is not None:
			self.analysis_rule_plug_in_name = analysis_rule_plug_in_name
		if auto_created is not None:
			self.auto_created = auto_created
		if category_names is not None:
			self.category_names = category_names
		if group_id is not None:
			self.group_id = group_id
		if has_notification is not None:
			self.has_notification = has_notification
		if has_target is not None:
			self.has_target = has_target
		if has_template is not None:
			self.has_template = has_template
		if is_configured is not None:
			self.is_configured = is_configured
		if is_time_rule_defined_by_template is not None:
			self.is_time_rule_defined_by_template = is_time_rule_defined_by_template
		if maximum_queue_size is not None:
			self.maximum_queue_size = maximum_queue_size
		if output_time is not None:
			self.output_time = output_time
		if priority is not None:
			self.priority = priority
		if publish_results is not None:
			self.publish_results = publish_results
		if status is not None:
			self.status = status
		if target_web_id is not None:
			self.target_web_id = target_web_id
		if template_name is not None:
			self.template_name = template_name
		if time_rule_plug_in_name is not None:
			self.time_rule_plug_in_name = time_rule_plug_in_name
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
	def analysis_rule_plug_in_name(self):
		return self._analysis_rule_plug_in_name

	@analysis_rule_plug_in_name.setter
	def analysis_rule_plug_in_name(self, analysis_rule_plug_in_name):
		self._analysis_rule_plug_in_name = analysis_rule_plug_in_name

	@property
	def auto_created(self):
		return self._auto_created

	@auto_created.setter
	def auto_created(self, auto_created):
		self._auto_created = auto_created

	@property
	def category_names(self):
		return self._category_names

	@category_names.setter
	def category_names(self, category_names):
		self._category_names = category_names

	@property
	def group_id(self):
		return self._group_id

	@group_id.setter
	def group_id(self, group_id):
		self._group_id = group_id

	@property
	def has_notification(self):
		return self._has_notification

	@has_notification.setter
	def has_notification(self, has_notification):
		self._has_notification = has_notification

	@property
	def has_target(self):
		return self._has_target

	@has_target.setter
	def has_target(self, has_target):
		self._has_target = has_target

	@property
	def has_template(self):
		return self._has_template

	@has_template.setter
	def has_template(self, has_template):
		self._has_template = has_template

	@property
	def is_configured(self):
		return self._is_configured

	@is_configured.setter
	def is_configured(self, is_configured):
		self._is_configured = is_configured

	@property
	def is_time_rule_defined_by_template(self):
		return self._is_time_rule_defined_by_template

	@is_time_rule_defined_by_template.setter
	def is_time_rule_defined_by_template(self, is_time_rule_defined_by_template):
		self._is_time_rule_defined_by_template = is_time_rule_defined_by_template

	@property
	def maximum_queue_size(self):
		return self._maximum_queue_size

	@maximum_queue_size.setter
	def maximum_queue_size(self, maximum_queue_size):
		self._maximum_queue_size = maximum_queue_size

	@property
	def output_time(self):
		return self._output_time

	@output_time.setter
	def output_time(self, output_time):
		self._output_time = output_time

	@property
	def priority(self):
		return self._priority

	@priority.setter
	def priority(self, priority):
		self._priority = priority

	@property
	def publish_results(self):
		return self._publish_results

	@publish_results.setter
	def publish_results(self, publish_results):
		self._publish_results = publish_results

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		self._status = status

	@property
	def target_web_id(self):
		return self._target_web_id

	@target_web_id.setter
	def target_web_id(self, target_web_id):
		self._target_web_id = target_web_id

	@property
	def template_name(self):
		return self._template_name

	@template_name.setter
	def template_name(self, template_name):
		self._template_name = template_name

	@property
	def time_rule_plug_in_name(self):
		return self._time_rule_plug_in_name

	@time_rule_plug_in_name.setter
	def time_rule_plug_in_name(self, time_rule_plug_in_name):
		self._time_rule_plug_in_name = time_rule_plug_in_name

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
		if not isinstance(other, PIAnalysis):
			return False
		return self.__dict__ == other.__dict__

