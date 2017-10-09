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

import unittest
from osisoft.pidevclub.piwebapi.models import PIAnalysis, PIItemsStreamValues, PIStreamValues, PITimedValue
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException


class TestData(unittest.TestCase):
    def getPIWebApiClient(self):
        return PIWebApiClient("https://webserver/piwebapi", False, "username", "password", True)


    def test_data_convertPathToWebId(self):
        client = self.getPIWebApiClient()
        webId = client.data.convert_path_to_web_id("pi:\\JUPITER001\sinusoid")
        print(webId)
        pass

    def test_data_convertPathToWebIds(self):
        client = self.getPIWebApiClient()
        paths = []
        paths.append("pi:\\JUPITER001\sinusoid")
        paths.append("pi:\\JUPITER001\sinusoidu")
        paths.append("pi:\\JUPITER001\cdt158")
        webIds = client.data.convert_paths_to_web_ids(paths)
        print(webIds)
        pass

    def test_data_recorded(self):
        client = self.getPIWebApiClient()

        df1 = client.data.get_recorded_values("pi:\\\\JUPITER001\\sinusoid",None, None, "*", None, None, None, None, "*-1d", None)
        df2 = client.data.get_recorded_values("pi:\\\\JUPITER001\\sinusoidu", None, None, "*", None, None, None, None,"*-10d", None)
        df3 = client.data.get_recorded_values("pi:\\\\JUPITER001\\cdt158", None, None, "*-9d", None, None, None, None, "*-10d", None)
        df4 = client.data.get_recorded_values("af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH", None, None, "*-9d", None, None, None, None, "*-10d", None)

        df5 = client.data.get_interpolated_values("pi:\\JUPITER001\\sinusoid",None, "*", None, None, "1h", None, "*-1d", None)
        df6 = client.data.get_interpolated_values("pi:\\JUPITER001\\sinusoidu",None, "*", None, None, "2h", None, "*-1d", None)
        df7 = client.data.get_interpolated_values("pi:\\JUPITER001\\cdt158",None, "*", None, None, "3h", None, "*-1d", None)
        df8 = client.data.get_interpolated_values("af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH", None, "*", None, None, "3h", None, "*-20d", None)



        df9 = client.data.get_plot_values("pi:\\\\JUPITER001\\sinusoid", None, "*", 15, None, "*-1d", None)
        df10 = client.data.get_plot_values("pi:\\\\JUPITER001\\sinusoidu", None, "*", 10, None, "*-3d", None)
        df11 = client.data.get_plot_values("pi:\\\\JUPITER001\\cdt158", None, "*", 20, None, "*-2d", None)
        df12 = client.data.get_plot_values("af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH", None, "*", 20, None, "*-40d", None)
        pass

    def test_data_multiple_recorded(self):
        client = self.getPIWebApiClient()
        dfs1 = client.data.get_multiple_recorded_values(["pi:\\\\JUPITER001\\sinusoid", "pi:\\\\JUPITER001\\sinusoidu", "pi:\\\\JUPITER001\\cdt158", "af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH"],None, "*", None, None, None, None, "*-1d", None)
        dfs2 = client.data.get_multiple_interpolated_values(["pi:\\\\JUPITER001\\sinusoid", "pi:\\\\JUPITER001\\sinusoidu", "pi:\\\\JUPITER001\\cdt158", "af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH"], "*", None, None, "1d", None, "*-5d", None)

        dfs3 = client.data.get_multiple_plot_values(["pi:\\\\JUPITER001\\sinusoid", "pi:\\\\JUPITER001\\sinusoidu", "pi:\\\\JUPITER001\\cdt158", "af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH"], "*", 10, None, "*-1d", None)

        pass


if __name__ == '__main__':
    unittest.main()
