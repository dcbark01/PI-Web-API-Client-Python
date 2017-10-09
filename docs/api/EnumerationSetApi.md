# EnumerationSetApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](EnumerationSetApi.md#getbypath) | **GET** /enumerationsets | Retrieve an enumeration set by path.
[**get**](EnumerationSetApi.md#get) | **GET** /enumerationsets/{webId} | Retrieve an enumeration set.
[**update**](EnumerationSetApi.md#update) | **PATCH** /enumerationsets/{webId} | Update an enumeration set by replacing items in its definition.
[**delete**](EnumerationSetApi.md#delete) | **DELETE** /enumerationsets/{webId} | Delete an enumeration set.
[**get_values**](EnumerationSetApi.md#getvalues) | **GET** /enumerationsets/{webId}/enumerationvalues | Retrieve an enumeration set's values.
[**create_value**](EnumerationSetApi.md#createvalue) | **POST** /enumerationsets/{webId}/enumerationvalues | Create an enumeration value for a enumeration set.
[**get_security**](EnumerationSetApi.md#getsecurity) | **GET** /enumerationsets/{webId}/security | Get the security information of the specified security item associated with the enumeration set for a specified user.
[**get_security_entries**](EnumerationSetApi.md#getsecurityentries) | **GET** /enumerationsets/{webId}/securityentries | Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.
[**create_security_entry**](EnumerationSetApi.md#createsecurityentry) | **POST** /enumerationsets/{webId}/securityentries | Create a security entry owned by the enumeration set.
[**get_security_entry_by_name**](EnumerationSetApi.md#getsecurityentrybyname) | **GET** /enumerationsets/{webId}/securityentries/{name} | Retrieve the security entry associated with the enumeration set with the specified name.
[**update_security_entry**](EnumerationSetApi.md#updatesecurityentry) | **PUT** /enumerationsets/{webId}/securityentries/{name} | Update a security entry owned by the enumeration set.
[**delete_security_entry**](EnumerationSetApi.md#deletesecurityentry) | **DELETE** /enumerationsets/{webId}/securityentries/{name} | Delete a security entry owned by the enumeration set.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an enumeration set by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target enumeration set.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIEnumerationSet**](../models/PIEnumerationSet.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIEnumerationSet**](../models/PIEnumerationSet.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'enumeration_set')

Update an enumeration set by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set to update.. | [required]
 **enumeration_set** | **PIEnumerationSet**| A partial enumeration set containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set to delete.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_values**
> get_values('web_id', 'selected_fields')

Retrieve an enumeration set's values.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsEnumerationValue**](../models/PIItemsEnumerationValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_value**
> create_value('web_id', 'enumeration_value')

Create an enumeration value for a enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set on which to create the enumeration value.. | [required]
 **enumeration_value** | **PIEnumerationValue**| The new enumeration value definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security**
> get_security('web_id', 'user_identity', 'force_refresh', 'selected_fields')

Get the security information of the specified security item associated with the enumeration set for a specified user.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set for the security to be checked.. | [required]
 **user_identity** | **list[str]**| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.. | [required]
 **force_refresh** | **bool**| Indicates if the security cache should be refreshed before getting security information. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityRights**](../models/PIItemsSecurityRights.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entries**
> get_security_entries('web_id', 'name_filter', 'selected_fields')

Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set.. | [required]
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityEntry**](../models/PIItemsSecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_security_entry**
> create_security_entry('web_id', 'security_entry', 'apply_to_children')

Create a security entry owned by the enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration set where the security entry will be created.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entry_by_name**
> get_security_entry_by_name('name', 'web_id', 'selected_fields')

Retrieve the security entry associated with the enumeration set with the specified name.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the enumeration set.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PISecurityEntry**](../models/PISecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_security_entry**
> update_security_entry('name', 'web_id', 'security_entry', 'apply_to_children')

Update a security entry owned by the enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry.. | [required]
 **web_id** | **str**| The ID of the enumeration set where the security entry will be updated.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete_security_entry**
> delete_security_entry('name', 'web_id', 'apply_to_children')

Delete a security entry owned by the enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the enumeration set where the security entry will be deleted.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
