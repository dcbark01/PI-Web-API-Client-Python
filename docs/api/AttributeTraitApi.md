# AttributeTraitApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_category**](AttributeTraitApi.md#getbycategory) | **GET** /attributetraits | Retrieve all attribute traits of the specified category/categories.
[**get**](AttributeTraitApi.md#get) | **GET** /attributetraits/{name} | Retrieve an attribute trait.


# **get_by_category**
> get_by_category('category', 'selected_fields')

Retrieve all attribute traits of the specified category/categories.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **category** | **list[str]**| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is "all", then all attribute traits of all categories will be returned.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsAttributeTrait**](../models/PIItemsAttributeTrait.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('name', 'selected_fields')

Retrieve an attribute trait.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name or abbreviation of the attribute trait.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAttributeTrait**](../models/PIAttributeTrait.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
