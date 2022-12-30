# iterator using next()
iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
# print(next(iter_list)) # Exception - StopIteration

# Using for in loop using iter()
iter_list2 = iter(['Geeks', 'For', 'Geeks'])

# for text in iter_list2:
for text in iter(iter_list2):
	print("inside loop: " + text)
