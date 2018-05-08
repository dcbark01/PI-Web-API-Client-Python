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
import base64

from osisoft.pidevclub.piwebapi.models import PIAttribute, PIElement, PIAssetServer, PIDataServer, PIAnalysis, \
	PIAnalysisTemplate, PIElementTemplate, PIEventFrame, PIAnalysisCategory, PIAnalysisRule, PIAnalysisRulePlugIn, \
	PIAttributeCategory, PIAttributeTemplate, PIAssetDatabase, PIElementCategory, PIEnumerationSet, PIEnumerationValue, \
	PITimeRule, PITimeRulePlugIn, PISecurityIdentity, PISecurityMapping, PITable, PITableCategory, PIPoint, PIUnit, \
	PIUnitClass
from osisoft.pidevclub.piwebapi.web_id.web_id_exception import WebIdException
from osisoft.pidevclub.piwebapi.web_id.web_id_info import WebIdInfo


class WebIdHelper(object):
	def __init__(self):
		self.marker_owner = None
		pass

	def get_web_id_info(self, web_id):
		return WebIdInfo(web_id)

	def generate_web_id_by_path(self, path,  objct_type, owner_type=None):
		self.validate_type_and_owner_type(objct_type, owner_type)
		marker = self.get_marker(objct_type)
		owner_marker = self.get_owner_marker(owner_type)
		if path[0:2] == "\\\\":
			path = path[2:]
		encoded_path = self.encode_string(path.upper())
		return "P1{}{}{}".format(marker, owner_marker, encoded_path)

	def validate_type_and_owner_type(self, object_type, owner_type):
		if isinstance(PIAttribute(), object_type):
			if isinstance(PIElement(), owner_type) and isinstance(PIEventFrame(), owner_type):
				raise WebIdException("PIAttribte owner type must be a PIElement or a PIEventFrame.")
		elif isinstance(PIAttributeTemplate(), object_type):
			if isinstance(PIElementTemplate(), owner_type):
				raise WebIdException("PIElementTemplate owner type must be a PIElementTemplate.")
		elif isinstance(PIEnumerationSet(), object_type) or isinstance(PIEnumerationValue(), object_type):
			if isinstance(PIDataServer(), owner_type) == False and isinstance(PIAssetServer(), owner_type) == False:
				raise  WebIdException("PIEnumerationSet and  PIEnumerationValue owner type must be a PIDataServer or PIAssetServer.")
		elif isinstance(PITimeRule(), object_type):
			if isinstance(PIAnalysis(), owner_type) and isinstance(PIAnalysisTemplate(), owner_type):
				raise WebIdException("PITimeRule owner type must be a PIAnalysis and PIAnalysisTemplate.")

	def get_owner_marker(self, owner_type):
		if owner_type == None:
			return ""
		if isinstance(PIAssetServer(),owner_type):
			self.marker_owner = "R"
		elif isinstance(PIDataServer(), owner_type):
			self.marker_owner = "D"
		elif isinstance(PIAnalysis(), owner_type):
			self.marker_owner = "X"
		elif isinstance(PIAnalysisTemplate(), owner_type):
			self.marker_owner = "T"
		elif isinstance(PIElement(), owner_type):
			self.marker_owner = "E"
		if isinstance(PIElementTemplate(), owner_type):
			self.marker_owner = "E"
		elif isinstance(PIEventFrame(), owner_type):
			self.marker_owner = "F"
		return self.marker_owner

	def get_marker(self, object_type):
		marker = None

		if isinstance(PIAnalysis(), object_type):
			marker = "Xs"
		elif isinstance(PIAnalysisCategory(), object_type):
			marker = "XC"
		elif isinstance(PIAnalysisTemplate(), object_type):
			marker = "XT"
		elif isinstance(PIAnalysisRule(), object_type):
			marker = "XR"
		elif isinstance(PIAnalysisRulePlugIn(), object_type):
			marker = "XP"
		elif isinstance(PIAttribute(), object_type):
			marker = "Ab"
		elif isinstance(PIAttributeCategory(), object_type):
			marker = "AC"
		elif isinstance(PIAttributeTemplate(), object_type):
			marker = "AT"
		elif isinstance(PIAssetDatabase(), object_type):
			marker = "RD"
		elif isinstance(PIAssetServer(), object_type):
			marker = "RS"
		elif isinstance(PIElement(), object_type):
			marker = "Em"
		elif isinstance(PIElementCategory(), object_type):
			marker = "EC"
		elif isinstance(PIElementTemplate(), object_type):
			marker = "ET"
		elif isinstance(PIEnumerationSet(), object_type):
			marker = "MS"
		elif isinstance(PIEnumerationValue(), object_type):
			marker = "MV"
		elif isinstance(PIEventFrame(), object_type):
			marker = "Fm"
		elif isinstance(PITimeRule(), object_type):
			marker = "TR"
		elif isinstance(PITimeRulePlugIn(), object_type):
			marker = "TP"
		elif isinstance(PISecurityIdentity(), object_type):
			marker = "SI"
		elif isinstance(PISecurityMapping(), object_type):
			marker = "SM"
		elif isinstance(PITable(), object_type):
			marker = "Bl"
		elif isinstance(PITableCategory(), object_type):
			marker = "BC"
		elif isinstance(PIPoint(), object_type):
			marker = "DP"
		elif isinstance(PIDataServer(), object_type):
			marker = "DS"
		elif isinstance(PIUnit(), object_type):
			marker = "Ut"
		elif isinstance(PIUnitClass(), object_type):
			marker = "UC"
		if (marker == None):
			raise WebIdException("Invalid object type.")
		return marker

	def encode_string(self, value):
		bytes = value.upper().encode('utf-8')
		return self.encode(bytes)

	def encode(self, value):
		encoded = base64.b64encode(value).decode()
		return encoded.strip('=').replace('+', '-').replace('/', '_')








