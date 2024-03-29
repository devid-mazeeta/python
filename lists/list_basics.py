# defining the list
list1 = ['a','b','c','d']
print(list1) # ['a', 'b', 'c', 'd']

# copying the list
list2 = list1
print(list2) # ['a', 'b', 'c', 'd']

# accessing the data from the list using index (or) string slicing concept
print(list1[0]) # a
print(list1[2]) # c
print(list1[-2]) # c
print(list1[1:]) # ['b', 'c', 'd']
print(list1[1:2]) # ['b']
print(list1[-2:]) # ['c', 'd']
print(list1[:]) # ['a', 'b', 'c', 'd']
print(list1[:3]) # ['a', 'b', 'c']

# Reverse a list using slicing
print(list2[::-1])

# Accessing List of list
list3 = [
	[1,2,3],
	[4,5,6]
]

print(list3[0][2]) # 3
print(list3[1][2]) # 6
