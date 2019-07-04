# rubik

A set of very useful tools for data wrangling and processing that could be used with the Python library Pandas. This tools allows the user to give to a Pandas DataFrame any kind of complex structured, being able to arrange columns and rows as if they were part of a Rubik's cube.

## Test and use rubik

```
import rubik as rk
import pandas as pd
```

## Available Functions:

This is a list of the functions with very simple examples for it use.

### 0. The header

```
import pandas as pd
from operator import itemgetter
pd.set_option('display.max_columns', 20)
```

After the Pandas Version 0.23, the used must explicitly specify the number of columns that will be printed in the standard output. When Pandas library is loaded the `set_option` method set the default to 20.

### 1. **changeNaNforEmptyList** function

`changeNaNforEmptyList(data_frame, column_name)`

From any column in a DataFrame, replace the NaN values with empty lists.

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
| 4     | user-5512 | [3,4]     |
| 5     | user-25   | [1, 2, 3] |

The **new table** is:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | [ ]       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | [ ]       |
| 4     | user-5512 | [3,4]     |
| 5     | user-25   | [1, 2, 3] |

The **code** is:

```
new = rk.changeNaNforEmptyList(original, 'Roles')
```

### 2. **concatColsToList** function

`concatColsToList(data_frame, column_list, column_new_name)`

Concatenate multiple columns of a data frame into a single list.

#### 2.1 Arguments:

```
data_frame      - The DataFrame we are going to work with.

column_list     - A List with the column names we are going to work with.

column_new_name - A String with the column name we are going to create.
```

### 3. **unGroupLists** function

`unGroupLists(data_frame, column_name)`

This function unnest a 'Series of Lists' in a Pandas data frame.

#### 3.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.
```

### 4. **splitDictCol** function

`splitDictCol(data_frame, column_name)`

This function flatten a data frame with dictionaries in a column.

#### 4.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name - A String with the column name we are going to modify.
```

### 5. **groupToList** function

`groupToList(data_frame, column_list, column_name)`

Group a variable (column_name) in to a single list in regards of agroup of variables (column_list).

#### 5.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.
```

### 6. **groupToTuple** function

`groupToTuple(data_frame, column_list, column_name)`

Group a variable (column_name) in to a tuple in regards of a group of variables (column_list).

#### 6.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.
```

### 7. **groupToSortedTuple** function

`groupToSortedTuple(data_frame, column_list, column_name, n=0)`

Group a variable (column_name) in to a single tuple in regards of a group of variables (column_list). Sort a list of tuples by the first, second, or n-1 element.

#### 7.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.

n           - An integer with the index of the sorting value (default n = 0).
```

### 8. **groupToDict** function

`groupToDict(data_frame, column_list, column_new_name)`

Generate new column with dictionaries having values of othe columns.

#### 8.1 Arguments:

```
data_frame      - The DataFrame we are going to work with.

column_list     - A List with the column names we are going to work with.

column_new_name - A String with the column name we are going to create.
```

### 9. **groupToSet** function

`groupToSet(data_frame, column_list, column_name)`

Group a variable (column_name) in to a single set in regards of a group of variables (column_list).

#### 9.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.
```

### 10. **groupToSortedSet** function

`groupToSortedSet(data_frame, column_list, column_name)`

Group a variable (column_name) into a sorted set in regards of a group of variables (column_list).

#### 10.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_list - A List with the column names we are going to work with.

column_name - A String with the column name we are going to modify.
```

### 11. **combineListColumns** function

`combineListColumns(data_frame, column_name_1, column_name_2, column_new_name)`

Expand 2 Pandas Series with every element being lists into a single column with lists.

#### 11.1 Arguments:

```
data_frame  - The DataFrame we are going to work with.

column_name_1 - A String with the column name we are going to modify.

column_name_2 - A String with the column name we are going to modify.

column_new_name - A String with the column name we are going to create.
```

### 12. **table** function

`table(_list)`

This function works like table() in R. It returns a data frame with the frequency of the elements in a given list.

#### 12.1 Arguments:

```
_list  - The List we are going to work with.
```

### 13. **flattenList** function

`flattenList(_list)`

Flatten a list with nested lists (e.g. [100,[103, [555]]], 102] = [100, 103, 555, 102])

#### 13.1 Arguments:

```
_list  - The List we are going to work with.
```

### 14. **chunkify** function

`chunkify(chunk_this_list, chunk_size)`

Flatten a list with nested lists (e.g. [100,[103, [555]]], 102] = [100, 103, 555, 102])

#### 14.1 Arguments:

```
chunk_this_list  - The List we are going to work with.

chunk_size       - An integer with the number of elements in a chunk.
```

## Versions:

- version - 1.3.1. *'Just a little bit higher, not too much.'*

    1. Standardizing names and the format.

- version 1.3 *'I should not be high in classes.'*
        
    1. Improvements in the flatDict.
            Avoid crashing names with the dictionary keys.
    2. Adding the chunkify function.

- version 0 *I am not the original one, but I'm old, thought.*
