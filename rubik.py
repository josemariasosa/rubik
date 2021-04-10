#!/usr/bin/env python
# coding=utf-8

# This is Rubik for Pandas, by josé maría.
# Version 2.2.3: Apr-10-2021

__version__ = '2.2.3'

import pandas as pd
from operator import itemgetter
pd.set_option('display.min_rows', 30)
pd.set_option('display.max_rows', 60)
pd.set_option('display.max_columns', 20)


def fillna_dict(data_frame, column_name):
    """From any column in a DataFrame, replace the NaN values with empty 
    dictionaries."""
    g_fun = lambda x: {}
    mask = data_frame[column_name].isnull()
    data_frame.loc[mask,[column_name]] = (data_frame.loc[mask,column_name]
                                          .apply(g_fun))
    return data_frame

# -----------------------------------------------------------------------------

def fillna_list(data_frame, column_name):
    """From any column in a DataFrame, replace the NaN values with empty 
    lists."""
    g_fun = lambda x: []
    mask = data_frame[column_name].isnull()
    data_frame.loc[mask,[column_name]] = (data_frame.loc[mask,column_name]
                                          .apply(g_fun))
    return data_frame

# -----------------------------------------------------------------------------

def concat_to_list(data_frame, column_list, column_new_name):
    """Concatenate multiple columns of a data frame into a single list."""
    data_frame[column_new_name] = data_frame[column_list].values.tolist()
    return data_frame.drop(column_list, axis=1)

# -----------------------------------------------------------------------------

def table(l):
    """This function works like table() in the R programming language."""
    l = pd.Series(l)
    counts = l.value_counts()
    counts = counts.rename('freq')
    counts.index.name = 'values'
    counts = counts.reset_index(drop=False)
    return counts

# -----------------------------------------------------------------------------

def ungroup_list(data_frame, column_name):
    """This function unnest a 'Series of Lists' in a Pandas Dataframe."""
    index_name = data_frame.index.name
    data_frame = data_frame.reset_index(drop=True)
    neededColumnIndex = (data_frame[column_name]
                        .to_frame()
                        .reset_index(drop=True))
    # Do the magic.
    flat = pd.DataFrame([[i, x] 
        for i, y in neededColumnIndex[column_name].apply(list).iteritems() 
            for x in y], columns=[index_name,column_name])
    flat = flat.set_index(index_name)
    flat.columns = [column_name + '_new']
    return (data_frame.join(flat)
                      .reset_index(drop=True)
                      .drop(column_name, axis=1)
                      .rename(columns={column_name+'_new':column_name}))

# -----------------------------------------------------------------------------

def ungroup_dict(data_frame, column_name, prefix=False):
    """This function flatten a DataFrame with dictionaries in a column.
    Avoid crashing columns names with the dictionary keys.
    Use the prefix argument as follow:
        - False: default, regular behavior, column names are the dict keys.
        - True: Use as prefix the original column name followed by an underscore.
        - String: The user can give any prefix.
    """
    uncrashable = 'uncrashable_NaMe_XxXxXxXxXxXxXxXxXx'
    data_frame = data_frame.rename(columns={column_name: uncrashable})
    data_frame = data_frame.reset_index(drop=True)
    data_frame.index.name = 'pivot'
    data_frame = data_frame.reset_index(drop=False)
    mask = data_frame[uncrashable].isnull()
    data_frame[uncrashable] = data_frame[uncrashable].where(~mask, None)
    data_frame_aux = pd.DataFrame([
        x if bool(x) else {} for x in data_frame[uncrashable].tolist()
    ])
    if bool(prefix):
        if isinstance(prefix, str):
            prefix_name = prefix + '_'
        else:
            prefix_name = column_name + '_'
        new_names = {
            col: prefix_name+col for col in data_frame_aux.columns.tolist()
        }
        data_frame_aux = data_frame_aux.rename(columns=new_names)

    data_frame_aux.index.name = 'pivot'
    data_frame_aux = data_frame_aux.reset_index(drop=False)
    # Merge the data_frames.
    return pd.merge(data_frame,
                    data_frame_aux,
                    how='left',
                    on='pivot').drop([uncrashable, 'pivot'], axis=1)

# -----------------------------------------------------------------------------

