import sys

# A generator function that yields 1 for first time, 2 second time and 3 third time
def simplegeneratorfunc():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simplegeneratorfunc():
	print(value)

################################################################

# A Python program to demonstrate use of generator object with next()

# gen_obj is a generator object
gen_obj = simplegeneratorfunc()
print(gen_obj)

# Iterating over the generator object using next
print(gen_obj.__next__()) # In Python 2, next()
print(gen_obj.__next__())
print(gen_obj.__next__())

################################################################

# A simple generator for Fibonacci Numbers
def fib(limit):

	# Initialize first two Fibonacci Numbers
	a, b = 0, 1

	# One by one yield next Fibonacci Number
	while a < limit:
		yield a
		a, b = b, a + b

# Create a generator object
gen_obj = fib(5)

# Iterating over the generator object using next
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
print(gen_obj.__next__())
# print(gen_obj.__next__()) # Exception - StopIteration

# Iterating over the generator object using for in loop.
print("\nUsing for in loop")
for i in fib(5):
	print(i)
