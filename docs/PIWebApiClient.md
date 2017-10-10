# PIWebApiClient

## **Constructor**
> PIWebApiClient(String baseUrl, bool String username, String password, Boolean verifySsl, Boolean debug)

Creates an instance of the PI Web API client top level object. Only Basic authentication can be used.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**baseUrl** | **str**| PI Web API base service url. | [required]
**useKerberos** | **bool**| Select True for Kerberos auth or False for Basic auth. | [required]
**username** | **str**| The username for basic authentication to authenticate against PI Web API. | [required]
**password** | **str**| The password for basic authentication to authenticate against PI Web API. | [required]
**verifySsl** | **bool**| Verify SSL certificate.| [required]

## **Properties**

Property | Controller
------------ | -------------
**home** | [**HomeApi**](/docs/api/HomeApi.md)
**analysis** | [**AnalysisApi**](/docs/api/AnalysisApi.md)
**analysisCategory** | [**AnalysisCategoryApi**](/docs/api/AnalysisCategoryApi.md)
**analysisRulePlugIn** | [**AnalysisRulePlugInApi**](/docs/api/AnalysisRulePlugInApi.md)
**analysisRule** | [**AnalysisRuleApi**](/docs/api/AnalysisRuleApi.md)
**analysisTemplate** | [**AnalysisTemplateApi**](/docs/api/AnalysisTemplateApi.md)
**assetDatabase** | [**AssetDatabaseApi**](/docs/api/AssetDatabaseApi.md)
**assetServer** | [**AssetServerApi**](/docs/api/AssetServerApi.md)
**attributeCategory** | [**AttributeCategoryApi**](/docs/api/AttributeCategoryApi.md)
**attribute** | [**AttributeApi**](/docs/api/AttributeApi.md)
**attributeTemplate** | [**AttributeTemplateApi**](/docs/api/AttributeTemplateApi.md)
**attributeTrait** | [**AttributeTraitApi**](/docs/api/AttributeTraitApi.md)
**calculation** | [**CalculationApi**](/docs/api/CalculationApi.md)
**channel** | [**ChannelApi**](/docs/api/ChannelApi.md)
**data** | [**DataApi**](/docs/api/DataApi.md)
**dataServer** | [**DataServerApi**](/docs/api/DataServerApi.md)
**elementCategory** | [**ElementCategoryApi**](/docs/api/ElementCategoryApi.md)
**element** | [**ElementApi**](/docs/api/ElementApi.md)
**elementTemplate** | [**ElementTemplateApi**](/docs/api/ElementTemplateApi.md)
**enumerationSet** | [**EnumerationSetApi**](/docs/api/EnumerationSetApi.md)
**enumerationValue** | [**EnumerationValueApi**](/docs/api/EnumerationValueApi.md)
**eventFrame** | [**EventFrameApi**](/docs/api/EventFrameApi.md)
**point** | [**PointApi**](/docs/api/PointApi.md)
**securityIdentity** | [**SecurityIdentityApi**](/docs/api/SecurityIdentityApi.md)
**securityMapping** | [**SecurityMappingApi**](/docs/api/SecurityMappingApi.md)
**stream** | [**StreamApi**](/docs/api/StreamApi.md)
**streamSet** | [**StreamSetApi**](/docs/api/StreamSetApi.md)
**system** | [**SystemApi**](/docs/api/SystemApi.md)
**configuration** | [**ConfigurationApi**](/docs/api/ConfigurationApi.md)
**tableCategory** | [**TableCategoryApi**](/docs/api/TableCategoryApi.md)
**table** | [**TableApi**](/docs/api/TableApi.md)
**timeRulePlugIn** | [**TimeRulePlugInApi**](/docs/api/TimeRulePlugInApi.md)
**timeRule** | [**TimeRuleApi**](/docs/api/TimeRuleApi.md)
**unitClass** | [**UnitClassApi**](/docs/api/UnitClassApi.md)
**unit** | [**UnitApi**](/docs/api/UnitApi.md)

[[Back to Model list]](../DOCUMENTATION.md#documentation-for-models) [[Back to API list]](../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to DOCUMENTATION]](../DOCUMENTATION.md)
