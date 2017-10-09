# AnalysisRuleApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](AnalysisRuleApi.md#getbypath) | **GET** /analysisrules | Retrieve an Analysis Rule by path.
[**get**](AnalysisRuleApi.md#get) | **GET** /analysisrules/{webId} | Retrieve an Analysis Rule.
[**update**](AnalysisRuleApi.md#update) | **PATCH** /analysisrules/{webId} | Update an Analysis Rule by replacing items in its definition.
[**delete**](AnalysisRuleApi.md#delete) | **DELETE** /analysisrules/{webId} | Delete an Analysis Rule.
[**get_analysis_rules**](AnalysisRuleApi.md#getanalysisrules) | **GET** /analysisrules/{webId}/analysisrules | Get the child Analysis Rules of the Analysis Rule.
[**create_analysis_rule**](AnalysisRuleApi.md#createanalysisrule) | **POST** /analysisrules/{webId}/analysisrules | Create a new Analysis Rule as a child of an existing Analysis Rule.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an Analysis Rule by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the Analysis Rule.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAnalysisRule**](../models/PIAnalysisRule.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an Analysis Rule.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAnalysisRule**](../models/PIAnalysisRule.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'analysis_rule')

Update an Analysis Rule by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule.. | [required]
 **analysis_rule** | **PIAnalysisRule**| A partial Analysis Rule containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an Analysis Rule.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the Analysis Rule.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_analysis_rules**
> get_analysis_rules('web_id', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index')

Get the child Analysis Rules of the Analysis Rule.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent Analysis Rule.. | [required]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding Analysis Rules. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]


### Return type

[**PIItemsAnalysisRule**](../models/PIItemsAnalysisRule.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_analysis_rule**
> create_analysis_rule('web_id', 'analysis_rule')

Create a new Analysis Rule as a child of an existing Analysis Rule.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent Analysis Rule, on which to create the child Analysis Rule.. | [required]
 **analysis_rule** | **PIAnalysisRule**| The definition of the new Analysis Rule.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
