# coding: utf-8

"""
	Copyright 2017 OSIsoft, LLC
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



from osisoft.pidevclub.piwebapi import api_client
from osisoft.pidevclub.piwebapi.api.batch_api import BatchApi
from osisoft.pidevclub.piwebapi.api.home_api import HomeApi
from osisoft.pidevclub.piwebapi.api.analysis_api import AnalysisApi
from osisoft.pidevclub.piwebapi.api.analysis_category_api import AnalysisCategoryApi
from osisoft.pidevclub.piwebapi.api.analysis_rule_plug_in_api import AnalysisRulePlugInApi
from osisoft.pidevclub.piwebapi.api.analysis_rule_api import AnalysisRuleApi
from osisoft.pidevclub.piwebapi.api.analysis_template_api import AnalysisTemplateApi
from osisoft.pidevclub.piwebapi.api.asset_database_api import AssetDatabaseApi
from osisoft.pidevclub.piwebapi.api.asset_server_api import AssetServerApi
from osisoft.pidevclub.piwebapi.api.attribute_category_api import AttributeCategoryApi
from osisoft.pidevclub.piwebapi.api.attribute_api import AttributeApi
from osisoft.pidevclub.piwebapi.api.attribute_template_api import AttributeTemplateApi
from osisoft.pidevclub.piwebapi.api.attribute_trait_api import AttributeTraitApi
from osisoft.pidevclub.piwebapi.api.calculation_api import CalculationApi
from osisoft.pidevclub.piwebapi.api.channel_api import ChannelApi
from osisoft.pidevclub.piwebapi.api.data_api import DataApi
from osisoft.pidevclub.piwebapi.api.data_server_api import DataServerApi
from osisoft.pidevclub.piwebapi.api.element_category_api import ElementCategoryApi
from osisoft.pidevclub.piwebapi.api.element_api import ElementApi
from osisoft.pidevclub.piwebapi.api.element_template_api import ElementTemplateApi
from osisoft.pidevclub.piwebapi.api.enumeration_set_api import EnumerationSetApi
from osisoft.pidevclub.piwebapi.api.enumeration_value_api import EnumerationValueApi
from osisoft.pidevclub.piwebapi.api.event_frame_api import EventFrameApi
from osisoft.pidevclub.piwebapi.api.point_api import PointApi
from osisoft.pidevclub.piwebapi.api.security_identity_api import SecurityIdentityApi
from osisoft.pidevclub.piwebapi.api.security_mapping_api import SecurityMappingApi
from osisoft.pidevclub.piwebapi.api.stream_api import StreamApi
from osisoft.pidevclub.piwebapi.api.stream_set_api import StreamSetApi
from osisoft.pidevclub.piwebapi.api.system_api import SystemApi
from osisoft.pidevclub.piwebapi.api.configuration_api import ConfigurationApi
from osisoft.pidevclub.piwebapi.api.table_category_api import TableCategoryApi
from osisoft.pidevclub.piwebapi.api.table_api import TableApi
from osisoft.pidevclub.piwebapi.api.time_rule_plug_in_api import TimeRulePlugInApi
from osisoft.pidevclub.piwebapi.api.time_rule_api import TimeRuleApi
from osisoft.pidevclub.piwebapi.api.unit_class_api import UnitClassApi
from osisoft.pidevclub.piwebapi.api.unit_api import UnitApi
from osisoft.pidevclub.piwebapi.web_id.web_id_helper import WebIdHelper




class PIWebApiClient(object):
    __baseUrl = None
    __useKerberos = True
    __username = None
    __password = None
    __verifySsl = True
    __config = None
    def __init__(self, baseUrl, useKerberos = True, username = None, password = None, verifySsl = True):
        self.__baseUrl = baseUrl
        self.__useKerberos = useKerberos
        self.__username = username
        self.__password = password
        self.__verifySsl = verifySsl
        self.__api_client = api_client.ApiClient(self.__baseUrl, self.__verifySsl)
        if (self.__useKerberos == True):
            self.__api_client.set_kerberos_auth()
        else:
            self.__api_client.set_basic_auth(self.__username, self.__password)

        self.__homeApi = HomeApi(self.__api_client)
        self.__analysisApi = AnalysisApi(self.__api_client)
        self.__analysisCategoryApi = AnalysisCategoryApi(self.__api_client)
        self.__analysisRulePlugInApi = AnalysisRulePlugInApi(self.__api_client)
        self.__analysisRuleApi = AnalysisRuleApi(self.__api_client)
        self.__analysisTemplateApi = AnalysisTemplateApi(self.__api_client)
        self.__assetDatabaseApi = AssetDatabaseApi(self.__api_client)
        self.__assetServerApi = AssetServerApi(self.__api_client)
        self.__attributeCategoryApi = AttributeCategoryApi(self.__api_client)
        self.__attributeApi = AttributeApi(self.__api_client)
        self.__attributeTemplateApi = AttributeTemplateApi(self.__api_client)
        self.__attributeTraitApi = AttributeTraitApi(self.__api_client)
        self.__calculationApi = CalculationApi(self.__api_client)
        self.__batchApi = BatchApi(self.__api_client)
        self.__channelApi = ChannelApi(self.__api_client)
        self.__dataServerApi = DataServerApi(self.__api_client)
        self.__elementCategoryApi = ElementCategoryApi(self.__api_client)
        self.__elementApi = ElementApi(self.__api_client)
        self.__elementTemplateApi = ElementTemplateApi(self.__api_client)
        self.__enumerationSetApi = EnumerationSetApi(self.__api_client)
        self.__enumerationValueApi = EnumerationValueApi(self.__api_client)
        self.__eventFrameApi = EventFrameApi(self.__api_client)
        self.__pointApi = PointApi(self.__api_client)
        self.__securityIdentityApi = SecurityIdentityApi(self.__api_client)
        self.__securityMappingApi = SecurityMappingApi(self.__api_client)
        self.__streamApi = StreamApi(self.__api_client)
        self.__streamSetApi = StreamSetApi(self.__api_client)
        self.__systemApi = SystemApi(self.__api_client)
        self.__configurationApi = ConfigurationApi(self.__api_client)
        self.__tableCategoryApi = TableCategoryApi(self.__api_client)
        self.__tableApi = TableApi(self.__api_client)
        self.__timeRulePlugInApi = TimeRulePlugInApi(self.__api_client)
        self.__timeRuleApi = TimeRuleApi(self.__api_client)
        self.__unitClassApi = UnitClassApi(self.__api_client)
        self.__unitApi = UnitApi(self.__api_client)
        self.__dataApi = DataApi(self.__streamApi, self.__streamSetApi,  self.__attributeApi,  self.__pointApi )
        self.__web_id_helper = WebIdHelper()



    @property
    def api_client(self):
        return self.__api_client
    @property
    def baseUrl(self):
        return self.__baseUrl

    @property
    def useKerberos(self):
        return self.__useKerberos

    @property
    def verifySsl(self):
        return self.__verifySsl

    @property
    def home(self):
      return self.__homeApi

    @property
    def analysis(self):
        return self.__analysisApi

    @property
    def analysisCategory(self):
        return self.__analysisCategoryApi

    @property
    def analysisRulePlugIn(self):
     return self.__analysisRulePlugInApi

    @property
    def analysisRule(self):
        return self.__analysisRuleApi

    @property
    def analysisTemplate(self):
        return self.__analysisTemplateApi

    @property
    def assetDatabase(self):
        return self.__assetDatabaseApi
    @property
    def assetServer(self):
        return self.__assetServerApi
    @property
    def attributeCategory(self):
        return self.__attributeCategoryApi

    @property
    def attribute(self):
        return self.__attributeApi

    @property
    def attributeTemplate(self):
        return self.__attributeTemplateApi

    @property
    def attributeTrait(self):
        return self.__attributeTraitApi

    @property
    def batch(self):
        return self.__batchApi;

    @property
    def calculation(self):
        return self.__calculationApi

    @property
    def channel(self):
        return self.__channelApi

    @property
    def data(self):
        return self.__dataApi

    @property
    def dataServer(self):
        return self.__dataServerApi

    @property
    def elementCategory(self):
        return self.__elementCategoryApi

    @property
    def element(self):
        return self.__elementApi

    @property
    def elementTemplate(self):
        return self.__elementTemplateApi

    @property
    def enumerationSet(self):
        return self.__enumerationSetApi

    @property
    def enumerationValue(self):
        return self.__enumerationValueApi

    @property
    def eventFrame(self):
     return self.__eventFrameApi

    @property
    def point(self):
        return self.__pointApi

    @property
    def securityIdentity(self):
        return self.__securityIdentityApi

    @property
    def securityMapping(self):
        return self.__securityMappingApi

    @property
    def stream(self):
        return self.__streamApi

    @property
    def streamSet(self):
        return self.__streamSetApi

    @property
    def system(self):
        return self.__systemApi

    @property
    def configuration(self):
     return self.__configurationApi

    @property
    def tableCategory(self):
        return self.__tableCategoryApi

    @property
    def table(self):
     return self.__tableApi

    @property
    def timeRulePlugIn(self):
     return self.__timeRulePlugInApi

    @property
    def timeRule(self):
     return self.__timeRuleApi

    @property
    def unitClass(self):
        return self.__unitClassApi

    @property
    def unit(self):
        return self.__unitApi

    @property
    def webIdHelper(self):
        return self.__web_id_helper