PI Web API client library for Python (2017 R2)
===

## Overview
This repository has the source code package of the PI Web API client libraries for Python. This version was developed on top of the PI Web API 2017 R2 swagger specification.

## Requirements

 - PI Web API 2017 R2 installed within your domain using Kerberos or Basic Authentication. If you are using an older version, some methods might not work.
 - Python 2.7 and 3.4+

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

This library was tested using PyCharm 2018.1.2.

## Documentation

All classes and methods are described on the [DOCUMENTATION](DOCUMENTATION.md). 

## Notes

 - Is is highly recommended to turn debug mode on in case you are using PI Web API 2017 R2+ in order to receive more detailed exception errors. This can be achieved by creating or editing the DebugMode attribute's value to TRUE from the System Configuration element.
 - The X-Requested-With header is added to work with CSRF defences.
 
## Examples

Please check the [test_main.py](/test/test_main.py) from this repository. Below there are also code snippets written in Python for you to get started using this library:


### Create an instance of the PI Web API top level object.

#### Basic Authentication
```python
    from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
    client = PIWebApiClient("https://test.osisoft.com/piwebapi", False, "username", "password")  
``` 

#### Kerberos Authentication
```python
    from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
    client = PIWebApiClient("https://test.osisoft.com/piwebapi", True)  
``` 




### Retrieving PI data to an Python pandas data frame


```python
    df1 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*")
    df2 = client.data.get_interpolated_values("pi:\\PISRV1\\sinusoid", start_time="*-1d", end_time="*", interval="1h")
    df3 = client.data.get_plot_values("pi:\\\\PISRV1\\sinusoid", end_time="*", intervals=15, start_time= "*-1d")
    df4 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*", selected_fields="items.value;items.timestamp")
	
    paths  = ["pi:\\\\PISRV1\\sinusoid", "pi:\\\\PISRV1\\sinusoidu", "pi:\\\\PISRV1\\cdt158"];
    dfs1 = client.data.get_multiple_recorded_values(paths, start_time="*-1d", end_time= "*")
    dfs2 = client.data.get_multiple_interpolated_values(paths, start_time="*-1d", end_time="*", interval="1h")
    dfs3 = client.data.get_multiple_plot_values(paths,  start_time="*-1d", end_time="*", intervals="14")
    dfs4 = client.data.get_multiple_recorded_values(paths, start_time="*-1d", end_time="*", selected_fields="items.items.value;items.items.timestamp")
```

The path from the methods above should start with "pi:" (if your stream is a PI Point) or "af:" (if your stream is an AF attribute).




### Get the PI Data Archive WebId

```python
    dataServer = client.dataServer.get_by_path("\\\\PISRV1");
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
    point1 = client.point.get_by_path("\\\\PISRV1\\sinusoid");
    point2 = client.point.get_by_path("\\\\PISRV1\\cdt158");
    point3 = client.point.get_by_path("\\\\PISRV1\\sinusoidu");
```

### Get recorded values in bulk using the StreamSet/GetRecordedAdHoc

```python
    webIds = list()
    webIds.append(point1.web_id);
    webIds.append(point2.web_id);
    webIds.append(point3.web_id);
    piItemsStreamValues = client.streamSet.get_recorded_ad_hoc(webIds, start_time="*-3d", end_time="*",
                                                                   include_filtered_values=True, max_count=1000)
            
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
    response = client.streamSet.update_values_ad_hoc_with_http_info(streamValues)
```


### Get an element and an attribute by path

```python
    element = client.element.get_by_path("\\\\PISRV1\\City Bikes\\(TO)BIKE")
    attribute = client.attribute.get_by_path("\\\\PISRV1\\City Bikes\\(TO)BIKE\\01. Certosa   P.le Avis|Empty Slots",
                                                 selected_fields="Name")     
```





## Licensing
Copyright 2018 OSIsoft, LLC.

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
