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
import binascii
import struct

from osisoft.pidevclub.piwebapi.web_id.web_id_type import WebIdType
from osisoft.pidevclub.piwebapi.web_id.web_id_string_type import WebIdStringType
from osisoft.pidevclub.piwebapi.web_id.web_id_exception import WebIdException
from osisoft.pidevclub.piwebapi.models.pi_analysis import PIAnalysis
from osisoft.pidevclub.piwebapi.models.pi_analysis_category import PIAnalysisCategory
from osisoft.pidevclub.piwebapi.models.pi_analysis_rule import PIAnalysisRule
from osisoft.pidevclub.piwebapi.models.pi_analysis_rule_plug_in import PIAnalysisRulePlugIn
from osisoft.pidevclub.piwebapi.models.pi_analysis_template import PIAnalysisTemplate
from osisoft.pidevclub.piwebapi.models.pi_asset_database import PIAssetDatabase
from osisoft.pidevclub.piwebapi.models.pi_asset_server import PIAssetServer
from osisoft.pidevclub.piwebapi.models.pi_attribute import PIAttribute
from osisoft.pidevclub.piwebapi.models.pi_attribute_category import PIAttributeCategory
from osisoft.pidevclub.piwebapi.models.pi_attribute_template import PIAttributeTemplate
from osisoft.pidevclub.piwebapi.models.pi_data_server import PIDataServer
from osisoft.pidevclub.piwebapi.models.pi_element import PIElement
from osisoft.pidevclub.piwebapi.models.pi_element_category import PIElementCategory
from osisoft.pidevclub.piwebapi.models.pi_element_template import PIElementTemplate
from osisoft.pidevclub.piwebapi.models.pi_enumeration_set import PIEnumerationSet
from osisoft.pidevclub.piwebapi.models.pi_enumeration_value import PIEnumerationValue
from osisoft.pidevclub.piwebapi.models.pi_event_frame import PIEventFrame
from osisoft.pidevclub.piwebapi.models.pi_point import PIPoint
from osisoft.pidevclub.piwebapi.models.pi_security_identity import PISecurityIdentity
from osisoft.pidevclub.piwebapi.models.pi_security_mapping import PISecurityMapping
from osisoft.pidevclub.piwebapi.models.pi_table import PITable
from osisoft.pidevclub.piwebapi.models.pi_table_category import PITableCategory
from osisoft.pidevclub.piwebapi.models.pi_time_rule import PITimeRule
from osisoft.pidevclub.piwebapi.models.pi_time_rule_plug_in import PITimeRulePlugIn
from osisoft.pidevclub.piwebapi.models.pi_unit import PIUnit
from osisoft.pidevclub.piwebapi.models.pi_unit_class import PIUnitClass


