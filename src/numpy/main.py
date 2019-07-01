import numpy

numpy_vector = numpy.array([1, 2, 3])
print("Original vector: ", numpy_vector)

# Numpy will treat "+" sign as vector addition, not concatenation as normal Python
print("sum of vectors: ", numpy_vector + numpy_vector)

# Mutiplication of vectors also works (in this case, a scalar multiplying a vector)
print("multiplying a vector by a scalar: ", numpy_vector * 2 )

# Let's try to square the vector
print("squaring each element in vector: ", numpy_vector ** 2 )

# Getting the square root of every element
print("square root of the vector: ", numpy.sqrt(numpy_vector) )

# Getting the Logarithm of every element
print("Log of the vector's elements: ", numpy.log(numpy_vector) )

# Getting e^(N) of each element
print("Exponential of vector: ", numpy.exp(numpy_vector) )