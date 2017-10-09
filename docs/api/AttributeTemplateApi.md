# AttributeTemplateApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](AttributeTemplateApi.md#getbypath) | **GET** /attributetemplates | Retrieve an attribute template by path.
[**get**](AttributeTemplateApi.md#get) | **GET** /attributetemplates/{webId} | Retrieve an attribute template.
[**update**](AttributeTemplateApi.md#update) | **PATCH** /attributetemplates/{webId} | Update an existing attribute template by replacing items in its definition.
[**delete**](AttributeTemplateApi.md#delete) | **DELETE** /attributetemplates/{webId} | Delete an attribute template.
[**get_attribute_templates**](AttributeTemplateApi.md#getattributetemplates) | **GET** /attributetemplates/{webId}/attributetemplates | Retrieve an attribute template's child attribute templates.
[**create_attribute_template**](AttributeTemplateApi.md#createattributetemplate) | **POST** /attributetemplates/{webId}/attributetemplates | Create an attribute template as a child of another attribute template.
[**get_categories**](AttributeTemplateApi.md#getcategories) | **GET** /attributetemplates/{webId}/categories | Get an attribute template's categories.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an attribute template by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the attribute template.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAttributeTemplate**](../models/PIAttributeTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an attribute template.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAttributeTemplate**](../models/PIAttributeTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'template')

Update an existing attribute template by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template.. | [required]
 **template** | **PIAttributeTemplate**| A partial attribute template containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an attribute template.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_attribute_templates**
> get_attribute_templates('web_id', 'selected_fields')

Retrieve an attribute template's child attribute templates.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsAttributeTemplate**](../models/PIItemsAttributeTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_attribute_template**
> create_attribute_template('web_id', 'template')

Create an attribute template as a child of another attribute template.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent attribute template on which to create the attribute template.. | [required]
 **template** | **PIAttributeTemplate**| The attribute template definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_categories**
> get_categories('web_id', 'selected_fields')

Get an attribute template's categories.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the attribute template.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsAttributeCategory**](../models/PIItemsAttributeCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
