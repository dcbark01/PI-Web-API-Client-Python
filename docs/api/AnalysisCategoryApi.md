# AnalysisCategoryApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](AnalysisCategoryApi.md#getbypath) | **GET** /analysiscategories | Retrieve an analysis category by path.
[**get**](AnalysisCategoryApi.md#get) | **GET** /analysiscategories/{webId} | Retrieve an analysis category.
[**update**](AnalysisCategoryApi.md#update) | **PATCH** /analysiscategories/{webId} | Update an analysis category by replacing items in its definition.
[**delete**](AnalysisCategoryApi.md#delete) | **DELETE** /analysiscategories/{webId} | Delete an analysis category.
[**get_security**](AnalysisCategoryApi.md#getsecurity) | **GET** /analysiscategories/{webId}/security | Get the security information of the specified security item associated with the analysis category for a specified user.
[**get_security_entries**](AnalysisCategoryApi.md#getsecurityentries) | **GET** /analysiscategories/{webId}/securityentries | Retrieve the security entries associated with the analysis category based on the specified criteria. By default, all security entries for this analysis category are returned.
[**create_security_entry**](AnalysisCategoryApi.md#createsecurityentry) | **POST** /analysiscategories/{webId}/securityentries | Create a security entry owned by the analysis category.
[**get_security_entry_by_name**](AnalysisCategoryApi.md#getsecurityentrybyname) | **GET** /analysiscategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the analysis category with the specified name.
[**update_security_entry**](AnalysisCategoryApi.md#updatesecurityentry) | **PUT** /analysiscategories/{webId}/securityentries/{name} | Update a security entry owned by the analysis category.
[**delete_security_entry**](AnalysisCategoryApi.md#deletesecurityentry) | **DELETE** /analysiscategories/{webId}/securityentries/{name} | Delete a security entry owned by the analysis category.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an analysis category by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target analysis category.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAnalysisCategory**](../models/PIAnalysisCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an analysis category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the analysis category.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAnalysisCategory**](../models/PIAnalysisCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'category')

Update an analysis category by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the analysis category to update.. | [required]
 **category** | **PIAnalysisCategory**| A partial analysis category containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an analysis category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the analysis category to delete.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security**
> get_security('web_id', 'user_identity', 'force_refresh', 'selected_fields')

Get the security information of the specified security item associated with the analysis category for a specified user.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the analysis category for the security to be checked.. | [required]
 **user_identity** | **list[str]**| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.. | [required]
 **force_refresh** | **bool**| Indicates if the security cache should be refreshed before getting security information. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityRights**](../models/PIItemsSecurityRights.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entries**
> get_security_entries('web_id', 'name_filter', 'selected_fields')

Retrieve the security entries associated with the analysis category based on the specified criteria. By default, all security entries for this analysis category are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the analysis category.. | [required]
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityEntry**](../models/PIItemsSecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_security_entry**
> create_security_entry('web_id', 'security_entry', 'apply_to_children')

Create a security entry owned by the analysis category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the analysis category, where the security entry will be created.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entry_by_name**
> get_security_entry_by_name('name', 'web_id', 'selected_fields')

Retrieve the security entry associated with the analysis category with the specified name.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the analysis category.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PISecurityEntry**](../models/PISecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_security_entry**
> update_security_entry('name', 'web_id', 'security_entry', 'apply_to_children')

Update a security entry owned by the analysis category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry.. | [required]
 **web_id** | **str**| The ID of the analysis category, where the security entry will be updated.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete_security_entry**
> delete_security_entry('name', 'web_id', 'apply_to_children')

Delete a security entry owned by the analysis category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the analysis category, where the security entry will be deleted.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
