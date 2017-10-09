# TimeRulePlugInApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](TimeRulePlugInApi.md#getbypath) | **GET** /timeruleplugins | Retrieve a Time Rule Plug-in by path.
[**get**](TimeRulePlugInApi.md#get) | **GET** /timeruleplugins/{webId} | Retrieve a Time Rule Plug-in.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve a Time Rule Plug-in by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the Time Rule Plug-in.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PITimeRulePlugIn**](../models/PITimeRulePlugIn.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve a Time Rule Plug-in.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Time Rule Plug-in.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PITimeRulePlugIn**](../models/PITimeRulePlugIn.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
