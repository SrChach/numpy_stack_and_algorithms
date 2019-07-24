import pandas as pd

# Getting data from CSV. Skipping 3 lines of footer,
#	and setting engine to python so that the program dont use de default engine "C"
dataframe = pd.read_csv("international_airline_passengers.csv", engine="python", skipfooter=3)


def managing_columns(dataframe):
	# Printing the original column names from DataFrame
	print("\nOriginal dataframe columns: ", dataframe.columns)

	# Changing the column name from a DataFrame
	dataframe.columns = ["month", "passengers"]
	print("\nChanged column names: ", dataframe.columns)

	# Getting the column, "dataframe.passengers" also works
	print(dataframe["passengers"])

	# Adding a new column, named "ones" and with a one in each value
	dataframe["ones"] = 1

	print(dataframe.head())


managing_columns(dataframe)