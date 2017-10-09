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


import  unittest
from osisoft.pidevclub.piwebapi.models import PIAnalysis, PIItemsStreamValues, PIStreamValues, PITimedValue
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException



class TestMain(unittest.TestCase):

    def getPIWebApiClient(self):
		return PIWebApiClient("https://webserver/piwebapi", False, "username", "password", True)



    def test_getHome(self):
        client = self.getPIWebApiClient()
        landing = client.home.get()
        pass


    def test_getDataServer(self):
        client = self.getPIWebApiClient()
        dataServer = client.dataServer.get_by_path("\\\\JUPITER001", None);
        pass


    def test_getMultiplePoints(self):
        client = self.getPIWebApiClient()
        dataServers = client.dataServer.list(selected_fields=None)
        point1 = client.point.get_by_path("\\\\JUPITER001\\sinusoid", None)
        point2 = client.point.get_by_path("\\\\JUPITER001\\cdt158", None)
        point3 = client.point.get_by_path("\\\\JUPITER001\\sinusoidu", None)

        pass


    def test_getDataInBulkTest(self):
        client = self.getPIWebApiClient()
        point1 = client.point.get_by_path("\\\\JUPITER001\\sinusoid", None);
        point2 = client.point.get_by_path("\\\\JUPITER001\\cdt158", None);
        point3 = client.point.get_by_path("\\\\JUPITER001\\sinusoidu", None);

        webIds = list()
        webIds.append(point1.web_id);
        webIds.append(point2.web_id);
        webIds.append(point3.web_id);

        piItemsStreamValues = client.streamSet.get_recorded_ad_hoc(webIds, None, "*", None, True, 1000, None, "*-3d",
                                                                   None);
        pass


    def test_getElement(self):
        client = self.getPIWebApiClient()
        myElement = client.element.get_by_path("\\\\JUPITER001\\Vitens\\Vitens", None)
        pass


    def test_getAttribute(self):
        client = self.getPIWebApiClient()
        attribute = client.attribute.get_by_path("\\\\JUPITER001\\Universities\\UC Davis\\Buildings|Campus Average EUI",
                                                 "Name")
        pass

    def test_getExceptionError(self):
        client = self.getPIWebApiClient()
        try:
            point1 = client.point.get_by_path("\\\\JUPITER001\\sinusoid12334322", None)
        except ApiException as e:
            print(e);
            errorMsg = e.error['Errors'][0]
            if "Not found" not in errorMsg:
                raise Exception('Unexpected exception')
        pass


    def test_updateValuesInBulk(self):
        client = self.getPIWebApiClient()
        point1 = client.point.get_by_path("\\\\JUPITER001\\sinusoid", None);
        point2 = client.point.get_by_path("\\\\JUPITER001\\cdt158", None);
        point3 = client.point.get_by_path("\\\\JUPITER001\\sinusoidu", None);
        streamValuesItems = PIItemsStreamValues()
        streamValue1 = PIStreamValues()
        streamValue2 = PIStreamValues()
        streamValue3 = PIStreamValues()
        value1 = PITimedValue()
        value2 = PITimedValue()
        value3 = PITimedValue()
        value4 = PITimedValue()
        value5 = PITimedValue()
        value6 = PITimedValue()
        value1.value = 2
        value1.timestamp = ("*-1d")
        value2.value = 3
        value2.timestamp = ("*-2d")
        value3.value = 4
        value3.timestamp = ("*-1d")
        value4.value = 5
        value4.timestamp = ("*-2d")
        value5.value = 6
        value5.timestamp = ("*-1d")
        value6.value = 7
        value6.timestamp = ("*-2d")

        streamValue1.web_id = point1.web_id
        streamValue2.web_id = point2.web_id
        streamValue3.web_id = point3.web_id

        values1 = list()
        values1.append(value1)
        values1.append(value2)
        streamValue1.items = values1

        values2 = list()
        values2.append(value3)
        values2.append(value4)
        streamValue2.items = values2

        values3 = list()
        values3.append(value5)
        values3.append(value6)
        streamValue3.items = values3

        streamValues = list()
        streamValues.append(streamValue1)
        streamValues.append(streamValue2)
        streamValues.append(streamValue3)
        response = client.streamSet.update_values_ad_hoc_with_http_info(streamValues, None, None)
        pass



if __name__ == '__main__':
    unittest.main()
