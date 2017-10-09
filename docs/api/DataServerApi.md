# DataServerApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**list**](DataServerApi.md#list) | **GET** /dataservers | Retrieve a list of Data Servers known to this service.
[**get_by_name**](DataServerApi.md#getbyname) | **GET** /dataservers#name | Retrieve a Data Server by name.
[**get_by_path**](DataServerApi.md#getbypath) | **GET** /dataservers#path | Retrieve a Data Server by path.
[**get**](DataServerApi.md#get) | **GET** /dataservers/{webId} | Retrieve a Data Server.
[**get_enumeration_sets**](DataServerApi.md#getenumerationsets) | **GET** /dataservers/{webId}/enumerationsets | Retrieve enumeration sets for given Data Server.
[**create_enumeration_set**](DataServerApi.md#createenumerationset) | **POST** /dataservers/{webId}/enumerationsets | Create an enumeration set on the Data Server.
[**get_points**](DataServerApi.md#getpoints) | **GET** /dataservers/{webId}/points | Retrieve a list of points on a specified Data Server.
[**create_point**](DataServerApi.md#createpoint) | **POST** /dataservers/{webId}/points | Create a point in the specified Data Server.


# **list**
> list('selected_fields')

Retrieve a list of Data Servers known to this service.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsDataServer**](../models/PIItemsDataServer.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_by_name**
> get_by_name('name', 'selected_fields')

Retrieve a Data Server by name.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the server.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIDataServer**](../models/PIDataServer.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve a Data Server by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the server. Note that the path supplied to this method must be of the form '\\servername'.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIDataServer**](../models/PIDataServer.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve a Data Server.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIDataServer**](../models/PIDataServer.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_enumeration_sets**
> get_enumeration_sets('web_id', 'selected_fields')

Retrieve enumeration sets for given Data Server.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsEnumerationSet**](../models/PIItemsEnumerationSet.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_enumeration_set**
> create_enumeration_set('web_id', 'enumeration_set')

Create an enumeration set on the Data Server.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server on which to create the enumeration set.. | [required]
 **enumeration_set** | **PIEnumerationSet**| The new enumeration set definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_points**
> get_points('web_id', 'max_count', 'name_filter', 'selected_fields', 'start_index')

Retrieve a list of points on a specified Data Server.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server.. | [required]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| A query string for filtering by point name. The default is no filter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is '0'.. | [optional]


### Return type

[**PIItemsPoint**](../models/PIItemsPoint.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_point**
> create_point('web_id', 'point_d_t_o')

Create a point in the specified Data Server.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the server.. | [required]
 **point_d_t_o** | **PIPoint**| The new point definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
