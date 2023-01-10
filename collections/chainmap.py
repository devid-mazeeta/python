# Python program to demonstrate ChainMap 
from collections import ChainMap 

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d4 = {'g': 7, 'h': 8}

# Defining the chainmap 
c = ChainMap(d1, d2, d3)
print(c)

for k,v in c.items():
	print(k,v)

# using new_child() to add new dictionary 
new_c = c.new_child(d4)

# printing chainMap
print("Displaying new ChainMap : ") 
print(new_c)

#############################################

# chain = [d1, d2, d3]
# print(chain)
# res_dict = {}

# # for ch in chain:
# for ch in [d1, d2, d3]:
# 	for k,v in ch.items():
# 		res_dict[k] = v
# 		print(k,v)

# print(res_dict)
