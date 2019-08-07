# Matplotlib

We've learned how to represent data and how to load data in from a file. Then we'll need how to look at our data visually. For this, we'll use Matplotlib, that is a library that allows us to easily make plots with Python.

## Creating a chart

Before plotting, we need the points that we're gonna plot. That, for a line chart, means that we need both *X* axis and *Y* axis. Remember that for every point in *X* corresponds a point into *Y*.

Example for printing a simple chart is [here](https://github.com/SrChach/numpy_stack_and_algorithms/blob/master/matplotlib/basics.py)

### Creating points for a chart

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

There are some types of chart that we can do, now we can use various of this to print some types of charts.

Here's a description of some of the supported chart types:

|Chart|Description|
|:---:|:---|
|Histogram|A discretized probability distribution of the data, or the frequency counts in each bucket of values (How many points of DATASET fall into each bucket)|

|Chart|Method|
|:---:|:---:|
|Linear|matplotlib.plot(VALUES_X_AXIS, VALUES_Y_AXIS)|
|Scatterplot|matplotlib.scatter(VALUES_X_AXIS, VALUES_Y_AXIS)|

Both of them uses the same parameters, that are two arrays representing the coordinates into *X* axis and into *Y* axis.

Assigning points to chart is simple as use one of these methods.

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

## Various charts in the same plot

Now, what if we want to have more than one single chart into a plot, maybe for data comparison?

Well, we can do it easily by calling another time `matplotlib.plot` or `matplotlib.scatter` with the desired conjunctions before show the plot.

An example of this can be:

``` python
# We assume that our test sets are already defined

# Creating a line chart
matplotlib.plot(EXAMPLE_X_AXIS, EXAMPLE_Y_AXIS)

# Adding a second chart
matplotlib.scatter(EXAMPLE_X_AXIS_1, EXAMPLE_X_AXIS_2)

# And then, just gonna plot all the charts defined previously
matplotlib.show()
```

A running example of two charts within the same plot is [Here](https://github.com/SrChach/numpy_stack_and_algorithms/blob/master/matplotlib/scatterplot.py)