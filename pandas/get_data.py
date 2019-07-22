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
	numpy_array = dataframe.as_matrix()

	# checking if converting was done
	print( "\ntype of converted dataFrame: ", type(numpy_array) )

dataframe_to_numpy_array(dataframe)


