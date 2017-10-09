# AttributeCategoryApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](AttributeCategoryApi.md#getbypath) | **GET** /attributecategories | Retrieve an attribute category by path.
[**get**](AttributeCategoryApi.md#get) | **GET** /attributecategories/{webId} | Retrieve an attribute category.
[**update**](AttributeCategoryApi.md#update) | **PATCH** /attributecategories/{webId} | Update an attribute category by replacing items in its definition.
[**delete**](AttributeCategoryApi.md#delete) | **DELETE** /attributecategories/{webId} | Delete an attribute category.
[**get_security**](AttributeCategoryApi.md#getsecurity) | **GET** /attributecategories/{webId}/security | Get the security information of the specified security item associated with the attribute category for a specified user.
[**get_security_entries**](AttributeCategoryApi.md#getsecurityentries) | **GET** /attributecategories/{webId}/securityentries | Retrieve the security entries associated with the attribute category based on the specified criteria. By default, all security entries for this attribute category are returned.
[**create_security_entry**](AttributeCategoryApi.md#createsecurityentry) | **POST** /attributecategories/{webId}/securityentries | Create a security entry owned by the attribute category.
[**get_security_entry_by_name**](AttributeCategoryApi.md#getsecurityentrybyname) | **GET** /attributecategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the attribute category with the specified name.
[**update_security_entry**](AttributeCategoryApi.md#updatesecurityentry) | **PUT** /attributecategories/{webId}/securityentries/{name} | Update a security entry owned by the attribute category.
[**delete_security_entry**](AttributeCategoryApi.md#deletesecurityentry) | **DELETE** /attributecategories/{webId}/securityentries/{name} | Delete a security entry owned by the attribute category.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an attribute category by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target attribute category.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAttributeCategory**](../models/PIAttributeCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an attribute category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The id of the attribute category.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAttributeCategory**](../models/PIAttributeCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'category')

Update an attribute category by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute category to update.. | [required]
 **category** | **PIAttributeCategory**| A partial attribute category containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an attribute category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute category to delete.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security**
> get_security('web_id', 'user_identity', 'force_refresh', 'selected_fields')

Get the security information of the specified security item associated with the attribute category for a specified user.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute category for the security to be checked.. | [required]
 **user_identity** | **list[str]**| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.. | [required]
 **force_refresh** | **bool**| Indicates if the security cache should be refreshed before getting security information. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityRights**](../models/PIItemsSecurityRights.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entries**
> get_security_entries('web_id', 'name_filter', 'selected_fields')

Retrieve the security entries associated with the attribute category based on the specified criteria. By default, all security entries for this attribute category are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute category.. | [required]
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityEntry**](../models/PIItemsSecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_security_entry**
> create_security_entry('web_id', 'security_entry', 'apply_to_children')

Create a security entry owned by the attribute category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute category where the security entry will be created.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entry_by_name**
> get_security_entry_by_name('name', 'web_id', 'selected_fields')

Retrieve the security entry associated with the attribute category with the specified name.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the attribute category.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PISecurityEntry**](../models/PISecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_security_entry**
> update_security_entry('name', 'web_id', 'security_entry', 'apply_to_children')

Update a security entry owned by the attribute category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry.. | [required]
 **web_id** | **str**| The ID of the attribute category where the security entry will be updated.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete_security_entry**
> delete_security_entry('name', 'web_id', 'apply_to_children')

Delete a security entry owned by the attribute category.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the attribute category where the security entry will be deleted.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
