# Numpy Basics

Numpy's meaning is "Numeric Python", and it's indeed optimized to get all the numeric operations simple and faster than normal python, without using loops and another slow operations.

But Numpy also treats its arrays and other things as mathematical objects, differently than python. Then, let's figure out how numpy do that.

Note: working examples of Numpy basics are [here](https://github.com/SrChach/numpy_stack_and_algorithms/blob/master/numpy/basics.py)

## Differences betwen numpy and python arrays

Although Numpy has arrays like python, it doesn't handle they the same way. For example operations like following will work in python, but not in Numpy.

``` python
some_list = [1, 2, 3]

some_list.append(4)
some_list = some_list + [ 5, 6 ]
```

So, what's special about Numpy?

## Vector Addition

While "+" between arrays into Python means concatenation, in Numpy it means vector sum.

Recalling that vector sum's formula is:
![vector_sum](../images/vector_sum.png)

If we indicates vectorial sum between two Numpy arrays, it will sum all the posicions into array, term by term as following.

``` python
numpy_vector = numpy.array([1, 2, 3])

# Will print [2, 4, 6]
print(numpy_vector + numpy_vector)
```

Notice that if *"numpy_vector"* were a *N* dimensions array, Numpy would also print the sum of vectors.

## Multiplying vector by scalar

In the case of multiplication, whereas multiplicate an array by a number *X* will return us the array concatenated *N* times in python, a Numpy vector will return the Vector multiplied by the *X* scalar

Remembering that Vector by Scalar formula is:

![Vector_by_scalar](../images/vector_by_scalar.png)

Which means the *X* constant will multiply **every** element in the vector.

``` python
N = 2

# will print a vector multiplied by the scalar "N"
print(numpy_vector * N)
```

## Multiplication betwen vectors

We can also do a multiplication between arrays. What this operation does is multiplicate each element by all the arrays, term by term, and returns to ours a new array with the content of this multiplication, with the same size of the input arrays.

This means that we can't multiply arrays with different sizes.

``` python
A_vector = numpy.array([1, 2, 3])
B_vector = numpy.array([2, 1, 8])
C_vector = numpy.array([5, 5, 0])
# components of vector  ^  ^  ^
#                       1  2  3

# Will print [10, 10, 0] because it's the sum component by component
print(A_vector * B_vector * C_vector)
```

## Other operations

We can also do another methematical operations to the Numpy vectors in a simple way.

Some examples of this can be:

``` python
# Squaring each element in the vector
print( numpy_vector ** 2 )

# Getting the square root of every element in vector
print( numpy.sqrt(numpy_vector))

# Getting the Logarithm of 
print( numpy.log(numpy_vector) )

# Getting e^(N) of each element
print( numpy.exp(numpy_vector) )
```

## Dot product

The Dot Product is an operation between vectors that give us a scalar product, and there are two forms to get it.

Note: working examples of Dot Product are [here](https://github.com/SrChach/numpy_stack_and_algorithms/blob/master/numpy/dot.py)

One of the ways to get the dot product is using the formula 
![Producto_punto](../images/dot_product.png)

In which we need to multiply all the posicion components of each vector, and then sum all the results, to get a escalar number. 

First we need to get the multiplication of these vectors. Since vector multiplication gives us another vector, then we can sum the result in a simple way.

``` python
multiplied_vector = A_vector * B_vector * C_vector

dot_result = numpy.sum(multiplied_vector)
```

Or we can just use the built-in formula for *dot product* into Numpy

``` python
dot_result = A_vector.dot(B) # numpy.dot(A_vector, B_vector) also works
```

And there's the result of our first dot product.

## Getting the normal from a vector

The normal or magnitude of a vector is simply its length. As we know, one vector can have many dimensions, so we need a formula to get its length. This is

![normal_of_vector](../images/normal_of_vector.png)

So, let's get the magnitude!

``` python
# Using the formula
magnitude = numpy.sqrt( A_vector ** 2 )

# Using the linear algebra Numpy's module, which has the "normal" operation
magnitude = numpy.linalg.norm(A_vector)
```

## Getting angle between two vectors

Well, we now need to get the angle between two vectors. This can be done appying an arccos to the result of the formula:

![coseno_entre_dos_vectores](../images/coseno_entre_dos_vectores.png)

Int the above example, we learned how to get the magnitude of a vector and we'll apply it into the formula.

``` python
# Getting the cosine
cos_of_the_angle = U_vector.dot(V_vector) / ( numpy.linalg.norm(U_vector) * numpy.linalg.norm(V_vector) )
```

And then, we only need to use the arccos function that comes with numpy to get the angle.

``` python
angle = numpy.arccos( cos_of_the_angle )
```

And we've got our angle!

