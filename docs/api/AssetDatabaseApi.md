# AssetDatabaseApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](AssetDatabaseApi.md#getbypath) | **GET** /assetdatabases | Retrieve an Asset Database by path.
[**get**](AssetDatabaseApi.md#get) | **GET** /assetdatabases/{webId} | Retrieve an Asset Database.
[**update**](AssetDatabaseApi.md#update) | **PATCH** /assetdatabases/{webId} | Update an asset database by replacing items in its definition.
[**delete**](AssetDatabaseApi.md#delete) | **DELETE** /assetdatabases/{webId} | Delete an asset database.
[**find_analyses**](AssetDatabaseApi.md#findanalyses) | **GET** /assetdatabases/{webId}/analyses | Retrieve analyses based on the specified conditions.
[**get_analysis_categories**](AssetDatabaseApi.md#getanalysiscategories) | **GET** /assetdatabases/{webId}/analysiscategories | Retrieve analysis categories for a given Asset Database.
[**create_analysis_category**](AssetDatabaseApi.md#createanalysiscategory) | **POST** /assetdatabases/{webId}/analysiscategories | Create an analysis category at the Asset Database root.
[**get_analysis_templates**](AssetDatabaseApi.md#getanalysistemplates) | **GET** /assetdatabases/{webId}/analysistemplates | Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.
[**create_analysis_template**](AssetDatabaseApi.md#createanalysistemplate) | **POST** /assetdatabases/{webId}/analysistemplates | Create an analysis template at the Asset Database root.
[**get_attribute_categories**](AssetDatabaseApi.md#getattributecategories) | **GET** /assetdatabases/{webId}/attributecategories | Retrieve attribute categories for a given Asset Database.
[**create_attribute_category**](AssetDatabaseApi.md#createattributecategory) | **POST** /assetdatabases/{webId}/attributecategories | Create an attribute category at the Asset Database root.
[**find_element_attributes**](AssetDatabaseApi.md#findelementattributes) | **GET** /assetdatabases/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified asset database.
[**get_element_categories**](AssetDatabaseApi.md#getelementcategories) | **GET** /assetdatabases/{webId}/elementcategories | Retrieve element categories for a given Asset Database.
[**create_element_category**](AssetDatabaseApi.md#createelementcategory) | **POST** /assetdatabases/{webId}/elementcategories | Create an element category at the Asset Database root.
[**get_elements**](AssetDatabaseApi.md#getelements) | **GET** /assetdatabases/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.
[**create_element**](AssetDatabaseApi.md#createelement) | **POST** /assetdatabases/{webId}/elements | Create a child element.
[**get_element_templates**](AssetDatabaseApi.md#getelementtemplates) | **GET** /assetdatabases/{webId}/elementtemplates | Retrieve element templates based on the specified criteria. Only templates of instance type "Element" and "EventFrame" are returned. By default, all element and event frame templates in the specified Asset Database are returned.
[**create_element_template**](AssetDatabaseApi.md#createelementtemplate) | **POST** /assetdatabases/{webId}/elementtemplates | Create a template at the Asset Database root. Specify InstanceType of "Element" or "EventFrame" to create element or event frame template respectively. Only these two types of templates can be created.
[**get_enumeration_sets**](AssetDatabaseApi.md#getenumerationsets) | **GET** /assetdatabases/{webId}/enumerationsets | Retrieve enumeration sets for given asset database.
[**create_enumeration_set**](AssetDatabaseApi.md#createenumerationset) | **POST** /assetdatabases/{webId}/enumerationsets | Create an enumeration set at the Asset Database.
[**find_event_frame_attributes**](AssetDatabaseApi.md#findeventframeattributes) | **GET** /assetdatabases/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified asset database.
[**get_event_frames**](AssetDatabaseApi.md#geteventframes) | **GET** /assetdatabases/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource with a start time in the past 8 hours.
[**create_event_frame**](AssetDatabaseApi.md#createeventframe) | **POST** /assetdatabases/{webId}/eventframes | Create an event frame.
[**export**](AssetDatabaseApi.md#export) | **GET** /assetdatabases/{webId}/export | Export the asset database.
[**import_data**](AssetDatabaseApi.md#import) | **POST** /assetdatabases/{webId}/import | Import an asset database.
[**get_referenced_elements**](AssetDatabaseApi.md#getreferencedelements) | **GET** /assetdatabases/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.
[**add_referenced_element**](AssetDatabaseApi.md#addreferencedelement) | **POST** /assetdatabases/{webId}/referencedelements | Add a reference to an existing element to the specified database.
[**remove_referenced_element**](AssetDatabaseApi.md#removereferencedelement) | **DELETE** /assetdatabases/{webId}/referencedelements | Remove a reference to an existing element from the specified database.
[**get_security**](AssetDatabaseApi.md#getsecurity) | **GET** /assetdatabases/{webId}/security | Get the security information of the specified security item associated with the asset database for a specified user.
[**get_security_entries**](AssetDatabaseApi.md#getsecurityentries) | **GET** /assetdatabases/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.
[**create_security_entry**](AssetDatabaseApi.md#createsecurityentry) | **POST** /assetdatabases/{webId}/securityentries | Create a security entry owned by the asset database.
[**get_security_entry_by_name**](AssetDatabaseApi.md#getsecurityentrybyname) | **GET** /assetdatabases/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset database with the specified name.
[**update_security_entry**](AssetDatabaseApi.md#updatesecurityentry) | **PUT** /assetdatabases/{webId}/securityentries/{name} | Update a security entry owned by the asset database.
[**delete_security_entry**](AssetDatabaseApi.md#deletesecurityentry) | **DELETE** /assetdatabases/{webId}/securityentries/{name} | Delete a security entry owned by the asset database.
[**get_table_categories**](AssetDatabaseApi.md#gettablecategories) | **GET** /assetdatabases/{webId}/tablecategories | Retrieve table categories for a given Asset Database.
[**create_table_category**](AssetDatabaseApi.md#createtablecategory) | **POST** /assetdatabases/{webId}/tablecategories | Create a table category on the Asset Database.
[**get_tables**](AssetDatabaseApi.md#gettables) | **GET** /assetdatabases/{webId}/tables | Retrieve tables for given Asset Database.
[**create_table**](AssetDatabaseApi.md#createtable) | **POST** /assetdatabases/{webId}/tables | Create a table on the Asset Database.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an Asset Database by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAssetDatabase**](../models/PIAssetDatabase.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIAssetDatabase**](../models/PIAssetDatabase.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'database')

Update an asset database by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **database** | **PIAssetDatabase**| A partial database containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **find_analyses**
> find_analyses('web_id', 'field', 'max_count', 'query', 'selected_fields', 'sort_field', 'sort_order', 'start_index')

Retrieve analyses based on the specified conditions.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to search for the analyses.. | [required]
 **field** | **list[str]**| Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.. | [required]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **query** | **str**| The query string used for finding analyses. The default is null.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]


### Return type

[**PIItemsAnalysis**](../models/PIItemsAnalysis.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_analysis_categories**
> get_analysis_categories('web_id', 'selected_fields')

Retrieve analysis categories for a given Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsAnalysisCategory**](../models/PIItemsAnalysisCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_analysis_category**
> create_analysis_category('web_id', 'analysis_category')

Create an analysis category at the Asset Database root.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the analysis category.. | [required]
 **analysis_category** | **PIAnalysisCategory**| The new analysis category definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_analysis_templates**
> get_analysis_templates('web_id', 'field', 'max_count', 'query', 'selected_fields', 'sort_field', 'sort_order')

Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to search.. | [required]
 **field** | **list[str]**| Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.. | [required]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **query** | **str**| The query string used for finding objects. The default is no query string.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]


### Return type

[**PIItemsAnalysisTemplate**](../models/PIItemsAnalysisTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_analysis_template**
> create_analysis_template('web_id', 'template')

Create an analysis template at the Asset Database root.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the analysis template.. | [required]
 **template** | **PIAnalysisTemplate**| The new analysis template definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_attribute_categories**
> get_attribute_categories('web_id', 'selected_fields')

Retrieve attribute categories for a given Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsAttributeCategory**](../models/PIItemsAttributeCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_attribute_category**
> create_attribute_category('web_id', 'attribute_category')

Create an attribute category at the Asset Database root.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the attribute category.. | [required]
 **attribute_category** | **PIAttributeCategory**| The new attribute category definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **find_element_attributes**
> find_element_attributes('web_id', 'attribute_category', 'attribute_description_filter', 'attribute_name_filter', 'attribute_type', 'element_category', 'element_description_filter', 'element_name_filter', 'element_template', 'element_type', 'max_count', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index')

Retrieves a list of element attributes matching the specified filters from the specified asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database to use as the root of the search.. | [required]
 **attribute_category** | **str**| Specify that returned attributes must have this category. The default is no filter.. | [optional]
 **attribute_description_filter** | **str**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.. | [optional]
 **attribute_name_filter** | **str**| The attribute name filter string used for finding objects. The default is no filter.. | [optional]
 **attribute_type** | **str**| Specify that returned attributes' value type must be this value type. The default is no filter.. | [optional]
 **element_category** | **str**| Specify that the owner of the returned attributes must have this category. The default is no filter.. | [optional]
 **element_description_filter** | **str**| The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.. | [optional]
 **element_name_filter** | **str**| The element name filter string used for finding objects. The default is no filter.. | [optional]
 **element_template** | **str**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.. | [optional]
 **element_type** | **str**| Specify that the element of the returned attributes must have this AFElementType. The default is no filter.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned (the page size). The default is 1000.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]


### Return type

[**PIItemsAttribute**](../models/PIItemsAttribute.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_element_categories**
> get_element_categories('web_id', 'selected_fields')

Retrieve element categories for a given Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsElementCategory**](../models/PIItemsElementCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_element_category**
> create_element_category('web_id', 'element_category')

Create an element category at the Asset Database root.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the element category.. | [required]
 **element_category** | **PIElementCategory**| The new element category definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_elements**
> get_elements('web_id', 'category_name', 'description_filter', 'element_type', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'template_name')

Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to use as the root of the search.. | [required]
 **category_name** | **str**| Specify that returned elements must have this category. The default is no category filter.. | [optional]
 **description_filter** | **str**| Specify that returned elements must have this description. The default is no description filter.. | [optional]
 **element_type** | **str**| Specify that returned elements must have this type. The default type is 'Any'.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding objects. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **template_name** | **str**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter.. | [optional]


### Return type

[**PIItemsElement**](../models/PIItemsElement.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_element**
> create_element('web_id', 'element')

Create a child element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database on which to create the element.. | [required]
 **element** | **PIElement**| The new element definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_element_templates**
> get_element_templates('web_id', 'field', 'max_count', 'query', 'selected_fields', 'sort_field', 'sort_order')

Retrieve element templates based on the specified criteria. Only templates of instance type "Element" and "EventFrame" are returned. By default, all element and event frame templates in the specified Asset Database are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database to search.. | [required]
 **field** | **list[str]**| Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.. | [required]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **query** | **str**| The query string used for finding objects. The default is no query string.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]


### Return type

[**PIItemsElementTemplate**](../models/PIItemsElementTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_element_template**
> create_element_template('web_id', 'template')

Create a template at the Asset Database root. Specify InstanceType of "Element" or "EventFrame" to create element or event frame template respectively. Only these two types of templates can be created.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the element template.. | [required]
 **template** | **PIElementTemplate**| The new element template definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_enumeration_sets**
> get_enumeration_sets('web_id', 'selected_fields')

Retrieve enumeration sets for given asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsEnumerationSet**](../models/PIItemsEnumerationSet.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_enumeration_set**
> create_enumeration_set('web_id', 'enumeration_set')

Create an enumeration set at the Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the enumeration set.. | [required]
 **enumeration_set** | **PIEnumerationSet**| The new enumeration set definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **find_event_frame_attributes**
> find_event_frame_attributes('web_id', 'attribute_category', 'attribute_description_filter', 'attribute_name_filter', 'attribute_type', 'end_time', 'event_frame_category', 'event_frame_description_filter', 'event_frame_name_filter', 'event_frame_template', 'max_count', 'referenced_element_name_filter', 'search_full_hierarchy', 'search_mode', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'start_time')

Retrieves a list of event frame attributes matching the specified filters from the specified asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database to use as the root of the search.. | [required]
 **attribute_category** | **str**| Specify that returned attributes must have this category. The default is no filter.. | [optional]
 **attribute_description_filter** | **str**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.. | [optional]
 **attribute_name_filter** | **str**| The attribute name filter string used for finding objects. The default is no filter.. | [optional]
 **attribute_type** | **str**| Specify that returned attributes' value type must be this value type. The default is no filter.. | [optional]
 **end_time** | **str**| A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is '*'.. | [optional]
 **event_frame_category** | **str**| Specify that the owner of the returned attributes must have this category. The default is no filter.. | [optional]
 **event_frame_description_filter** | **str**| The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.. | [optional]
 **event_frame_name_filter** | **str**| The event frame name filter string used for finding objects. The default is no filter.. | [optional]
 **event_frame_template** | **str**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned (the page size). The default is 1000.. | [optional]
 **referenced_element_name_filter** | **str**| The name query string which must match the name of a referenced element. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.. | [optional]
 **search_mode** | **str**| Determines how the startTime and endTime parameters are treated when searching for event frames.     The default is 'Overlapped'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **start_time** | **str**| A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is '*-8h'.. | [optional]


### Return type

[**PIItemsAttribute**](../models/PIItemsAttribute.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_event_frames**
> get_event_frames('web_id', 'can_be_acknowledged', 'category_name', 'end_time', 'is_acknowledged', 'max_count', 'name_filter', 'referenced_element_name_filter', 'referenced_element_template_name', 'search_full_hierarchy', 'search_mode', 'selected_fields', 'severity', 'sort_field', 'sort_order', 'start_index', 'start_time', 'template_name')

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource with a start time in the past 8 hours.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database to use as the root of the search.. | [required]
 **can_be_acknowledged** | **bool**| Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.. | [optional]
 **category_name** | **str**| Specify that returned event frames must have this category. The default is no category filter.. | [optional]
 **end_time** | **str**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values.. | [optional]
 **is_acknowledged** | **bool**| Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding event frames. The default is no filter.. | [optional]
 **referenced_element_name_filter** | **str**| The name query string which must match the name of a referenced element. The default is no filter.. | [optional]
 **referenced_element_template_name** | **str**| Specify that returned event frames must have an element in the event frame's referenced elements collection that derives from the template. Specify this parameter by name.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.. | [optional]
 **search_mode** | **str**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the 'Backward*' or 'Forward*' values, none of endTime, sortField, or sortOrder may be specified. The default is 'Overlapped'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **severity** | **list[str]**| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name' if searchMode is not one of the 'Backward*' or 'Forward*' values.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending' if searchMode is not one of the 'Backward*' or 'Forward*' values.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **start_time** | **str**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.. | [optional]
 **template_name** | **str**| Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name.. | [optional]


### Return type

[**PIItemsEventFrame**](../models/PIItemsEventFrame.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_event_frame**
> create_event_frame('web_id', 'event_frame')

Create an event frame.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database on which to create the event frame.. | [required]
 **event_frame** | **PIEventFrame**| The new event frame definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **export**
> export('web_id', 'end_time', 'export_mode', 'start_time')

Export the asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **end_time** | **str**| The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*'.. | [optional]
 **export_mode** | **list[str]**| Indicates the type of export to perform. The default is 'StrongReferences'. Multiple export modes may be specified by using multiple instances of exportMode.. | [optional]
 **start_time** | **str**| The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*-30d'.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **import_data**
> import_data('web_id', 'import_mode')

Import an asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database.. | [required]
 **import_mode** | **list[str]**| Indicates the type of import to perform. The default is 'AllowCreate | AllowUpdate | AutoCheckIn'. Multiple import modes may be specified by using multiple instances of importMode.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_referenced_elements**
> get_referenced_elements('web_id', 'category_name', 'description_filter', 'element_type', 'max_count', 'name_filter', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'template_name')

Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search.. | [required]
 **category_name** | **str**| Specify that returned elements must have this category. The default is no category filter.. | [optional]
 **description_filter** | **str**| Specify that returned elements must have this description. The default is no description filter.. | [optional]
 **element_type** | **str**| Specify that returned elements must have this type. The default type is 'Any'.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding objects. The default is no filter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **template_name** | **str**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter.. | [optional]


### Return type

[**PIItemsElement**](../models/PIItemsElement.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **add_referenced_element**
> add_referenced_element('web_id', 'referenced_element_web_id', 'reference_type')

Add a reference to an existing element to the specified database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database which the referenced element will be added to.. | [required]
 **referenced_element_web_id** | **list[str]**| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.. | [required]
 **reference_type** | **str**| The name of the reference type between the parent and the referenced element. This must be a "strong" reference type. The default is "parent-child".. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **remove_referenced_element**
> remove_referenced_element('web_id', 'referenced_element_web_id')

Remove a reference to an existing element from the specified database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database which the referenced element will be removed from.. | [required]
 **referenced_element_web_id** | **list[str]**| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security**
> get_security('web_id', 'security_item', 'user_identity', 'force_refresh', 'selected_fields')

Get the security information of the specified security item associated with the asset database for a specified user.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database for the security to be checked.. | [required]
 **security_item** | **list[str]**| The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only 'Default' security item of the security information will be returned.. | [required]
 **user_identity** | **list[str]**| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.. | [required]
 **force_refresh** | **bool**| Indicates if the security cache should be refreshed before getting security information. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityRights**](../models/PIItemsSecurityRights.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entries**
> get_security_entries('web_id', 'name_filter', 'security_item', 'selected_fields')

Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database.. | [required]
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter.. | [optional]
 **security_item** | **str**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityEntry**](../models/PIItemsSecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_security_entry**
> create_security_entry('web_id', 'security_entry', 'apply_to_children', 'security_item')

Create a security entry owned by the asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the asset database where the security entry will be created.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]
 **security_item** | **str**| The security item of the desired security entries to be created. If the parameter is not specified, security entries of the 'Default' security item will be created.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entry_by_name**
> get_security_entry_by_name('name', 'web_id', 'security_item', 'selected_fields')

Retrieve the security entry of the specified security item associated with the asset database with the specified name.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the asset database.. | [required]
 **security_item** | **str**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PISecurityEntry**](../models/PISecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_security_entry**
> update_security_entry('name', 'web_id', 'security_entry', 'apply_to_children', 'security_item')

Update a security entry owned by the asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry.. | [required]
 **web_id** | **str**| The ID of the asset database where the security entry will be updated.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]
 **security_item** | **str**| The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the 'Default' security item will be updated.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete_security_entry**
> delete_security_entry('name', 'web_id', 'apply_to_children', 'security_item')

Delete a security entry owned by the asset database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the asset database where the security entry will be deleted.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]
 **security_item** | **str**| The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the 'Default' security item will be deleted.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_table_categories**
> get_table_categories('web_id', 'selected_fields')

Retrieve table categories for a given Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsTableCategory**](../models/PIItemsTableCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_table_category**
> create_table_category('web_id', 'table_category')

Create a table category on the Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the table category.. | [required]
 **table_category** | **PITableCategory**| The new table category definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_tables**
> get_tables('web_id', 'selected_fields')

Retrieve tables for given Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsTable**](../models/PIItemsTable.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_table**
> create_table('web_id', 'table')

Create a table on the Asset Database.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the database in which to create the table.. | [required]
 **table** | **PITable**| The new table definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
