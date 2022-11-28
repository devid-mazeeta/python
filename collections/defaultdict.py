# Python program to demonstrate defaultdict	
from collections import defaultdict

# Defining the dict
d = defaultdict(int) # defaultdict(<class 'int'>, {})
print(d)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list for keeping the count
for i in L:
	# The default value is 0 so there is no need to enter the key first
	d[i] += 1

print(d)

# Python program to demonstrate defaultdict
from collections import defaultdict 

# Defining a dict 
d = defaultdict(list)

for i in range(5): 
	d[i].append(i)

print("Dictionary with values as list:") 
print(d)