def list_to_columns(data_frame, column_name):
    def to_dict(l):
        if not isinstance(l, list):
            mess = 'All the values in the column {} must be lists. '
            mess = mess + 'Try using rubik\'s function fillna_list()'
            raise ValueError(mess.format(column_name))
        d = {}
        for i, v in enumerate(l):
            d.update({
                column_name+'_'+str(i+1): v
            })
        return d
    data_frame[column_name] = data_frame[column_name].map(to_dict)
    data_frame = ungroup_dict(data_frame, column_name)
    return data_frame

# -----------------------------------------------------------------------------

def groupto_list(data_frame, column_list, column_name):
    """Group a variable (column_name) in to a single list in regards of a
    group of variables (column_list)."""
    return (data_frame.groupby(column_list)[column_name]
                      .apply(lambda x: x.tolist())
                      .rename(column_name)
                      .reset_index(drop=False))

# -----------------------------------------------------------------------------

def groupto_tuple(data_frame, column_list, column_name):
    """ Group a variable (column_name) in to a tuple in regards of a
        group of variables (column_list)."""
    return (data_frame.groupby(column_list)[column_name]
                      .apply(lambda x: tuple(x.tolist()))
                      .rename(column_name)
                      .reset_index(drop=False))

# -----------------------------------------------------------------------------

def groupto_sorted_tuple(data_frame, column_list, column_name, n=0):
    """ Group a variable (column_name) in to a single tuple in regards of a
        group of variables (column_list).
        Sort a list of tuples by first, second, or n element."""
    aux_fun = lambda x: tuple(sorted(x, key=itemgetter(n)))
    return (data_frame.groupby(column_list)[column_name]
                      .apply(lambda x: aux_fun(x.tolist()))
                      .rename(column_name)
                      .reset_index(drop=False))

# -----------------------------------------------------------------------------

def groupto_dict(data_frame, column_list, column_new_name):
    """ Generate new column with dictionaries having values of othe columns."""
    all_cols = list(data_frame.columns)
    # Remove from the column list the name of the columns that will be grouped.
    for to_rem in column_list:
        all_cols.remove(to_rem)
    no_group_data = data_frame[all_cols]
    group_data = (pd.Series(data_frame[column_list]
                    .to_dict(orient='records'))
                    .rename(column_new_name))
    return pd.concat([no_group_data, group_data], axis=1)

# -----------------------------------------------------------------------------

def groupto_set(data_frame, column_list, column_name):
    """ Group a variable (column_name) in to a single list/set in regards of a
        group of variables (column_list)."""
    return (data_frame.groupby(column_list)[column_name]
                      .apply(lambda x: list(set(x)))
                      .rename(column_name)
                      .reset_index(drop=False))

# -----------------------------------------------------------------------------

def groupto_sorted_set(data_frame, column_list, column_name):
    """ Group a variable (column_name) in to a single list/set in regards of a
        group of variables (column_list)."""
    def aux_fun(x):
        x = list(set(x))
        x.sort()
        return x
    return (data_frame.groupby(column_list)[column_name]
                      .apply(aux_fun)
                      .rename(column_name)
                      .reset_index(drop=False))

# -----------------------------------------------------------------------------

def flat_list(l):
    """ Flatten a list with nested lists.
        [100,[103, [555]]], 102] = [100, 103, 555, 102]"""
    if isinstance(l, pd.Series):
        l = l.tolist()
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
        l = flat_list(l)
    return l

# -----------------------------------------------------------------------------

def extend_column(data_frame, col_name_1, col_name_2, col_new_name):
    data_frame = data_frame.to_dict(orient='records')
    for e in data_frame:
        if not isinstance(e[col_name_1], list):
            e[col_name_1] = []
        if not isinstance(e[col_name_2], list):
            e[col_name_2] = []
        _1 = list(e[col_name_1])
        _2 = list(e[col_name_2])
        _1.extend(_2)
        del e[col_name_1]
        del e[col_name_2]
        e[col_new_name] = _1
    data_frame = pd.DataFrame(data_frame)
    return data_frame

# -----------------------------------------------------------------------------

def chunkify(chunk_this, chunk_size):
    """ Create smaller chunks in the same list. If a pandas DataFrame is used
        then the result is a list of DataFrames."""
    if isinstance(chunk_this, pd.DataFrame):
        chunk_this = chunk_this.to_dict(orient='records')
        return ([pd.DataFrame(chunk_this[x:x+chunk_size])
                for x in range(0,len(chunk_this),chunk_size)])
    return ([chunk_this[x:x+chunk_size]
            for x in range(0,len(chunk_this),chunk_size)])

# -----------------------------------------------------------------------------
