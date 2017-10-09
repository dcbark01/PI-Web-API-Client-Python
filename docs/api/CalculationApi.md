# CalculationApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_at_intervals**](CalculationApi.md#getatintervals) | **GET** /calculation/intervals | Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.
[**get_at_recorded**](CalculationApi.md#getatrecorded) | **GET** /calculation/recorded | Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.
[**get_summary**](CalculationApi.md#getsummary) | **GET** /calculation/summary | Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.
[**get_at_times**](CalculationApi.md#getattimes) | **GET** /calculation/times | Returns the result of evaluating the expression at the specified timestamps.


# **get_at_intervals**
> get_at_intervals('end_time', 'expression', 'sample_interval', 'selected_fields', 'start_time', 'web_id')

Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.. | [optional]
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.. | [optional]


### Return type

[**PITimedValues**](../models/PITimedValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_at_recorded**
> get_at_recorded('end_time', 'expression', 'selected_fields', 'start_time', 'web_id')

Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.. | [optional]


### Return type

[**PITimedValues**](../models/PITimedValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_summary**
> get_summary('calculation_basis', 'end_time', 'expression', 'sample_interval', 'sample_type', 'selected_fields', 'start_time', 'summary_duration', 'summary_type', 'time_type', 'web_id')

Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **calculation_basis** | **str**| Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.. | [optional]
 **end_time** | **str**| An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.. | [optional]
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.. | [optional]
 **sample_interval** | **str**| A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is 'Interval'.. | [optional]
 **sample_type** | **str**| A flag which specifies one or more summaries to compute for each interval over the time range. The default is 'ExpressionRecordedValues'.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_time** | **str**| An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.. | [optional]
 **summary_duration** | **str**| The duration of each summary interval.. | [optional]
 **summary_type** | **list[str]**| Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.. | [optional]
 **time_type** | **str**| Specifies how to calculate the timestamp for each interval. The default is 'Auto'.. | [optional]
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.. | [optional]


### Return type

[**PIItemsSummaryValue**](../models/PIItemsSummaryValue.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_at_times**
> get_at_times('expression', 'selected_fields', 'sort_order', 'time', 'web_id')

Returns the result of evaluating the expression at the specified timestamps.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**| A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **sort_order** | **str**| The order that the returned collection is sorted. The default is 'Ascending'.. | [optional]
 **time** | **list[str]**| A list of timestamps at which to calculate the expression.. | [optional]
 **web_id** | **str**| The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.. | [optional]


### Return type

[**PITimedValues**](../models/PITimedValues.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
