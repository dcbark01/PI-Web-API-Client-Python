# coding: utf-8

"""
	Copyright 2017 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from __future__ import absolute_import

import pandas as pd


class DataApi(object):
	def __init__(self, streamApi, streamSetApi, attributeApi, pointApi):
		self.streamApi = streamApi
		self.streamSetApi = streamSetApi
		self.attributeApi = attributeApi
		self.pointApi = pointApi

	def convert_path_to_web_id(self, fullPath):
		system = fullPath[0:3]
		path = fullPath[3:None]
		if (system == "af:"):
			res = self.attributeApi.get_by_path(path, None, None)
			return (res.web_id)
		elif (system == "pi:"):
			res = self.pointApi.get_by_path(path, None, None)
			return (res.web_id)
		else:
			print("Error: invalid path. It needs to start with \"pi\" or \"af\"")
			return

	def convert_paths_to_web_ids(self, paths):
		lengthPaths = len(paths)
		webIds = []
		for path in paths:
			webIds.append(self.convert_path_to_web_id(path))
		return webIds

	def rename_df(self, df, i):
		df.rename(columns={'Value': 'Value' + str(i + 1)}, inplace=True)
		df.rename(columns={'Timestamp': 'Timestamp' + str(i + 1)}, inplace=True)
		df.rename(columns={'UnitsAbbreviation': 'UnitsAbbreviation' + str(i + 1)}, inplace=True)
		df.rename(columns={'Good': 'Good' + str(i + 1)}, inplace=True)
		df.rename(columns={'Questionable': 'Questionable' + str(i + 1)}, inplace=True)
		df.rename(columns={'Substituted': 'Substituted' + str(i + 1)}, inplace=True)
		return  df

	def calculateItemsIndex(self, web_id, items):
		for i in range(0, len(items)):
			if (items[i].web_id == web_id):
				return i
		return  -1


	def convert_multiple_streams_to_df(self, items, gatherInOneDataFrame, web_ids, selected_fields, paths):
		if (items is None):
			raise Exception('The returned data is Null or None')

		streamsLength = len(items)
		if (streamsLength == 0):
			raise Exception('The returned data is Null or None')

		for i in range(0, streamsLength):
			if ((items[i] == None) or (items[i].items == None)):
				raise Exception('Some items are Null or None.')


		if (gatherInOneDataFrame == True):
			main_df = df_ = pd.DataFrame()
			for i in range(0, streamsLength):
				j = self.calculateItemsIndex(web_ids[i], items);
				df = self.convert_to_df(items[j].items, selected_fields)
				df = self.rename_df(df, i)
				main_df = pd.concat([main_df , df], axis = 1)
			return main_df
		else:
			dfs = {}
			for i in range(0, streamsLength):
				key = paths[i]
				j = self.calculateItemsIndex(web_ids[i], items)
				df = self.convert_to_df(items[j].items, selected_fields)
				dfs[key] = df
			return dfs



	def convert_to_df(self, items, selected_fields):

		if (items is None):
			raise Exception('The returned data is Null or None')

		streamsLength = len(items)
		if (streamsLength == 0):
			raise Exception('The returned data is Null or None')


		addValues = False
		addTimeStamp = False
		addUnitAbbr = False
		addGood = False
		addQuestionable = False
		addSubstituded = False
		value = []
		timestamp = []
		unitsAbbreviation = []
		good = []
		questionable = []
		substituted = []

		if (selected_fields != None and selected_fields != ""):
			if ("timestamp" in selected_fields):
				addTimeStamp = True
			if ("value" in selected_fields):
				addValues = True

			if ("questionable" in selected_fields):
				addQuestionable = True

			if ("unitabbr" in selected_fields):
				addUnitAbbr = True

			if ("good" in selected_fields):
				addGood = True

			if ("substituted" in selected_fields):
				addSubstituded = True
		else:
			addValues = True
			addTimeStamp = True
			addUnitAbbr = True
			addGood = True
			addQuestionable = True
			addSubstituded = True


		for	item in items:
			if (addValues == True):
				value.append(item.value)
			if (addTimeStamp == True):
				timestamp.append(item.timestamp)
			if (addUnitAbbr == True):
				unitsAbbreviation.append(item.units_abbreviation)
			if (addGood == True):
				good.append(item.good)
			if (addQuestionable == True):
				questionable.append(item.questionable)
			if (addSubstituded == True):
				substituted.append(item.substituted)

		data = {}
		if (addValues == True):
			data['Value'] = value;
		if (addTimeStamp == True):
			data['Timestamp'] = timestamp;
		if (addUnitAbbr == True):
			data['UnitsAbbreviation'] = unitsAbbreviation;
		if (addGood == True):
			data['Good'] = good;
		if (addQuestionable == True):
			data['Questionable'] = questionable;
		if (addSubstituded == True):
			data['Substituted'] = substituted;
		df = pd.DataFrame(data)
		return  df

	def get_recorded_values(self, path, boundary_type=None, desired_units=None, end_time="*", filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, start_time="*-1h", time_zone=None):
		if (path is None):
			print("The variable path cannot be null.")
			return

		web_id = self.convert_path_to_web_id(path)
		res = self.streamApi.get_recorded(web_id, boundary_type, desired_units, end_time, filter_expression, include_filtered_values, max_count, selected_fields, start_time, time_zone)
		df = self.convert_to_df(res.items, selected_fields)
		return df



	def get_interpolated_values(self, path, desired_units=None, end_time="*", filter_expression=None, include_filtered_values=None, interval="1h", selected_fields=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None):
		if (path is None):
			print("The variable path cannot be null.")
			return

		web_id = self.convert_path_to_web_id(path)
		res = self.streamApi.get_interpolated(web_id, desired_units, end_time, filter_expression, include_filtered_values, interval, selected_fields, start_time, sync_time, sync_time_boundary_type, time_zone)
		df = self.convert_to_df(res.items, selected_fields)
		return df


	def get_plot_values(self, path, desired_units=None, end_time="*", intervals = 10, selected_fields=None, start_time="*-1d", time_zone=None):
		if (path is None):
			print("The variable path cannot be null.")
			return

		web_id = self.convert_path_to_web_id(path)
		res = self.streamApi.get_plot(web_id, desired_units, end_time, intervals, selected_fields, start_time, time_zone)
		df = self.convert_to_df(res.items, selected_fields)
		return df

	def get_multiple_interpolated_values(self, paths, end_time="*", filter_expression=None, include_filtered_values=None, interval="1h", selected_fields=None, sort_field=None, sort_order=None, start_time="*-1d", sync_time=None, sync_time_boundary_type=None, time_zone=None, web_id_type=None):
		if (paths is None):
			print("The variable paths cannot be null.")
			return

		web_ids = self.convert_paths_to_web_ids(paths)
		res = self.streamSetApi.get_interpolated_ad_hoc(web_ids, end_time, filter_expression, include_filtered_values, interval, selected_fields, sort_field, sort_order, start_time, sync_time, sync_time_boundary_type, time_zone, web_id_type)
		df = self.convert_multiple_streams_to_df(res.items, True, web_ids, selected_fields, None)
		return df

	def get_multiple_plot_values(self, paths, end_time="*", intervals="1h", selected_fields=None, sort_field=None, sort_order=None, start_time="*-1d", time_zone=None, web_id_type=None):
		if (paths is None):
			print("The variable paths cannot be null.")
			return

		web_ids = self.convert_paths_to_web_ids(paths)
		res = self.streamSetApi.get_plot_ad_hoc(web_ids, end_time, intervals, selected_fields, sort_field, sort_order, start_time, time_zone, web_id_type)
		df = self.convert_multiple_streams_to_df(res.items, True, web_ids, selected_fields, None)
		return df

	def get_multiple_recorded_values(self, paths,  boundary_type=None, end_time="*", filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None):
		if (paths is None):
			print("The variable paths cannot be null.")
			return

		web_ids = self.convert_paths_to_web_ids(paths)
		res = self.streamSetApi.get_recorded_ad_hoc(web_ids, boundary_type, end_time, filter_expression, include_filtered_values, max_count, selected_fields, sort_field, sort_order, start_time, time_zone, web_id_type)
		df = self.convert_multiple_streams_to_df(res.items, False, web_ids, selected_fields, paths)
		return df






