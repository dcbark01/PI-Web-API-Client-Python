## Documentation for PI Web API top level object

- [PIWebApiClient](docs/PIWebApiClient.md)

## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HomeApi* | [**get**](docs/api/HomeApi.md#get) | **GET** / | Get top level links for this PI System Web API instance.
*AnalysisApi* | [**get_by_path**](docs/api/AnalysisApi.md#get_by_path) | **GET** /analyses | Retrieve an Analysis by path.
*AnalysisApi* | [**get**](docs/api/AnalysisApi.md#get) | **GET** /analyses/{webId} | Retrieve an Analysis.
*AnalysisApi* | [**update**](docs/api/AnalysisApi.md#update) | **PATCH** /analyses/{webId} | Update an Analysis.
*AnalysisApi* | [**delete**](docs/api/AnalysisApi.md#delete) | **DELETE** /analyses/{webId} | Delete an Analysis.
*AnalysisApi* | [**get_categories**](docs/api/AnalysisApi.md#get_categories) | **GET** /analyses/{webId}/categories | Get an Analysis' categories.
*AnalysisApi* | [**get_security**](docs/api/AnalysisApi.md#get_security) | **GET** /analyses/{webId}/security | Get the security information of the specified security item associated with the Analysis for a specified user.
*AnalysisApi* | [**get_security_entries**](docs/api/AnalysisApi.md#get_security_entries) | **GET** /analyses/{webId}/securityentries | Retrieve the security entries associated with the analysis based on the specified criteria. By default, all security entries for this analysis are returned.
*AnalysisApi* | [**create_security_entry**](docs/api/AnalysisApi.md#create_security_entry) | **POST** /analyses/{webId}/securityentries | Create a security entry owned by the analysis.
*AnalysisApi* | [**get_security_entry_by_name**](docs/api/AnalysisApi.md#get_security_entry_by_name) | **GET** /analyses/{webId}/securityentries/{name} | Retrieve the security entry associated with the analysis with the specified name.
*AnalysisApi* | [**update_security_entry**](docs/api/AnalysisApi.md#update_security_entry) | **PUT** /analyses/{webId}/securityentries/{name} | Update a security entry owned by the analysis.
*AnalysisApi* | [**delete_security_entry**](docs/api/AnalysisApi.md#delete_security_entry) | **DELETE** /analyses/{webId}/securityentries/{name} | Delete a security entry owned by the analysis.
*AnalysisApi* | [**get_analyses_query**](docs/api/AnalysisApi.md#get_analyses_query) | **GET** /analyses/search | Retrieve analyses based on the specified conditions. By default, returns all analyses.
*AnalysisCategoryApi* | [**get_by_path**](docs/api/AnalysisCategoryApi.md#get_by_path) | **GET** /analysiscategories | Retrieve an analysis category by path.
*AnalysisCategoryApi* | [**get**](docs/api/AnalysisCategoryApi.md#get) | **GET** /analysiscategories/{webId} | Retrieve an analysis category.
*AnalysisCategoryApi* | [**update**](docs/api/AnalysisCategoryApi.md#update) | **PATCH** /analysiscategories/{webId} | Update an analysis category by replacing items in its definition.
*AnalysisCategoryApi* | [**delete**](docs/api/AnalysisCategoryApi.md#delete) | **DELETE** /analysiscategories/{webId} | Delete an analysis category.
*AnalysisCategoryApi* | [**get_security**](docs/api/AnalysisCategoryApi.md#get_security) | **GET** /analysiscategories/{webId}/security | Get the security information of the specified security item associated with the analysis category for a specified user.
*AnalysisCategoryApi* | [**get_security_entries**](docs/api/AnalysisCategoryApi.md#get_security_entries) | **GET** /analysiscategories/{webId}/securityentries | Retrieve the security entries associated with the analysis category based on the specified criteria. By default, all security entries for this analysis category are returned.
*AnalysisCategoryApi* | [**create_security_entry**](docs/api/AnalysisCategoryApi.md#create_security_entry) | **POST** /analysiscategories/{webId}/securityentries | Create a security entry owned by the analysis category.
*AnalysisCategoryApi* | [**get_security_entry_by_name**](docs/api/AnalysisCategoryApi.md#get_security_entry_by_name) | **GET** /analysiscategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the analysis category with the specified name.
*AnalysisCategoryApi* | [**update_security_entry**](docs/api/AnalysisCategoryApi.md#update_security_entry) | **PUT** /analysiscategories/{webId}/securityentries/{name} | Update a security entry owned by the analysis category.
*AnalysisCategoryApi* | [**delete_security_entry**](docs/api/AnalysisCategoryApi.md#delete_security_entry) | **DELETE** /analysiscategories/{webId}/securityentries/{name} | Delete a security entry owned by the analysis category.
*AnalysisRulePlugInApi* | [**get_by_path**](docs/api/AnalysisRulePlugInApi.md#get_by_path) | **GET** /analysisruleplugins | Retrieve an Analysis Rule Plug-in by path.
*AnalysisRulePlugInApi* | [**get**](docs/api/AnalysisRulePlugInApi.md#get) | **GET** /analysisruleplugins/{webId} | Retrieve an Analysis Rule Plug-in.
*AnalysisRuleApi* | [**get_by_path**](docs/api/AnalysisRuleApi.md#get_by_path) | **GET** /analysisrules | Retrieve an Analysis Rule by path.
*AnalysisRuleApi* | [**get**](docs/api/AnalysisRuleApi.md#get) | **GET** /analysisrules/{webId} | Retrieve an Analysis Rule.
*AnalysisRuleApi* | [**update**](docs/api/AnalysisRuleApi.md#update) | **PATCH** /analysisrules/{webId} | Update an Analysis Rule by replacing items in its definition.
*AnalysisRuleApi* | [**delete**](docs/api/AnalysisRuleApi.md#delete) | **DELETE** /analysisrules/{webId} | Delete an Analysis Rule.
*AnalysisRuleApi* | [**get_analysis_rules**](docs/api/AnalysisRuleApi.md#get_analysis_rules) | **GET** /analysisrules/{webId}/analysisrules | Get the child Analysis Rules of the Analysis Rule.
*AnalysisRuleApi* | [**create_analysis_rule**](docs/api/AnalysisRuleApi.md#create_analysis_rule) | **POST** /analysisrules/{webId}/analysisrules | Create a new Analysis Rule as a child of an existing Analysis Rule.
*AnalysisTemplateApi* | [**get_by_path**](docs/api/AnalysisTemplateApi.md#get_by_path) | **GET** /analysistemplates | Retrieve an analysis template by path.
*AnalysisTemplateApi* | [**create_from_analysis**](docs/api/AnalysisTemplateApi.md#create_from_analysis) | **POST** /analysistemplates | Create an Analysis template based upon a specified Analysis.
*AnalysisTemplateApi* | [**get**](docs/api/AnalysisTemplateApi.md#get) | **GET** /analysistemplates/{webId} | Retrieve an analysis template.
*AnalysisTemplateApi* | [**update**](docs/api/AnalysisTemplateApi.md#update) | **PATCH** /analysistemplates/{webId} | Update an analysis template by replacing items in its definition.
*AnalysisTemplateApi* | [**delete**](docs/api/AnalysisTemplateApi.md#delete) | **DELETE** /analysistemplates/{webId} | Delete an analysis template.
*AnalysisTemplateApi* | [**get_categories**](docs/api/AnalysisTemplateApi.md#get_categories) | **GET** /analysistemplates/{webId}/categories | Get an analysis template's categories.
*AnalysisTemplateApi* | [**get_security**](docs/api/AnalysisTemplateApi.md#get_security) | **GET** /analysistemplates/{webId}/security | Get the security information of the specified security item associated with the analysis template for a specified user.
*AnalysisTemplateApi* | [**get_security_entries**](docs/api/AnalysisTemplateApi.md#get_security_entries) | **GET** /analysistemplates/{webId}/securityentries | Retrieve the security entries associated with the analysis template based on the specified criteria. By default, all security entries for this analysis template are returned.
*AnalysisTemplateApi* | [**create_security_entry**](docs/api/AnalysisTemplateApi.md#create_security_entry) | **POST** /analysistemplates/{webId}/securityentries | Create a security entry owned by the analysis template.
*AnalysisTemplateApi* | [**get_security_entry_by_name**](docs/api/AnalysisTemplateApi.md#get_security_entry_by_name) | **GET** /analysistemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the analysis template with the specified name.
*AnalysisTemplateApi* | [**update_security_entry**](docs/api/AnalysisTemplateApi.md#update_security_entry) | **PUT** /analysistemplates/{webId}/securityentries/{name} | Update a security entry owned by the analysis template.
*AnalysisTemplateApi* | [**delete_security_entry**](docs/api/AnalysisTemplateApi.md#delete_security_entry) | **DELETE** /analysistemplates/{webId}/securityentries/{name} | Delete a security entry owned by the analysis template.
*AnalysisTemplateApi* | [**get_analysis_templates_query**](docs/api/AnalysisTemplateApi.md#get_analysis_templates_query) | **GET** /analysistemplates/search | Retrieve analysis templates based on the specified conditions. By default, returns all analysis templates.
*AssetDatabaseApi* | [**get_by_path**](docs/api/AssetDatabaseApi.md#get_by_path) | **GET** /assetdatabases | Retrieve an Asset Database by path.
*AssetDatabaseApi* | [**get**](docs/api/AssetDatabaseApi.md#get) | **GET** /assetdatabases/{webId} | Retrieve an Asset Database.
*AssetDatabaseApi* | [**update**](docs/api/AssetDatabaseApi.md#update) | **PATCH** /assetdatabases/{webId} | Update an asset database by replacing items in its definition.
*AssetDatabaseApi* | [**delete**](docs/api/AssetDatabaseApi.md#delete) | **DELETE** /assetdatabases/{webId} | Delete an asset database.
*AssetDatabaseApi* | [**find_analyses**](docs/api/AssetDatabaseApi.md#find_analyses) | **GET** /assetdatabases/{webId}/analyses | Retrieve analyses based on the specified conditions.
*AssetDatabaseApi* | [**get_analysis_categories**](docs/api/AssetDatabaseApi.md#get_analysis_categories) | **GET** /assetdatabases/{webId}/analysiscategories | Retrieve analysis categories for a given Asset Database.
*AssetDatabaseApi* | [**create_analysis_category**](docs/api/AssetDatabaseApi.md#create_analysis_category) | **POST** /assetdatabases/{webId}/analysiscategories | Create an analysis category at the Asset Database root.
*AssetDatabaseApi* | [**get_analysis_templates**](docs/api/AssetDatabaseApi.md#get_analysis_templates) | **GET** /assetdatabases/{webId}/analysistemplates | Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.
*AssetDatabaseApi* | [**create_analysis_template**](docs/api/AssetDatabaseApi.md#create_analysis_template) | **POST** /assetdatabases/{webId}/analysistemplates | Create an analysis template at the Asset Database root.
*AssetDatabaseApi* | [**get_attribute_categories**](docs/api/AssetDatabaseApi.md#get_attribute_categories) | **GET** /assetdatabases/{webId}/attributecategories | Retrieve attribute categories for a given Asset Database.
*AssetDatabaseApi* | [**create_attribute_category**](docs/api/AssetDatabaseApi.md#create_attribute_category) | **POST** /assetdatabases/{webId}/attributecategories | Create an attribute category at the Asset Database root.
*AssetDatabaseApi* | [**find_element_attributes**](docs/api/AssetDatabaseApi.md#find_element_attributes) | **GET** /assetdatabases/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified asset database.
*AssetDatabaseApi* | [**get_element_categories**](docs/api/AssetDatabaseApi.md#get_element_categories) | **GET** /assetdatabases/{webId}/elementcategories | Retrieve element categories for a given Asset Database.
*AssetDatabaseApi* | [**create_element_category**](docs/api/AssetDatabaseApi.md#create_element_category) | **POST** /assetdatabases/{webId}/elementcategories | Create an element category at the Asset Database root.
*AssetDatabaseApi* | [**get_elements**](docs/api/AssetDatabaseApi.md#get_elements) | **GET** /assetdatabases/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.
*AssetDatabaseApi* | [**create_element**](docs/api/AssetDatabaseApi.md#create_element) | **POST** /assetdatabases/{webId}/elements | Create a child element.
*AssetDatabaseApi* | [**get_element_templates**](docs/api/AssetDatabaseApi.md#get_element_templates) | **GET** /assetdatabases/{webId}/elementtemplates | Retrieve element templates based on the specified criteria. Only templates of instance type "Element" and "EventFrame" are returned. By default, all element and event frame templates in the specified Asset Database are returned.
*AssetDatabaseApi* | [**create_element_template**](docs/api/AssetDatabaseApi.md#create_element_template) | **POST** /assetdatabases/{webId}/elementtemplates | Create a template at the Asset Database root. Specify InstanceType of "Element" or "EventFrame" to create element or event frame template respectively. Only these two types of templates can be created.
*AssetDatabaseApi* | [**get_enumeration_sets**](docs/api/AssetDatabaseApi.md#get_enumeration_sets) | **GET** /assetdatabases/{webId}/enumerationsets | Retrieve enumeration sets for given asset database.
*AssetDatabaseApi* | [**create_enumeration_set**](docs/api/AssetDatabaseApi.md#create_enumeration_set) | **POST** /assetdatabases/{webId}/enumerationsets | Create an enumeration set at the Asset Database.
*AssetDatabaseApi* | [**find_event_frame_attributes**](docs/api/AssetDatabaseApi.md#find_event_frame_attributes) | **GET** /assetdatabases/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified asset database.
*AssetDatabaseApi* | [**get_event_frames**](docs/api/AssetDatabaseApi.md#get_event_frames) | **GET** /assetdatabases/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours.
*AssetDatabaseApi* | [**create_event_frame**](docs/api/AssetDatabaseApi.md#create_event_frame) | **POST** /assetdatabases/{webId}/eventframes | Create an event frame.
*AssetDatabaseApi* | [**export**](docs/api/AssetDatabaseApi.md#export) | **GET** /assetdatabases/{webId}/export | Export the asset database.
*AssetDatabaseApi* | [**import_data**](docs/api/AssetDatabaseApi.md#import_data) | **POST** /assetdatabases/{webId}/import | Import an asset database.
*AssetDatabaseApi* | [**get_referenced_elements**](docs/api/AssetDatabaseApi.md#get_referenced_elements) | **GET** /assetdatabases/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.
*AssetDatabaseApi* | [**add_referenced_element**](docs/api/AssetDatabaseApi.md#add_referenced_element) | **POST** /assetdatabases/{webId}/referencedelements | Add a reference to an existing element to the specified database.
*AssetDatabaseApi* | [**remove_referenced_element**](docs/api/AssetDatabaseApi.md#remove_referenced_element) | **DELETE** /assetdatabases/{webId}/referencedelements | Remove a reference to an existing element from the specified database.
*AssetDatabaseApi* | [**get_security**](docs/api/AssetDatabaseApi.md#get_security) | **GET** /assetdatabases/{webId}/security | Get the security information of the specified security item associated with the asset database for a specified user.
*AssetDatabaseApi* | [**get_security_entries**](docs/api/AssetDatabaseApi.md#get_security_entries) | **GET** /assetdatabases/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.
*AssetDatabaseApi* | [**create_security_entry**](docs/api/AssetDatabaseApi.md#create_security_entry) | **POST** /assetdatabases/{webId}/securityentries | Create a security entry owned by the asset database.
*AssetDatabaseApi* | [**get_security_entry_by_name**](docs/api/AssetDatabaseApi.md#get_security_entry_by_name) | **GET** /assetdatabases/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset database with the specified name.
*AssetDatabaseApi* | [**update_security_entry**](docs/api/AssetDatabaseApi.md#update_security_entry) | **PUT** /assetdatabases/{webId}/securityentries/{name} | Update a security entry owned by the asset database.
*AssetDatabaseApi* | [**delete_security_entry**](docs/api/AssetDatabaseApi.md#delete_security_entry) | **DELETE** /assetdatabases/{webId}/securityentries/{name} | Delete a security entry owned by the asset database.
*AssetDatabaseApi* | [**get_table_categories**](docs/api/AssetDatabaseApi.md#get_table_categories) | **GET** /assetdatabases/{webId}/tablecategories | Retrieve table categories for a given Asset Database.
*AssetDatabaseApi* | [**create_table_category**](docs/api/AssetDatabaseApi.md#create_table_category) | **POST** /assetdatabases/{webId}/tablecategories | Create a table category on the Asset Database.
*AssetDatabaseApi* | [**get_tables**](docs/api/AssetDatabaseApi.md#get_tables) | **GET** /assetdatabases/{webId}/tables | Retrieve tables for given Asset Database.
*AssetDatabaseApi* | [**create_table**](docs/api/AssetDatabaseApi.md#create_table) | **POST** /assetdatabases/{webId}/tables | Create a table on the Asset Database.
*AssetServerApi* | [**list**](docs/api/AssetServerApi.md#list) | **GET** /assetservers | Retrieve a list of all Asset Servers known to this service.
*AssetServerApi* | [**get_by_name**](docs/api/AssetServerApi.md#get_by_name) | **GET** /assetservers#name | Retrieve an Asset Server by name.
*AssetServerApi* | [**get_by_path**](docs/api/AssetServerApi.md#get_by_path) | **GET** /assetservers#path | Retrieve an Asset Server by path.
*AssetServerApi* | [**get**](docs/api/AssetServerApi.md#get) | **GET** /assetservers/{webId} | Retrieve an Asset Server.
*AssetServerApi* | [**get_analysis_rule_plug_ins**](docs/api/AssetServerApi.md#get_analysis_rule_plug_ins) | **GET** /assetservers/{webId}/analysisruleplugins | Retrieve a list of all Analysis Rule Plug-in's.
*AssetServerApi* | [**get_databases**](docs/api/AssetServerApi.md#get_databases) | **GET** /assetservers/{webId}/assetdatabases | Retrieve a list of all Asset Databases on the specified Asset Server.
*AssetServerApi* | [**create_asset_database**](docs/api/AssetServerApi.md#create_asset_database) | **POST** /assetservers/{webId}/assetdatabases | Create an asset database.
*AssetServerApi* | [**get_security**](docs/api/AssetServerApi.md#get_security) | **GET** /assetservers/{webId}/security | Get the security information of the specified security item associated with the asset server for a specified user.
*AssetServerApi* | [**get_security_entries**](docs/api/AssetServerApi.md#get_security_entries) | **GET** /assetservers/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.
*AssetServerApi* | [**create_security_entry**](docs/api/AssetServerApi.md#create_security_entry) | **POST** /assetservers/{webId}/securityentries | Create a security entry owned by the asset server.
*AssetServerApi* | [**get_security_entry_by_name**](docs/api/AssetServerApi.md#get_security_entry_by_name) | **GET** /assetservers/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset server with the specified name.
*AssetServerApi* | [**update_security_entry**](docs/api/AssetServerApi.md#update_security_entry) | **PUT** /assetservers/{webId}/securityentries/{name} | Update a security entry owned by the asset server.
*AssetServerApi* | [**delete_security_entry**](docs/api/AssetServerApi.md#delete_security_entry) | **DELETE** /assetservers/{webId}/securityentries/{name} | Delete a security entry owned by the asset server.
*AssetServerApi* | [**get_security_identities**](docs/api/AssetServerApi.md#get_security_identities) | **GET** /assetservers/{webId}/securityidentities | Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.
*AssetServerApi* | [**create_security_identity**](docs/api/AssetServerApi.md#create_security_identity) | **POST** /assetservers/{webId}/securityidentities | Create a security identity.
*AssetServerApi* | [**get_security_identities_for_user**](docs/api/AssetServerApi.md#get_security_identities_for_user) | **GET** /assetservers/{webId}/securityidentities#userIdentity | Retrieve security identities for a specific user.
*AssetServerApi* | [**get_security_mappings**](docs/api/AssetServerApi.md#get_security_mappings) | **GET** /assetservers/{webId}/securitymappings | Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.
*AssetServerApi* | [**create_security_mapping**](docs/api/AssetServerApi.md#create_security_mapping) | **POST** /assetservers/{webId}/securitymappings | Create a security mapping.
*AssetServerApi* | [**get_time_rule_plug_ins**](docs/api/AssetServerApi.md#get_time_rule_plug_ins) | **GET** /assetservers/{webId}/timeruleplugins | Retrieve a list of all Time Rule Plug-in's.
*AssetServerApi* | [**get_unit_classes**](docs/api/AssetServerApi.md#get_unit_classes) | **GET** /assetservers/{webId}/unitclasses | Retrieve a list of all unit classes on the specified Asset Server.
*AssetServerApi* | [**create_unit_class**](docs/api/AssetServerApi.md#create_unit_class) | **POST** /assetservers/{webId}/unitclasses | Create a unit class in the specified Asset Server.
*AttributeCategoryApi* | [**get_by_path**](docs/api/AttributeCategoryApi.md#get_by_path) | **GET** /attributecategories | Retrieve an attribute category by path.
*AttributeCategoryApi* | [**get**](docs/api/AttributeCategoryApi.md#get) | **GET** /attributecategories/{webId} | Retrieve an attribute category.
*AttributeCategoryApi* | [**update**](docs/api/AttributeCategoryApi.md#update) | **PATCH** /attributecategories/{webId} | Update an attribute category by replacing items in its definition.
*AttributeCategoryApi* | [**delete**](docs/api/AttributeCategoryApi.md#delete) | **DELETE** /attributecategories/{webId} | Delete an attribute category.
*AttributeCategoryApi* | [**get_security**](docs/api/AttributeCategoryApi.md#get_security) | **GET** /attributecategories/{webId}/security | Get the security information of the specified security item associated with the attribute category for a specified user.
*AttributeCategoryApi* | [**get_security_entries**](docs/api/AttributeCategoryApi.md#get_security_entries) | **GET** /attributecategories/{webId}/securityentries | Retrieve the security entries associated with the attribute category based on the specified criteria. By default, all security entries for this attribute category are returned.
*AttributeCategoryApi* | [**create_security_entry**](docs/api/AttributeCategoryApi.md#create_security_entry) | **POST** /attributecategories/{webId}/securityentries | Create a security entry owned by the attribute category.
*AttributeCategoryApi* | [**get_security_entry_by_name**](docs/api/AttributeCategoryApi.md#get_security_entry_by_name) | **GET** /attributecategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the attribute category with the specified name.
*AttributeCategoryApi* | [**update_security_entry**](docs/api/AttributeCategoryApi.md#update_security_entry) | **PUT** /attributecategories/{webId}/securityentries/{name} | Update a security entry owned by the attribute category.
*AttributeCategoryApi* | [**delete_security_entry**](docs/api/AttributeCategoryApi.md#delete_security_entry) | **DELETE** /attributecategories/{webId}/securityentries/{name} | Delete a security entry owned by the attribute category.
*AttributeApi* | [**get_by_path**](docs/api/AttributeApi.md#get_by_path) | **GET** /attributes | Retrieve an attribute by path.
*AttributeApi* | [**get**](docs/api/AttributeApi.md#get) | **GET** /attributes/{webId} | Retrieve an attribute.
*AttributeApi* | [**update**](docs/api/AttributeApi.md#update) | **PATCH** /attributes/{webId} | Update an attribute by replacing items in its definition.
*AttributeApi* | [**delete**](docs/api/AttributeApi.md#delete) | **DELETE** /attributes/{webId} | Delete an attribute.
*AttributeApi* | [**get_attributes**](docs/api/AttributeApi.md#get_attributes) | **GET** /attributes/{webId}/attributes | Get the child attributes of the specified attribute.
*AttributeApi* | [**create_attribute**](docs/api/AttributeApi.md#create_attribute) | **POST** /attributes/{webId}/attributes | Create a new attribute as a child of the specified attribute.
*AttributeApi* | [**get_categories**](docs/api/AttributeApi.md#get_categories) | **GET** /attributes/{webId}/categories | Get an attribute's categories.
*AttributeApi* | [**create_config**](docs/api/AttributeApi.md#create_config) | **POST** /attributes/{webId}/config | Create or update an attribute's DataReference configuration (Create/Update PI point for PI Point DataReference).
*AttributeApi* | [**get_value**](docs/api/AttributeApi.md#get_value) | **GET** /attributes/{webId}/value | Get the attribute's value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.
*AttributeApi* | [**set_value**](docs/api/AttributeApi.md#set_value) | **PUT** /attributes/{webId}/value | Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.
*AttributeApi* | [**get_multiple**](docs/api/AttributeApi.md#get_multiple) | **GET** /attributes/multiple | Retrieve multiple attributes by web id or path.
*AttributeApi* | [**get_attributes_query**](docs/api/AttributeApi.md#get_attributes_query) | **GET** /attributes/search | Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string.
*AttributeTemplateApi* | [**get_by_path**](docs/api/AttributeTemplateApi.md#get_by_path) | **GET** /attributetemplates | Retrieve an attribute template by path.
*AttributeTemplateApi* | [**get**](docs/api/AttributeTemplateApi.md#get) | **GET** /attributetemplates/{webId} | Retrieve an attribute template.
*AttributeTemplateApi* | [**update**](docs/api/AttributeTemplateApi.md#update) | **PATCH** /attributetemplates/{webId} | Update an existing attribute template by replacing items in its definition.
*AttributeTemplateApi* | [**delete**](docs/api/AttributeTemplateApi.md#delete) | **DELETE** /attributetemplates/{webId} | Delete an attribute template.
*AttributeTemplateApi* | [**get_attribute_templates**](docs/api/AttributeTemplateApi.md#get_attribute_templates) | **GET** /attributetemplates/{webId}/attributetemplates | Retrieve an attribute template's child attribute templates.
*AttributeTemplateApi* | [**create_attribute_template**](docs/api/AttributeTemplateApi.md#create_attribute_template) | **POST** /attributetemplates/{webId}/attributetemplates | Create an attribute template as a child of another attribute template.
*AttributeTemplateApi* | [**get_categories**](docs/api/AttributeTemplateApi.md#get_categories) | **GET** /attributetemplates/{webId}/categories | Get an attribute template's categories.
*AttributeTraitApi* | [**get_by_category**](docs/api/AttributeTraitApi.md#get_by_category) | **GET** /attributetraits | Retrieve all attribute traits of the specified category/categories.
*AttributeTraitApi* | [**get**](docs/api/AttributeTraitApi.md#get) | **GET** /attributetraits/{name} | Retrieve an attribute trait.
*BatchApi* | [**execute**](docs/api/BatchApi.md#execute) | **POST** /batch | Execute a batch of requests against the service. As shown in the Sample Request, the input is a dictionary with IDs as keys and request objects as values. Each request object specifies the HTTP method and the resource and, optionally, the content and a list of parent IDs. The list of parent IDs specifies which other requests must complete before the given request will be executed. The example first creates an element, then gets the element by the response's Location header, then creates an attribute for the element. Note that the resource can be an absolute URL or a JsonPath that references the response to the parent request. The batch's response is a dictionary uses keys corresponding those provided in the request, with response objects containing a status code, response headers, and the response body. A request can alternatively specify a request template in place of a resource. In this case, a single JsonPath may select multiple tokens, and a separate subrequest will be made from the template for each token. The responses of these subrequests will returned as the content of a single outer response.
*CalculationApi* | [**get_at_intervals**](docs/api/CalculationApi.md#get_at_intervals) | **GET** /calculation/intervals | Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.
*CalculationApi* | [**get_at_recorded**](docs/api/CalculationApi.md#get_at_recorded) | **GET** /calculation/recorded | Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.
*CalculationApi* | [**get_summary**](docs/api/CalculationApi.md#get_summary) | **GET** /calculation/summary | Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.
*CalculationApi* | [**get_at_times**](docs/api/CalculationApi.md#get_at_times) | **GET** /calculation/times | Returns the result of evaluating the expression at the specified timestamps.
*ChannelApi* | [**instances**](docs/api/ChannelApi.md#instances) | **GET** /channels/instances | Retrieves a list of currently running channel instances.
*DataApi* | [**get_recorded_values**](docs/api/DataApi.md#get_recorded_values) |  Returns a pandas dataframe with compressed values for the requested time range from the source provider.
*DataApi* | [**get_interpolated_values**](docs/api/DataApi.md#get_interpolated_values) | Retrieves a pandas dataframe with interpolated values over the specified time range at the specified sampling interval.
*DataApi* | [**get_plot_values**](docs/api/DataApi.md#get_plot_values*) | Retrieves a pandas dataframe with values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
*DataApi* | [**get_multiple_recorded_values**](docs/api/DataApi.md#get_multiple_recorded_values) | Returns an array of pandas dataframe with recorded values of the specified streams.
*DataApi* | [**get_multiple_interpolated_values**](docs/api/DataApi.md#get_multiple_interpolated_values) | Returns a dataframe with interpolated values of the specified streams over the specified time range at the specified sampling interval..
*DataApi* | [**get_multiple_plot_values**](docs/api/DataApi.md#get_multiple_plot_values) |  Returns a pandas dataframe with values of the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
*DataServerApi* | [**list**](docs/api/DataServerApi.md#list) | **GET** /dataservers | Retrieve a list of Data Servers known to this service.
*DataServerApi* | [**get_by_name**](docs/api/DataServerApi.md#get_by_name) | **GET** /dataservers#name | Retrieve a Data Server by name.
*DataServerApi* | [**get_by_path**](docs/api/DataServerApi.md#get_by_path) | **GET** /dataservers#path | Retrieve a Data Server by path.
*DataServerApi* | [**get**](docs/api/DataServerApi.md#get) | **GET** /dataservers/{webId} | Retrieve a Data Server.
*DataServerApi* | [**get_enumeration_sets**](docs/api/DataServerApi.md#get_enumeration_sets) | **GET** /dataservers/{webId}/enumerationsets | Retrieve enumeration sets for given Data Server.
*DataServerApi* | [**create_enumeration_set**](docs/api/DataServerApi.md#create_enumeration_set) | **POST** /dataservers/{webId}/enumerationsets | Create an enumeration set on the Data Server.
*DataServerApi* | [**get_license**](docs/api/DataServerApi.md#get_license) | **GET** /dataservers/{webId}/license | Retrieves the specified license for the given Data Server. The fields of the response object are string representations of the numerical values reported by the Data Server, with "Infinity" representing a license field with no limit.
*DataServerApi* | [**get_points**](docs/api/DataServerApi.md#get_points) | **GET** /dataservers/{webId}/points | Retrieve a list of points on a specified Data Server.
*DataServerApi* | [**create_point**](docs/api/DataServerApi.md#create_point) | **POST** /dataservers/{webId}/points | Create a point in the specified Data Server.
*ElementCategoryApi* | [**get_by_path**](docs/api/ElementCategoryApi.md#get_by_path) | **GET** /elementcategories | Retrieve an element category by path.
*ElementCategoryApi* | [**get**](docs/api/ElementCategoryApi.md#get) | **GET** /elementcategories/{webId} | Retrieve an element category.
*ElementCategoryApi* | [**update**](docs/api/ElementCategoryApi.md#update) | **PATCH** /elementcategories/{webId} | Update an element category by replacing items in its definition.
*ElementCategoryApi* | [**delete**](docs/api/ElementCategoryApi.md#delete) | **DELETE** /elementcategories/{webId} | Delete an element category.
*ElementCategoryApi* | [**get_security**](docs/api/ElementCategoryApi.md#get_security) | **GET** /elementcategories/{webId}/security | Get the security information of the specified security item associated with the element category for a specified user.
*ElementCategoryApi* | [**get_security_entries**](docs/api/ElementCategoryApi.md#get_security_entries) | **GET** /elementcategories/{webId}/securityentries | Retrieve the security entries associated with the element category based on the specified criteria. By default, all security entries for this element category are returned.
*ElementCategoryApi* | [**create_security_entry**](docs/api/ElementCategoryApi.md#create_security_entry) | **POST** /elementcategories/{webId}/securityentries | Create a security entry owned by the element category.
*ElementCategoryApi* | [**get_security_entry_by_name**](docs/api/ElementCategoryApi.md#get_security_entry_by_name) | **GET** /elementcategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the element category with the specified name.
*ElementCategoryApi* | [**update_security_entry**](docs/api/ElementCategoryApi.md#update_security_entry) | **PUT** /elementcategories/{webId}/securityentries/{name} | Update a security entry owned by the element category.
*ElementCategoryApi* | [**delete_security_entry**](docs/api/ElementCategoryApi.md#delete_security_entry) | **DELETE** /elementcategories/{webId}/securityentries/{name} | Delete a security entry owned by the element category.
*ElementApi* | [**get_by_path**](docs/api/ElementApi.md#get_by_path) | **GET** /elements | Retrieve an element by path.
*ElementApi* | [**get**](docs/api/ElementApi.md#get) | **GET** /elements/{webId} | Retrieve an element.
*ElementApi* | [**update**](docs/api/ElementApi.md#update) | **PATCH** /elements/{webId} | Update an element by replacing items in its definition.
*ElementApi* | [**delete**](docs/api/ElementApi.md#delete) | **DELETE** /elements/{webId} | Delete an element.
*ElementApi* | [**get_analyses**](docs/api/ElementApi.md#get_analyses) | **GET** /elements/{webId}/analyses | Retrieve analyses based on the specified conditions.
*ElementApi* | [**create_analysis**](docs/api/ElementApi.md#create_analysis) | **POST** /elements/{webId}/analyses | Create an Analysis.
*ElementApi* | [**get_attributes**](docs/api/ElementApi.md#get_attributes) | **GET** /elements/{webId}/attributes | Get the attributes of the specified element.
*ElementApi* | [**create_attribute**](docs/api/ElementApi.md#create_attribute) | **POST** /elements/{webId}/attributes | Create a new attribute of the specified element.
*ElementApi* | [**get_categories**](docs/api/ElementApi.md#get_categories) | **GET** /elements/{webId}/categories | Get an element's categories.
*ElementApi* | [**create_config**](docs/api/ElementApi.md#create_config) | **POST** /elements/{webId}/config | Executes the create configuration function of the data references found within the attributes of the element, and optionally, its children.
*ElementApi* | [**find_element_attributes**](docs/api/ElementApi.md#find_element_attributes) | **GET** /elements/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified element.
*ElementApi* | [**get_elements**](docs/api/ElementApi.md#get_elements) | **GET** /elements/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified element.
*ElementApi* | [**create_element**](docs/api/ElementApi.md#create_element) | **POST** /elements/{webId}/elements | Create a child element.
*ElementApi* | [**get_event_frames**](docs/api/ElementApi.md#get_event_frames) | **GET** /elements/{webId}/eventframes | Retrieve event frames that reference this element based on the specified conditions. By default, returns all event frames that reference this element that have been active in the past 8 hours.
*ElementApi* | [**get_referenced_elements**](docs/api/ElementApi.md#get_referenced_elements) | **GET** /elements/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements of the current resource.
*ElementApi* | [**add_referenced_element**](docs/api/ElementApi.md#add_referenced_element) | **POST** /elements/{webId}/referencedelements | Add a reference to an existing element to the child elements collection.
*ElementApi* | [**remove_referenced_element**](docs/api/ElementApi.md#remove_referenced_element) | **DELETE** /elements/{webId}/referencedelements | Remove a reference to an existing element from the child elements collection.
*ElementApi* | [**get_security**](docs/api/ElementApi.md#get_security) | **GET** /elements/{webId}/security | Get the security information of the specified security item associated with the element for a specified user.
*ElementApi* | [**get_security_entries**](docs/api/ElementApi.md#get_security_entries) | **GET** /elements/{webId}/securityentries | Retrieve the security entries associated with the element based on the specified criteria. By default, all security entries for this element are returned.
*ElementApi* | [**create_security_entry**](docs/api/ElementApi.md#create_security_entry) | **POST** /elements/{webId}/securityentries | Create a security entry owned by the element.
*ElementApi* | [**get_security_entry_by_name**](docs/api/ElementApi.md#get_security_entry_by_name) | **GET** /elements/{webId}/securityentries/{name} | Retrieve the security entry associated with the element with the specified name.
*ElementApi* | [**update_security_entry**](docs/api/ElementApi.md#update_security_entry) | **PUT** /elements/{webId}/securityentries/{name} | Update a security entry owned by the element.
*ElementApi* | [**delete_security_entry**](docs/api/ElementApi.md#delete_security_entry) | **DELETE** /elements/{webId}/securityentries/{name} | Delete a security entry owned by the element.
*ElementApi* | [**get_multiple**](docs/api/ElementApi.md#get_multiple) | **GET** /elements/multiple | Retrieve multiple elements by web id or path.
*ElementApi* | [**get_elements_query**](docs/api/ElementApi.md#get_elements_query) | **GET** /elements/search | Retrieve elements based on the specified conditions. By default, returns all the elements.
*ElementApi* | [**create_search_by_attribute**](docs/api/ElementApi.md#create_search_by_attribute) | **POST** /elements/searchbyattribute | Create a link for a "Search Elements By Attribute Value" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root Element. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the Elements. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
*ElementApi* | [**execute_search_by_attribute**](docs/api/ElementApi.md#execute_search_by_attribute) | **GET** /elements/searchbyattribute/{searchId} | Execute a "Search Elements By Attribute Value" operation.
*ElementTemplateApi* | [**get_by_path**](docs/api/ElementTemplateApi.md#get_by_path) | **GET** /elementtemplates | Retrieve an element template by path.
*ElementTemplateApi* | [**get**](docs/api/ElementTemplateApi.md#get) | **GET** /elementtemplates/{webId} | Retrieve an element template.
*ElementTemplateApi* | [**update**](docs/api/ElementTemplateApi.md#update) | **PATCH** /elementtemplates/{webId} | Update an element template by replacing items in its definition.
*ElementTemplateApi* | [**delete**](docs/api/ElementTemplateApi.md#delete) | **DELETE** /elementtemplates/{webId} | Delete an element template.
*ElementTemplateApi* | [**get_analysis_templates**](docs/api/ElementTemplateApi.md#get_analysis_templates) | **GET** /elementtemplates/{webId}/analysistemplates | Get analysis templates for an element template.
*ElementTemplateApi* | [**get_attribute_templates**](docs/api/ElementTemplateApi.md#get_attribute_templates) | **GET** /elementtemplates/{webId}/attributetemplates | Get child attribute templates for an element template.
*ElementTemplateApi* | [**create_attribute_template**](docs/api/ElementTemplateApi.md#create_attribute_template) | **POST** /elementtemplates/{webId}/attributetemplates | Create an attribute template.
*ElementTemplateApi* | [**get_categories**](docs/api/ElementTemplateApi.md#get_categories) | **GET** /elementtemplates/{webId}/categories | Get an element template's categories.
*ElementTemplateApi* | [**get_security**](docs/api/ElementTemplateApi.md#get_security) | **GET** /elementtemplates/{webId}/security | Get the security information of the specified security item associated with the element template for a specified user.
*ElementTemplateApi* | [**get_security_entries**](docs/api/ElementTemplateApi.md#get_security_entries) | **GET** /elementtemplates/{webId}/securityentries | Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.
*ElementTemplateApi* | [**create_security_entry**](docs/api/ElementTemplateApi.md#create_security_entry) | **POST** /elementtemplates/{webId}/securityentries | Create a security entry owned by the element template.
*ElementTemplateApi* | [**get_security_entry_by_name**](docs/api/ElementTemplateApi.md#get_security_entry_by_name) | **GET** /elementtemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the element template with the specified name.
*ElementTemplateApi* | [**update_security_entry**](docs/api/ElementTemplateApi.md#update_security_entry) | **PUT** /elementtemplates/{webId}/securityentries/{name} | Update a security entry owned by the element template.
*ElementTemplateApi* | [**delete_security_entry**](docs/api/ElementTemplateApi.md#delete_security_entry) | **DELETE** /elementtemplates/{webId}/securityentries/{name} | Delete a security entry owned by the element template.
*EnumerationSetApi* | [**get_by_path**](docs/api/EnumerationSetApi.md#get_by_path) | **GET** /enumerationsets | Retrieve an enumeration set by path.
*EnumerationSetApi* | [**get**](docs/api/EnumerationSetApi.md#get) | **GET** /enumerationsets/{webId} | Retrieve an enumeration set.
*EnumerationSetApi* | [**update**](docs/api/EnumerationSetApi.md#update) | **PATCH** /enumerationsets/{webId} | Update an enumeration set by replacing items in its definition.
*EnumerationSetApi* | [**delete**](docs/api/EnumerationSetApi.md#delete) | **DELETE** /enumerationsets/{webId} | Delete an enumeration set.
*EnumerationSetApi* | [**get_values**](docs/api/EnumerationSetApi.md#get_values) | **GET** /enumerationsets/{webId}/enumerationvalues | Retrieve an enumeration set's values.
*EnumerationSetApi* | [**create_value**](docs/api/EnumerationSetApi.md#create_value) | **POST** /enumerationsets/{webId}/enumerationvalues | Create an enumeration value for a enumeration set.
*EnumerationSetApi* | [**get_security**](docs/api/EnumerationSetApi.md#get_security) | **GET** /enumerationsets/{webId}/security | Get the security information of the specified security item associated with the enumeration set for a specified user.
*EnumerationSetApi* | [**get_security_entries**](docs/api/EnumerationSetApi.md#get_security_entries) | **GET** /enumerationsets/{webId}/securityentries | Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.
*EnumerationSetApi* | [**create_security_entry**](docs/api/EnumerationSetApi.md#create_security_entry) | **POST** /enumerationsets/{webId}/securityentries | Create a security entry owned by the enumeration set.
*EnumerationSetApi* | [**get_security_entry_by_name**](docs/api/EnumerationSetApi.md#get_security_entry_by_name) | **GET** /enumerationsets/{webId}/securityentries/{name} | Retrieve the security entry associated with the enumeration set with the specified name.
*EnumerationSetApi* | [**update_security_entry**](docs/api/EnumerationSetApi.md#update_security_entry) | **PUT** /enumerationsets/{webId}/securityentries/{name} | Update a security entry owned by the enumeration set.
*EnumerationSetApi* | [**delete_security_entry**](docs/api/EnumerationSetApi.md#delete_security_entry) | **DELETE** /enumerationsets/{webId}/securityentries/{name} | Delete a security entry owned by the enumeration set.
*EnumerationValueApi* | [**get_by_path**](docs/api/EnumerationValueApi.md#get_by_path) | **GET** /enumerationvalues | Retrieve an enumeration value by path.
*EnumerationValueApi* | [**get**](docs/api/EnumerationValueApi.md#get) | **GET** /enumerationvalues/{webId} | Retrieve an enumeration value mapping
*EnumerationValueApi* | [**update_enumeration_value**](docs/api/EnumerationValueApi.md#update_enumeration_value) | **PATCH** /enumerationvalues/{webId} | Update an enumeration value by replacing items in its definition.
*EnumerationValueApi* | [**delete_enumeration_value**](docs/api/EnumerationValueApi.md#delete_enumeration_value) | **DELETE** /enumerationvalues/{webId} | Delete an enumeration value from an enumeration set.
*EventFrameApi* | [**get_by_path**](docs/api/EventFrameApi.md#get_by_path) | **GET** /eventframes | Retrieve an event frame by path.
*EventFrameApi* | [**get**](docs/api/EventFrameApi.md#get) | **GET** /eventframes/{webId} | Retrieve an event frame.
*EventFrameApi* | [**update**](docs/api/EventFrameApi.md#update) | **PATCH** /eventframes/{webId} | Update an event frame by replacing items in its definition.
*EventFrameApi* | [**delete**](docs/api/EventFrameApi.md#delete) | **DELETE** /eventframes/{webId} | Delete an event frame.
*EventFrameApi* | [**acknowledge**](docs/api/EventFrameApi.md#acknowledge) | **PATCH** /eventframes/{webId}/acknowledge | Calls the EventFrame's Acknowledge method.
*EventFrameApi* | [**get_annotations**](docs/api/EventFrameApi.md#get_annotations) | **GET** /eventframes/{webId}/annotations | Get an event frame's annotations.
*EventFrameApi* | [**create_annotation**](docs/api/EventFrameApi.md#create_annotation) | **POST** /eventframes/{webId}/annotations | Create an annotation on an event frame.
*EventFrameApi* | [**get_annotation_by_id**](docs/api/EventFrameApi.md#get_annotation_by_id) | **GET** /eventframes/{webId}/annotations/{id} | Get a specific annotation on an event frame.
*EventFrameApi* | [**update_annotation**](docs/api/EventFrameApi.md#update_annotation) | **PATCH** /eventframes/{webId}/annotations/{id} | Update an annotation on an event frame by replacing items in its definition.
*EventFrameApi* | [**delete_annotation**](docs/api/EventFrameApi.md#delete_annotation) | **DELETE** /eventframes/{webId}/annotations/{id} | Delete an annotation on an event frame.
*EventFrameApi* | [**get_attributes**](docs/api/EventFrameApi.md#get_attributes) | **GET** /eventframes/{webId}/attributes | Get the attributes of the specified event frame.
*EventFrameApi* | [**create_attribute**](docs/api/EventFrameApi.md#create_attribute) | **POST** /eventframes/{webId}/attributes | Create a new attribute of the specified event frame.
*EventFrameApi* | [**capture_values**](docs/api/EventFrameApi.md#capture_values) | **POST** /eventframes/{webId}/attributes/capture | Calls the EventFrame's CaptureValues method.
*EventFrameApi* | [**get_categories**](docs/api/EventFrameApi.md#get_categories) | **GET** /eventframes/{webId}/categories | Get an event frame's categories.
*EventFrameApi* | [**create_config**](docs/api/EventFrameApi.md#create_config) | **POST** /eventframes/{webId}/config | Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.
*EventFrameApi* | [**find_event_frame_attributes**](docs/api/EventFrameApi.md#find_event_frame_attributes) | **GET** /eventframes/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified event frame.
*EventFrameApi* | [**get_event_frames**](docs/api/EventFrameApi.md#get_event_frames) | **GET** /eventframes/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours.
*EventFrameApi* | [**create_event_frame**](docs/api/EventFrameApi.md#create_event_frame) | **POST** /eventframes/{webId}/eventframes | Create an event frame as a child of the specified event frame.
*EventFrameApi* | [**get_referenced_elements**](docs/api/EventFrameApi.md#get_referenced_elements) | **GET** /eventframes/{webId}/referencedelements | Retrieve the event frame's referenced elements.
*EventFrameApi* | [**get_security**](docs/api/EventFrameApi.md#get_security) | **GET** /eventframes/{webId}/security | Get the security information of the specified security item associated with the event frame for a specified user.
*EventFrameApi* | [**get_security_entries**](docs/api/EventFrameApi.md#get_security_entries) | **GET** /eventframes/{webId}/securityentries | Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.
*EventFrameApi* | [**create_security_entry**](docs/api/EventFrameApi.md#create_security_entry) | **POST** /eventframes/{webId}/securityentries | Create a security entry owned by the event frame.
*EventFrameApi* | [**get_security_entry_by_name**](docs/api/EventFrameApi.md#get_security_entry_by_name) | **GET** /eventframes/{webId}/securityentries/{name} | Retrieve the security entry associated with the event frame with the specified name.
*EventFrameApi* | [**update_security_entry**](docs/api/EventFrameApi.md#update_security_entry) | **PUT** /eventframes/{webId}/securityentries/{name} | Update a security entry owned by the event frame.
*EventFrameApi* | [**delete_security_entry**](docs/api/EventFrameApi.md#delete_security_entry) | **DELETE** /eventframes/{webId}/securityentries/{name} | Delete a security entry owned by the event frame.
*EventFrameApi* | [**get_multiple**](docs/api/EventFrameApi.md#get_multiple) | **GET** /eventframes/multiple | Retrieve multiple event frames by web ids or paths.
*EventFrameApi* | [**get_event_frames_query**](docs/api/EventFrameApi.md#get_event_frames_query) | **GET** /eventframes/search | Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string.
*EventFrameApi* | [**create_search_by_attribute**](docs/api/EventFrameApi.md#create_search_by_attribute) | **POST** /eventframes/searchbyattribute | Create a link for a "Search EventFrames By Attribute Value" operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
*EventFrameApi* | [**execute_search_by_attribute**](docs/api/EventFrameApi.md#execute_search_by_attribute) | **GET** /eventframes/searchbyattribute/{searchId} | Execute a "Search EventFrames By Attribute Value" operation.
*PointApi* | [**get_by_path**](docs/api/PointApi.md#get_by_path) | **GET** /points | Get a point by path.
*PointApi* | [**get**](docs/api/PointApi.md#get) | **GET** /points/{webId} | Get a point.
*PointApi* | [**update**](docs/api/PointApi.md#update) | **PATCH** /points/{webId} | Update a point.
*PointApi* | [**delete**](docs/api/PointApi.md#delete) | **DELETE** /points/{webId} | Delete a point.
*PointApi* | [**get_attributes**](docs/api/PointApi.md#get_attributes) | **GET** /points/{webId}/attributes | Get point attributes.
*PointApi* | [**get_attribute_by_name**](docs/api/PointApi.md#get_attribute_by_name) | **GET** /points/{webId}/attributes/{name} | Get a point attribute by name.
*PointApi* | [**get_multiple**](docs/api/PointApi.md#get_multiple) | **GET** /points/multiple | Retrieve multiple points by web id or path.
*SecurityIdentityApi* | [**get_by_path**](docs/api/SecurityIdentityApi.md#get_by_path) | **GET** /securityidentities | Retrieve a security identity by path.
*SecurityIdentityApi* | [**get**](docs/api/SecurityIdentityApi.md#get) | **GET** /securityidentities/{webId} | Retrieve a security identity.
*SecurityIdentityApi* | [**update**](docs/api/SecurityIdentityApi.md#update) | **PATCH** /securityidentities/{webId} | Update a security identity by replacing items in its definition.
*SecurityIdentityApi* | [**delete**](docs/api/SecurityIdentityApi.md#delete) | **DELETE** /securityidentities/{webId} | Delete a security identity.
*SecurityIdentityApi* | [**get_security**](docs/api/SecurityIdentityApi.md#get_security) | **GET** /securityidentities/{webId}/security | Get the security information of the specified security item associated with the security identity for a specified user.
*SecurityIdentityApi* | [**get_security_entries**](docs/api/SecurityIdentityApi.md#get_security_entries) | **GET** /securityidentities/{webId}/securityentries | Retrieve the security entries associated with the security identity based on the specified criteria. By default, all security entries for this security identity are returned.
*SecurityIdentityApi* | [**get_security_entry_by_name**](docs/api/SecurityIdentityApi.md#get_security_entry_by_name) | **GET** /securityidentities/{webId}/securityentries/{name} | Retrieve the security entry associated with the security identity with the specified name.
*SecurityIdentityApi* | [**get_security_mappings**](docs/api/SecurityIdentityApi.md#get_security_mappings) | **GET** /securityidentities/{webId}/securitymappings | Get security mappings for the specified security identity.
*SecurityMappingApi* | [**get_by_path**](docs/api/SecurityMappingApi.md#get_by_path) | **GET** /securitymappings | Retrieve a security mapping by path.
*SecurityMappingApi* | [**get**](docs/api/SecurityMappingApi.md#get) | **GET** /securitymappings/{webId} | Retrieve a security mapping.
*SecurityMappingApi* | [**update**](docs/api/SecurityMappingApi.md#update) | **PATCH** /securitymappings/{webId} | Update a security mapping by replacing items in its definition.
*SecurityMappingApi* | [**delete**](docs/api/SecurityMappingApi.md#delete) | **DELETE** /securitymappings/{webId} | Delete a security mapping.
*SecurityMappingApi* | [**get_security**](docs/api/SecurityMappingApi.md#get_security) | **GET** /securitymappings/{webId}/security | Get the security information of the specified security item associated with the security mapping for a specified user.
*SecurityMappingApi* | [**get_security_entries**](docs/api/SecurityMappingApi.md#get_security_entries) | **GET** /securitymappings/{webId}/securityentries | Retrieve the security entries associated with the security mapping based on the specified criteria. By default, all security entries for this security mapping are returned.
*SecurityMappingApi* | [**get_security_entry_by_name**](docs/api/SecurityMappingApi.md#get_security_entry_by_name) | **GET** /securitymappings/{webId}/securityentries/{name} | Retrieve the security entry associated with the security mapping with the specified name.
*StreamApi* | [**get_channel**](docs/api/StreamApi.md#get_channel) | **GET** /streams/{webId}/channel | Opens a channel that will send messages about any value changes for the specified stream.
*StreamApi* | [**get_end**](docs/api/StreamApi.md#get_end) | **GET** /streams/{webId}/end | Returns the end-of-stream value of the stream.
*StreamApi* | [**get_interpolated**](docs/api/StreamApi.md#get_interpolated) | **GET** /streams/{webId}/interpolated | Retrieves interpolated values over the specified time range at the specified sampling interval.
*StreamApi* | [**get_interpolated_at_times**](docs/api/StreamApi.md#get_interpolated_at_times) | **GET** /streams/{webId}/interpolatedattimes | Retrieves interpolated values over the specified time range at the specified sampling interval.
*StreamApi* | [**get_plot**](docs/api/StreamApi.md#get_plot) | **GET** /streams/{webId}/plot | Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
*StreamApi* | [**get_recorded**](docs/api/StreamApi.md#get_recorded) | **GET** /streams/{webId}/recorded | Returns a list of compressed values for the requested time range from the source provider.
*StreamApi* | [**update_values**](docs/api/StreamApi.md#update_values) | **POST** /streams/{webId}/recorded | Updates multiple values for the specified stream.
*StreamApi* | [**get_recorded_at_time**](docs/api/StreamApi.md#get_recorded_at_time) | **GET** /streams/{webId}/recordedattime | Returns a single recorded value based on the passed time and retrieval mode from the stream.
*StreamApi* | [**get_recorded_at_times**](docs/api/StreamApi.md#get_recorded_at_times) | **GET** /streams/{webId}/recordedattimes | Retrieves recorded values at the specified times.
*StreamApi* | [**get_summary**](docs/api/StreamApi.md#get_summary) | **GET** /streams/{webId}/summary | Returns a summary over the specified time range for the stream.
*StreamApi* | [**get_value**](docs/api/StreamApi.md#get_value) | **GET** /streams/{webId}/value | Returns the value of the stream at the specified time. By default, this is usually the current value.
*StreamApi* | [**update_value**](docs/api/StreamApi.md#update_value) | **POST** /streams/{webId}/value | Updates a value for the specified stream.
*StreamSetApi* | [**get_channel**](docs/api/StreamSetApi.md#get_channel) | **GET** /streamsets/{webId}/channel | Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.
*StreamSetApi* | [**get_end**](docs/api/StreamSetApi.md#get_end) | **GET** /streamsets/{webId}/end | Returns End of stream values of the attributes for an Element, Event Frame or Attribute
*StreamSetApi* | [**get_interpolated**](docs/api/StreamSetApi.md#get_interpolated) | **GET** /streamsets/{webId}/interpolated | Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.
*StreamSetApi* | [**get_interpolated_at_times**](docs/api/StreamSetApi.md#get_interpolated_at_times) | **GET** /streamsets/{webId}/interpolatedattimes | Returns interpolated values of attributes for an element, event frame or attribute at the specified times.
*StreamSetApi* | [**get_plot**](docs/api/StreamSetApi.md#get_plot) | **GET** /streamsets/{webId}/plot | Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
*StreamSetApi* | [**get_recorded**](docs/api/StreamSetApi.md#get_recorded) | **GET** /streamsets/{webId}/recorded | Returns recorded values of the attributes for an element, event frame, or attribute.
*StreamSetApi* | [**update_values**](docs/api/StreamSetApi.md#update_values) | **POST** /streamsets/{webId}/recorded | Updates multiple values for the specified streams.
*StreamSetApi* | [**get_recorded_at_time**](docs/api/StreamSetApi.md#get_recorded_at_time) | **GET** /streamsets/{webId}/recordedattime | Returns recorded values of the attributes for an element, event frame, or attribute.
*StreamSetApi* | [**get_recorded_at_times**](docs/api/StreamSetApi.md#get_recorded_at_times) | **GET** /streamsets/{webId}/recordedattimes | Returns recorded values of attributes for an element, event frame or attribute at the specified times.
*StreamSetApi* | [**get_summaries**](docs/api/StreamSetApi.md#get_summaries) | **GET** /streamsets/{webId}/summary | Returns summary values of the attributes for an element, event frame or attribute.
*StreamSetApi* | [**get_values**](docs/api/StreamSetApi.md#get_values) | **GET** /streamsets/{webId}/value | Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.
*StreamSetApi* | [**update_value**](docs/api/StreamSetApi.md#update_value) | **POST** /streamsets/{webId}/value | Updates a single value for the specified streams.
*StreamSetApi* | [**get_channel_ad_hoc**](docs/api/StreamSetApi.md#get_channel_ad_hoc) | **GET** /streamsets/channel | Opens a channel that will send messages about any value changes for the specified streams.
*StreamSetApi* | [**get_end_ad_hoc**](docs/api/StreamSetApi.md#get_end_ad_hoc) | **GET** /streamsets/end | Returns End Of Stream values for attributes of the specified streams
*StreamSetApi* | [**get_interpolated_ad_hoc**](docs/api/StreamSetApi.md#get_interpolated_ad_hoc) | **GET** /streamsets/interpolated | Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.
*StreamSetApi* | [**get_interpolated_at_times_ad_hoc**](docs/api/StreamSetApi.md#get_interpolated_at_times_ad_hoc) | **GET** /streamsets/interpolatedattimes | Returns interpolated values of the specified streams at the specified times.
*StreamSetApi* | [**get_plot_ad_hoc**](docs/api/StreamSetApi.md#get_plot_ad_hoc) | **GET** /streamsets/plot | Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
*StreamSetApi* | [**get_recorded_ad_hoc**](docs/api/StreamSetApi.md#get_recorded_ad_hoc) | **GET** /streamsets/recorded | Returns recorded values of the specified streams.
*StreamSetApi* | [**update_values_ad_hoc**](docs/api/StreamSetApi.md#update_values_ad_hoc) | **POST** /streamsets/recorded | Updates multiple values for the specified streams.
*StreamSetApi* | [**get_recorded_at_time_ad_hoc**](docs/api/StreamSetApi.md#get_recorded_at_time_ad_hoc) | **GET** /streamsets/recordedattime | Returns recorded values based on the passed time and retrieval mode.
*StreamSetApi* | [**get_recorded_at_times_ad_hoc**](docs/api/StreamSetApi.md#get_recorded_at_times_ad_hoc) | **GET** /streamsets/recordedattimes | Returns recorded values of the specified streams at the specified times.
*StreamSetApi* | [**get_summaries_ad_hoc**](docs/api/StreamSetApi.md#get_summaries_ad_hoc) | **GET** /streamsets/summary | Returns summary values of the specified streams.
*StreamSetApi* | [**get_values_ad_hoc**](docs/api/StreamSetApi.md#get_values_ad_hoc) | **GET** /streamsets/value | Returns values of the specified streams.
*StreamSetApi* | [**update_value_ad_hoc**](docs/api/StreamSetApi.md#update_value_ad_hoc) | **POST** /streamsets/value | Updates a single value for the specified streams.
*SystemApi* | [**landing**](docs/api/SystemApi.md#landing) | **GET** /system | Get system links for this PI System Web API instance.
*SystemApi* | [**cache_instances**](docs/api/SystemApi.md#cache_instances) | **GET** /system/cacheinstances | Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service's authentication method, and the cache instance configuration.
*SystemApi* | [**status**](docs/api/SystemApi.md#status) | **GET** /system/status | Get the system uptime, the system state and the number of cache instances for this PI System Web API instance.
*SystemApi* | [**user_info**](docs/api/SystemApi.md#user_info) | **GET** /system/userinfo | Get information about the Windows identity used to fulfill the request. This depends on the service's authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.
*SystemApi* | [**versions**](docs/api/SystemApi.md#versions) | **GET** /system/versions | Get the current versions of the PI Web API instance and all external plugins.
*ConfigurationApi* | [**list**](docs/api/ConfigurationApi.md#list) | **GET** /system/configuration | Get the current system configuration.
*ConfigurationApi* | [**get**](docs/api/ConfigurationApi.md#get) | **GET** /system/configuration/{key} | Get the value of a configuration item.
*ConfigurationApi* | [**delete**](docs/api/ConfigurationApi.md#delete) | **DELETE** /system/configuration/{key} | Delete a configuration item.
*TableCategoryApi* | [**get_by_path**](docs/api/TableCategoryApi.md#get_by_path) | **GET** /tablecategories | Retrieve a table category by path.
*TableCategoryApi* | [**get**](docs/api/TableCategoryApi.md#get) | **GET** /tablecategories/{webId} | Retrieve a table category.
*TableCategoryApi* | [**update**](docs/api/TableCategoryApi.md#update) | **PATCH** /tablecategories/{webId} | Update a table category by replacing items in its definition.
*TableCategoryApi* | [**delete**](docs/api/TableCategoryApi.md#delete) | **DELETE** /tablecategories/{webId} | Delete a table category.
*TableCategoryApi* | [**get_security**](docs/api/TableCategoryApi.md#get_security) | **GET** /tablecategories/{webId}/security | Get the security information of the specified security item associated with the table category for a specified user.
*TableCategoryApi* | [**get_security_entries**](docs/api/TableCategoryApi.md#get_security_entries) | **GET** /tablecategories/{webId}/securityentries | Retrieve the security entries associated with the table category based on the specified criteria. By default, all security entries for this table category are returned.
*TableCategoryApi* | [**create_security_entry**](docs/api/TableCategoryApi.md#create_security_entry) | **POST** /tablecategories/{webId}/securityentries | Create a security entry owned by the table category.
*TableCategoryApi* | [**get_security_entry_by_name**](docs/api/TableCategoryApi.md#get_security_entry_by_name) | **GET** /tablecategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the table category with the specified name.
*TableCategoryApi* | [**update_security_entry**](docs/api/TableCategoryApi.md#update_security_entry) | **PUT** /tablecategories/{webId}/securityentries/{name} | Update a security entry owned by the table category.
*TableCategoryApi* | [**delete_security_entry**](docs/api/TableCategoryApi.md#delete_security_entry) | **DELETE** /tablecategories/{webId}/securityentries/{name} | Delete a security entry owned by the table category.
*TableApi* | [**get_by_path**](docs/api/TableApi.md#get_by_path) | **GET** /tables | Retrieve a table by path.
*TableApi* | [**get**](docs/api/TableApi.md#get) | **GET** /tables/{webId} | Retrieve a table.
*TableApi* | [**update**](docs/api/TableApi.md#update) | **PATCH** /tables/{webId} | Update a table by replacing items in its definition.
*TableApi* | [**delete**](docs/api/TableApi.md#delete) | **DELETE** /tables/{webId} | Delete a table.
*TableApi* | [**get_categories**](docs/api/TableApi.md#get_categories) | **GET** /tables/{webId}/categories | Get a table's categories.
*TableApi* | [**get_data**](docs/api/TableApi.md#get_data) | **GET** /tables/{webId}/data | Get the table's data.
*TableApi* | [**update_data**](docs/api/TableApi.md#update_data) | **PUT** /tables/{webId}/data | Update the table's data.
*TableApi* | [**get_security**](docs/api/TableApi.md#get_security) | **GET** /tables/{webId}/security | Get the security information of the specified security item associated with the table for a specified user.
*TableApi* | [**get_security_entries**](docs/api/TableApi.md#get_security_entries) | **GET** /tables/{webId}/securityentries | Retrieve the security entries associated with the table based on the specified criteria. By default, all security entries for this table are returned.
*TableApi* | [**create_security_entry**](docs/api/TableApi.md#create_security_entry) | **POST** /tables/{webId}/securityentries | Create a security entry owned by the table.
*TableApi* | [**get_security_entry_by_name**](docs/api/TableApi.md#get_security_entry_by_name) | **GET** /tables/{webId}/securityentries/{name} | Retrieve the security entry associated with the table with the specified name.
*TableApi* | [**update_security_entry**](docs/api/TableApi.md#update_security_entry) | **PUT** /tables/{webId}/securityentries/{name} | Update a security entry owned by the table.
*TableApi* | [**delete_security_entry**](docs/api/TableApi.md#delete_security_entry) | **DELETE** /tables/{webId}/securityentries/{name} | Delete a security entry owned by the table.
*TimeRulePlugInApi* | [**get_by_path**](docs/api/TimeRulePlugInApi.md#get_by_path) | **GET** /timeruleplugins | Retrieve a Time Rule Plug-in by path.
*TimeRulePlugInApi* | [**get**](docs/api/TimeRulePlugInApi.md#get) | **GET** /timeruleplugins/{webId} | Retrieve a Time Rule Plug-in.
*TimeRuleApi* | [**get_by_path**](docs/api/TimeRuleApi.md#get_by_path) | **GET** /timerules | Retrieve a Time Rule by path.
*TimeRuleApi* | [**get**](docs/api/TimeRuleApi.md#get) | **GET** /timerules/{webId} | Retrieve a Time Rule.
*TimeRuleApi* | [**update**](docs/api/TimeRuleApi.md#update) | **PATCH** /timerules/{webId} | Update a Time Rule by replacing items in its definition.
*TimeRuleApi* | [**delete**](docs/api/TimeRuleApi.md#delete) | **DELETE** /timerules/{webId} | Delete a Time Rule.
*UnitClassApi* | [**get_by_path**](docs/api/UnitClassApi.md#get_by_path) | **GET** /unitclasses | Retrieve a unit class by path.
*UnitClassApi* | [**get**](docs/api/UnitClassApi.md#get) | **GET** /unitclasses/{webId} | Retrieve a unit class.
*UnitClassApi* | [**update**](docs/api/UnitClassApi.md#update) | **PATCH** /unitclasses/{webId} | Update a unit class.
*UnitClassApi* | [**delete**](docs/api/UnitClassApi.md#delete) | **DELETE** /unitclasses/{webId} | Delete a unit class.
*UnitClassApi* | [**get_canonical_unit**](docs/api/UnitClassApi.md#get_canonical_unit) | **GET** /unitclasses/{webId}/canonicalunit | Get the canonical unit of a unit class.
*UnitClassApi* | [**get_units**](docs/api/UnitClassApi.md#get_units) | **GET** /unitclasses/{webId}/units | Get a list of all units belonging to the unit class.
*UnitClassApi* | [**create_unit**](docs/api/UnitClassApi.md#create_unit) | **POST** /unitclasses/{webId}/units | Create a unit in the specified Unit Class.
*UnitApi* | [**get_by_path**](docs/api/UnitApi.md#get_by_path) | **GET** /units | Retrieve a unit by path.
*UnitApi* | [**get**](docs/api/UnitApi.md#get) | **GET** /units/{webId} | Retrieve a unit.
*UnitApi* | [**update**](docs/api/UnitApi.md#update) | **PATCH** /units/{webId} | Update a unit.
*UnitApi* | [**delete**](docs/api/UnitApi.md#delete) | **DELETE** /units/{webId} | Delete a unit.

## Documentation For Models

- [PIAnalysis](docs/models/PIAnalysis.md)
- [PIAnalysisCategory](docs/models/PIAnalysisCategory.md)
- [PIAnalysisCategoryLinks](docs/models/PIAnalysisCategoryLinks.md)
- [PIAnalysisLinks](docs/models/PIAnalysisLinks.md)
- [PIAnalysisRule](docs/models/PIAnalysisRule.md)
- [PIAnalysisRuleLinks](docs/models/PIAnalysisRuleLinks.md)
- [PIAnalysisRulePlugIn](docs/models/PIAnalysisRulePlugIn.md)
- [PIAnalysisRulePlugInLinks](docs/models/PIAnalysisRulePlugInLinks.md)
- [PIAnalysisTemplate](docs/models/PIAnalysisTemplate.md)
- [PIAnalysisTemplateLinks](docs/models/PIAnalysisTemplateLinks.md)
- [PIAnnotation](docs/models/PIAnnotation.md)
- [PIAnnotationLinks](docs/models/PIAnnotationLinks.md)
- [PIAssetDatabase](docs/models/PIAssetDatabase.md)
- [PIAssetDatabaseLinks](docs/models/PIAssetDatabaseLinks.md)
- [PIAssetServer](docs/models/PIAssetServer.md)
- [PIAssetServerLinks](docs/models/PIAssetServerLinks.md)
- [PIAttribute](docs/models/PIAttribute.md)
- [PIAttributeCategory](docs/models/PIAttributeCategory.md)
- [PIAttributeCategoryLinks](docs/models/PIAttributeCategoryLinks.md)
- [PIAttributeLinks](docs/models/PIAttributeLinks.md)
- [PIAttributeTemplate](docs/models/PIAttributeTemplate.md)
- [PIAttributeTemplateLinks](docs/models/PIAttributeTemplateLinks.md)
- [PIAttributeTrait](docs/models/PIAttributeTrait.md)
- [PIAttributeTraitLinks](docs/models/PIAttributeTraitLinks.md)
- [PICacheInstance](docs/models/PICacheInstance.md)
- [PIChannelInstance](docs/models/PIChannelInstance.md)
- [PIDataServer](docs/models/PIDataServer.md)
- [PIDataServerLicense](docs/models/PIDataServerLicense.md)
- [PIDataServerLicenseLinks](docs/models/PIDataServerLicenseLinks.md)
- [PIDataServerLinks](docs/models/PIDataServerLinks.md)
- [PIElement](docs/models/PIElement.md)
- [PIElementCategory](docs/models/PIElementCategory.md)
- [PIElementCategoryLinks](docs/models/PIElementCategoryLinks.md)
- [PIElementLinks](docs/models/PIElementLinks.md)
- [PIElementTemplate](docs/models/PIElementTemplate.md)
- [PIElementTemplateLinks](docs/models/PIElementTemplateLinks.md)
- [PIEnumerationSet](docs/models/PIEnumerationSet.md)
- [PIEnumerationSetLinks](docs/models/PIEnumerationSetLinks.md)
- [PIEnumerationValue](docs/models/PIEnumerationValue.md)
- [PIEnumerationValueLinks](docs/models/PIEnumerationValueLinks.md)
- [PIErrors](docs/models/PIErrors.md)
- [PIEventFrame](docs/models/PIEventFrame.md)
- [PIEventFrameLinks](docs/models/PIEventFrameLinks.md)
- [PIItemAttribute](docs/models/PIItemAttribute.md)
- [PIItemElement](docs/models/PIItemElement.md)
- [PIItemEventFrame](docs/models/PIItemEventFrame.md)
- [PIItemPoint](docs/models/PIItemPoint.md)
- [PIItemsAnalysis](docs/models/PIItemsAnalysis.md)
- [PIItemsAnalysisCategory](docs/models/PIItemsAnalysisCategory.md)
- [PIItemsAnalysisRule](docs/models/PIItemsAnalysisRule.md)
- [PIItemsAnalysisRulePlugIn](docs/models/PIItemsAnalysisRulePlugIn.md)
- [PIItemsAnalysisTemplate](docs/models/PIItemsAnalysisTemplate.md)
- [PIItemsAnnotation](docs/models/PIItemsAnnotation.md)
- [PIItemsAssetDatabase](docs/models/PIItemsAssetDatabase.md)
- [PIItemsAssetServer](docs/models/PIItemsAssetServer.md)
- [PIItemsAttribute](docs/models/PIItemsAttribute.md)
- [PIItemsAttributeCategory](docs/models/PIItemsAttributeCategory.md)
- [PIItemsAttributeTemplate](docs/models/PIItemsAttributeTemplate.md)
- [PIItemsAttributeTrait](docs/models/PIItemsAttributeTrait.md)
- [PIItemsCacheInstance](docs/models/PIItemsCacheInstance.md)
- [PIItemsChannelInstance](docs/models/PIItemsChannelInstance.md)
- [PIItemsDataServer](docs/models/PIItemsDataServer.md)
- [PIItemsElement](docs/models/PIItemsElement.md)
- [PIItemsElementCategory](docs/models/PIItemsElementCategory.md)
- [PIItemsElementTemplate](docs/models/PIItemsElementTemplate.md)
- [PIItemsEnumerationSet](docs/models/PIItemsEnumerationSet.md)
- [PIItemsEnumerationValue](docs/models/PIItemsEnumerationValue.md)
- [PIItemsEventFrame](docs/models/PIItemsEventFrame.md)
- [PIItemsItemAttribute](docs/models/PIItemsItemAttribute.md)
- [PIItemsItemElement](docs/models/PIItemsItemElement.md)
- [PIItemsItemEventFrame](docs/models/PIItemsItemEventFrame.md)
- [PIItemsItemPoint](docs/models/PIItemsItemPoint.md)
- [PIItemsItemsSubstatus](docs/models/PIItemsItemsSubstatus.md)
- [PIItemsPoint](docs/models/PIItemsPoint.md)
- [PIItemsPointAttribute](docs/models/PIItemsPointAttribute.md)
- [PIItemsSecurityEntry](docs/models/PIItemsSecurityEntry.md)
- [PIItemsSecurityIdentity](docs/models/PIItemsSecurityIdentity.md)
- [PIItemsSecurityMapping](docs/models/PIItemsSecurityMapping.md)
- [PIItemsSecurityRights](docs/models/PIItemsSecurityRights.md)
- [PIItemsStreamSummaries](docs/models/PIItemsStreamSummaries.md)
- [PIItemsStreamValue](docs/models/PIItemsStreamValue.md)
- [PIItemsStreamValues](docs/models/PIItemsStreamValues.md)
- [PIItemsSubstatus](docs/models/PIItemsSubstatus.md)
- [PIItemsSummaryValue](docs/models/PIItemsSummaryValue.md)
- [PIItemsTable](docs/models/PIItemsTable.md)
- [PIItemsTableCategory](docs/models/PIItemsTableCategory.md)
- [PIItemsTimeRulePlugIn](docs/models/PIItemsTimeRulePlugIn.md)
- [PIItemsUnitClass](docs/models/PIItemsUnitClass.md)
- [PILanding](docs/models/PILanding.md)
- [PILandingLinks](docs/models/PILandingLinks.md)
- [PIPaginationLinks](docs/models/PIPaginationLinks.md)
- [PIPoint](docs/models/PIPoint.md)
- [PIPointAttribute](docs/models/PIPointAttribute.md)
- [PIPointAttributeLinks](docs/models/PIPointAttributeLinks.md)
- [PIPointLinks](docs/models/PIPointLinks.md)
- [PIPropertyError](docs/models/PIPropertyError.md)
- [PIRequest](docs/models/PIRequest.md)
- [PIRequestTemplate](docs/models/PIRequestTemplate.md)
- [PIResponse](docs/models/PIResponse.md)
- [PISearchByAttribute](docs/models/PISearchByAttribute.md)
- [PISecurity](docs/models/PISecurity.md)
- [PISecurityEntry](docs/models/PISecurityEntry.md)
- [PISecurityEntryLinks](docs/models/PISecurityEntryLinks.md)
- [PISecurityIdentity](docs/models/PISecurityIdentity.md)
- [PISecurityIdentityLinks](docs/models/PISecurityIdentityLinks.md)
- [PISecurityMapping](docs/models/PISecurityMapping.md)
- [PISecurityMappingLinks](docs/models/PISecurityMappingLinks.md)
- [PISecurityRights](docs/models/PISecurityRights.md)
- [PISecurityRightsLinks](docs/models/PISecurityRightsLinks.md)
- [PIStreamSummaries](docs/models/PIStreamSummaries.md)
- [PIStreamSummariesLinks](docs/models/PIStreamSummariesLinks.md)
- [PIStreamValue](docs/models/PIStreamValue.md)
- [PIStreamValueLinks](docs/models/PIStreamValueLinks.md)
- [PIStreamValues](docs/models/PIStreamValues.md)
- [PIStreamValuesLinks](docs/models/PIStreamValuesLinks.md)
- [PISubstatus](docs/models/PISubstatus.md)
- [PISummaryValue](docs/models/PISummaryValue.md)
- [PISystemLanding](docs/models/PISystemLanding.md)
- [PISystemLandingLinks](docs/models/PISystemLandingLinks.md)
- [PISystemStatus](docs/models/PISystemStatus.md)
- [PITable](docs/models/PITable.md)
- [PITableCategory](docs/models/PITableCategory.md)
- [PITableCategoryLinks](docs/models/PITableCategoryLinks.md)
- [PITableData](docs/models/PITableData.md)
- [PITableLinks](docs/models/PITableLinks.md)
- [PITimedValue](docs/models/PITimedValue.md)
- [PITimedValues](docs/models/PITimedValues.md)
- [PITimeRule](docs/models/PITimeRule.md)
- [PITimeRuleLinks](docs/models/PITimeRuleLinks.md)
- [PITimeRulePlugIn](docs/models/PITimeRulePlugIn.md)
- [PITimeRulePlugInLinks](docs/models/PITimeRulePlugInLinks.md)
- [PIUnit](docs/models/PIUnit.md)
- [PIUnitClass](docs/models/PIUnitClass.md)
- [PIUnitClassLinks](docs/models/PIUnitClassLinks.md)
- [PIUnitLinks](docs/models/PIUnitLinks.md)
- [PIUserInfo](docs/models/PIUserInfo.md)
- [PIValue](docs/models/PIValue.md)
- [PIValueQuery](docs/models/PIValueQuery.md)
- [PIVersion](docs/models/PIVersion.md)
- [PIWebException](docs/models/PIWebException.md)
