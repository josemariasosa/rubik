# rubik

A set of very useful tools for data wrangling and data processing that could be used with the Python library Pandas. This set of tools allows the user to give to a Pandas DataFrame any kind of complex structure, being able to arrange columns and rows as if they were part of a Rubik's cube.

Share **rubik** with all your panda friends!

## List of Content

1. [**fillna_list()**](https://github.com/josemariasosa/rubik#1-the-rkfillna_list-function)
2. [**concat_to_list()**](https://github.com/josemariasosa/rubik#2-the-rkconcat_to_list-function)
3. [**ungroup_list()**](https://github.com/josemariasosa/rubik#3-the-rkungroup_list-function)
4. [**ungroup_dict()**](https://github.com/josemariasosa/rubik#4-the-rkungroup_dict-function)
5. [**list_to_columns()**](https://github.com/josemariasosa/rubik#5-the-rklist_to_columns-function)
6. [**groupto_list()**](https://github.com/josemariasosa/rubik#6-the-rkgroupto_list-function)
7. [**groupto_tuple()**](https://github.com/josemariasosa/rubik#7-the-rkgroupto_tuple-function)
8. [**groupto_sorted_tuple()**](https://github.com/josemariasosa/rubik#8-the-rkgroupto_sorted_tuple-function)
9. [**groupto_dict()**](https://github.com/josemariasosa/rubik#9-the-rkgroupto_dict-function)
10. [**groupto_set()**](https://github.com/josemariasosa/rubik#10-the-rkgroupto_set-function)
11. [**groupto_sorted_set()**](https://github.com/josemariasosa/rubik#11-the-rkgroupto_sorted_set-function)
12. [**extend_column()**](https://github.com/josemariasosa/rubik#12-the-rkextend_column-function)
13. [**table()**](https://github.com/josemariasosa/rubik#13-the-rktable-function)
14. [**flat_list()**](https://github.com/josemariasosa/rubik#14-the-rkflat_list-function)
15. [**chunkify()**](https://github.com/josemariasosa/rubik#15-the-rkchunkify-function)
16. [**fillna_dict()**](https://github.com/josemariasosa/rubik#16-the-rkfillna_dict-function)

## Test and use rubik

### Install rubik

To install rubik from the terminal, first create a virtual environment `venv`, then use the `pip install` command:

```bash
python3 -m venv venv
source venv/bin/activate

pip install git+https://github.com/josemariasosa/rubik
```

### Check version

To make sure the installation was correct, check Rubik's version using the following command from the terminal:

```bash
python -c 'import rubik; print(rubik.__version__)'
# 2.1.0
```

### Use rubik in your scripts

Import the module using the `rk` alias for rubik.

```python
import rubik as rk
import pandas as pd
```

## Available Functions:

This is a list of the functions with very simple examples for it use.

### 0. The header

```python
import pandas as pd
from operator import itemgetter
pd.set_option('display.min_rows', 30)
pd.set_option('display.max_rows', 60)
pd.set_option('display.max_columns', 20)
```

After the Pandas Version 0.23, the used must explicitly specify the number of columns that will be printed in the standard output. When Pandas library is loaded the `set_option` method set the default to 20.

---

### 1. The `rk.fillna_list` Function

`rk.fillna_list(data_frame, column_name)`

From any column in a DataFrame, replace the `NaN` values with empty lists.

#### 1.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.
```

#### 1.2 Example:

The **original table** is:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | NaN       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | NaN       |
| 4     | user-5512 | [3, 4]    |
| 5     | user-25   | [1, 2, 3] |

The **new table** is:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | [ ]       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | [ ]       |
| 4     | user-5512 | [3, 4]    |
| 5     | user-25   | [1, 2, 3] |

The **code** is:

```python
new = rk.fillna_list(original, 'Roles')
```

---

### 2. The `rk.concat_to_list` Function

`rk.concat_to_list(data_frame, column_list, column_new_name)`

Concatenate multiple columns of a data frame into a single list.

#### 2.1 Arguments:

```
data_frame      - The DataFrame we are going to work with.

column_list     - A List with the column names we are going to work with.

column_new_name - A String with the column name we are going to create.
```

#### 2.2 Example:

The **original table** is:

| Entry | Id        | Role 1 | Role 2 |
|-------|-----------|--------|--------|
| 0     | user-123  | 1      | 2      |
| 1     | user-452  | 1      | 3      |
| 2     | user-21   | 5      | 2      |
| 3     | user-621  | 3      | 1      |
| 4     | user-5512 | 3      | 4      |
| 5     | user-25   | 1      | 3      |

The **new table** is:

| Entry | Id        | Roles  |
|-------|-----------|--------|
| 0     | user-123  | [1, 2] |
| 1     | user-452  | [1, 3] |
| 2     | user-21   | [5, 2] |
| 3     | user-621  | [3, 1] |
| 4     | user-5512 | [3, 4] |
| 5     | user-25   | [1, 3] |

The **code** is:

```python
new = rk.concat_to_list(original, ['Role 1', 'Role 2'], 'Roles')
```

---

### 3. The `rk.ungroup_list` Function

`rk.ungroup_list(data_frame, column_name)`

This function unnest a 'Series of Lists' in a Pandas data frame.

⚡️ Note that the number of rows for the result may increase.

#### 3.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.
```

#### 3.2 Example:

The **original table** is:

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | [1, 2] |
| 1     | user-452 | [5, 7] |
| 2     | user-21  | [3]    |

The **new table** is:

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 1     |
| 0     | user-123 | 2     |
| 1     | user-452 | 5     |
| 1     | user-452 | 7     |
| 2     | user-21  | 3     |

The **code** is:

```python
new = rk.ungroup_list(original, 'Roles')
```

---

### 4. The `rk.ungroup_dict` Function

`rk.ungroup_dict(data_frame, column_name, prefix=False)`

This function flatten a data frame with dictionaries in a column.

#### 4.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.

prefix - Use the prefix argument as follow:
    - False: default, regular behavior, column names are the dict keys.
    - True: Use as prefix the original column name followed by an underscore.
    - String: The user can give any prefix.
```

#### 4.2 Example:

The **original table** is:

| Entry | Id        | Roles                       |
|-------|-----------|-----------------------------|
| 0     | user-123  | {"main": 1, "secondary": 2} |
| 1     | user-452  | {"main": 3, "secondary": 1} |
| 2     | user-21   | {"main": 7}                 |
| 3     | user-621  | {"main": 2, "secondary": 6} |
| 4     | user-5512 | {"main": 7, "secondary": 5} |
| 5     | user-25   | {"main": 3}                 |

The **new table** is:

| Entry | Id        | main | secondary |
|-------|-----------|------|-----------|
| 0     | user-123  | 1    | 2         |
| 1     | user-452  | 3    | 1         |
| 2     | user-21   | 7    | NaN       |
| 3     | user-621  | 2    | 6         |
| 4     | user-5512 | 7    | 5         |
| 5     | user-25   | 3    | NaN       |

The **code** is:

```python
new = rk.ungroup_dict(original, 'Roles')
```

---

### 5. The `rk.list_to_columns` Function

`rk.list_to_columns(data_frame, column_name)`

This function creates multiple columns from a single column with lists.

#### 5.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.
```

#### 5.2 Example:

The **original table** is:

| Entry | Id        | Roles  |
|-------|-----------|--------|
| 0     | user-123  | [1, 2] |
| 1     | user-452  | [1, 3] |
| 2     | user-21   | [5, 2] |
| 3     | user-621  | [3, 1] |
| 4     | user-5512 | [3, 4] |
| 5     | user-25   | [1, 3] |

The **new table** is:

| Entry | Id        | Roles_1 | Roles_2 |
|-------|-----------|---------|---------|
| 0     | user-123  | 1       | 2       |
| 1     | user-452  | 1       | 3       |
| 2     | user-21   | 5       | 2       |
| 3     | user-621  | 3       | 1       |
| 4     | user-5512 | 3       | 4       |
| 5     | user-25   | 1       | 3       |

The **code** is:

```python
new = rk.list_to_columns(original, 'Roles')
```

---

### 6. The `rk.groupto_list` Function

`rk.groupto_list(data_frame, column_list, column_name)`

Group a variable (column_name) in to a single list in regards of agroup of variables (column_list).

#### 6.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with as pivot columns.

column_name - A String with the column name we are going to modify.
```

#### 6.2 Example:

The **original table** is:

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 1     |
| 0     | user-123 | 2     |
| 1     | user-452 | 5     |
| 1     | user-452 | 7     |
| 2     | user-21  | 3     |

The **new table** is:

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | [1, 2] |
| 1     | user-452 | [5, 7] |
| 2     | user-21  | [3]    |

The **code** is:

```python
new = rk.groupto_list(original, ['Entry', 'Id'], 'Roles')
```

---

### 7. The `rk.groupto_tuple` Function

`rk.groupto_tuple(data_frame, column_list, column_name)`

Group a variable (column_name) into a tuple in regards of a group of variables (column_list).

#### 7.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with as pivot columns.

column_name - A String with the column name we are going to modify.
```

#### 7.2 Example:

The **original table** is:

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 1     |
| 0     | user-123 | 2     |
| 1     | user-452 | 5     |
| 1     | user-452 | 7     |
| 2     | user-21  | 3     |

The **new table** is:

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | (1, 2) |
| 1     | user-452 | (5, 7) |
| 2     | user-21  | (3, )  |

The **code** is:

```python
new = rk.groupto_tuple(original, ['Entry', 'Id'], 'Roles')
```

---

### 8. The `rk.groupto_sorted_tuple` Function

`rk.groupto_sorted_tuple(data_frame, column_list, column_name, n=0)`

Group a variable (column_name) in to a single tuple in regards of a group of variables (column_list). Sort a list of tuples by the first, second, or n-1 element.

#### 8.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.

n           - An integer with the index of the sorting value (default n = 0).
```

#### 8.2 Example:

The **original table** is:

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 2     |
| 0     | user-123 | 1     |
| 1     | user-452 | 7     |
| 1     | user-452 | 5     |
| 2     | user-21  | 3     |

The **new table** is:

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | (1, 2) |
| 1     | user-452 | (5, 7) |
| 2     | user-21  | (3, )  |

The **code** is:

```python
new = rk.groupto_sorted_tuple(original, ['Entry', 'Id'], 'Roles')
```

---

### 9. The `rk.groupto_dict` Function

`rk.groupto_dict(data_frame, column_list, column_new_name)`

Generate new column with dictionaries having values of othe columns.

#### 9.1 Arguments:

```
data_frame      - The DataFrame we are going to work with.

column_list     - A List with the column names we are going to work with.

column_new_name - A String with the column name we are going to create.
```

#### 9.2 Example:

The **original table** is:

| Entry | Id        | main | secondary |
|-------|-----------|------|-----------|
| 0     | user-123  | 1    | 2         |
| 1     | user-452  | 3    | 1         |
| 2     | user-21   | 7    | 3         |
| 3     | user-621  | 2    | 6         |
| 4     | user-5512 | 7    | 5         |
| 5     | user-25   | 3    | 3         |

The **new table** is:

| Entry | Id        | Roles                       |
|-------|-----------|-----------------------------|
| 0     | user-123  | {"main": 1, "secondary": 2} |
| 1     | user-452  | {"main": 3, "secondary": 1} |
| 2     | user-21   | {"main": 7, "secondary": 3} |
| 3     | user-621  | {"main": 2, "secondary": 6} |
| 4     | user-5512 | {"main": 7, "secondary": 5} |
| 5     | user-25   | {"main": 3, "secondary": 3} |

The **code** is:

```python
new = rk.groupto_dict(original, ['main', 'secondary'], 'Roles')
```

---

### 10. The `rk.groupto_set` Function

`rk.groupto_set(data_frame, column_list, column_name)`

Group a variable (column_name) in to a single set in regards of a group of variables (column_list).

**The returned object type is List, not an actual set.**

#### 10.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.
```

#### 10.2 Example:

The **original table** is:

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 2     |
| 0     | user-123 | 1     |
| 1     | user-452 | 7     |
| 1     | user-452 | 7     |
| 2     | user-21  | 3     |

The **new table** is:

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | [2, 1] |
| 1     | user-452 | [7]    |
| 2     | user-21  | [3]    |

The **code** is:

```python
new = rk.groupto_set(original, ['Entry', 'Id'], 'Roles')
```

---

### 11. The `rk.groupto_sorted_set` Function

`rk.groupto_sorted_set(data_frame, column_list, column_name)`

Group a variable (column_name) into a sorted set in regards of a group of variables (column_list).

**The returned object type is List, not an actual set.**

#### 11.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.
```

#### 11.2 Example:

The **original table** is:

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 2     |
| 0     | user-123 | 1     |
| 1     | user-452 | 7     |
| 1     | user-452 | 7     |
| 2     | user-21  | 3     |

The **new table** is:

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | [1, 2] |
| 1     | user-452 | [7]    |
| 2     | user-21  | [3]    |

The **code** is:

```python
new = rk.groupto_sorted_set(original, ['Entry', 'Id'], 'Roles')
```

---

### 12. The `rk.extend_column` Function

`rk.extend_column(data_frame, col_name_1, col_name_2, col_new_name)`

Expand 2 Pandas Series with every element being lists into a single column with lists.

#### 12.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

col_name_1 - A String with the column name we are going to modify.

col_name_2 - A String with the column name we are going to modify.

col_new_name - A String with the column name we are going to create.
```

#### 12.2 Example:

The **original table** is:

| Entry | Id        | Roles1 | Roles2 |
|-------|-----------|--------|--------|
| 0     | user-123  | [1, 2] | [ ]    |
| 1     | user-452  | [3, 1] | [2]    |
| 2     | user-21   | [7]    | [5, 4] |
| 3     | user-621  | [2, 6] | [ ]    |
| 4     | user-5512 | [7, 5] | [1]    |
| 5     | user-25   | [3]    | [4, 5] |

The **new table** is:

| Entry | Id        | Roles    |
|-------|-----------|-----------|
| 0     | user-123  | [1, 2]    |
| 1     | user-452  | [3, 1, 2] |
| 2     | user-21   | [7, 5, 4] |
| 3     | user-621  | [2, 6]    |
| 4     | user-5512 | [7, 5, 1] |
| 5     | user-25   | [3, 4, 5] |

The **code** is:

```python
new = rk.extend_column(original, 'Roles1', 'Roles2', 'Roles')
```

---

### 13. The `rk.table` Function

`rk.table(_list)`

This function works like table() in R. It returns a data frame with the frequency of the elements in a given list.

The response is a Pandas DataFrame.

#### 13.1 Arguments:

```
_list  - The List we are going to work with.
```

#### 13.2 Example:

The **original list** is:

`[100, 103, 555, 102, 100, 100, 100, 102, 103, 103]`

The **new table** is:

| value | freq |
|-------|------|
| 100   | 4    |
| 103   | 3    |
| 102   | 2    |
| 555   | 1    |

The **code** is:

```python
original = [100, 103, 555, 102, 100, 100, 100, 102, 103, 103]

new = rk.table(original)
```

---

### 14. The `rk.flat_list` Function

`rk.flat_list(_list)`

Flatten a list with nested lists.

#### 14.1 Arguments:

```
_list  - The List we are going to work with.
```

#### 14.2 Example:

The **original list** is:

`[[100,[103, [555]]], 102]`

The **new list** is:

`[100, 103, 555, 102]`

The **code** is:

```python
original = [[100,[103, [555]]], 102]

new = rk.flat_list(original)

print(new)
# [100, 103, 555, 102]
```

---

### 15. The `rk.chunkify` Function

`rk.chunkify(chunk_this_list, chunk_size)`

Create smaller chunks in the same list.

#### 15.1 Arguments:

```
chunk_this_list  - The List we are going to work with.

chunk_size       - An integer with the number of elements in a chunk.
```

#### 15.2 Example:

The **original list** is:

`[100, 103, 555, 102, 100, 100, 100, 102, 103]`

The **new list** is:

`[[100, 103], [555, 102], [100, 100], [100, 102], [103]]`

The **code** is:

```python
original = [100, 103, 555, 102, 100, 100, 100, 102, 103, 103]

new = rk.chunkify(original, 2)

print(new)
# [[100, 103], [555, 102], [100, 100], [100, 102], [103]]
```

---

### 16. The `rk.fillna_dict` Function

`rk.fillna_dict(data_frame, column_name)`

From any column in a DataFrame, replace the NaN values with empty dictionaries.

#### 16.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.
```

#### 16.2 Example:

The **original table** is:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | NaN       |
| 1     | user-452  | NaN       |
| 2     | user-21   | {'r': 1}  |
| 3     | user-621  | NaN       |
| 4     | user-5512 | {'r': 2}  |
| 5     | user-25   | NaN       |

The **new table** is:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | { }       |
| 1     | user-452  | [1]       |
| 2     | user-21   | {'r': 1}  |
| 3     | user-621  | { }       |
| 4     | user-5512 | {'r': 2}  |
| 5     | user-25   | { }       |

The **code** is:

```python
new = rk.fillna_dict(original, 'Roles')
```

---

Get the code of the last version [here](https://github.com/josemariasosa/rubik/blob/master/rubik.py).

## Versions:

- version - 2.2.3 *'Pareciera ser todo más oscuro acá abajo.'*

    1. `flat_list` is more compatible with Pandas.
    2. I removed the versions funny names from the code.

- version - 2.2.2 *'My guitar is not too loud!'*

    1. Fixing edge case for the `flat_list` function.

- version - 2.2.1 *'Never stop until the cube is done.'*

    1. Fixing edge case for the `ungroup_dict` function using math.
    https://docs.python.org/3/library/math.html#math.isnan
    2. New function. fillna_dict.

- version - 2.2 *'Pandemic leisure.'*

    1. Updating function. For `ungroup_dict`, the user may use a prefix for the new columns that will be created.

- version - 2.1 *'This is the end of a decade.'*

    1. (deleted) New function. Expand a column with a list, into multiple columns.
    2. Updating function. chunkify receives now a list or a DataFrame.

- version - 2.0. *'PyCon Latam 2019 - Puerto Vallarta.'*

    1. New function names. Again! In compliance with PEP8.
    2. Create the rubik Package for git.
    3. pip install git+https://github.com/josemariasosa/rubik

- version - 1.3.2. *'New job. New opportunities.'*

    1. Displaying a DataFrame in the standard output in a pretty way.
        - Once the display.max_rows is exceeded, the display.min_rows
        options determines how many rows are shown in the truncated
        repr.

- version - 1.3.1. *'Just a little bit higher. Not too much.'*

    1. Standardizing names and the format.

- version - 1.3. *'I should not be high in classes.'*
            
	1. Improvements in the flatDict function.
        - Avoid crashing names with the dictionary keys.

    2. Adding the chunkify function.

- version - 0. *'I am not the original one, but I'm old, thought.'*
