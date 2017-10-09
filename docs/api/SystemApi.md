# SystemApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**landing**](SystemApi.md#landing) | **GET** /system | Get system links for this PI System Web API instance.
[**cache_instances**](SystemApi.md#cacheinstances) | **GET** /system/cacheinstances | Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service's authentication method, and the cache instance configuration.
[**status**](SystemApi.md#status) | **GET** /system/status | Get the system uptime, the system state and the number of cache instances for this PI System Web API instance.
[**user_info**](SystemApi.md#userinfo) | **GET** /system/userinfo | Get information about the Windows identity used to fulfill the request. This depends on the service's authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.
[**versions**](SystemApi.md#versions) | **GET** /system/versions | Get the current versions of the PI Web API instance and all external plugins.


# **landing**
> landing()

Get system links for this PI System Web API instance.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PISystemLanding**](../models/PISystemLanding.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **cache_instances**
> cache_instances()

Get AF cache instances currently in use by the system. These are caches from which user requests are serviced. The number of instances depends on the number of users connected to the service, the service's authentication method, and the cache instance configuration.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PIItemsCacheInstance**](../models/PIItemsCacheInstance.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **status**
> status()

Get the system uptime, the system state and the number of cache instances for this PI System Web API instance.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PISystemStatus**](../models/PISystemStatus.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **user_info**
> user_info()

Get information about the Windows identity used to fulfill the request. This depends on the service's authentication method and the credentials passed by the client. The impersonation level of the Windows identity is included.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PIUserInfo**](../models/PIUserInfo.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **versions**
> versions()

Get the current versions of the PI Web API instance and all external plugins.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------


### Return type

dict<str, PIVersion>

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
