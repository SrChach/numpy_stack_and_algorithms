#------------------------------------------------------
def accessing_to_an_index():
    # string
    str_example = 'hola'
    print( 'index 3 from a string: ' + str_example[3] )

    # List
    list_example = ['uno', 'dos', 'tres']
    print( 'index 0 from a list: ' + list_example[0] )

    # Tuple. (Note: Tuples are like Lists, but they're immutable) 
    tuple_example =  ('inmutable_1', 'inmutable_2', 'inmutable_3')
    print( 'index 1 from a tuple: ' + tuple_example[1] )

#------------------------------------------------------
def slicing():
    # Slicing a String, tuple or array, works as follow
    #   variable[start : end + 1 : step] (default step is 1)

    print('"abcdefg"[ 1 : 3]: ', 'abcdefg'[1 : 3]) # Will print 'bc'
    print('"123456"[ 1 : 6 : 2]: ', '123456'[1 : 6 : 2]) # Will print '246'
    print('"palabra"[ 3 : ]: ', 'palabra'[ 3 : ]) # Will print 'abra' because second parameter empty's meaning is end of the string
    print('"palabra"[ : 5 ]', 'palabra'[ : 5]) # print 'palab' because first parameter empty means begin of the string

    print('ultimo_caracter'[-1])
    print('ultimos_tres'[-3 : ])
    print('todo_menos_ultimos_dos'[ : -2])

#------------------------------------------------------
# We can combine to sequences at the same type using '+'
def combining_items():
	# String
	concatenate = 'com' + 'ida'
	print(concatenate)

	# List
	join_lists = ['uno', 'dos'] + ['tres']
	print(join_lists)

	# Tuple
	join_tuple = ('1', '2') + ('3', ) # If there's not a comma, it´s only a string in parentheses. With comma is a tuple
	print(join_tuple)

#------------------------------------------------------
def do_multiple_times():
	# Do domething multiple times

	# string
	multistring = 'hola ' * 3 # Will put 'hola ' 3 times in a string
	print('multi-string: ', multistring)

	# List
	multilist = [1, 5] * 4
	print('multi-list: ', multilist)

	# Tuple
	multituple = (1, 2, 3) * 2
	print('multi-tuple: ', multituple)

#------------------------------------------------------
def in_a_sequence():
	in_string = 'string'
	print('"g" is in "string": ', 'g' in in_string)
	print('"x" is in "string": ', 'x' in in_string)

	in_tuple = ('cow', 'chicken', 'dog')
	print("'cow' is in ", in_tuple, "? :", 'cow' in in_tuple)
	print("'dog' not in ", in_tuple, 'dog' not in in_tuple)


#------------------------------------------------------
def iterating_in_items():
	list_iterating = [12, 43, 2]
	print('we print listed items as folowing: "for item in items"')
	for item in list_iterating:
		print(item)

	print('we print an item with its index as following: "for index, item in enumerate(items)"')
	list_with_index = (98, 43, 5)
	for index, item in enumerate(list_with_index):
		print('llave: ', index, ', valor:', item)

#------------------------------------------------------
def get_size():
	sized_string = 'cinco'
	print('sizeof string "cinco": ', len(sized_string))

	sized_list = [ 22, 33, 11 ]
	print('sizeof a list: ', len(sized_list))

	sized_tuple = ( 1, 54 )
	print('size of a tuple: ', len(sized_tuple))

# min of string/list/tuple: min(variable)
# Maximuum: max(variable)
# sum (only numeric array or tuples): sum(arrayOrTuple)
# Can be combined with slicing xD sum(array[ -2 :  ])
# Can sort: sort(StringOrArrayOrTuple)