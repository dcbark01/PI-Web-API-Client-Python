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


class PITimeRulePlugIn(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'path': 'str',
		'assembly_file_name': 'str',
		'assembly_i_d': 'str',
		'assembly_load_properties': 'list[str]',
		'assembly_time': 'str',
		'compatibility_version': 'int',
		'is_browsable': 'bool',
		'is_non_editable_config': 'bool',
		'loaded_assembly_time': 'str',
		'loaded_version': 'str',
		'version': 'str',
		'links': 'PITimeRulePlugInLinks',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'path': 'Path',
		'assembly_file_name': 'AssemblyFileName',
		'assembly_i_d': 'AssemblyID',
		'assembly_load_properties': 'AssemblyLoadProperties',
		'assembly_time': 'AssemblyTime',
		'compatibility_version': 'CompatibilityVersion',
		'is_browsable': 'IsBrowsable',
		'is_non_editable_config': 'IsNonEditableConfig',
		'loaded_assembly_time': 'LoadedAssemblyTime',
		'loaded_version': 'LoadedVersion',
		'version': 'Version',
		'links': 'Links',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, path=None, assembly_file_name=None, assembly_i_d=None, assembly_load_properties=None, assembly_time=None, compatibility_version=None, is_browsable=None, is_non_editable_config=None, loaded_assembly_time=None, loaded_version=None, version=None, links=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._path = None
		self._assembly_file_name = None
		self._assembly_i_d = None
		self._assembly_load_properties = None
		self._assembly_time = None
		self._compatibility_version = None
		self._is_browsable = None
		self._is_non_editable_config = None
		self._loaded_assembly_time = None
		self._loaded_version = None
		self._version = None
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
		if assembly_file_name is not None:
			self.assembly_file_name = assembly_file_name
		if assembly_i_d is not None:
			self.assembly_i_d = assembly_i_d
		if assembly_load_properties is not None:
			self.assembly_load_properties = assembly_load_properties
		if assembly_time is not None:
			self.assembly_time = assembly_time
		if compatibility_version is not None:
			self.compatibility_version = compatibility_version
		if is_browsable is not None:
			self.is_browsable = is_browsable
		if is_non_editable_config is not None:
			self.is_non_editable_config = is_non_editable_config
		if loaded_assembly_time is not None:
			self.loaded_assembly_time = loaded_assembly_time
		if loaded_version is not None:
			self.loaded_version = loaded_version
		if version is not None:
			self.version = version
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
	def assembly_file_name(self):
		return self._assembly_file_name

	@assembly_file_name.setter
	def assembly_file_name(self, assembly_file_name):
		self._assembly_file_name = assembly_file_name

	@property
	def assembly_i_d(self):
		return self._assembly_i_d

	@assembly_i_d.setter
	def assembly_i_d(self, assembly_i_d):
		self._assembly_i_d = assembly_i_d

	@property
	def assembly_load_properties(self):
		return self._assembly_load_properties

	@assembly_load_properties.setter
	def assembly_load_properties(self, assembly_load_properties):
		self._assembly_load_properties = assembly_load_properties

	@property
	def assembly_time(self):
		return self._assembly_time

	@assembly_time.setter
	def assembly_time(self, assembly_time):
		self._assembly_time = assembly_time

	@property
	def compatibility_version(self):
		return self._compatibility_version

	@compatibility_version.setter
	def compatibility_version(self, compatibility_version):
		self._compatibility_version = compatibility_version

	@property
	def is_browsable(self):
		return self._is_browsable

	@is_browsable.setter
	def is_browsable(self, is_browsable):
		self._is_browsable = is_browsable

	@property
	def is_non_editable_config(self):
		return self._is_non_editable_config

	@is_non_editable_config.setter
	def is_non_editable_config(self, is_non_editable_config):
		self._is_non_editable_config = is_non_editable_config

	@property
	def loaded_assembly_time(self):
		return self._loaded_assembly_time

	@loaded_assembly_time.setter
	def loaded_assembly_time(self, loaded_assembly_time):
		self._loaded_assembly_time = loaded_assembly_time

	@property
	def loaded_version(self):
		return self._loaded_version

	@loaded_version.setter
	def loaded_version(self, loaded_version):
		self._loaded_version = loaded_version

	@property
	def version(self):
		return self._version

	@version.setter
	def version(self, version):
		self._version = version

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
		if not isinstance(other, PITimeRulePlugIn):
			return False
		return self.__dict__ == other.__dict__

