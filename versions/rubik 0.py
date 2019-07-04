#!/usr/bin/env python
# coding=utf-8

# This is Rubik for Pandas, by josé maría.
# Version: Jul-30-2018

import pandas as pd
from operator import itemgetter
pd.set_option('display.max_columns', 20)


def fillNanWithLists(df, column):

	g_fun = lambda x: []
	mask = df[column].isnull()
	df.loc[mask,[column]] = df.loc[mask,column].apply(g_fun)

	return df

# ------------------------------------------------------------------------------

def concatColsToList(data_frame, group_to_list, new_name):

	""" Concatenate multiple columns of a data frame into a single list.
	"""

	data_frame[new_name] = data_frame[group_to_list].values.tolist()
	
	return data_frame.drop(group_to_list, axis=1)

# ------------------------------------------------------------------------------

def table(x):

	""" This function works like table() in R. """

	x = pd.Series(x)
	counts = x.value_counts()

	my_dict = dict(counts)

	# Creating a Data Frame.
	e = {
		'freq': my_dict.values(),
		'names': my_dict.keys()
	} 
	e = pd.DataFrame(e)

	# Sorting by frequency.
	e = e.sort_values('freq', ascending=False).reset_index(drop=True)

	return e[['names','freq']]

# ------------------------------------------------------------------------------

def unGroupLists(user_data_frame, column_name):

	""" Formerly known as: unnestDataFrame 
		This function unnest a 'Series of Lists' in a Pandas' Dataframe.
	"""

	# Save the index name.
	index_name = user_data_frame.index.name
	user_data_frame = user_data_frame.reset_index(drop=True)
	neededColumnIndex = (user_data_frame[column_name]
						.to_frame()
						.reset_index(drop=True))

	# Do the magic.
	flat = pd.DataFrame([[i, x] 
		for i, y in neededColumnIndex[column_name].apply(list).iteritems() 
			for x in y], columns=[index_name,column_name])

	flat = flat.set_index(index_name)

	flat.columns = [column_name + '_new']

	return (user_data_frame.join(flat)
							.reset_index(drop=True)
							.drop(column_name, axis=1)
							.rename(columns={column_name+'_new':column_name}))

# ------------------------------------------------------------------------------

def flatDict(data_frame, flat_col):

	""" Formerly known as: flatteningDataframe 
		This function flatten a data frame with dictionaries in a column.
	"""

	# Define a pivot column.
	data_frame = data_frame.reset_index(drop=True)
	data_frame.index.name = 'pivot'
	data_frame = data_frame.reset_index(drop=False)

	data_frame_aux = pd.DataFrame(data_frame[flat_col].tolist())
	data_frame_aux.index.name = 'pivot'
	data_frame_aux = data_frame_aux.reset_index(drop=False)

	# Merge the data_frames.
	data_frame = pd.merge(data_frame,
							data_frame_aux,
							how='left',
							on='pivot')

	return data_frame.drop([flat_col, 'pivot'], axis=1)

# ------------------------------------------------------------------------------

def groupToList(data_frame, common_factors, factor_to_list):

	""" Group a variable (factor_to_list) in to a single list in regards of a
		group of variables (common_factors).
	"""
	
	return (data_frame.groupby(common_factors)[factor_to_list]
						.apply(lambda x: x.tolist())
						.rename(factor_to_list)
						.reset_index(drop=False))

# ------------------------------------------------------------------------------

def groupToTuple(data_frame, common_factors, factor_to_list):

	""" Group a variable (factor_to_list) in to a single list in regards of a
		group of variables (common_factors).
	"""
	
	return (data_frame.groupby(common_factors)[factor_to_list]
						.apply(lambda x: tuple(x.tolist()))
						.rename(factor_to_list)
						.reset_index(drop=False))

# ------------------------------------------------------------------------------

def groupToSortedTuple(data_frame, common_factors, factor_to_list, n=0):

	""" Group a variable (factor_to_list) in to a single tuple in regards of a
		group of variables (common_factors).

		Sort a list of tuples by first, second, or n-1 element.
	"""

	def h_fun(x):
		return tuple(sorted(x, key=itemgetter(n)))
	
	return (data_frame.groupby(common_factors)[factor_to_list]
						.apply(lambda x: h_fun(x.tolist()))
						.rename(factor_to_list)
						.reset_index(drop=False))

# ------------------------------------------------------------------------------

def groupToDict(data_frame, group_to_dict, new_name):

	""" Formerly known as: unFlatteningDataframe
		Generate new column with dictionaries having values of othe columns.
	"""

	all_cols = list(data_frame.columns)

	# Remove from the column list the name of the columns that will be grouped.
	for to_rem in group_to_dict:
		all_cols.remove(to_rem)

	no_group_data = data_frame[all_cols]
	group_data = (pd.Series(data_frame[group_to_dict]
					.to_dict(orient='records'))
						.rename(new_name))

	return pd.concat([no_group_data, group_data], axis=1)

# ------------------------------------------------------------------------------

def groupToSet(data_frame, common_factors, factor_to_list):

	""" Group a variable (factor_to_list) in to a single list in regards of a
		group of variables (common_factors).
	"""
	
	return (data_frame.groupby(common_factors)[factor_to_list]
						.apply(lambda x: list(set(x)))
						.rename(factor_to_list)
						.reset_index(drop=False))

# ------------------------------------------------------------------------------

def groupToSortedSet(data_frame, common_factors, factor_to_list):

	""" Group a variable (factor_to_list) in to a single list in regards of a
		group of variables (common_factors).
	"""

	def h_fun(x):
		x = list(set(x))
		x.sort()
		return x

	return (data_frame.groupby(common_factors)[factor_to_list]
						.apply(h_fun)
						.rename(factor_to_list)
						.reset_index(drop=False))

# ------------------------------------------------------------------------------

def flattenList(l):

	""" Flatten a list with nested lists.
	[100,[103, [555]]], 102] = [100, 103, 555, 102]
	"""

	if not isinstance(l, list):
		my_list = []
		my_list.append(l)
		l = my_list

	# All elements on the list should be lists.
	for i in range(len(l)):
		if not isinstance(l[i], list):
			my_list = []
			my_list.append(l[i])
			l[i] = my_list

	# Main operation.
	l = [item for sublist in l for item in sublist]

	# Review if more lists are nested.
	flag = False
	for i in range(len(l)):
		if isinstance(l[i], list):
			flag = True

	# If more lists are on the list, do a recursive operation.
	if flag:
		l = flattenList(l)

	return l

# ------------------------------------------------------------------------------

def combineListColumns(data_frame, column_1, column_2, new_column):

	data_frame = data_frame.to_dict(orient='records')

	for e in data_frame:
		if not isinstance(e[column_1], list):
			e[column_1] = []
		if not isinstance(e[column_2], list):
			e[column_2] = []
		
		_1 = list(e[column_1])
		_2 = list(e[column_2])
		_1.extend(_2)

		del e[column_1]
		del e[column_2]

		e[new_column] = _1

	data_frame = pd.DataFrame(data_frame)

	return data_frame

# ------------------------------------------------------------------------------
