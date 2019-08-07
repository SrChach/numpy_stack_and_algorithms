import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/data_1d.csv', header=None).values

x_axis = data[:, 0]
y_axis = data[:, 1]

# plt.hist(x_axis)
# plt.show()

# # Demonstrating that random() gives us data uniformly distributed
# rd = np.random.random(1000)

# # You can control the number of buckets shown by the "bins" parameter

# plt.hist(rd, bins=50)
# plt.show()

# Demonstrating that some shit it's normally distributed
y_actual =  (2*x_axis) + 1

residuals = y_axis - y_actual

plt.hist(residuals)
# Seems like it has a normal distribution (the Bell)
plt.show()