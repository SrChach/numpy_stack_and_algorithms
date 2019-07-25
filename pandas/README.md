# Pandas

While working as data scientists, one of our main problems is get and transform data. Specifically with CSV files, we need to tokenize, split and assign our data into memory. 

## What is pandas

Pandas is a library that makes easier working with CSV files, and converting it automatically into an analizable object.

Its a lot like R, and various of the operations are contra-intuitive if you don't come from an R background.

Getting information from a CSV with Pandas it's simpler like

``` python
import pandas

# Reading info from a CSV file
pandas_data = pandas.read_csv("example_file.csv", header=None)
```

> Note: The second argument passed to *read_data()* is for specify that the first row of the CSV isn't the header 

## Dataframes

When we execute the ***type()*** function to data readed by pandas, we'll notice that its dataType is *dataframe*.

``` python
# Getting dataType (will return pandas.core.frame.DataFrame)
print( type(pandas_data) )
```

Now, we can work directly and get some useful data from dataFrames functions.

``` python
# getting DataFrame info
pandas_data.info()

# Getting the first N rows from the DataFrame
N = 3
dataframe.head( N )
```

But here there are more than that. So, how do DataFrames really works?

## Exporting DataFrames to Numpy arrays

Notice that we cannot access to dataframe elements this way
 
> dataframe[0, 1]

Due to that, we will often need to convert it to a Numpy array. This can be achieved simply by using

``` python
# Converting dataFrame into numpy's array
numpy_array = dataframe.values
```

## Accessing to data in DataFrames

But... there's a main difference while accessing data between Numpy and Pandas

``` python
# Where in Numpy this means accessing to the first row ( 0th row )
numpy_matrix_example[0]

# Into pandas means accessing to the first column ( column with name 0 ), not the row as we're used to
dataframe[0]
```

And, if we compare a 2D Pandas DataFrame with one column of the same DataFrame, we'll notice that... They have different types!

``` python
# Getting the DataFrame's type: <class 'pandas.core.frame.DataFrame'>
type(dataframe)

# Accessing to a DataFrame column
column = dataframe[0]
# Getting column's type: <class 'pandas.core.series.Series'>
type(column)
```

So, we use *DataFrame* type for **2D** arrays and *Series* type for **1D** array.

We've seen how to get a column from a DataFrame. Now it's time 
to know how to retrieve a row.

``` python
# Both of there ways will work the same, and get the row as expected

dataframe.iloc[0]
# or
dataframe.loc[0]
```

Above lines returned a type *Series*. So, anything with 1D in Pandas is a *Series*.

## Getting specific information

To get specific number of columns, we can do

``` python
example_num_1 = 0
example_num_2 = 2

# Accessing to two specific columns of DataFrame (this case, 0 and 2)
specific_columns = dataframe[ [example_num_1, example_num_2] ]
```

The line above will print the two columns that we've specified. And it works the same for rows

``` python
# Accessing to specific rows of the dataframe (in this case, rows 3, 12 and 45)
specific_rows = dataframe.iloc[ [3, 12, 45] ]
```

We can also select rows or columns that meet a specific condition. The syntax is: 
Inside the square brackets, select a column and compare it to some value. 

```python
# In this case, where the value in column "0" is less than 5
condition_met = dataframe[ dataframe[0] < 5 ]
```

and, like when we access to specific columns, we can do the same for rows.

## Managing DataFrame columns

### Changing column names

When reading data from a CSV, sometimes we need to change it's original names because them could be very large or confusing.

The syntax for achieving this is to pass an array with **exactly** the same name of elements that have the DataFrame as columns. Here's an example

``` python
# "dataframe" for this example is a DataFrame "with" 3 columns
dataframe.columns = ["new_column_name_1", "new_column_name_2", "new_column_name_3"]
```

### Adding new columns

And another times we need to add new columns into an existing DataFrame. We can add columns two ways.

The first is adding a column and within it ALL the values will be the same.

The syntax for it is passing the dataframe name and into square brackets the name of the new column. And equals it to the value that ALL the column will have.

``` python
# this will add a column named NEW_COLUMN_NAME, where all its values will be true 
example_dataframe["NEW_COLUMN_NAME"] = True
```

The second way solves this question: What do we do if we want to assign a new column value based on the other data in its row?

Here's when the *apply* function becomes on action.

The basic syntax is as following

> example_dataframe["NEW_COLUMN_NAME"] = example_dataframe.apply(get_interaction_function, axis=1)

Where get_interaction_function is the function that we will pass to manage the data of current row. This function receives the row as argument and return a value that will be put into the new column. And "NEW_COLUMN_NAME" it's the column in where will be putted the result of that operation.

An example. Suppose that "x1" and "x2" are columns with numbers

``` python
# This will get the DataFrame with a new column that contains the result of multiplicate the values into "x1" by "x2" 
example_dataframe["multiplied"] = example_dataframe(lambda row: row["x1"] * row["x2"])
```


