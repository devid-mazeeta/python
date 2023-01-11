# python code to demonstrate working of reduce()
# reduce(fun, iter) 
from functools import reduce

# initializing list
mylist = [ 1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a + b, mylist))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, mylist))
