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
        piDataServerWebId = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1", type(PIDataServer()), None)
        point1webId = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\SINUSOID", type(PIPoint()))
        point2webId = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\CDT158", type(PIPoint()))
        point3webId = client.webIdHelper.generate_web_id_by_path("\\\\PISRV1\\SINUSOIDU", type(PIPoint()))
        piAttributeWebId = client.webIdHelper.generate_web_id_by_path(
            "\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building|Electricity Totalizer",
            type(PIAttribute()), type(PIElement()))

        piElementWebId = client.webIdHelper.generate_web_id_by_path(
            "\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building", type(PIElement()), None)



        piDataServer = client.dataServer.get(piDataServerWebId)
        piAttribute = client.attribute.get(piAttributeWebId)
        piElement = client.element.get(piElementWebId)



        piAttributeWebIdInfo = client.webIdHelper.get_web_id_info(piAttributeWebId)
        piElementWebIdInfo = client.webIdHelper.get_web_id_info(piElementWebId)
        piDataServerWebIdInfo = client.webIdHelper.get_web_id_info(piDataServerWebId)

if __name__ == '__main__':
    unittest.main()
