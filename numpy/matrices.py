import numpy as np


def defining_matrix():

	# Initializing a Matrix directly as a Matrix
	# A matrix is almost the same thing that an array, but not completely. Altough we can use same operations in both.
	# 	Note: Official documentation recommends not using matrix, so we'll use arrays
	matrix_real = np.matrix([
			[1, 2],
			[3, 4] 
		])

	# We can convert a Matrix into an array matrix by the following operation
	matrix = np.array(matrix_real)

	# initializing a Numpy matrix as a list of lists, or a bidimensional array.
	# Notice that the sub-lists must have the same size
	#	Convention: THe first index is the Row, and second index the column
	matrix = np.array([ [1, 2], [3, 4] ])

	return matrix


def accesing_to_matrix_element(matrix):
	# There are two ways to access to an element into a Matrix

	print("accesing to [0][0] element into the matrix: ", matrix[0][0])

	print("another way [0, 0] to access to a matrix item: ", matrix[0, 0])


matrix = defining_matrix()

accesing_to_matrix_element(matrix)

print("original matrix: ", matrix)

# Note that even though this is an array, we still have convenient matrix operations
# For example, following operation will gives us the transpose of matrix
print("transpose of matrix: ", matrix.T)


def generating_arrays():
	number_of_zeros = 10

	# will return us an 1-Dimension array of length "number_of_zeros"
	array_full_of_zeros = np.zeros( number_of_zeros )

	# Will return us a matrix with size 10 X 10, full of zeros
	# Notice that the input is still one, but now is a tumple containing the dimensions
	matrix_full_of_zeros = np.zeros( (10, 10) )

	# A similar function, but filling all the elements with "1"
	matrix_full_of_ones = np.ones( (10, 10) )

	# Now we enter into the land of Random MAtrices

	# A function that gives us a array with random floats between 0 and 1 is
	matrix_random_elements = np.random.random( (10, 10) )

	# A function that give us a matrix with random but gaussian-distributed numbers
	# this is unique that can't get a tuple, but each dimension as an argument
	matrix_random_gaussian = np.random.randn  ( 10, 10 )

	return matrix_random_gaussian


# We can also pass probabilistic functions to matrices
def calculate_statistics(matrix):
	print("Matrix's mean: ", matrix.mean() )

	print("Matrix vaiance: ", matrix.var() )


matrix_random_gaussian = generating_arrays()

calculate_statistics(matrix_random_gaussian)


#-----------------------

def matrix_multiplication_example():
	# Matrix multiplication formula is
	# C(i, j) = sum(k=1, K){ A(i, k) · B(k, j) }
	# So, it needs that number of columns in the first matrix be equals 
	# 	to the name of rows in the second matrix

	A = np.array([ 
			[1, 2], 
			[3, 4] 
		])
	B = np.array([
			[2],
			[2] 
		])

	# This is a simple element-wise multiplication (not matrix muliplication)
	print("wise-element multiplication:\n", A * B)

	# This can be printed because height(A) = width(B)
	print("matrix multiplication result:\n ", A.dot(B))

	# This cannot be possiblee due to the above rule
	# print(B.dot(A))

def inverse(matrix):
	inverse = np.linalg.inv(matrix)
	return inverse

def determinant(matrix):
	determinant = np.linalg.det(matrix)
	return determinant

# If you pass a 2D array to diag(), you'll get a 1D array, and if you pass a 1D array, you'll get a 2D array
def get_diagonal_of_matrix(matrix):
	diagonal = np.diag(matrix)
	return diagonal

matrix_multiplication_example()

def inner_and_outer_products():
	A_vector = np.array([1, 2])
	B_vector = np.array([3, 4])

	print('outer product between two vectors:\n', np.outer(A_vector, B_vector), "\n" )
	
	# these two followings are the same
	print('inner product between two vectors:\n', np.inner(A_vector, B_vector), "\n" )
	print('another way to do the inner product:\n', A_vector.dot(B_vector), "\n" )

# Matrix trace is the sum of the diagonals of the matrix
def matrix_trace(matrix):
	# can be done by getting the diagonal and then sum it
	np.diag(matrix).sum()

	# Or by directly use a built-in function
	trace = np.trace(matrix)
	print("trace of matrix: ", trace, "\n")

matrix_trace(matrix)

# Eigenvalues and Eigenvectors (i need to check it as pribabilistic approach)
def eigen():
	# create 100 by 3 gaussian-distributed data points
	# notation: row = sample, column = feature
	# this case, matrix has 100 samples and 3 features
	X = np.random.randn(100, 3)

	# Remember that to get the covariance from a matrix, you want to transpose it first
	# Getting the Covariance of the matrix
	transpose = X.T
	covariance = np.cov(transpose)

	print('Covariance:\n', covariance, "\n")

	# Getting the shape to be sure that covariance is correct
	# print("shape from the covariance\n", covariance.shape)

	# There are two ways to get the eigenvalues and eigenvectors from a matrix(from its covariance)
	# First way: (eigh is for simetric and Hermitian matrices)
	eigen_result = np.linalg.eigh(covariance)

	# Second way
	eigen_result = np.linalg.eig(covariance)
	print("eigenvalues and eigenvectors, respectively:\n", eigen_result, "\n")

inner_and_outer_products()

eigen()


#--------------------- resolving a linear system -------------------

A = np.array([
		[1, 2],
		[3, 4]	
	])

b = np.array([1, 2])

def resolving_linear_system(matrix, vector):
	# We can get the solution for a linear system by
	# taking the inverse of the matrix and multiply it
	# by the "output" vector
	solution = np.linalg.inv(matrix).dot(vector)

	# another form for solving a linear system is using the built-in function
	# try to always use solve() and never the inverse method
	solution = np.linalg.solve(matrix, vector)
	return solution


equation_resolved = resolving_linear_system(A, b)
print("solution for the linear system:\n", equation_resolved, "\n")

