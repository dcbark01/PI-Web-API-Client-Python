# StreamSetApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_channel**](StreamSetApi.md#getchannel) | **GET** /streamsets/{webId}/channel | Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.
[**get_end**](StreamSetApi.md#getend) | **GET** /streamsets/{webId}/end | Returns End of stream values of the attributes for an Element, Event Frame or Attribute
[**get_interpolated**](StreamSetApi.md#getinterpolated) | **GET** /streamsets/{webId}/interpolated | Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.
[**get_interpolated_at_times**](StreamSetApi.md#getinterpolatedattimes) | **GET** /streamsets/{webId}/interpolatedattimes | Returns interpolated values of attributes for an element, event frame or attribute at the specified times.
[**get_plot**](StreamSetApi.md#getplot) | **GET** /streamsets/{webId}/plot | Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**get_recorded**](StreamSetApi.md#getrecorded) | **GET** /streamsets/{webId}/recorded | Returns recorded values of the attributes for an element, event frame, or attribute.
[**update_values**](StreamSetApi.md#updatevalues) | **POST** /streamsets/{webId}/recorded | Updates multiple values for the specified streams.
[**get_recorded_at_time**](StreamSetApi.md#getrecordedattime) | **GET** /streamsets/{webId}/recordedattime | Returns recorded values of the attributes for an element, event frame, or attribute.
[**get_recorded_at_times**](StreamSetApi.md#getrecordedattimes) | **GET** /streamsets/{webId}/recordedattimes | Returns recorded values of attributes for an element, event frame or attribute at the specified times.
[**get_summaries**](StreamSetApi.md#getsummaries) | **GET** /streamsets/{webId}/summary | Returns summary values of the attributes for an element, event frame or attribute.
[**get_values**](StreamSetApi.md#getvalues) | **GET** /streamsets/{webId}/value | Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.
[**update_value**](StreamSetApi.md#updatevalue) | **POST** /streamsets/{webId}/value | Updates a single value for the specified streams.
[**get_channel_ad_hoc**](StreamSetApi.md#getchanneladhoc) | **GET** /streamsets/channel | Opens a channel that will send messages about any value changes for the specified streams.
[**get_end_ad_hoc**](StreamSetApi.md#getendadhoc) | **GET** /streamsets/end | Returns End Of Stream values for attributes of the specified streams
[**get_interpolated_ad_hoc**](StreamSetApi.md#getinterpolatedadhoc) | **GET** /streamsets/interpolated | Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.
[**get_interpolated_at_times_ad_hoc**](StreamSetApi.md#getinterpolatedattimesadhoc) | **GET** /streamsets/interpolatedattimes | Returns interpolated values of the specified streams at the specified times.
[**get_plot_ad_hoc**](StreamSetApi.md#getplotadhoc) | **GET** /streamsets/plot | Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).
[**get_recorded_ad_hoc**](StreamSetApi.md#getrecordedadhoc) | **GET** /streamsets/recorded | Returns recorded values of the specified streams.
[**update_values_ad_hoc**](StreamSetApi.md#updatevaluesadhoc) | **POST** /streamsets/recorded | Updates multiple values for the specified streams.
[**get_recorded_at_time_ad_hoc**](StreamSetApi.md#getrecordedattimeadhoc) | **GET** /streamsets/recordedattime | Returns recorded values based on the passed time and retrieval mode.
[**get_recorded_at_times_ad_hoc**](StreamSetApi.md#getrecordedattimesadhoc) | **GET** /streamsets/recordedattimes | Returns recorded values of the specified streams at the specified times.
[**get_summaries_ad_hoc**](StreamSetApi.md#getsummariesadhoc) | **GET** /streamsets/summary | Returns summary values of the specified streams.
[**get_values_ad_hoc**](StreamSetApi.md#getvaluesadhoc) | **GET** /streamsets/value | Returns values of the specified streams.
[**update_value_ad_hoc**](StreamSetApi.md#updatevalueadhoc) | **POST** /streamsets/value | Updates a single value for the specified streams.


# **get_channel**
> get_channel('web_id', 'category_name', 'include_initial_values', 'name_filter', 'search_full_hierarchy', 'show_excluded', 'show_hidden', 'template_name')

Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **include_initial_values** | **bool**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]


### Return type

[**PIItemsStreamValue**](../models/PIItemsStreamValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_end**
> get_end('web_id', 'category_name', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'template_name')

Returns End of stream values of the attributes for an Element, Event Frame or Attribute

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]


### Return type

[**PIItemsStreamValue**](../models/PIItemsStreamValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_interpolated**
> get_interpolated('web_id', 'category_name', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'start_time', 'template_name', 'time_zone')

Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **interval** | **str**| The sampling interval, in AFTimeSpan format.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_interpolated_at_times**
> get_interpolated_at_times('web_id', 'time', 'category_name', 'filter_expression', 'include_filtered_values', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_order', 'template_name', 'time_zone')

Returns interpolated values of attributes for an element, event frame or attribute at the specified times.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **time** | **list[str]**| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_plot**
> get_plot('web_id', 'category_name', 'end_time', 'intervals', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'start_time', 'template_name', 'time_zone')

Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_recorded**
> get_recorded('web_id', 'boundary_type', 'category_name', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'start_time', 'template_name', 'time_zone')

Returns recorded values of the attributes for an element, event frame, or attribute.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.. | [optional]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_values**
> update_values('web_id', 'values', 'buffer_option', 'update_option')

Updates multiple values for the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.. | [required]
 **values** | **list[PIStreamValues]**| The values to add or update.. | [required]
 **buffer_option** | **str**| The desired AFBufferOption. The default is 'BufferIfPossible'.. | [optional]
 **update_option** | **str**| The desired AFUpdateOption. The default is 'Replace'.. | [optional]


### Return type

[**PIItemsItemsSubstatus**](../models/PIItemsItemsSubstatus.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_recorded_at_time**
> get_recorded_at_time('web_id', 'time', 'category_name', 'name_filter', 'retrieval_mode', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'template_name', 'time_zone')

Returns recorded values of the attributes for an element, event frame, or attribute.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **time** | **str**| The timestamp at which the values are desired.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_recorded_at_times**
> get_recorded_at_times('web_id', 'time', 'category_name', 'name_filter', 'retrieval_mode', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'sort_order', 'template_name', 'time_zone')

Returns recorded values of attributes for an element, event frame or attribute at the specified times.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **time** | **list[str]**| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_summaries**
> get_summaries('web_id', 'calculation_basis', 'category_name', 'end_time', 'filter_expression', 'name_filter', 'sample_interval', 'sample_type', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'start_time', 'summary_duration', 'summary_type', 'template_name', 'time_type', 'time_zone')

Returns summary values of the attributes for an element, event frame or attribute.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.. | [required]
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.. | [optional]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.. | [optional]
 **sample_type** | **str**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **summary_duration** | **str**| The duration of each summary interval.. | [optional]
 **summary_type** | **list[str]**| Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is 'Auto'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamSummaries**](../models/PIItemsStreamSummaries.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_values**
> get_values('web_id', 'category_name', 'name_filter', 'search_full_hierarchy', 'selected_fields', 'show_excluded', 'show_hidden', 'template_name', 'time', 'time_zone')

Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.. | [required]
 **category_name** | **str**| Specify that included attributes must have this category. The default is no category filter.. | [optional]
 **name_filter** | **str**| The name query string used for filtering attributes. The default is no filter.. | [optional]
 **search_full_hierarchy** | **bool**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **show_excluded** | **bool**| Specified if the search should include attributes with the Excluded property set. The default is 'false'.. | [optional]
 **show_hidden** | **bool**| Specified if the search should include attributes with the Hidden property set. The default is 'false'.. | [optional]
 **template_name** | **str**| Specify that included attributes must be members of this template. The default is no template filter.. | [optional]
 **time** | **str**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValue**](../models/PIItemsStreamValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_value**
> update_value('web_id', 'values', 'buffer_option', 'update_option')

Updates a single value for the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.. | [required]
 **values** | **list[PIStreamValue]**| The values to add or update.. | [required]
 **buffer_option** | **str**| The desired AFBufferOption. The default is 'BufferIfPossible'.. | [optional]
 **update_option** | **str**| The desired AFUpdateOption. The default is 'Replace'.. | [optional]


### Return type

[**PIItemsSubstatus**](../models/PIItemsSubstatus.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_channel_ad_hoc**
> get_channel_ad_hoc('web_id', 'include_initial_values')

Opens a channel that will send messages about any value changes for the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **include_initial_values** | **bool**| Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is 'false'.. | [optional]


### Return type

[**PIItemsStreamValue**](../models/PIItemsStreamValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_end_ad_hoc**
> get_end_ad_hoc('web_id', 'selected_fields')

Returns End Of Stream values for attributes of the specified streams

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_interpolated_ad_hoc**
> get_interpolated_ad_hoc('web_id', 'end_time', 'filter_expression', 'include_filtered_values', 'interval', 'selected_fields', 'start_time', 'time_zone')

Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **interval** | **str**| The sampling interval, in AFTimeSpan format.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_interpolated_at_times_ad_hoc**
> get_interpolated_at_times_ad_hoc('time', 'web_id', 'filter_expression', 'include_filtered_values', 'selected_fields', 'sort_order', 'time_zone')

Returns interpolated values of the specified streams at the specified times.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **time** | **list[str]**| The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.. | [required]
 **web_id** | **list[str]**| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_plot_ad_hoc**
> get_plot_ad_hoc('web_id', 'end_time', 'intervals', 'selected_fields', 'start_time', 'time_zone')

Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **intervals** | **int**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_recorded_ad_hoc**
> get_recorded_ad_hoc('web_id', 'boundary_type', 'end_time', 'filter_expression', 'include_filtered_values', 'max_count', 'selected_fields', 'start_time', 'time_zone')

Returns recorded values of the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **boundary_type** | **str**| An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.. | [optional]
 **include_filtered_values** | **bool**| Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.. | [optional]
 **max_count** | **int**| The maximum number of values to be returned. The default is 1000.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_values_ad_hoc**
> update_values_ad_hoc('values', 'buffer_option', 'update_option')

Updates multiple values for the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **values** | **list[PIStreamValues]**| The values to add or update.. | [required]
 **buffer_option** | **str**| The desired AFBufferOption. The default is 'BufferIfPossible'.. | [optional]
 **update_option** | **str**| The desired AFUpdateOption. The default is 'Replace'.. | [optional]


### Return type

[**PIItemsItemsSubstatus**](../models/PIItemsItemsSubstatus.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_recorded_at_time_ad_hoc**
> get_recorded_at_time_ad_hoc('time', 'web_id', 'retrieval_mode', 'selected_fields', 'time_zone')

Returns recorded values based on the passed time and retrieval mode.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **time** | **str**| The timestamp at which the values are desired.. | [required]
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValue**](../models/PIItemsStreamValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_recorded_at_times_ad_hoc**
> get_recorded_at_times_ad_hoc('time', 'web_id', 'retrieval_mode', 'selected_fields', 'sort_order', 'time_zone')

Returns recorded values of the specified streams at the specified times.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **time** | **list[str]**| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.. | [required]
 **web_id** | **list[str]**| The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **retrieval_mode** | **str**| An optional value that determines the values to return when values don't exist at the exact time specified. The default is 'Auto'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValues**](../models/PIItemsStreamValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_summaries_ad_hoc**
> get_summaries_ad_hoc('web_id', 'calculation_basis', 'end_time', 'filter_expression', 'sample_interval', 'sample_type', 'selected_fields', 'start_time', 'summary_duration', 'summary_type', 'time_type', 'time_zone')

Returns summary values of the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*'. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **filter_expression** | **str**| A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute. The default is no filtering.. | [optional]
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.. | [optional]
 **sample_type** | **str**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d'.. | [optional]
 **summary_duration** | **str**| The duration of each summary interval.. | [optional]
 **summary_type** | **list[str]**| Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.. | [optional]
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is 'Auto'.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamSummaries**](../models/PIItemsStreamSummaries.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_values_ad_hoc**
> get_values_ad_hoc('web_id', 'selected_fields', 'time', 'time_zone')

Returns values of the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **list[str]**| The ID of a stream.  Multiple streams may be specified with multiple instances of the parameter.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **time** | **str**| An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.. | [optional]
 **time_zone** | **str**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.. | [optional]


### Return type

[**PIItemsStreamValue**](../models/PIItemsStreamValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **update_value_ad_hoc**
> update_value_ad_hoc('values', 'buffer_option', 'update_option')

Updates a single value for the specified streams.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **values** | **list[PIStreamValue]**| The values to add or update.. | [required]
 **buffer_option** | **str**| The desired AFBufferOption. The default is 'BufferIfPossible'.. | [optional]
 **update_option** | **str**| The desired AFUpdateOption. The default is 'Replace'.. | [optional]


### Return type

[**PIItemsSubstatus**](../models/PIItemsSubstatus.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
