import pandas as pd
from datetime import datetime

# Getting data from CSV. Skipping 3 lines of footer,
#	and setting engine to python so that the program dont use de default engine "C"
dataframe = pd.read_csv("datasets/international_airline_passengers.csv", engine="python", skipfooter=3)


def managing_columns(dataframe):
	# Printing the original column names from DataFrame
	print("\nOriginal dataframe columns: ", dataframe.columns)

	# Changing the column name from a DataFrame
	dataframe.columns = ["month", "passengers"]
	print("\nChanged column names: ", dataframe.columns)

	# Getting the column as "dataframe.passengers" also works
	print("\nfirst passengers:\n", dataframe["passengers"].head())

	# Adding a new column, named "ones" and with a one in each value
	dataframe["ones"] = 1

	print("\nchecking if the dataframe was modified:\n", dataframe.head())

# Before use Apply, we need to know lambdas and how it works
# Lambda is like passing a function as an argument

# This function creates a column that contains the string-style dates converted to datetime-style
def adding_columns_based_on_actual_data(dataframe):
	# The function we'll passing takes an argument, and that argument is the row
	# Axis = 1 means lambda will applied each row at a time, instead of each column
	dataframe["date_object"] = dataframe.apply(lambda row: datetime.strptime(row["month"], "%Y-%m"), axis=1)
	print("\nDataframe with a column with 'string-date' converted to 'datetime' object added:\n", dataframe.head())


managing_columns(dataframe)
adding_columns_based_on_actual_data(dataframe)


