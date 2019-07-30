# Matplotlib

We've learned how to represent data and how to load data in from a file. Then we'll need how to look at our data visually. For this, we'll use Matplotlib, that is a library that allows us to easily make plots with Python.

 ## Line chart

 Here we create a line chart, that's for every point in *X* axis corresponds a point into *Y* axis. First we need to define from what point to what point we're plotting, and how many points are in the middle.

 More points means more precision in the chart, but more computing cost too.

``` python
import matplotlib as plt

# Defining the range of plotting
beginning_point_of_chart = 0
final_point_of_chart = 10
number_of_points = 100

x_axis = np.linspace(beginning_point_of_chart, final_point_of_chart, number_of_points)
```

