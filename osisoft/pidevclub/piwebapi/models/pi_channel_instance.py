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


class PIChannelInstance(object):
	swagger_types = {
		'id': 'str',
		'start_time': 'str',
		'last_message_sent_time': 'str',
		'sent_message_count': 'int',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'id': 'Id',
		'start_time': 'StartTime',
		'last_message_sent_time': 'LastMessageSentTime',
		'sent_message_count': 'SentMessageCount',
		'web_exception': 'WebException',
	}
	def __init__(self, id=None, start_time=None, last_message_sent_time=None, sent_message_count=None, web_exception=None):

		self._id = None
		self._start_time = None
		self._last_message_sent_time = None
		self._sent_message_count = None
		self._web_exception = None

		if id is not None:
			self.id = id
		if start_time is not None:
			self.start_time = start_time
		if last_message_sent_time is not None:
			self.last_message_sent_time = last_message_sent_time
		if sent_message_count is not None:
			self.sent_message_count = sent_message_count
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def start_time(self):
		return self._start_time

	@start_time.setter
	def start_time(self, start_time):
		self._start_time = start_time

	@property
	def last_message_sent_time(self):
		return self._last_message_sent_time

	@last_message_sent_time.setter
	def last_message_sent_time(self, last_message_sent_time):
		self._last_message_sent_time = last_message_sent_time

	@property
	def sent_message_count(self):
		return self._sent_message_count

	@sent_message_count.setter
	def sent_message_count(self, sent_message_count):
		self._sent_message_count = sent_message_count

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
		if not isinstance(other, PIChannelInstance):
			return False
		return self.__dict__ == other.__dict__

