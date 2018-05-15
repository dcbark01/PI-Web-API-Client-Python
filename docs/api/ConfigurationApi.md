# ConfigurationApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**list**](ConfigurationApi.md#list) | **GET** /system/configuration | Get the current system configuration.
[**get**](ConfigurationApi.md#get) | **GET** /system/configuration/{key} | Get the value of a configuration item.
[**delete**](ConfigurationApi.md#delete) | **DELETE** /system/configuration/{key} | Delete a configuration item.


# **list**
> list()

Get the current system configuration.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------


### Return type

dict(str, object)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get**
> get('key')

Get the value of a configuration item.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the configuration item.. | [required]


### Return type

object

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **delete**
> delete('key')

Delete a configuration item.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the configuration item to remove.. | [required]


### Return type

None

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
