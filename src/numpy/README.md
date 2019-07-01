# Numpy Basics

## Differences betwen numpy and python arrays

Although Numpy has arrays like python, it doesn't handle they the same way. For example operations like following will work in python, but not in Numpy.

``` python
some_list.append(4)
some_list = some_list + [ 5, 6 ]
```

So, what's special about Numpy?

Numpy treat arrays as mathematical objects. But what does this mean? Let's see.

### Vector Addition

First difference is while "+" between arrays into Python means concatenation, in Numpy it means vector sum. Let's take a look.

``` python
import numpy

# concatenation with a normal array
some_list = [1, 2, 3]
print(some_list + some_list) # Will print [1, 2, 3, 1, 2, 3]

# Numpy vector addition
numpy_vector = numpy.array([1, 2, 3])
print(numpy_vector + numpy_vector) # Will print [2, 4, 6]
```

Notice that if *"numpy_vector"* had two dimensions, Numpy would also print the sum of vectors.

### Vector Multiplication

In the case of multiplication, whereas multiplicate an array by a number *N* will return us the array concatenated *N* times, a Numpy vector will return the Vector multiplied by the *N* scalar.

``` python
N = 2

print(some_list * N) # Will print the list concatenated N times

print(numpy_vector * N) # will print a vector multiplied by the scalar "N"
```

### Other operations

Thus, we can also do another operations to the Numpy vector in a simple way, without using a for loop as needed by simple Python. Due that for loops are very slow, we need to avoid them as we can when doing mathematical operations. Some examples of this can be:

Squaring each element in the vector
``` python
print(numpy_vector ** 2) # Print each element squared
```

Getting the square root of the vector
``` python
print( numpy.sqrt(numpy_vector)) # Print each element's square root
```

Getting the Logarithm of every element
```python
print("Log of the vector's elements: ", numpy.log(numpy_vector))
```

Getting e^(N) of each element
```python
print("Exponential of vector: ", numpy.exp(numpy_vector))
```
