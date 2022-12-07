list1 = ['p', 'q', 'r', 's']
list2 = ['a', 'b', 'c', 'd']

# adds a single element to the end of the list
list1.append('e')
print(list1)

# inserts the element in the given index, shifts the other elements to its right
list1.insert(2, 'q')
print(list1)

# adds the one list elements to another list
list1.extend(list2) # ['p', 'q', 'q', 'r', 's', 'e', 'a', 'b', 'c', 'd']
print(list1)

# searches the given element in the list and returns its first matching index
print(list1.index('q')) # 1
print(list1.index('z')) # 

# searches the first instance of the given element in a list and removes it
list1.remove('q') # ['p', 'q', 'r', 's', 'e', 'a', 'b', 'c', 'd']
print(list1)

# sorts the list - ascending order
list1.sort() # ['a', 'b', 'c', 'd', 'e', 'p', 'q', 'r', 's']
print(list1)

# reverses the list
list1.reverse() # ['s', 'r', 'q', 'p', 'e', 'd', 'c', 'b', 'a']
print(list1)

# removes and returns the element at the given index / opposite to append
list1.pop(5)
print(list1)
list1.pop() # removes and returns the rightmost element if index is not given
print(list1)
