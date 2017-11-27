PI Web API Client libraries for Python
===

## Overview
This repository has the source code package of the PI Web API Client libraries for Python.

## Requirements.

Python 2.7 and 3.4+


## Installation
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/osimloeff/PI-Web-API-Client-Python.git
```
You may need to run `pip` with root permission: `sudo pip install git+https://github.com/osimloeff/PI-Web-API-Client-Python.git`. If you are using Windows, remember to open the command prompt running as administrator. You must have Git installed on your machine.

Then import the package:
```python
import osisoft.pidevclub.piwebapi 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osisoft.pidevclub.piwebapi
```

This library was tested using PyCharm 2017.1.5 and Anaconda3 5.0.0

## Documentation

All classes and methods are described on the [DOCUMENTATION](DOCUMENTATION.md). 

 
## Examples

Please check the [test_main.py](/test/test_main.py) from this repository. Below there are also code snippets written in Python for you to get started using this library:


### Create an instance of the PI Web API top level object.

```python
    from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
    client = PIWebApiClient("https://test.osisoft.com/piwebapi", False, "username", "password", True)  
``` 

Only Basic Authentication is available in this version. Therefore, the variable useKerberos should always be False. Do not forget to set the username and password accordingly.


### Retrieving PI data to an Python pandas data frame


```python
    df1 = client.data.get_recorded_values("pi:\\\\JUPITER001\\cdt158", None, None, "*-9d", None, None, None, None, "*-10d", None)df4 = client.data.get_multiple_recorded_values(["pi:\\JUPITER001\sinusoid", "pi:\\JUPITER001\sinusoidu", "pi:\\JUPITER001\cdt158"],None, "*", None, None, None, None, "*-1d", None)
    df2 = client.data.get_interpolated_values("pi:\\JUPITER001\\sinusoidu",None, "*", None, None, "2h", None, "*-1d", None)
    df3 = client.data.get_plot_values("pi:\\\\JUPITER001\\sinusoidu", None, "*", 10, None, "*-3d", None)
    df4 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", None, None, "*", None, None, None, "items.value;items.timestamp", "*-1d", None)
    df5 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", None, None, "*", None, None, None, "items.good;items.questionable;items.substituted", "*-1d", None)
	dfs1 = client.data.get_multiple_recorded_values(["pi:\\\\JUPITER001\\sinusoid", "pi:\\\\JUPITER001\\sinusoidu", "pi:\\\\JUPITER001\\cdt158", "af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH"],None, "*", None, None, None, None, "*-1d", None)
    dfs2 = client.data.get_multiple_interpolated_values(["pi:\\\\JUPITER001\\sinusoid", "pi:\\\\JUPITER001\\sinusoidu", "pi:\\\\JUPITER001\\cdt158", "af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH"], "*", None, None, "1d", None, "*-5d", None)
    dfs3 = client.data.get_multiple_plot_values(["pi:\\\\JUPITER001\\sinusoid", "pi:\\\\JUPITER001\\sinusoidu", "pi:\\\\JUPITER001\\cdt158", "af:\\\\JUPITER001\\Vitens\\Vitens\\Friesland province\\01 Production sites\\Production Site Noordbergum\\Distribution\\Quality|pH"], "*", 10, None, "*-1d", None)
    dfs4 = client.data.get_multiple_recorded_values(paths, None, "*", None, None, None, "items.items.value;items.items.timestamp", "*-1d", None)
    dfs5 = client.data.get_multiple_interpolated_values(paths, "*", None, None, "1h", "items.items.value;items.items.timestamp", "*-5d", None)
```

The path from the methods above should start with "pi:" (if your stream is a PI Point) or "af:" (if your stream is an AF attribute).




### Get the PI Data Archive WebId

```python
    dataServer = client.dataServer.get_by_path("\\\\JUPITER001", None);
```

### Create a new PI Point

```python
    newPoint = PIPoint()
    newPoint.name  = "SINUSOID_TEST"
    newPoint.descriptor = "Test PI Point for Python PI Web API Client"
    newPoint.point_class = "classic"
    newPoint.point_type = "float32"
    newPoint.future = False
    res = client.dataServer.create_point_with_http_info(dataServer.web_id, newPoint);         
```

### Get PI Points WebIds

```python
    point1 = client.point.get_by_path("\\\\JUPITER001\\sinusoid", None)
    point2 = client.point.get_by_path("\\\\JUPITER001\\cdt158", None)
    point3 = client.point.get_by_path("\\\\JUPITER001\\sinusoidu", None)
```

### Get recorded values in bulk using the StreamSet/GetRecordedAdHoc

```python
    webIds = list()
    webIds.append(point1.web_id);
    webIds.append(point2.web_id);
    webIds.append(point3.web_id);
    piItemsStreamValues = client.streamSet.get_recorded_ad_hoc(webIds, None, "*", None, True, 1000, None, "*-3d", None);
            
```

### Send values in bulk using the StreamSet/UpdateValuesAdHoc

```python
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
```


### Get an element and an attribute by path

```python
    element = client.element.get_by_path("\\\\JUPITER001\\Universities\\UC Davis", None)
    attribute = client.attribute.get_by_path("\\\\JUPITER001\\Universities\\UC Davis\\Buildings|Campus Average EUI", "Name")
           
```





## Licensing
Copyright 2017 OSIsoft, LLC.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
Please see the file named [LICENSE.md](LICENSE.md).
