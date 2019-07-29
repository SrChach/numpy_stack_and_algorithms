import numpy as np
import matplotlib.pyplot as plt

# Creating data points to the X axis
#	Linspace is another way to generate data that we haven't seen yet
#	Takes the starting point, the end point and how many points will be between
x_axis = np.linspace(0, 10, 100)

# Creating a sine for the x_axis, element by element
y_axis = np.sin(x_axis)

# assigning coordinates to the plot
plt.plot(x_axis, y_axis)

# Adding a name to X coordinates
plt.xlabel("time")

# Adding a name to Y coordinates
plt.ylabel("some function")

# Adding a customized name to chart 
plt.title("My first chart")

# Showing the built chart
plt.show()



