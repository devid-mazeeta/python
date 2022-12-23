# zero division error
try:
	num1 = 10
	num2 = 0
	result = num1/num2
except ZeroDivisionError as ze:
	print('Zero Division Error :: ' + str(ze))
	print('*' * 50)

# type error
try:
	num1 = 10
	print('num :: ' + num1)
except TypeError as te:
	print('Type Error :: ' + str(te))
	print('*' * 50)

# value error
try:
	int("xyz")
except ValueError as ve:
	print('Value Error :: ' + str(ve))
	print('*' * 50)

# handling multiple type of errors
try:
	num1 = 10
	num2 = int(input("Enter num 2 :: ")) # Chance of ValueError
	result = num1/num2 # Chance of ZeroDivisionError
	print('result :: ' + result) # TypeError
except (ZeroDivisionError,ValueError,TypeError) as me:
	print('Multiple Error :: ' + str(me))
	print('*' * 50)