class WebIdInfo(object):
    def __init__(self, web_id):
        self.web_id = web_id
        self.marker = None
        self.web_id_type_letter = None
        self.object_type = None
        self.owner_type = None
        self.path = None
        self.owner_id = None
        self.marker_owner = None
        self.point_id = None
        self.object_id = None
        self.server_id = None
        self.web_id_type = self.get_web_id_type(web_id)
        if (self.web_id_type == WebIdType.DefaultIDOnly) or (self.web_id_type == WebIdType.LocalIDOnly):
            raise WebIdException(
                "This library is not compatible with DefaultIDOnly "
                "or LocalIDOnly. Use Full, PathOnly or IDOnly instead.")

        self.version = int(web_id[1:2])
        if self.version == 0:
            raise WebIdException("This tool is compatible with Web ID 2.0 only."
                                 " The second character of the Web ID must be 1.")

        self.process_type(web_id)
        self.process_guids_and_paths(web_id)

    def get_web_id_type(self, web_id):
        self.web_id_type_letter = web_id[0:1]
        if self.web_id_type_letter == "F":
            return WebIdType.Full
        elif self.web_id_type_letter == "I":
            return WebIdType.IDOnly
        elif self.web_id_type_letter == "P":
            return WebIdType.PathOnly
        elif self.web_id_type_letter == "L":
            return WebIdType.LocalIDOnly
        elif self.web_id_type_letter == "D":
            return WebIdType.DefaultIDOnly
        raise WebIdException("Incorrect Web ID type (first letter).")

    def process_type(self, web_id):
        self.marker = web_id[2:4]
        if self.marker == "Xs":
            self.objectType = type(PIAnalysis())
        elif self.marker == "XC":
            self.objectType = type(PIAnalysisCategory())
        elif self.marker == "XT":
            self.objectType = type(PIAnalysisTemplate())
        elif self.marker == "XR":
            self.objectType = type(PIAnalysisRule())
        elif self.marker == "XP":
            self.objectType = type(PIAnalysisRulePlugIn())
        elif self.marker == "Ab":
            self.objectType = type(PIAttribute())
        elif self.marker == "AC":
            self.objectType = type(PIAttributeCategory())
        elif self.marker == "AT":
            self.objectType = type(PIAttributeTemplate())
        elif self.marker == "RD":
            self.objectType = type(PIAssetDatabase())
        elif self.marker == "Em":
            self.objectType = type(PIElement())
        elif self.marker == "EC":
            self.objectType = type(PIElementCategory())
        elif self.marker == "ET":
            self.objectType = type(PIElementTemplate())
        elif self.marker == "MS":
            self.objectType = type(PIEnumerationSet())
        elif self.marker == "MV":
            self.objectType = type(PIEnumerationValue())
        elif self.marker == "Fm":
            self.objectType = type(PIEventFrame())
        elif self.marker == "TR":
            self.objectType = type(PITimeRule())
        elif self.marker == "TP":
            self.objectType = type(PITimeRulePlugIn())
        elif self.marker == "SI":
            self.objectType = type(PISecurityIdentity())
        elif self.marker == "SM":
            self.objectType = type(PISecurityMapping())
        elif self.marker == "Bl":
            self.objectType = type(PITable())
        elif self.marker == "BC":
            self.objectType = type(PITableCategory())
        elif self.marker == "DP":
            self.objectType = type(PIPoint())
        elif self.marker == "DS":
            self.objectType = type(PIDataServer())
        elif self.marker == "RS":
            self.objectType = type(PIAssetServer())
        elif self.marker == "Ut":
            self.objectType = type(PIUnit())
        elif self.marker == "UC":
            self.objectType = type(PIUnitClass())
        return

    def process_guids_and_paths(self, web_id):
        if isinstance(PIAnalysis(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIAnalysisCategory(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIAnalysisTemplate(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIAnalysisRule(), self.objectType):
            self.process_guids_and_paths2(web_id, True, WebIdStringType.ThreeGuids, False)
        elif isinstance(PIAnalysisRulePlugIn(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIAttribute(), self.objectType):
            self.process_guids_and_paths2(web_id, True, WebIdStringType.ThreeGuids, False)
        elif isinstance(PIAttributeCategory(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIAttributeTemplate(), self.objectType):
            self.process_guids_and_paths2(web_id, True, WebIdStringType.ThreeGuids, False)
            self.owner_type = type(PIElementTemplate())
        elif isinstance(PIAssetDatabase(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIElement(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIElementCategory(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIElementTemplate(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIEnumerationSet(), self.objectType):
            self.process_guids_and_paths2(web_id, True, WebIdStringType.TwoGuids, False)
        elif isinstance(PIEnumerationValue(), self.objectType):
            self.process_guids_and_paths2(web_id, True, WebIdStringType.ThreeGuids, False)
        elif isinstance(PIEventFrame(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PITimeRule(), self.objectType):
            self.process_guids_and_paths2(web_id, True, WebIdStringType.ThreeGuids, False)
        elif isinstance(PITimeRulePlugIn(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PISecurityIdentity(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PISecurityMapping(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PITable(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PITableCategory(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIPoint(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, True)
        elif isinstance(PIDataServer(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.OneGuid, False)
        elif isinstance(PIAssetServer(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.OneGuid, False)
        elif isinstance(PIUnit(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)
        elif isinstance(PIUnitClass(), self.objectType):
            self.process_guids_and_paths2(web_id, False, WebIdStringType.TwoGuids, False)

    def process_guids_and_paths2(self, web_id, has_marker_owner, web_id_string_type, use_point):
        rest_web_id = web_id[4:]
        if has_marker_owner:
            self.marker_owner = rest_web_id[0:1]
            self.process_owner_type(self.marker_owner)
            rest_web_id = rest_web_id[1:]

        if (self.web_id_type == WebIdType.Full) or (self.web_id_type == WebIdType.IDOnly):
            encoded_server_id = rest_web_id[0:22]
            self.server_id = self.decode_guid(encoded_server_id)
            rest_web_id = rest_web_id[22:]

            if web_id_string_type == WebIdStringType.ThreeGuids:
                encoded_owner_id = rest_web_id[0:22]
                self.owner_id = self.decode_guid(encoded_owner_id)
                rest_web_id = rest_web_id[22:]

            if (web_id_string_type == WebIdStringType.ThreeGuids) or (web_id_string_type == WebIdStringType.TwoGuids):
                if use_point:
                    encoded_object_id = rest_web_id[0:6]
                    self.point_id = self.decode_int(encoded_object_id)
                    rest_web_id = rest_web_id[6:]
                else:
                    encoded_object_id = rest_web_id[0:22]
                    self.object_id = self.decode_guid(encoded_object_id)
                    rest_web_id = rest_web_id[22:]

        if (self.web_id_type == WebIdType.Full) or (self.web_id_type == WebIdType.PathOnly):
            encoded_path = rest_web_id
            self.path = self.decode_string(encoded_path)
        return


    def process_owner_type(self, market_owner):
        if self.marker_owner == "R":
            self.owner_type = type(PIAssetServer())
        elif self.marker_owner == "D":
            self.owner_type = type(PIDataServer())
        elif self.marker_owner == "X":
            self.owner_type = type(PIAnalysis())
        elif self.marker_owner == "T":
            self.owner_type = type(PIAnalysisTemplate())
        elif self.marker_owner == "E":
            self.owner_type = type(PIElement())
        elif self.marker_owner == "F":
            self.owner_type = type(PIEventFrame())

    def decode(self, value):
        decodestring = value.replace('-', '+').replace('_', '/')
        pad_needed = (4 - (len(decodestring) % 4)) % 4
        for i in range(0, pad_needed):
            decodestring = decodestring + '='
        bytes = base64.b64decode(decodestring)
        return bytes;


    def decode_guid(self, encoded_object_id):
        bytes = self.decode(encoded_object_id)
        guid = self.hex_to_guid(bytes.hex())
        return guid

    def decode_string(self, encoded_path):
        bytes = self.decode(encoded_path)
        str = bytes.decode('utf-8')
        return str

    def decode_int(self, encoded_object_id):
        bytes = self.decode(encoded_object_id)
        intgr = struct.unpack('<L', bytes)[0]
        return intgr

    def revert_array(self, bytes):
        b = bytearray(bytes)
        b.reverse()
        return b



    def hex_to_guid(self, hex):
        """Convert a hex string to a Microsoft GUID"""
        h = binascii.unhexlify(hex)

        # The Microsoft GUID format has four named fields.  Split the
        # bytes into the four fields.  Since the fields are big-endian,
        # we need to reverse the stream returned by unhexlify().
        # https://msdn.microsoft.com/en-us/library/aa373931(VS.85).aspx
        data1 = self.revert_array(h[0:4])
        data2 = self.revert_array(h[4:6])
        data3 = self.revert_array(h[6:8])
        data4a = h[8:10]
        data4b = h[10:]

        components = [data1, data2, data3, data4a, data4b]

        hex_bytes = [binascii.hexlify(d) for d in components]
        decoded = [bytes.decode(b) for b in hex_bytes]

        return '-'.join(decoded)