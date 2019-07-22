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

Now, we can work directly and get some useful functions from dataFrames, for example

``` python
# getting DataFrame info
pandas_data.info()

N = 3

# Getting the first N rows from the DataFrame
dataframe.head( N )
```

## Accesing to DataFrames

Now, because we cannot access to dataframe elements this way
 
> dataframe[0, 1]

we need to convert it to a Numpy's array, this can be achieed with this function



But we still have another ways to access to the data in a DataFrame

``` python
# Converting dataFrame into numpy's array
numpy_array = dataframe.as_matrix()

# Accesing to data with square brackets will return the column, not the row as we used to
numpy_array[0]
```






[dataframe operations](https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html)


