# Python program to demonstrate defaultdict	
from collections import defaultdict

# Defining the dict
defintdict = defaultdict(int)
print(defintdict) # defaultdict(<class 'int'>, {})

# Iterate through the list for keeping the count
for num in [1, 2, 3, 4, 2, 4, 1, 2]:
	# The default value is 0 so there is no need to enter the key first
	defintdict[num] += 1

print(defintdict)

###################################################################

# Defining a dict 
deflistdict = defaultdict(list)
print(deflistdict)

for i in range(5): 
	deflistdict[i].append(i)

print("Dictionary with values as list:") 
print(deflistdict)
