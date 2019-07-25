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

# This contains an example of doing a join between two dataframes
def joins():
	# Reading tables from the CSV's
	table_1 = pd.read_csv("datasets/table1.csv")
	table_2 = pd.read_csv("datasets/table2.csv")

	print("\n\nPrinting the two tables we're gonna join:\n", table_1, "\n\n", table_2)

	# Joining the two tables by a criteria (specified in "on")
	# If you don't pass "on", it will merge by row index
	#	table_1.merge(table_2, "user_id") also works
	new_dataframe = pd.merge(table_1, table_2, on="user_id")

	# In the case that first table index is different to second table index we can do
	#	new_dataframe = pd.merge(table_1, table_2, left_on='TABLE_1_INDEX', right_on='TABLE_2_INDEX')

	print("\ntable with the Join done:\n", new_dataframe)


managing_columns(dataframe)
adding_columns_based_on_actual_data(dataframe)
joins()

