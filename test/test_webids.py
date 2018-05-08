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
from osisoft.pidevclub.piwebapi.models import PIAnalysis, PIItemsStreamValues, PIStreamValues, PITimedValue, PIPoint, \
    PIDataServer, PIElement, PIAttribute
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException



class TestMain(unittest.TestCase):

    def getPIWebApiClient(self):
        return PIWebApiClient("https://devdata.osisoft.com/piwebapi", False, "webapiuser", "!try3.14webapi!", True)

    def test_webIdInfo(self):
        client = self.getPIWebApiClient()
        point1 = client.point.get_by_path("\\\\PISRV1\\CDF144_Repeated24h_forward", None, None)
        web_id_info1 = client.webIdHelper.get_web_id_info(point1.web_id)
        print(web_id_info1)
        pass

    def test_generateWebIdInfo(self):
        client = self.getPIWebApiClient()
        path = "\\\\PISRV1\\CDF144_Repeated24h_forward"
        web_id1 = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\CDF144_Repeated24h_forward", type(PIPoint()))
        pt = client.point.get(selected_fields="WebId", web_id=web_id1)
        web_id2 = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1", type(PIDataServer()))
        ds = client.dataServer.get(web_id2)

        pass

    def test_more_tests(self):
        client = self.getPIWebApiClient()
        pi_data_server_web_id = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1", type(PIDataServer()), None)
        point1_web_id = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\SINUSOID", type(PIPoint()))
        point2_web_id = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\CDT158", type(PIPoint()))
        point3_web_id = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\SINUSOIDU", type(PIPoint()))
        pi_attribute_web_id = client.webIdHelper.generate_web_id_by_path(
            "\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building|Electricity Totalizer",
            type(PIAttribute()), type(PIElement()))

        pi_element_web_id = client.webIdHelper.generate_web_id_by_path(
            "\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building", type(PIElement()), None)

        pi_data_server = client.dataServer.get(pi_data_server_web_id)
        pi_attribute = client.attribute.get(pi_attribute_web_id)
        pi_element = client.element.get(pi_element_web_id)

        pi_attribute_web_id_info = client.webIdHelper.get_web_id_info(pi_attribute_web_id)
        pi_element_web_id_info = client.webIdHelper.get_web_id_info(pi_element_web_id)
        pi_dataServer_web_id_info = client.webIdHelper.get_web_id_info(pi_data_server_web_id)

if __name__ == '__main__':
    unittest.main()
