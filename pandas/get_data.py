import numpy as np
import pandas as pd


## getting the data traditional way (without pandas)
def normal_get_from_csv():
	array = []

	# opening the file
	for line in open("data_2d.csv"):
		row = line.split(',') # getting an array of strings of each row
		sample = list( map(float, row) ) # Converting list into float numbers
		array.append(sample)

	# Converting normal array into numpy array
	array = np.array(array)

	return array


# Getting data from CSV with Pandas
def pandas_get_from_csv():
	# We specify header:None to tell Pandas that the first row is not the header of the table 
	dataframe = pd.read_csv("data_2d.csv", header=None)

	# Pandas return dataframes while reading from CSV
	print("\nwhat type of dataType this returns?: ", type(dataframe), "\n")

	# getting dataframe info:
	print(dataframe.info(), "\n")
	print("preview of what's into the dataFrame:\n", dataframe.head(3))

	return dataframe


# printing not the array but its sizes
print("Getting data from CSV normal way:", normal_get_from_csv().shape, "\n")

# note: In general, Pandas will try to use the most specific data type possible while reading
dataframe = pandas_get_from_csv()


def dataframe_to_numpy_array(dataframe):
	# Converting to a numpy array
	numpy_array = dataframe.values

	# checking if converting was done
	print( "\ntype of converted dataFrame: ", type(numpy_array) )


def accessing_to_dataframe_column(dataframe, column_name):
	# Remember that DataFrame is matrix-style, and its type is "Dataframe"
	
	# what we pass to square brackets is the name of the column we want to retrieve
	column = dataframe[column_name]

	# the new column has only one Dimension, and a different type: "Series"
	print("\nType of the retrieved DataFrame's column: ", type(column))


def accessing_to_dataframe_row(dataframe, row_name):
	# We can access to DataFrame rows these two ways
	row = dataframe.loc[row_name]

	# or
	row = dataframe.iloc[row_name]

	print("\nRow retrieved:\n", row)
	print("\nType of a DataFrame' row: ", type(row))


dataframe_to_numpy_array(dataframe)
accessing_to_dataframe_column(dataframe, 0)
accessing_to_dataframe_row(dataframe, 0)


def accessing_with_some_criteria(dataframe):
	# Accessing to specific columns of the dataframe (in this case, columns 0 and 2)
	specific_columns = dataframe[ [0, 2] ]

	# Because is 2D, will return a DataFrame type
	print("\nAccessing to specific columns:\n", specific_columns.head(), "\n")

	# Accessing to specific rows of the dataframe (in this case, rows 3, 12 and 45)
	specific_rows = dataframe.iloc[ [3, 12, 45] ]
	print("Accessing to specific rows:\n", specific_rows.head(), "\n")

	# We can also select rows or columns that meet a specific condition
	#	So the syntax is: Inside the square brackets, select the column and compare to 
	# some value. In this case, where the value in column "0" is less than 5
	condition_met = dataframe[ dataframe[0] < 5 ]

	print("\nWhere meeting a condition: (value in column '0' less than 5)\n", condition_met)

	# Here we will check what's passing while checking for a condition into DataFrame
	checked = (dataframe[0] < 5)
	print("\nWhile checking for a condition in a dataframe, we obtain\n", checked.head() )
	print("and its type is, of course, '{}'".format(type(checked).__name__) )


accessing_with_some_criteria(dataframe)


