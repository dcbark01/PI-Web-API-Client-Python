# ElementApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_by_path**](ElementApi.md#getbypath) | **GET** /elements | Retrieve an element by path.
[**get**](ElementApi.md#get) | **GET** /elements/{webId} | Retrieve an element.
[**update**](ElementApi.md#update) | **PATCH** /elements/{webId} | Update an element by replacing items in its definition.
[**delete**](ElementApi.md#delete) | **DELETE** /elements/{webId} | Delete an element.
[**get_analyses**](ElementApi.md#getanalyses) | **GET** /elements/{webId}/analyses | Retrieve analyses based on the specified conditions.
[**create_analysis**](ElementApi.md#createanalysis) | **POST** /elements/{webId}/analyses | Create an Analysis.
[**get_attributes**](ElementApi.md#getattributes) | **GET** /elements/{webId}/attributes | Get the attributes of the specified element.
[**create_attribute**](ElementApi.md#createattribute) | **POST** /elements/{webId}/attributes | Create a new attribute of the specified element.
[**get_categories**](ElementApi.md#getcategories) | **GET** /elements/{webId}/categories | Get an element's categories.
[**create_config**](ElementApi.md#createconfig) | **POST** /elements/{webId}/config | Executes the create configuration function of the data references found within the attributes of the element, and optionally, its children.
[**find_element_attributes**](ElementApi.md#findelementattributes) | **GET** /elements/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified element.
[**get_elements**](ElementApi.md#getelements) | **GET** /elements/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified element.
[**create_element**](ElementApi.md#createelement) | **POST** /elements/{webId}/elements | Create a child element.
[**get_event_frames**](ElementApi.md#geteventframes) | **GET** /elements/{webId}/eventframes | Retrieve event frames that reference this element based on the specified conditions. By default, returns all event frames that reference this element with a start time in the past 8 hours.
[**get_referenced_elements**](ElementApi.md#getreferencedelements) | **GET** /elements/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements of the current resource.
[**add_referenced_element**](ElementApi.md#addreferencedelement) | **POST** /elements/{webId}/referencedelements | Add a reference to an existing element to the child elements collection.
[**remove_referenced_element**](ElementApi.md#removereferencedelement) | **DELETE** /elements/{webId}/referencedelements | Remove a reference to an existing element from the child elements collection.
[**get_security**](ElementApi.md#getsecurity) | **GET** /elements/{webId}/security | Get the security information of the specified security item associated with the element for a specified user.
[**get_security_entries**](ElementApi.md#getsecurityentries) | **GET** /elements/{webId}/securityentries | Retrieve the security entries associated with the element based on the specified criteria. By default, all security entries for this element are returned.
[**create_security_entry**](ElementApi.md#createsecurityentry) | **POST** /elements/{webId}/securityentries | Create a security entry owned by the element.
[**get_security_entry_by_name**](ElementApi.md#getsecurityentrybyname) | **GET** /elements/{webId}/securityentries/{name} | Retrieve the security entry associated with the element with the specified name.
[**update_security_entry**](ElementApi.md#updatesecurityentry) | **PUT** /elements/{webId}/securityentries/{name} | Update a security entry owned by the element.
[**delete_security_entry**](ElementApi.md#deletesecurityentry) | **DELETE** /elements/{webId}/securityentries/{name} | Delete a security entry owned by the element.
[**get_multiple**](ElementApi.md#getmultiple) | **GET** /elements/multiple | Retrieve multiple elements by web id or path.
[**create_search_by_attribute**](ElementApi.md#createsearchbyattribute) | **POST** /elements/searchbyattribute | Create a link for a "Search Elements By Attribute Value" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root Element. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the Elements. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
[**execute_search_by_attribute**](ElementApi.md#executesearchbyattribute) | **GET** /elements/searchbyattribute/{searchId} | Execute a "Search Elements By Attribute Value" operation.


# **get_by_path**
> get_by_path('path', 'selected_fields')

Retrieve an element by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the element.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIElement**](../models/PIElement.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('web_id', 'selected_fields')

Retrieve an element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIElement**](../models/PIElement.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update**
> update('web_id', 'element')

Update an element by replacing items in its definition.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]
 **element** | **PIElement**| A partial element containing the desired changes.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('web_id')

Delete an element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_analyses**
> get_analyses('web_id', 'max_count', 'selected_fields', 'sort_field', 'sort_order', 'start_index')

Retrieve analyses based on the specified conditions.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element, which is the Target of the analyses.. | [required]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]


### Return type

[**PIItemsAnalysis**](../models/PIItemsAnalysis.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_analysis**
> create_analysis('web_id', 'analysis')

Create an Analysis.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element on which to create the Analysis.. | [required]
 **analysis** | **PIAnalysis**| The new Analysis definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_attributes**
> get_attributes('web_id', 'category_name', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_field', 'sort_order', 'start_index', 'template_name', 'value_type')

Get the attributes of the specified element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]
 **category_name** | **str**| Specify that returned attributes must have this category. The default is no category filter.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **template_name** | **str**| Specify that returned attributes must be members of this template. The default is no template filter.. | [optional]
 **value_type** | **str**| Specify that returned attributes' value type must be the given value type. The default is no value type filter.. | [optional]


### Return type

[**PIItemsAttribute**](../models/PIItemsAttribute.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_attribute**
> create_attribute('web_id', 'attribute')

Create a new attribute of the specified element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element on which to create the attribute.. | [required]
 **attribute** | **PIAttribute**| The definition of the new attribute.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_categories**
> get_categories('web_id', 'selected_fields')

Get an element's categories.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsElementCategory**](../models/PIItemsElementCategory.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_config**
> create_config('web_id', 'include_child_elements')

Executes the create configuration function of the data references found within the attributes of the element, and optionally, its children.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]
 **include_child_elements** | **bool**| If true, includes the child elements of the specified element.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **find_element_attributes**
> find_element_attributes('web_id', 'attribute_category', 'attribute_description_filter', 'attribute_name_filter', 'attribute_type', 'element_category', 'element_description_filter', 'element_name_filter', 'element_template', 'element_type', 'max_count', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index')

Retrieves a list of element attributes matching the specified filters from the specified element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element to use as the root of the search.. | [required]
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

# **get_elements**
> get_elements('web_id', 'category_name', 'description_filter', 'element_type', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'template_name')

Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element to use as the root of the search.. | [required]
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
 **web_id** | **str**| The ID of the parent element on which to create the element.. | [required]
 **element** | **PIElement**| The new element definition.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_event_frames**
> get_event_frames('web_id', 'can_be_acknowledged', 'category_name', 'end_time', 'is_acknowledged', 'max_count', 'name_filter', 'search_mode', 'selected_fields', 'severity', 'sort_field', 'sort_order', 'start_index', 'start_time', 'template_name')

Retrieve event frames that reference this element based on the specified conditions. By default, returns all event frames that reference this element with a start time in the past 8 hours.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element whose related event frames are sought.. | [required]
 **can_be_acknowledged** | **bool**| Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.. | [optional]
 **category_name** | **str**| Specify that returned event frames must have this category. The default is no category filter.. | [optional]
 **end_time** | **str**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values.. | [optional]
 **is_acknowledged** | **bool**| Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding event frames. The default is no filter.. | [optional]
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

# **get_referenced_elements**
> get_referenced_elements('web_id', 'category_name', 'description_filter', 'element_type', 'max_count', 'name_filter', 'selected_fields', 'sort_field', 'sort_order', 'start_index', 'template_name')

Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements of the current resource.

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

Add a reference to an existing element to the child elements collection.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element which the referenced element will be added to.. | [required]
 **referenced_element_web_id** | **list[str]**| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.. | [required]
 **reference_type** | **str**| The name of the reference type between the parent and the referenced element. The default is "parent-child".. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **remove_referenced_element**
> remove_referenced_element('web_id', 'referenced_element_web_id')

Remove a reference to an existing element from the child elements collection.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element which the referenced element will be removed from.. | [required]
 **referenced_element_web_id** | **list[str]**| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security**
> get_security('web_id', 'user_identity', 'force_refresh', 'selected_fields')

Get the security information of the specified security item associated with the element for a specified user.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element for the security to be checked.. | [required]
 **user_identity** | **list[str]**| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.. | [required]
 **force_refresh** | **bool**| Indicates if the security cache should be refreshed before getting security information. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityRights**](../models/PIItemsSecurityRights.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entries**
> get_security_entries('web_id', 'name_filter', 'selected_fields')

Retrieve the security entries associated with the element based on the specified criteria. By default, all security entries for this element are returned.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element.. | [required]
 **name_filter** | **str**| The name query string used for filtering security entries. The default is no filter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsSecurityEntry**](../models/PIItemsSecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_security_entry**
> create_security_entry('web_id', 'security_entry', 'apply_to_children')

Create a security entry owned by the element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the element where the security entry will be created.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_security_entry_by_name**
> get_security_entry_by_name('name', 'web_id', 'selected_fields')

Retrieve the security entry associated with the element with the specified name.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the element.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PISecurityEntry**](../models/PISecurityEntry.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_security_entry**
> update_security_entry('name', 'web_id', 'security_entry', 'apply_to_children')

Update a security entry owned by the element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry.. | [required]
 **web_id** | **str**| The ID of the element where the security entry will be updated.. | [required]
 **security_entry** | **PISecurityEntry**| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete_security_entry**
> delete_security_entry('name', 'web_id', 'apply_to_children')

Delete a security entry owned by the element.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the security entry. For every backslash character (\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\username.. | [required]
 **web_id** | **str**| The ID of the element where the security entry will be deleted.. | [required]
 **apply_to_children** | **bool**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_multiple**
> get_multiple('as_parallel', 'include_mode', 'path', 'selected_fields', 'web_id')

Retrieve multiple elements by web id or path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **as_parallel** | **bool**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'.. | [optional]
 **include_mode** | **str**| The include mode for the return list. The default is 'All'.. | [optional]
 **path** | **list[str]**| The path of an element. Multiple elements may be specified with multiple instances of the parameter.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id** | **list[str]**| The ID of an element. Multiple elements may be specified with multiple instances of the parameter.. | [optional]


### Return type

[**PIItemsItemElement**](../models/PIItemsItemElement.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **create_search_by_attribute**
> create_search_by_attribute('search')

Create a link for a "Search Elements By Attribute Value" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root Element. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the Elements. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **search** | **PISearchByAttributeElement**| . | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **execute_search_by_attribute**
> execute_search_by_attribute('search_id', 'category_name', 'description_filter', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'sort_field', 'sort_order', 'start_index')

Execute a "Search Elements By Attribute Value" operation.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| The encoded search Id of the "Search Elements By Attribute Value" operation.. | [required]
 **category_name** | **str**| Specify that the owner of the returned attributes must have this category. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.. | [optional]
 **description_filter** | **str**| The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned. The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for finding objects. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_field** | **str**| The field or property of the object used to sort the returned collection. The default is 'Name'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
