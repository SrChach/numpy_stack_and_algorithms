# Matplotlib

We've learned how to represent data and how to load data in from a file. Then we'll need how to look at our data visually. For this, we'll use Matplotlib, that is a library that allows us to easily make plots with Python.

## Line chart

Before plotting, we need the points that we're gonna plot. That, for a line chart, means that we need both *X* axis and *Y* axis. Remember that for every point in *X* corresponds a point into *Y*.

### Creating points for chart

First we need to define from what point to what point we're plotting in both axis, and how many points are in the middle.

More points means more precision in the chart, but more computing cost too.

``` python
import numpy
import matplotlib

# Defining the range of plotting in
beginning_point_of_chart = 0
final_point_of_chart = 10
number_of_points = 100

# This will return a Numpy Array with "numer_of_points" items
x_axis = numpy.linspace(beginning_point_of_chart, final_point_of_chart, number_of_points)

# y_axis contains the sin() for each element in x_axis. It's a numpy array
y_axis = numpy.sin(x_axis)
```

### Assigning points to chart

Assigning points to chart is simple as

``` python
# assigning coordinates to the plot
matplotib.plot(x_axis, y_axis)
```

The above function will take two numpy arrays as parameters, the first is for *x* axis and the second for *y* axis.

### Naming the chart and axes

So far, we've defined our chart. But, if we need to change the name of axes, how we do it?

Because by default matplotlib prints 2D charts, there's a method for each of these two axis.

``` python
# Adding a name to X axis
matplotlib.xlabel("some name for x axis")

# Adding a name to Y axis
matplotlib.ylabel("some name for y axis")
```

Now, there's another function to give a title to the chart

``` python
# Putting a name to the chart
matplotlib.title("An amazing title!")
```

### Plotting

And, to plot the chart the only thing that we need to do is

``` python
# Printing the chart
matplotlib.show()
```

and yeah, that's all. Enjoy your chart.