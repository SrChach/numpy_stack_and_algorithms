import pandas as pd
import numpy as np

# why this??
import matplotlib.pyplot as plt

# Reading the file
data = pd.read_csv('datasets/data_1d.csv', header=None).values

# Because the X axis is the data in the first column, and the 
#	Y axis is the data into second column, we'll get it.
# In this case, ":" means "select all from this dimension"
#	below sentences means "select all the samples but only one of the columns"
x_axis = data[:, 0]
y_axis = data[:, 1]

# defining the scatterplot chart
plt.scatter(x_axis, y_axis)


# We can add another chart to first chart, and we'll do it 
#	(all the steps from here to down were adressed previously)

# defining axis
x_line =  np.linspace(0, 100, 100)
y_line =  (2 * x_line) + 1

# adding a new chart
plt.plot(x_line, y_line)



# showing the chart
plt.show()