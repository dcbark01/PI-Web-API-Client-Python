# DataApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_recorded_values**](DataApi.md#get_recorded_values) |  Returns a pandas dataframe with compressed values for the requested time range from the source provider.
[**get_interpolated_values**](DataApi.md#get_interpolated_values) | Retrieves a pandas dataframe with interpolated values over the specified time range at the specified sampling interval.
[**get_plot_values**](DataApi.md#get_plot_values*) | Retrieves a pandas dataframe with values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**get_multiple_recorded_values**](DataApi.md#get_multiple_recorded_values) | Returns an array of pandas dataframe with recorded values of the specified streams.
[**get_multiple_interpolated_values**](DataApi.md#get_multiple_interpolated_values) | Returns a dataframe with interpolated values of the specified streams over the specified time range at the specified sampling interval.
[**get_multiple_plot_values**](DataApi.md#get_multiple_plot_values) |  Returns a pandas dataframe with values of the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).



# **get_recorded_values**
> get_recorded_values('path', 'boundary_type', 'desired_units', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'selected_fields', 'start_time', 'time_zone')

Returns a pandas dataframe with compressed values for the requested time range from the source provider.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the stream (for a PI Point use "pi:\\servername\pointname" or "af:\\afservername\database\element|attribute" for an attribute). | [required]
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.. | [optional]
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

Pandas Dataframe

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)


# **get_interpolated_values**
> get_interpolated_values('path', 'desired_units', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'selected_fields', 'start_time', 'time_zone')

Retrieves a pandas dataframe with interpolated values over the specified time range at the specified sampling interval.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the stream (for a PI Point use "pi:\\servername\pointname" or "af:\\afservername\database\element|attribute" for an attribute). | [required]
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **interval** | **str**| The sampling interval, in AFTimeSpan format.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

Pandas Dataframe

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)




# **get_plot_values**
> get_plot_values**('path', 'desired_units', 'end_time', 'intervals', 'selected_fields', 'start_time', 'time_zone')

Retrieves a pandas dataframe with values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the stream (for a PI Point use "pi:\\servername\pointname" or "af:\\afservername\database\element|attribute" for an attribute). | [required]
 **desired_units** | **str**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

Pandas Dataframe

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)



# **get_multiple_recorded_values**
> get_multiple_recorded_values('path', 'boundary_type', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'selected_fields', 'start_time', 'time_zone')

Returns recorded values of the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **list[str]**| The paths of  multiple streams (for a PI Point use "pi:\\servername\pointname" or "af:\\afservername\database\element|attribute" for an attribute). | [required]
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

Array of Pandas Dataframe

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)


# **get_multiple_interpolated_values**
> get_multiple_interpolated_values('path', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'selected_fields', 'start_time', 'time_zone')

Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **list[str]**| The paths of  multiple streams (for a PI Point use "pi:\\servername\pointname" or "af:\\afservername\database\element|attribute" for an attribute). | [required
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **interval** | **str**| The sampling interval, in AFTimeSpan format.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

Pandas Dataframe

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)



# **get_multiple_plot_values**
> get_multiple_plot_values('path', 'end_time', 'intervals', 'selected_fields', 'start_time', 'time_zone')

Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **list[str]**| The paths of  multiple streams (for a PI Point use "pi:\\servername\pointname" or "af:\\afservername\database\element|attribute" for an attribute). | [required
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

Pandas Dataframe

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)



