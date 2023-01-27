list1 = ['p', 'q', 'r', 's']
list2 = ['a', 'b', 'c', 'd']

# adds a single element to the end of the list
list1.append('e') # ['p', 'q', 'r', 's', 'e']
print(list1)

# inserts the element in the given index, shifts the other elements to its right
list1.insert(2, 'q') # ['p', 'q', 'q', 'r', 's', 'e']
print(list1)

# adds the one list elements to another list
list1.extend(list2) # ['p', 'q', 'q', 'r', 's', 'e', 'a', 'b', 'c', 'd']
print(list1)

# list1 += list2
# print(list1)

# searches the first instance of the given element in a list and removes it
list1.remove('q') # ['p', 'q', 'r', 's', 'e', 'a', 'b', 'c', 'd']
list1.remove('q') # ['p', 'r', 's', 'e', 'a', 'b', 'c', 'd']
# list1.remove('q') # ValueError: list.remove(x): x not in list
print(list1)

# removes and returns the element at the given index / opposite to append
list1.pop(5)
print(list1) # ['p', 'r', 's', 'e', 'a', 'c', 'd']
list1.pop() # removes and returns the rightmost element if index is not given
print(list1) # ['p', 'r', 's', 'e', 'a', 'c']

# searches the given element in the list and returns its first matching index
print(list1.index('s')) # 2
# print(list1.index('z')) # ValueError: 'z' is not in list

# sorts the list - ascending order
list1.sort() # ['a', 'c', 'e', 'p', 'r', 's']
print(list1)

# reverses the list
list1.reverse() # ['s', 'r', 'p', 'e', 'c', 'a']
print(list1)
