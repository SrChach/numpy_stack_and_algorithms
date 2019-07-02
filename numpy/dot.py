import numpy

# Defining the vectors we will use
A_vector = numpy.array([1, 2])
B_vector = numpy.array([2, 1])

def dot_product_loop(A, B):
	result = 0

	for (element_of_A, element_of_B) in zip(A, B):
		result += element_of_A * element_of_B

	return result

def dot_product_multiplying_arrays(A, B):
	# this operation returns an array with the multiplication of each element
	multiplied = A * B

	# Sum all the elements in the new vector into one variable
	# Notice that this operation can be written shortly as
	#	numpy.sum(A * B)
	# or
	#	(A * B).sum()
	# this last because sum function is an instance method of a numpy array itself
	return numpy.sum(multiplied)

def dot_product(A, B):
	# Can also use numpy.dot(A, B)
	return A.dot(B)

print( "result of dot product, term by term in a loop: ", dot_product_loop(A_vector, B_vector) )
print("dot product using arrays multiplication: ", dot_product_multiplying_arrays(A_vector, B_vector))
print("Built-in dot product: ", dot_product(A_vector, B_vector))

#-------------------------------------------

# Magnitude of a vector
def vector_magnitude(vector):
	# Calculate the lenght of the vector(Mathematically)

	# lenght([a, b, c, ..., n]) = √(a^2 + b^2 + c^2 + ... + n^2)
	# The size is the square root of the sum of each element squared

	# There's one way to get the magnitude
	magnitude = numpy.sqrt( sum( vector ** 2 ) )

	# there's a simpler way to get the magnitude
	magnitude = numpy.linalg.norm( vector )

	return magnitude

print("magnitude of a vector: ", vector_magnitude(A_vector))

# Getting the cosine between two vectors
def angle_between_vectors(A, B):
	
	# So, cosine of the angle between A and B it's
	# Cos( angle_between_vectors ) = ( A . B )/( |A|*|B| )
	# then, the angle must be the arccos of these

	# Getting the cosine
	cos_of_angle = A.dot(B) / ( vector_magnitude(A) * vector_magnitude(B) )

	# using arccos to get the angle
	angle = numpy.arccos( cos_of_angle )

	return angle

print(angle_between_vectors(A_vector, B_vector))