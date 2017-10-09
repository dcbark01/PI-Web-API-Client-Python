# EnumerationValueApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](EnumerationValueApi.md#getbypath) | **GET** /enumerationvalues | Retrieve an enumeration value by path.
[**get**](EnumerationValueApi.md#get) | **GET** /enumerationvalues/{webId} | Retrieve an enumeration value mapping
[**update_enumeration_value**](EnumerationValueApi.md#updateenumerationvalue) | **PATCH** /enumerationvalues/{webId} | Update an enumeration value by replacing items in its definition.
[**delete_enumeration_value**](EnumerationValueApi.md#deleteenumerationvalue) | **DELETE** /enumerationvalues/{webId} | Delete an enumeration value from an enumeration set.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an enumeration value by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the target enumeration value.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIEnumerationValue**](../models/PIEnumerationValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an enumeration value mapping

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration value.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIEnumerationValue**](../models/PIEnumerationValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_enumeration_value**
> update_enumeration_value('web_id', 'enumeration_value')

Update an enumeration value by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration value to update.. | [required]
 **enumeration_value** | **PIEnumerationValue**| A partial enumeration value containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete_enumeration_value**
> delete_enumeration_value('web_id')

Delete an enumeration value from an enumeration set.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the enumeration value.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
