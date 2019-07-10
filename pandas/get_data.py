import numpy as np
import pandas as pd

## getting the data traditional way (no pandas)

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

# printing not the array but its sizes
print("Getting data from CSV:", normal_get_from_csv().shape, "\n")

# Getting data from CSV with Pandas
def pandas_get_from_csv():
	# We specify header:None to tell Pandas that the first row is not the header of the table 
	array = pd.read_csv("data_2d.csv", header=None)

	# Pandas return dataframes while reading from CSV
	print("\nwhat type of dataType this returns?: ", type(array), "\n")

	return array

# note: In general, Pandas will try to use the most specific data type possible
pandas_dataframe = pandas_get_from_csv()

print("info from the CSV with Pandas:\n")
print(pandas_dataframe.info(), "\n")

print("preview of what's in the dataFrame:\n", pandas_dataframe.head(3))